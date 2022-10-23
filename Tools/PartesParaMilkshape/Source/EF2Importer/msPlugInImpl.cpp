// =========================================================
// | Assimilation Software presents...                     |
// |                                                       |
// |  Milkshape Plugins  - (c) Graham (gameRevolt)         |
// =========================================================


// Include header files
#include "stdafx.h"
#include "msPlugInImpl.h"
#include "../common/include/msLib.h"
#include <math.h>
#include <sys/stat.h>
#include "../common/include/il/il.h"
#include "../common/include/mathlib.h"


// Boring dll stuff
BOOL APIENTRY DllMain(HANDLE hModule, DWORD ul_reason_for_call, LPVOID lpReserved)
{
    switch (ul_reason_for_call)
    {
        case DLL_PROCESS_ATTACH:
        case DLL_THREAD_ATTACH:
        case DLL_THREAD_DETACH:
        case DLL_PROCESS_DETACH:
            break;
    }
    return TRUE;
}


// Milkshape plugin object stuff
cMsPlugIn* CreatePlugIn ()
{
    return new cPlugIn ();
}
cPlugIn::cPlugIn ()
{
    strcpy (szTitle, "Elite Force 2...");
}
cPlugIn::~cPlugIn ()
{
}
int cPlugIn::GetType ()
{
    return cMsPlugIn::eTypeImport;
}
const char* cPlugIn::GetTitle ()
{
    return szTitle;
}

// Our file management class
class ass_file
{
public:

   char * data;
   int pointer;
   int size;

   ass_file() {}

   ass_file(char filename[])
   {
       load(filename);
   }

   void load(char filename[])
   {
      pointer=0;
      data=NULL;
      FILE * temp=fopen(filename,"rb");
      if (!temp) return;
      struct _stat s;
      _stat(filename, &s);
      size=s.st_size;
      data=(char *)malloc(size);
      fread(data,size,1,temp);
   }

   ~ass_file()
   {
    free(data);
   }
};
void ass_fread(void * place,int amount,int i,ass_file * file);
void ass_fread(void * place,int amount,int i,ass_file * file)
{
   int j;
   for (j=0;j<i;j++)
   {
      if ((amount+file->pointer)<file->size) 
         memcpy(place,file->data+file->pointer,amount);
      file->pointer+=amount;
   }
}

// Some types used
typedef float Matrix34_t[3][4]; 
typedef float matrix_t[3][4];
typedef struct
{
    matrix_t    mRelative;
    matrix_t    mAbsolute;
    matrix_t    mRelativeFinal;
    matrix_t    mFinal;
} myBone_t;

// Declare some functions
char * get_texture_filename(char * identifier);
int load_ska(msModel *pModel);
int load_ska(ass_file * myfile, msModel *pModel);
void errorMessage(char * message);
float * quaternion_to_euler(int * quat);
void Matrix34GetEulerAnglesXYZ(const Matrix34_t m, vec3_t angles);
void QuaternionToMatrix34(const vec4_t q, Matrix34_t m);
void SetupBones(msModel * m_pModel,int type=0);


// Main body
int cPlugIn::Execute (msModel *pModel)
{
    if (!pModel)
        return -1;

    //
    // choose filename
    //
    OPENFILENAME ofn;
    memset (&ofn, 0, sizeof (OPENFILENAME));
    
    char szFile[MS_MAX_PATH];
    char szFileTitle[MS_MAX_PATH];
    char szDefExt[32] = "skb";
    char szFilter[128] = "Object Files (*.tan)\0*.tan\0Skeletal Base Files (*.skb)\0*.skb\0Skeletal Animation Files (*.ska)\0*.ska\0All Files (*.*)\0*.*\0\0";
    szFile[0] = '\0';
    szFileTitle[0] = '\0';

    ofn.lStructSize = sizeof (OPENFILENAME);
    ofn.lpstrDefExt = szDefExt;
    ofn.lpstrFilter = szFilter;
    ofn.lpstrFile = szFile;
    ofn.nMaxFile = MS_MAX_PATH;
    ofn.lpstrFileTitle = szFileTitle;
    ofn.nMaxFileTitle = MS_MAX_PATH;
    ofn.Flags = OFN_HIDEREADONLY | OFN_FILEMUSTEXIST | OFN_PATHMUSTEXIST;
    ofn.lpstrTitle = "Import from Elite Force 2 -- assimsoft.com";

    if (!::GetOpenFileName (&ofn))
        return 0;

    //
    // import
    //
    ass_file myfile(szFile);
    if (!myfile.data)
    {
        errorMessage("Couldn't open the file");
        return 0;
    }

    int place;
    char filepath[256];
    strcpy(filepath,"");
    for (place=strlen(szFile)-1;place>=0;place--)
    {
       if (szFile[place]=='\\')
       {
           strcpy(filepath,szFile);
           filepath[place+1]='\0';
           break;
       }
    }

    // Header
    char magic[4];
    int type=0;
    #define TYPE_TAN 0
    #define TYPE_SKL 1
    #define TYPE_SKA 2
    ass_fread(magic,4,1,&myfile);
    if (strncmp(magic,"TAN ",4)==0) type=TYPE_TAN;
    else if (strncmp(magic,"SKL ",4)==0) type=TYPE_SKL;
    else if (strncmp(magic,"SKAN",4)==0) type=TYPE_SKA;
    else {
        errorMessage("This is not a known filetype!");
        return 1;
    }
    int version;
    ass_fread(&version,4,1,&myfile);
    if (type==TYPE_TAN)
    {
        if (version!=2)
        {
            errorMessage("Unknown version of a TAN .tan file");
            return 1;
        }
    }
    else if (type==TYPE_SKL)
    {
        if (version!=4)
        {
            errorMessage("Unknown version of a SKL .skb file");
            return 1;
        }
    }
    else if (type==TYPE_SKA)
    {
        myfile.pointer=0;
        return load_ska(&myfile,pModel);
    }
    
    msModel_Destroy (pModel);
    msModel_SetTotalFrames(pModel,0);

    myfile.pointer+=64; // Ignore original file path
    int no_tags,no_frames;
    if (type==TYPE_TAN)
    {
        ass_fread(&no_frames,4,1,&myfile);
        ass_fread(&no_tags,4,1,&myfile);
    }
    int no_meshes;
    ass_fread(&no_meshes,4,1,&myfile);
    int keyframe_offset;
    int node_offset;
    int no_nodes;
    if (type==TYPE_TAN)
    {
        myfile.pointer+=16; // No support for keyframes
        ass_fread(&keyframe_offset,4,1,&myfile);
    }
    else if (type==TYPE_SKL)
    {
        ass_fread(&no_nodes,4,1,&myfile);
        ass_fread(&node_offset,4,1,&myfile);
    }
    int mesh_offset,offset_bones;
    ass_fread(&mesh_offset,4,1,&myfile);
    int offset_tags;
    if (type==TYPE_SKL)
    {
        ass_fread(&offset_bones,4,1,&myfile);
    }
    else if (type==TYPE_TAN)
    {
        ass_fread(&offset_tags,4,1,&myfile);
        myfile.pointer+=16;
    }

    int counter,subcounter;

    float scale[3],offset[3];
    if (type==TYPE_TAN)
    {
        // Load in first frame transform info
        myfile.pointer=keyframe_offset+24;
        ass_fread(scale,12,1,&myfile);
        ass_fread(offset,12,1,&myfile);
    }
    else if (type==TYPE_SKL)
    {
        // Load in first frame transform info
        myfile.pointer=node_offset;
        for (counter=0;counter<no_nodes;counter++)
        {
            int parent;
            ass_fread(&parent,4,1,&myfile);
            myfile.pointer+=4; // Skip flags
            char name[65];
            name[64]='\0';
            ass_fread(name,64,1,&myfile);

            // Milkshape-erise
            msBone * giveADogA=msModel_GetBoneAt(pModel,msModel_AddBone(pModel));
            msBone_SetName(giveADogA,name);
            if (parent==-1) msBone_SetParentName(giveADogA,"");
            else {
                char parentName[65];
                parentName[64]='\0';
                msBone_GetName(msModel_GetBoneAt(pModel,parent),parentName,64);
                msBone_SetParentName(giveADogA,parentName);
            }

            int oldpos=myfile.pointer;
            myfile.pointer=offset_bones+counter*16;
            short quat[4];
            short offset[3];
            memset(quat,0,8);
            memset(offset,0,8);
            if (parent!=-1)
            {
                ass_fread(quat,8,1,&myfile);
                ass_fread(offset,6,1,&myfile);
            }
            int _quat[4];
            _quat[0]=quat[0];
            _quat[1]=quat[1];
            _quat[2]=quat[2];
            _quat[3]=quat[3];
            msVec3 myPos;
            myPos[0]=(float)offset[0]/64;
            myPos[1]=(float)offset[1]/64;
            myPos[2]=(float)offset[2]/64;
            msBone_SetPosition(giveADogA,myPos);
            msBone_SetRotation(giveADogA,quaternion_to_euler(_quat));
            myfile.pointer=oldpos;
        }
    }

    // Load meshes
    for (counter=0;counter<no_meshes;counter++)
    {
        myfile.pointer=mesh_offset;

        char materialName[65];
        ass_fread(materialName,64,1,&myfile);
        materialName[64]='\0';

        // Header
        myfile.pointer+=4; // Ignore flags
        if (type==TYPE_TAN) myfile.pointer+=4; // Ignore vertex deformation animation
        int numVertices;
        int numTriangles;
        int offsetTriangles;
        int offsetUV;
        int offsetVertices;
        int new_mesh_offset;
        if (type==TYPE_TAN)
        {
            ass_fread(&numVertices,4,1,&myfile);
            myfile.pointer+=4; // Ignore minimum lod
            ass_fread(&numTriangles,4,1,&myfile);
            ass_fread(&offsetTriangles,4,1,&myfile);
            myfile.pointer+=4; // Ignore collapse map
            ass_fread(&offsetUV,4,1,&myfile);
            ass_fread(&offsetVertices,4,1,&myfile);
            ass_fread(&new_mesh_offset,4,1,&myfile);
        } else
        if (type==TYPE_SKL)
        {
            ass_fread(&numTriangles,4,1,&myfile);
            myfile.pointer+=4; // Ignore minimum lod
            ass_fread(&numVertices,4,1,&myfile);
            ass_fread(&offsetTriangles,4,1,&myfile);
            ass_fread(&offsetVertices,4,1,&myfile);
            myfile.pointer+=4; // Ignore collapse map
            ass_fread(&new_mesh_offset,4,1,&myfile);
        }

        // Don't load bone attached meshes (don't know why they're here!)
        if (msModel_FindBoneByName(pModel,materialName+4)!=-1)
        {
            mesh_offset+=new_mesh_offset;
            continue;
        }

        // Bring up material
        char materialPath[MS_MAX_PATH];
        strcpy(materialPath,get_texture_filename(materialName+4));
        int matIndex=msModel_AddMaterial(pModel);
        msMaterial * myMaterial=msModel_GetMaterialAt(pModel,matIndex);
        msMaterial_SetName(myMaterial,materialName);
        msMaterial_SetDiffuseTexture(myMaterial,materialPath);
        msVec4 diffuse;
        diffuse[0]=255;
        diffuse[1]=255;
        diffuse[2]=255;
        diffuse[3]=255;
        msMaterial_SetDiffuse(myMaterial,diffuse);

        // Create
        msMesh * myMesh=msModel_GetMeshAt(pModel,msModel_AddMesh(pModel));
        msMesh_SetMaterialIndex(myMesh,matIndex);

        // Load in vertices
        myfile.pointer=mesh_offset+offsetVertices;
        for (subcounter=0;subcounter<numVertices;subcounter++)
        {
            msVec2 uv;
            msVec3 v;

            int best_bone=-1;

            if (type==TYPE_TAN)
            {
                // Coordinates
                myfile.pointer=mesh_offset+offsetVertices+subcounter*8;
                unsigned short x,y,z;
                ass_fread(&x,2,1,&myfile);
                ass_fread(&y,2,1,&myfile);
                ass_fread(&z,2,1,&myfile);
                v[0]=(float)((x-32768)*scale[0]+offset[0]);
                v[1]=(float)((y-32768)*scale[1]+offset[1]);
                v[2]=(float)((z-32768)*scale[2]+offset[2]);
                myfile.pointer+=2; // Ignore the normals

                // UV Mapping
                myfile.pointer=mesh_offset+offsetUV+subcounter*8;
                ass_fread(uv,8,1,&myfile);
            } else
            if (type==TYPE_SKL)
            {
                myfile.pointer+=12; // Ignore the normals
                ass_fread(uv,8,1,&myfile);

                // Choose highest weight as the bone we will bind to
                int num_weights;
                ass_fread(&num_weights,4,1,&myfile);
                int i;
                v[0]=0;
                v[1]=0;
                v[2]=0;
                float best_score=0;
//              #define BLEND 1
                for (i=0;i<num_weights;i++)
                {
                    float current_score;
                    float current_offset[3];
                    int current_bone;
                    ass_fread(&current_bone,4,1,&myfile);
                    ass_fread(&current_score,4,1,&myfile);
                    ass_fread(current_offset,12,1,&myfile);
                    if ((current_score>best_score) || (best_bone==-1))
                    {
                        best_score=current_score;
                        best_bone=current_bone;
                        #ifndef BLEND
                            v[0]=current_offset[0];
                            v[1]=current_offset[1];
                            v[2]=current_offset[2];
                        #endif
                    }
                    #ifdef BLEND
                        v[0]+=current_offset[0]*current_score;
                        v[1]+=current_offset[1]*current_score;
                        v[2]+=current_offset[2]*current_score;
                    #endif
                }
            }

            // Ms3d'erise
            msVertex * myVertex=msMesh_GetVertexAt(myMesh,msMesh_AddVertex(myMesh));
            msVertex_SetVertex(myVertex,v);
            msVertex_SetTexCoords(myVertex,uv);
            if (type==TYPE_SKL) msVertex_SetBoneIndex(myVertex,best_bone);
        }

        // Load in triangles
        myfile.pointer=mesh_offset+offsetTriangles;
        for (subcounter=0;subcounter<numTriangles;subcounter++)
        {
            // Coordinates
            int a,b,c;
            ass_fread(&a,4,1,&myfile);
            ass_fread(&b,4,1,&myfile);
            ass_fread(&c,4,1,&myfile);

            // Ms3d'erise
            unsigned short v[3];
            v[0]=c;
            v[1]=b;
            v[2]=a;
            msTriangle * myTriangle=msMesh_GetTriangleAt(myMesh,msMesh_AddTriangle(myMesh));
            msTriangle_SetVertexIndices(myTriangle,v);
        }

        // Again, again!
        mesh_offset+=new_mesh_offset;
    }

    if (type==TYPE_TAN) // Load tags
    {
        myfile.pointer=offset_tags;
        for (counter=0;counter<no_tags;counter++)
        {
            char tagName[64];
            ass_fread(tagName,64,1,&myfile);
            vec3_t pos;
            ass_fread(pos,12,1,&myfile);
            vec3_t axes[3];
            ass_fread(axes,36,1,&myfile);
            axes[0][0]+=pos[0];
            axes[0][1]+=pos[1];
            axes[0][2]+=pos[2];
            axes[1][0]+=pos[0];
            axes[1][1]+=pos[1];
            axes[1][2]+=pos[2];
            axes[2][0]+=pos[0];
            axes[2][1]+=pos[1];
            axes[2][2]+=pos[2];
            msMesh* myMesh=msModel_GetMeshAt(pModel,msModel_AddMesh(pModel));
            msMesh_SetName(myMesh,tagName);
            msVertex* myVert;
            myVert=msMesh_GetVertexAt(myMesh,msMesh_AddVertex(myMesh));
            msVertex_SetVertex(myVert,axes[0]);
            myVert=msMesh_GetVertexAt(myMesh,msMesh_AddVertex(myMesh));
            msVertex_SetVertex(myVert,axes[1]);
            myVert=msMesh_GetVertexAt(myMesh,msMesh_AddVertex(myMesh));
            msVertex_SetVertex(myVert,axes[2]);
            myfile.pointer+=48*(no_frames-1);
        }
    }

    if (type==TYPE_SKL) SetupBones(pModel,0);

    /*if (type==TYPE_SKL)
    {
        // Load ska
        return load_ska(pModel);
    }*/

    return 0;
}

// Choose a filename and load and check a ska file
int load_ska(msModel *pModel)
{
    //
    // choose filename
    //
    OPENFILENAME ofn;
    memset (&ofn, 0, sizeof (OPENFILENAME));
    
    char szFile[MS_MAX_PATH];
    char szFileTitle[MS_MAX_PATH];
    char szDefExt[32] = "ska";
    char szFilter[128] = "Skeletal Animation Files (*.ska)\0*.ska\0All Files (*.*)\0*.*\0\0";
    szFile[0] = '\0';
    szFileTitle[0] = '\0';

    ofn.lStructSize = sizeof (OPENFILENAME);
    ofn.lpstrDefExt = szDefExt;
    ofn.lpstrFilter = szFilter;
    ofn.lpstrFile = szFile;
    ofn.nMaxFile = MS_MAX_PATH;
    ofn.lpstrFileTitle = szFileTitle;
    ofn.nMaxFileTitle = MS_MAX_PATH;
    ofn.Flags = OFN_HIDEREADONLY | OFN_FILEMUSTEXIST | OFN_PATHMUSTEXIST;
    ofn.lpstrTitle = "Import skeletal animation file (ska)";

    if (!::GetOpenFileName (&ofn))
    {
        errorMessage("No file chosen: you will need to import one if you want any animation");
        return 0;
    }

    ass_file myfile(szFile);
    if (!myfile.data)
    {
        errorMessage("Couldn't open the file");
        return 0;
    }

    return load_ska(&myfile,pModel);
}

int load_ska(ass_file * myfile, msModel *pModel)
{
    SetupBones(pModel,1);

    // Header
    char magic[4];
    ass_fread(magic,4,1,myfile);
    if (strncmp(magic,"SKAN",4)!=0)
    {
        errorMessage("This is not a SKAN .ska file!");
        return 1;
    }
    int version;
    ass_fread(&version,4,1,myfile);
    if (version!=4)
    {
        errorMessage("Unknown version of a SKAN .ska file");
        return 1;
    }

    myfile->pointer+=64; // Skip filename
    myfile->pointer+=4; // Skip type
    int numFrames,numNodes,offsetFrames,offsetNodes;
    float animationLength, frameLength;
    ass_fread(&numFrames,4,1,myfile);
    ass_fread(&numNodes,4,1,myfile);
    ass_fread(&animationLength,4,1,myfile);
    ass_fread(&frameLength,4,1,myfile);
    myfile->pointer+=12; // Skip delta
    ass_fread(&offsetNodes,4,1,myfile);
    ass_fread(&offsetFrames,4,1,myfile);

    // Make sure we don't have too many bones for our bone map
    int counter;
    #define MAX_BONES 200
    if (numNodes>=200)
    {
        errorMessage("Too many bones: contact gameRevolt to have the limit increased");
        return 1;
    }

    // Load in nodes (bones)
    char bonemap[MAX_BONES][33];
    myfile->pointer=offsetNodes;
    for (counter=0;counter<numNodes;counter++) 
    {
        myfile->pointer+=4; // Skip ID (wouldn't know what to do with it anyway)
        bonemap[counter][32]='\0';
        ass_fread(bonemap[counter],32,1,myfile);
    }

    // Load in frames
    myfile->pointer=offsetFrames;
    msModel_SetTotalFrames(pModel,numFrames);
    #define MAX_FRAMES 2000
    float px[MAX_FRAMES],py[MAX_FRAMES],pz[MAX_FRAMES];
    float prx[MAX_FRAMES],pry[MAX_FRAMES],prz[MAX_FRAMES];
    for (counter=0;counter<numFrames;counter++) 
    {
        myfile->pointer+=24+12+4; // Skip some stuff we don't need

        msModel_SetFrame(pModel,counter);

        // Load nodes (bones)
        int subcounter;
        for (subcounter=0;subcounter<numNodes;subcounter++)
        {
            char * name=bonemap[subcounter];
            int boneLoc=msModel_FindBoneByName(pModel,name);
            if (boneLoc==-1)
            {
                errorMessage("Missing bone: you are not importing an animation for an open character");
                return 1;
            }
            msBone * giveADogA=msModel_GetBoneAt(pModel,boneLoc);

            short quat[4];
            short offset[3];
            memset(quat,0,8);
            memset(offset,0,8);
            if (strlen(giveADogA->szParentName)!=0)
            {
                ass_fread(quat,8,1,myfile);
                ass_fread(offset,6,1,myfile);
            } else myfile->pointer+=14;
            myfile->pointer+=2;

            // Milkshape'erise
            msVec3 myPos;
            myPos[0]=(float)offset[0]/64;
            myPos[1]=(float)offset[1]/64;
            myPos[2]=(float)offset[2]/64;
            int _quat[4];
            _quat[0]=quat[0];
            _quat[1]=quat[1];
            _quat[2]=quat[2];
            _quat[3]=quat[3];
            float *myRot=quaternion_to_euler(_quat);

            if (msBone_GetPositionKeyCount(giveADogA)<=counter)
                msBone_AddPositionKey(giveADogA,frameLength*(counter),myPos);
            msPositionKey* posKey=msBone_GetPositionKeyAt(giveADogA,counter);
            posKey->fTime=frameLength*10*(counter);
            if (counter==0)
            {
/*              msBone_SetPosition(giveADogA,myPos);
                posKey->Position[0]=0;
                posKey->Position[1]=0;
                posKey->Position[2]=0;*/
                posKey->Position[0]=myPos[0]-giveADogA->Position[0];
                posKey->Position[1]=myPos[1]-giveADogA->Position[1];
                posKey->Position[2]=myPos[2]-giveADogA->Position[2];
            } else
            {
                posKey->Position[0]=myPos[0]-px[subcounter];
                posKey->Position[1]=myPos[1]-py[subcounter];
                posKey->Position[2]=myPos[2]-pz[subcounter];
            }
            if (counter==0)
            {
/*              px[subcounter]=myPos[0];
                py[subcounter]=myPos[1];
                pz[subcounter]=myPos[2];*/
                px[subcounter]=giveADogA->Position[0];
                py[subcounter]=giveADogA->Position[1];
                pz[subcounter]=giveADogA->Position[2];
            }

            if (msBone_GetRotationKeyCount(giveADogA)<=counter)
                msBone_AddRotationKey(giveADogA,frameLength*(counter),myRot);
            msRotationKey* rotKey=msBone_GetRotationKeyAt(giveADogA,counter);
            rotKey->fTime=frameLength*10*(counter);
            if (counter==0)
            {
/*              msBone_SetRotation(giveADogA,myRot);
                rotKey->Rotation[0]=0;
                rotKey->Rotation[1]=0;
                rotKey->Rotation[2]=0;*/
                rotKey->Rotation[0]=myRot[0]-giveADogA->Rotation[0];
                rotKey->Rotation[1]=myRot[1]-giveADogA->Rotation[1];
                rotKey->Rotation[2]=myRot[2]-giveADogA->Rotation[2];
            } else
            {
                rotKey->Rotation[0]=myRot[0]-prx[subcounter];
                rotKey->Rotation[1]=myRot[1]-pry[subcounter];
                rotKey->Rotation[2]=myRot[2]-prz[subcounter];
            }
            if (counter==0)
            {
                prx[subcounter]=giveADogA->Rotation[0];
                pry[subcounter]=giveADogA->Rotation[1];
                prz[subcounter]=giveADogA->Rotation[2];
            }
        }
    }

    SetupBones(pModel,0);

    return 0;
}

// Converts a quaternion to a set of euler angles
vec3_t myRot;
float * quaternion_to_euler(int * quat)
{
    Matrix34_t myMatrix;
    vec4_t q;
    float scale=(float)3.14159/(float)32768.0/2;
    q[0]=(float)quat[0]*scale;
    q[1]=(float)quat[1]*scale;
    q[2]=(float)quat[2]*scale;
    q[3]=(float)quat[3]*scale;
    QuaternionToMatrix34(q, myMatrix);
    Matrix34GetEulerAnglesXYZ(myMatrix, myRot);
    return myRot;
}

// Get a texture filename from a requested identifier and convert if necessary
char szFile[MS_MAX_PATH];
char * get_texture_filename(char * identifier)
{
    strcpy(szFile,"");

    // See if we can search out a .tik file in here and discern what texture to load from it
    WIN32_FIND_DATA FindFileData;
    HANDLE hFind;
    hFind = FindFirstFile("*.tik", &FindFileData);
    FindFileData.cFileName;
    if ((int)hFind>0) // Search inside tiki
    {
        char searchstring[200];
        memset(szFile,0,MS_MAX_PATH-1);
        strcpy(searchstring,"surface ");
        strcat(searchstring,identifier);
        strcat(searchstring," shader ");

        ass_file tikifile;
        char * place=0;
        int ret;
        do
        {
            tikifile.load(FindFileData.cFileName);

            place=strstr(tikifile.data,searchstring);

            ret=1;
            if (!place)
                ret=FindNextFile(hFind, &FindFileData);
        }
        while ((!place) && (ret!=0));

        if (place)
        {
            place+=+strlen(searchstring);
            char * place2=strchr(place,13);
            strncpy(szFile,place,(int)(place2-place));
            if (*(szFile+strlen(szFile)-4)!='.') strcat(szFile,".tga");
        }
    }

    if (strlen(szFile)==0)  // Browse for file
    {
        OPENFILENAME ofn;
        memset (&ofn, 0, sizeof (OPENFILENAME));
    
        char szFileTitle[MS_MAX_PATH];
        char szDefExt[32] = "tan";
        char szFilter[128] = "DDS Files (*.dds)\0*.dds\0TGA Files (*.tga)\0*.tga\0\0";
        szFile[0] = '\0';
        szFileTitle[0] = '\0';

        ofn.lStructSize = sizeof (OPENFILENAME);
        ofn.lpstrDefExt = szDefExt;
        ofn.lpstrFilter = szFilter;
        ofn.lpstrFile = szFile;
        ofn.nMaxFile = MS_MAX_PATH;
        ofn.lpstrFileTitle = szFileTitle;
        ofn.nMaxFileTitle = MS_MAX_PATH;
        ofn.Flags = OFN_HIDEREADONLY | OFN_FILEMUSTEXIST | OFN_PATHMUSTEXIST;
        ofn.lpstrTitle = identifier;

        ::GetOpenFileName (&ofn);
        if (strcmp(szFile,"")==0) return szFile; // Cancelled
    }

    // Convert from dds if we need to (huge messy hack)
    ilInit();
    strcpy(szFile+strlen(szFile)-3,"dds");
    if (ilLoadImage(szFile))
    {
        strcpy(szFile+strlen(szFile)-3,"tga");
        ilSaveImage(szFile);
    } else  strcpy(szFile+strlen(szFile)-3,"tga");

    return szFile;
}

// Make us an error message
void errorMessage(char * message)
{
    MessageBox (NULL,message,NULL,MB_OK);
}



//--------------------------------------------------------------------------- 
// Matrix34GetEulerAnglesXYZ 
//--------------------------------------------------------------------------- 
void Matrix34GetEulerAnglesXYZ(const Matrix34_t m, vec3_t angles) 
{ 
    float cy = (float) sqrt(m[0][0]*m[0][0] + m[1][0]*m[1][0]); 

    if (cy > 16 * 0.001) 
    { 
        angles[0] = (float) atan2 (m[2][1], m[2][2]); 
        angles[1] = (float) atan2 (-m[2][0], cy); 
        angles[2] = (float) atan2 (m[1][0], m[0][0]); 
    } 
    else 
    { 
        angles[0] = (float) atan2 (-m[1][2], m[1][1]); 
        angles[1] = (float) atan2 (-m[2][0], cy); 
        angles[2] = 0.0f; 
    } 
} 

void QuaternionToMatrix34(const vec4_t q, Matrix34_t m) 
{ 
    float X2,Y2,Z2; //2*QX, 2*QY, 2*QZ 
    float XX2,YY2,ZZ2; //2*QX*QX, 2*QY*QY, 2*QZ*QZ 
    float XY2,XZ2,XW2; //2*QX*QY, 2*QX*QZ, 2*QX*QW 
    float YZ2,YW2,ZW2; // ... 

    X2 = 2.0f * q[0]; 
    XX2 = X2 * q[0]; 
    XY2 = X2 * q[1]; 
    XZ2 = X2 * q[2]; 
    XW2 = X2 * q[3]; 

    Y2 = 2.0f * q[1]; 
    YY2 = Y2 * q[1]; 
    YZ2 = Y2 * q[2]; 
    YW2 = Y2 * q[3]; 

    Z2 = 2.0f * q[2]; 
    ZZ2 = Z2 * q[2]; 
    ZW2 = Z2 * q[3]; 

    m[0][0] = 1.0f - YY2 - ZZ2; 
    m[1][0] = XY2 - ZW2; 
    m[2][0] = XZ2 + YW2; 

    m[0][1] = XY2 + ZW2; 
    m[1][1] = 1.0f - XX2 - ZZ2; 
    m[2][1] = YZ2 - XW2; 

    m[0][2] = XZ2 - YW2; 
    m[1][2] = YZ2 + XW2; 
    m[2][2] = 1.0f - XX2 - YY2; 

    m[0][3] = 0.0f; 
    m[0][3] = 0.0f; 
    m[0][3] = 0.0f; 
}


void SetupBones(msModel * m_pModel, int type)
{
    int nBoneCount = msModel_GetBoneCount (m_pModel);
    myBone_t *m_pBones;
    m_pBones = new myBone_t[nBoneCount];

    int i, j;
    for (i = 0; i < nBoneCount; i++)
    {
        msBone *pBone = msModel_GetBoneAt (m_pModel, i);
        msVec3 vRot;
        vRot[0] = pBone->Rotation[0] * 180 / (float) Q_PI;
        vRot[1] = pBone->Rotation[1] * 180 / (float) Q_PI;
        vRot[2] = pBone->Rotation[2] * 180 / (float) Q_PI;
        AngleMatrix (vRot, m_pBones[i].mRelative);
        m_pBones[i].mRelative[0][3] = pBone->Position[0];
        m_pBones[i].mRelative[1][3] = pBone->Position[1];
        m_pBones[i].mRelative[2][3] = pBone->Position[2];
        int nParentBone = msModel_FindBoneByName (m_pModel, pBone->szParentName);
        if (nParentBone != -1)
        {
            R_ConcatTransforms (m_pBones[nParentBone].mAbsolute, m_pBones[i].mRelative, m_pBones[i].mAbsolute);
            memcpy (m_pBones[i].mFinal, m_pBones[i].mAbsolute, sizeof (matrix_t));
        }
        else
        {
            memcpy (m_pBones[i].mAbsolute, m_pBones[i].mRelative, sizeof (matrix_t));
            memcpy (m_pBones[i].mFinal, m_pBones[i].mRelative, sizeof (matrix_t));
        }
    }

    for (i = 0; i < msModel_GetMeshCount (m_pModel); i++)
    {
        msMesh *pMesh = msModel_GetMeshAt (m_pModel, i);
        for (j = 0; j < msMesh_GetVertexCount (pMesh); j++)
        {
            msVertex *pVertex = msMesh_GetVertexAt (pMesh, j);
            if (pVertex->nBoneIndex != -1)
            {
                msVec3 vTmp;
                if (type==0)
                {
                    VectorRotate (pVertex->Vertex, m_pBones[pVertex->nBoneIndex].mAbsolute, vTmp);
                    VectorCopy (vTmp, pVertex->Vertex);
                    pVertex->Vertex[0] += m_pBones[pVertex->nBoneIndex].mAbsolute[0][3];
                    pVertex->Vertex[1] += m_pBones[pVertex->nBoneIndex].mAbsolute[1][3];
                    pVertex->Vertex[2] += m_pBones[pVertex->nBoneIndex].mAbsolute[2][3];
                } else {
                    pVertex->Vertex[0] -= m_pBones[pVertex->nBoneIndex].mAbsolute[0][3];
                    pVertex->Vertex[1] -= m_pBones[pVertex->nBoneIndex].mAbsolute[1][3];
                    pVertex->Vertex[2] -= m_pBones[pVertex->nBoneIndex].mAbsolute[2][3];
                    VectorIRotate (pVertex->Vertex, m_pBones[pVertex->nBoneIndex].mAbsolute, vTmp);
                    VectorCopy (vTmp, pVertex->Vertex);
                }
            }
        }
    }
}
