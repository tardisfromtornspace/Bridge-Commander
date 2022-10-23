// =========================================================
// | Assimilation Software presents...                     |
// |                                                       |
// |  Milkshape Plugins  - (c) Graham (gameRevolt)         |
// =========================================================

#include "stdafx.h"
#include "msPlugInImpl.h"
#include "msLib.h"

#include <math.h>
#include <sys/stat.h>

#define SCALE 2.25

#define MAX_VERTICES 5000

BOOL APIENTRY DllMain( HANDLE hModule, 
                       DWORD  ul_reason_for_call, 
                       LPVOID lpReserved
					 )
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



cMsPlugIn*
CreatePlugIn ()
{
    return new cPlugIn ();
}



cPlugIn::cPlugIn ()
{
    strcpy (szTitle, "Star Fleet Command (MOD)...");
}



cPlugIn::~cPlugIn ()
{
}



int
cPlugIn::GetType ()
{
    return cMsPlugIn::eTypeImport;
}



const char*
cPlugIn::GetTitle ()
{
    return szTitle;
}

class ass_file
{
public:

   char * data;
   int pointer;
   int size;

   ass_file(char filename[])
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

int
cPlugIn::Execute (msModel *pModel)
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
    char szDefExt[32] = "mod";
    char szFilter[128] = "MOD Files (*.mod)\0*.mod\0All Files (*.*)\0*.*\0\0";
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
    ofn.lpstrTitle = "Import SFC MOD -- assimsoft.com";

    if (!::GetOpenFileName (&ofn))
        return 0;

    //
    // import
    //
    ass_file myfile(szFile);
    if (!myfile.data) return 0;

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

   msModel_Destroy (pModel);

	int lods=-1;
	int no_vertices=-1,no_polygons=-1,more_junk;
	float junk;
	bool done_lod=false,done_verts=false;
	int done_poly=0;
	char *string_text=NULL;
	int string_size;
	int count;
   float ambient[255];
   float diffuse[255];
   float emissive[255];
   float v[MAX_VERTICES][3];
	int vid[MAX_VERTICES];
	count=0;
   char texture[255][256];
   char lightmap[255][256];
   char texturename[255][50];
   msMaterial* materials[255];
   memset(materials,0,255*sizeof(msMaterial*));
   msMesh * mesh[255];
   memset(mesh,0,255*sizeof(msMesh*));

   do
	{
		char chunk[5];
		chunk[4]='\0';
		ass_fread(chunk,4,1,&myfile);
		int size;
		ass_fread(&size,sizeof(long),1,&myfile);

		// Header chunk
		if (strcmp(chunk,"MDLS")==0)
		{
			int version;
			ass_fread(&version,sizeof(int),1,&myfile);
			ass_fread(&junk,sizeof(float),1,&myfile);
			ass_fread(&lods,sizeof(int),1,&myfile);
			ass_fread(&junk,sizeof(float),1,&myfile);
			ass_fread(&junk,sizeof(float),1,&myfile);
			ass_fread(&junk,sizeof(float),1,&myfile);
			ass_fread(&junk,sizeof(float),1,&myfile);
			ass_fread(&junk,sizeof(float),1,&myfile);
			ass_fread(&junk,sizeof(float),1,&myfile);
		} else
		if ((strcmp(chunk,"MOD0")==0) && (!done_lod))
		{
			done_lod=true;
			ass_fread(&no_vertices,sizeof(int),1,&myfile);
			ass_fread(&no_polygons,sizeof(int),1,&myfile);
		} else
		if ((strcmp(chunk,"PNTS")==0) && (!done_lod))
		{
         int counter=0;
         while (counter<size)
         {
				msVec3 position;
            ass_fread(&position[2],4,1,&myfile);
            ass_fread(&position[1],4,1,&myfile);
            ass_fread(&position[0],4,1,&myfile);
				position[0]*=SCALE;
				position[1]*=SCALE;
				position[2]*=SCALE;
            int temp;
            ass_fread(&temp,4,1,&myfile);
				char name[30];
            strcpy(name,string_text+temp);

				msBone* myBone=msModel_GetBoneAt(pModel,msModel_AddBone(pModel));
				msBone_SetName(myBone,name);
				msBone_SetPosition(myBone,position);

            counter+=16;
			}
		} else
      if ((strcmp(chunk,"STRS")==0) && (!done_verts))
		{
         string_text=(char *)malloc(size+1);
			ass_fread(string_text,size,1,&myfile);
			string_size=size;

			// Cut off any appended 0's
			char t;
			do
			{
				ass_fread(&t,1,1,&myfile);
			}
			while (t==0);
			myfile.pointer--;
		} else
		if (strcmp(chunk,"MATS")==0)
		{
			int counter=0;
			int mats=0;
			while (counter<size)
			{
            // Flags
				int properties;
				ass_fread(&properties,sizeof(int),1,&myfile);

            // Color (ignore)
				float color_junk;
				ass_fread(&color_junk,sizeof(float),1,&myfile);

            // Ambient
				ass_fread(&ambient[mats],sizeof(float),1,&myfile);

            // Diffuse
				ass_fread(&diffuse[mats],sizeof(float),1,&myfile);

            // Emittance
				ass_fread(&emissive[mats],sizeof(float),1,&myfile);
				emissive[mats]=1; // This is irritating (makes things black): turn its effect off

            // Where the texture string links in
				int id;
				ass_fread(&id,sizeof(int),1,&myfile);
				int start;
				ass_fread(&start,sizeof(int),1,&myfile);

				counter+=28;

            // Import texture
            strcpy(texture[mats],string_text+start);
            strcat(texture[mats],".bmp");
            struct _stat s;
            if (_stat(texture[mats], &s)!=0)
            {
               strcpy(texture[mats],string_text+start);
               strcat(texture[mats],".pcx");
            }
				sprintf(texturename[mats],"%d_%s",mats,string_text+start);

            // Luminance texture
            strcpy(lightmap[mats],"");
            if (properties&32)
				{
					ass_fread(&id,sizeof(int),1,&myfile);
					ass_fread(&start,sizeof(int),1,&myfile);

               // Import texture
               strcpy(lightmap[mats],string_text+start);
               strcat(lightmap[mats],".bmp");
               if (_stat(lightmap[mats], &s)!=0)
               {
                  strcpy(lightmap[mats],string_text+start);
                  strcat(lightmap[mats],".pcx");
               }

					counter+=8;
				}

				mats++;
			}
		} else
		if ((strcmp(chunk,"VTXS")==0) && (!done_verts))
		{
			done_verts=true;
			long counter;
			for (counter=0;counter<no_vertices;counter++)
			{
				ass_fread(&v[counter][2],sizeof(float),1,&myfile);
				ass_fread(&v[counter][1],sizeof(float),1,&myfile);
				ass_fread(&v[counter][0],sizeof(float),1,&myfile);
				v[counter][0]*=SCALE;
				v[counter][1]*=SCALE;
				v[counter][2]*=SCALE;
			}
      } else
		if ((strcmp(chunk,"POLY")==0) && (done_poly!=no_polygons))
		{
			int no_local_vertices;
			ass_fread(&no_local_vertices,sizeof(int),1,&myfile);
			int tex_id;
			ass_fread(&tex_id,sizeof(int),1,&myfile);

         // Make sure we have our material made
         if (!materials[tex_id])
         {
            materials[tex_id]=msModel_GetMaterialAt(pModel,msModel_AddMaterial (pModel));
            msMaterial_SetName(materials[tex_id],texturename[tex_id]);
            float _ambient[4];
            float _diffuse[4];
            float _emissive[4];
            _ambient[0]=_ambient[1]=_ambient[2]=_ambient[3]=ambient[tex_id];
            _diffuse[0]=_diffuse[1]=_diffuse[2]=_diffuse[3]=diffuse[tex_id];
            _emissive[0]=_emissive[1]=_emissive[2]=_emissive[3]=emissive[tex_id];
            msMaterial_SetAmbient(materials[tex_id],_ambient);
            msMaterial_SetDiffuse(materials[tex_id],_diffuse);
            msMaterial_SetEmissive(materials[tex_id],_emissive);
            msMaterial_SetDiffuseTexture(materials[tex_id],texture[tex_id]);
            msMaterial_SetAlphaTexture(materials[tex_id],lightmap[tex_id]);
         }

         // Make sure we have our mesh made
         if (!mesh[tex_id])
         {
            mesh[tex_id]=msModel_GetMeshAt(pModel,msModel_AddMesh (pModel));
            msMesh_SetMaterialIndex(mesh[tex_id],msModel_FindMaterialByName(pModel,texturename[tex_id]));
            msMesh_SetName(mesh[tex_id],texturename[tex_id]);
				for (count=0;count<MAX_VERTICES;count++)
					vid[count]=-1;
         }

         // Vertices
			ass_fread(&junk,sizeof(float),1,&myfile);
			ass_fread(&junk,sizeof(float),1,&myfile);
			ass_fread(&junk,sizeof(float),1,&myfile);
			int counter;
         unsigned short vertex[4];
         unsigned short normal[4];
         bool invalid=false;
         if (no_local_vertices>4) invalid=true;
//         if (done_poly>1000) invalid=true;
			for (counter=0;counter<no_local_vertices;counter++)
			{
            msVec3 n;
				unsigned int vertex1=0;
				ass_fread(&vertex1,sizeof(short),1,&myfile);
				myfile.pointer+=2;
            if (vertex1>=(unsigned)no_vertices) invalid=true;
				ass_fread(&n[2],sizeof(float),1,&myfile);
				ass_fread(&n[1],sizeof(float),1,&myfile);
				ass_fread(&n[0],sizeof(float),1,&myfile);
            float n_len=(float)sqrt(n[2]*n[2]+n[1]*n[1]+n[0]*n[0]);
            if (n_len!=0)
            {
               n[0]/=n_len;
               n[1]/=n_len;
               n[2]/=n_len;
            }
				float st[2];
				ass_fread(&st[0],sizeof(float),1,&myfile);
				ass_fread(&st[1],sizeof(float),1,&myfile);
            st[1]=1-st[1];
            more_junk=0;
				ass_fread(&more_junk,sizeof(int),1,&myfile);

            if (!invalid)
            {
					if (vid[vertex1]==-1)
					{
	   				vertex[counter]=msMesh_AddVertex(mesh[tex_id]);
						vid[vertex1]=vertex[counter];
					} else
					{
	               msVertex* oldvert=msMesh_GetVertexAt(mesh[tex_id],vid[vertex1]);
						if ((oldvert->u==st[0]) && (oldvert->v==st[1]))
						{
							vertex[counter]=vid[vertex1];
						} else
						{
		   				vertex[counter]=msMesh_AddVertex(mesh[tex_id]);
						}
					}
               normal[counter]=msMesh_AddVertexNormal(mesh[tex_id]);
               msVertex* vert=msMesh_GetVertexAt(mesh[tex_id],vertex[counter]);
               msVertex_SetVertex(vert,v[vertex1]);
               msMesh_SetVertexNormalAt(mesh[tex_id],normal[counter],n);
               msVertex_SetTexCoords(vert, st);
               msVertex_SetBoneIndex(vert,-1);
            }
			}

         if (!invalid)
         {
            if (no_local_vertices==3)
            {
               msTriangle * tri=msMesh_GetTriangleAt(mesh[tex_id],msMesh_AddTriangle(mesh[tex_id]));
               msTriangle_SetVertexIndices (tri, vertex);
               msTriangle_SetNormalIndices (tri, normal);
               msTriangle_SetSmoothingGroup(tri, 1);
            } else
            if (no_local_vertices==4)
            {
               unsigned short first[3],second[3];
               first[0]=vertex[0];
               first[1]=vertex[1];
               first[2]=vertex[2];
               second[0]=vertex[2];
               second[1]=vertex[3];
               second[2]=vertex[0];
               unsigned short first_n[3],second_n[3];
               first_n[0]=normal[0];
               first_n[1]=normal[1];
               first_n[2]=normal[2];
               second_n[0]=normal[2];
               second_n[1]=normal[3];
               second_n[2]=normal[0];

               msTriangle * tri=msMesh_GetTriangleAt(mesh[tex_id],msMesh_AddTriangle(mesh[tex_id]));
               msTriangle_SetVertexIndices (tri, first);
               msTriangle_SetNormalIndices (tri, first_n);
               msTriangle_SetSmoothingGroup(tri, 1);
               tri=msMesh_GetTriangleAt(mesh[tex_id],msMesh_AddTriangle(mesh[tex_id]));
               msTriangle_SetVertexIndices (tri, second);
               msTriangle_SetNormalIndices (tri, second_n);
               msTriangle_SetSmoothingGroup(tri, 1);
            }
         }

         done_poly++;
		} else 
		{
			myfile.pointer+=size;
		}

		count++;
	}
	while ((myfile.pointer<myfile.size-1) && (done_poly!=no_polygons));

	// C'est fini!
	free(string_text);

    return 0;
}
