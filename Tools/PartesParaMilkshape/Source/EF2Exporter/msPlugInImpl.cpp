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
    return cMsPlugIn::eTypeExport;
}
const char* cPlugIn::GetTitle ()
{
    return szTitle;
}

// Declare some functions
char * get_texture_filename(char * identifier);
void errorMessage(char * message);

// Main body
int cPlugIn::Execute (msModel *pModel)
{
    if (!pModel)
        return -1;

    //
    // check, if we have something to export
    //
    if (msModel_GetMeshCount (pModel) == 0)
    {
        ::MessageBox (NULL, "The model is empty!  Nothing exported!", "TIKI Export", MB_OK | MB_ICONWARNING);
        return 0;
    }

    //
    // choose filename
    //
    OPENFILENAME ofn;
    memset (&ofn, 0, sizeof (OPENFILENAME));
    
    char szFile[MS_MAX_PATH];
    char szFileTitle[MS_MAX_PATH];
    char szDefExt[32] = "skb";
    char szFilter[128] = "Object Files (*.tan)\0*.tan\0All Files (*.*)\0*.*\0\0";
    szFile[0] = '\0';
    szFileTitle[0] = '\0';

    ofn.lStructSize = sizeof (OPENFILENAME);
    ofn.lpstrDefExt = szDefExt;
    ofn.lpstrFilter = szFilter;
    ofn.lpstrFile = szFile;
    ofn.nMaxFile = MS_MAX_PATH;
    ofn.lpstrFileTitle = szFileTitle;
    ofn.nMaxFileTitle = MS_MAX_PATH;
    ofn.Flags = OFN_HIDEREADONLY | OFN_OVERWRITEPROMPT | OFN_PATHMUSTEXIST;
    ofn.lpstrTitle = "Export from Elite Force 2 -- assimsoft.com";

    if (!::GetSaveFileName (&ofn))
        return 0;

    //
    // import
    //
    FILE *myfile = fopen (szFile, "wb");
    if (!myfile)
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

    // Some useful things
    float floatZero=0,floatOne=1;
    int wordZero=0,wordOne=1;

    // Header
    char magic[4];
    strcpy(magic,"TAN ",4);
    fwrite(magic,4,1,myfile);
    int version=2;
    fwrite(&version,4,1,myfile);
    fwrite(szFile,64,1,myfile);

    int no_frames=1;
    fwrite(&no_frames,4,1,myfile);
    int no_tags=0;
    fwrite(&no_tags,4,1,myfile);
    int no_meshes=msModel_GetMeshCount(pModel);
    fwrite(&no_meshes,4,1,myfile);
    int keyframe_offset=128;
    fwrite(&floatZero,4,1,myfile);
    fwrite(&floatZero,4,1,myfile);
    fwrite(&floatZero,4,1,myfile);
    fwrite(&floatZero,4,1,myfile);
    fwrite(&keyframe_offset,4,1,myfile);
    int mesh_offset=184;
    fwrite(&mesh_offset,4,1,myfile);
    int offset_tags=0;
    fwrite(&offset_tags,4,1,myfile);
    fwrite(&offset_tags,4,1,myfile);
    fwrite(&offset_tags,4,1,myfile);
    fwrite(&offset_tags,4,1,myfile);
    fwrite(&offset_tags,4,1,myfile);

    // Work out bounds
    int counter,subcounter;
    float minX=0,minY=0,minZ=0,maxX=0,maxY=0,maxZ=0;
    float radius=0;
    for (counter=0;counter<no_meshes;counter++)
    {
        msMesh * myMesh=msModel_GetMeshAt(pModel,counter);
        for (subcounter=0;subcounter<msMesh_GetVertexCount(myMesh);subcounter++)
        {
            msVertex * myVertex=msMesh_GetVertexAt(myMesh,subcounter);
            if ((counter==0) && (subcounter==0))
            {
                minX=myVertex->Vertex[0];
                minY=myVertex->Vertex[1];
                minZ=myVertex->Vertex[2];

                maxX=myVertex->Vertex[0];
                mazY=myVertex->Vertex[1];
                maxZ=myVertex->Vertex[2];
            } else {
                if (myVertex->Vertex[0]>maxX) maxX=myVertex->Vertex[0];
                if (myVertex->Vertex[1]>maxY) maxY=myVertex->Vertex[1];
                if (myVertex->Vertex[2]>maxZ) maxZ=myVertex->Vertex[2];

                if (myVertex->Vertex[0]<minX) minX=myVertex->Vertex[0];
                if (myVertex->Vertex[1]<minY) minY=myVertex->Vertex[1];
                if (myVertex->Vertex[2]<minZ) minZ=myVertex->Vertex[2];
            }

            float thisRadius=sqrt(myVertex->Vertex[0]*myVertex->Vertex[0]+myVertex->Vertex[1]*myVertex->Vertex[1]+myVertex->Vertex[2]*myVertex->Vertex[2]);
            if (thisRadius>radius) radius=thisRadius;
        }
    }

    // First frame transform info
    fwrite(&minX,4,1,myfile);   fwrite(&minY,4,1,myfile);   fwrite(&minZ,4,1,myfile);
    fwrite(&maxX,4,1,myfile);   fwrite(&maxY,4,1,myfile);   fwrite(&maxZ,4,1,myfile);
    fwrite(&floatOne,4,1,myfile);   fwrite(&floatOne,4,1,myfile);   fwrite(&floatOne,4,1,myfile);
    fwrite(&floatZero,4,1,myfile);  fwrite(&floatZero,4,1,myfile);  fwrite(&floatZero,4,1,myfile);
    fwrite(&floatZero,4,1,myfile);  fwrite(&floatZero,4,1,myfile);  fwrite(&floatZero,4,1,myfile);
    fwrite(&radius,4,1,myfile);
    fwrite(&floatZero,4,1,myfile);

    // Load meshes
    for (counter=0;counter<no_meshes;counter++)
    {
        msMesh * myMesh=msModel_GetMeshAt(pModel,counter);

        char materialName[64];
        char materialNameStub[60];
        strcpy(materialName,"TAN ");
        msMaterial_GetName(msMesh_GetMaterialIndex(myMesh),materialNameStub,60);
        strcat(materialName,materialNameStub);
        fwrite(materialName,64,1,myfile);

        // Header
        int flags=0;
        fwrite(&flags,4,1,myfile);
        fwrite(&wordZero,4,1,myfile); // No mesh deformation animation
        int numVertices=myMesh->nNumVertices;
        int numTriangles=myMesh->nNumTriangles;
        int offsetTriangles=124;
        int offsetCollapse=offsetTriangles+numTriangles*6;
        int offsetUV=offsetCollapse+numVertices*4;
        int offsetVertices=offsetUV+numVertices*8;
        int new_mesh_offset=offsetVertices+numVertices*8;
        fwrite(&numVertices,4,1,myfile);
        fwrite(&floatOne,4,1,myfile); // Minimum LOD is maximum, as I don't trust my collapse map
        fwrite(&numTriangles,4,1,myfile);
        fwrite(&offsetTriangles,4,1,myfile);
        fwrite(&offsetCollapse,4,1,myfile);
        fwrite(&offsetUV,4,1,myfile);
        fwrite(&offsetVertices,4,1,myfile);
        fwrite(&new_mesh_offset,4,1,myfile);

        // triangles
        for (subcounter=0;subcounter<numTriangles;subcounter++)
        {
            msTriangle * myTri=msMesh_GetTriangleAt(myMesh,subcounter);

            // Coordinates
            int a=myTri->nVertexIndices[2],b=myTri->nVertexIndices[1],c=myTri->nVertexIndices[0];
            fwrite(&a,4,1,myfile);
            fwrite(&b,4,1,myfile);
            fwrite(&c,4,1,myfile);
        }

        // collapse map... this is a hopefully working but not efficient collapse map
        for (subcounter=0;subcounter<numVertices;subcounter++)
        {
            msVertex * myVertex=msMesh_GetVertexAt(myMesh,subcounter);

            int i;
            short target=-1;
            float dist;
            for (i=subcounter+1;i<numVertices;i++)
            {
                msVertex * myVertex2=msMesh_GetVertexAt(myMesh,i);

                float dx=(myVertex2->Vertex[0]-myVertex->Vertex[0]);
                float dy=(myVertex2->Vertex[1]-myVertex->Vertex[1]);
                float dz=(myVertex2->Vertex[2]-myVertex->Vertex[2]);

                float thisDist=sqrt(dx*dx+dy*dy+dz*dz);
                if ((target==-1) || (thisDist<dist))
                {
                    dist=thisDist;
                    target=i;
                }
            }
            if (target==-1) target=0;

            fwrite(
        }

        // uv

        // vertices
        for (subcounter=0;subcounter<numVertices;subcounter++)
        {
            msVertex * myVertex=msMesh_GetVertexAt(myMesh,subcounter);

            // Coordinates
            unsigned short x,y,z;
            x=myVertex->Vertex[0]+32768;
            y=myVertex->Vertex[0]+32768;
            z=myVertex->Vertex[0]+32768;
            fwrite(&x,2,1,myfile);
            fwrite(&y,2,1,myfile);
            fwrite(&z,2,1,myfile);
            msVec3 Normal;
            msMesh_GetVertexNormalAt (myMesh, subcounter, Normal);
            unsigned char quakeNormal[2];
            NormalToLatLong(Normal,quakeNormal);
            fwrite(&quakeNormal,2,1,myfile);
        }
    }

    return 0;
}

// Make us an error message
void errorMessage(char * message)
{
    MessageBox (NULL,message,NULL,MB_OK);
}
