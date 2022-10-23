// =========================================================
// | Assimilation Software presents...                     |
// |                                                       |
// |  Milkshape Plugins  - (c) Graham (gameRevolt)         |
// =========================================================

#include "stdafx.h"
#include "msPlugInImpl.h"
#include "msLib.h"

#include "../common/include/il/il.h"
#include "../common/include/il/ilu.h"


void insert_header(FILE * myfile, char header[],bool skip=false);

void insert_NiImage(char mesh_image[],FILE *myfile);
void insert_NiTextureProperty(FILE *myfile, unsigned int img_id);
void insert_NiTextureModeProperty(FILE *myfile, unsigned short flags, unsigned int value);
void insert_NiVertexColorProperty(FILE *myfile);
void insert_NiZBufferProperty(FILE *myfile);
void insert_NiNode(char node_name[],int no_properties,unsigned int *properties,int no_nodes,unsigned int *nodes,int no_blocks,unsigned int *blocks,FILE *myfile);
void insert_NiMaterialProperty(char mat_name[],float ambient[3],float diffuse[3],float shininess,float alpha,FILE *myfile);
void insert_NiTriShape(char mesh_name[],int no_properties,unsigned int *properties,unsigned int data_id,FILE *myfile);

int no_chunks;

#define SCALE 15.6

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
   strcpy (szTitle, "Bridge Commander NIF...");
}



cPlugIn::~cPlugIn ()
{
}



int
cPlugIn::GetType ()
{
    return cMsPlugIn::eTypeExport;
}



const char*
cPlugIn::GetTitle ()
{
    return szTitle;
}

static void MakeShortFileName (const char *szName, char *szOut);

static void
MakeShortFileName (const char *szName, char *szOut)
{
    int j;
    for (j=strlen(szName)-1;j>=0;j--)
    {
        if ((szName[j]=='\\') || (szName[j]=='/')) 
        {
            j++;
            break;
        }
    }
    if (j<0) j=0;

	 strcpy(szOut,szName+j);
}


// Make us an error message
void errorMessage(char * message)
{
    MessageBox (NULL,message,NULL,MB_OK);
}


int
cPlugIn::Execute (msModel *pModel)
{
    if (!pModel)
        return -1;

    //
    // check, if we have something to export
    //
    if (msModel_GetMeshCount (pModel) == 0)
    {
        ::MessageBox (NULL, "The model is empty!  Nothing exported!", "Bridge Commander NIF Export", MB_OK | MB_ICONWARNING);
        return 0;
    }

    no_chunks=0;

    //
    // choose filename
    //
    OPENFILENAME ofn;
    memset (&ofn, 0, sizeof (OPENFILENAME));
    
    char szFile[MS_MAX_PATH];
    char szFileTitle[MS_MAX_PATH];
    char szDefExt[32] = "txt";
    char szFilter[128] = "Bridge Commander NIF Files (*.nif)\0*.nif\0All Files (*.*)\0*.*\0\0";
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
    ofn.lpstrTitle = "Export Bridge Commander NIF -- assimsoft.com";

    if (!::GetSaveFileName (&ofn))
        return 0;

    //
    // export
    //
    FILE *myfile = fopen (szFile, "wb");
    if (!myfile)
        return -1;

    int i;

    //
    // header
    //
    float one=1,zero=0;
    char header[130];
    strcpy(header,"NetImmerse File Format, Version 3.1\nNumerical Design Limited, Chapel Hill, NC 27514\nCopyright (c) 1996-2000\nAll Rights Reserved\n");
    fwrite(header,128,1,myfile);

    //
    // Chunks now
    //
    insert_header(myfile,"Top Level Object",true);

    // Root Node
    unsigned int properties[10];
    properties[0]=no_chunks+1;
    unsigned int nodes[10];
    nodes[0]=no_chunks+2;
    insert_NiNode("",1,properties,1,nodes,0,NULL,myfile);

    // ZBufferProperty
    insert_NiZBufferProperty(myfile);

    // Subroot
    properties[0]=no_chunks+1;
    properties[1]=no_chunks+2;
    nodes[0]=no_chunks+3;
    insert_NiNode("",2,properties,1,nodes,0,NULL,myfile);

    // Subroot properties
    insert_NiTextureModeProperty(myfile,0x00C2,0xFFB50000);
    insert_NiVertexColorProperty(myfile);

    // Real Scene Root
    int no_meshes=msModel_GetMeshCount(pModel);
    unsigned int meshes[20];
    for (i=0;i<no_meshes;i++) meshes[i]=no_chunks+i*7+1;
    insert_NiNode("Scene Root",0,NULL,no_meshes,meshes,0,NULL,myfile);

    // The meshes
    for (i=0;i<no_meshes;i++)
    {
       char mesh_name[MS_MAX_NAME];
       msMesh * pMesh=msModel_GetMeshAt(pModel,i);
       msMesh_GetName(pMesh,mesh_name,MS_MAX_NAME);

       // Holder node
       nodes[0]=no_chunks+1;
       insert_NiNode(mesh_name,0,NULL,1,nodes,0,NULL,myfile);

       // Holder Trishape
       properties[0]=no_chunks+1;
       properties[1]=no_chunks+2;
       properties[2]=no_chunks+4;
       insert_NiTriShape(mesh_name,3,properties,no_chunks+5,myfile);

       // Two minor properties
       insert_NiTextureModeProperty(myfile,0x03D2,0xFFFE0000);
       insert_NiTextureProperty(myfile,no_chunks+1);

       // Image map
       char _mesh_image[MS_MAX_PATH];
       msMaterial* _mat=NULL;
       int mat=msMesh_GetMaterialIndex(pMesh);
       if (mat==-1)
       {
          errorMessage("All meshes must be bound to a material");
			 return 0;
       } else
       {
          _mat=msModel_GetMaterialAt(pModel,mat);
          char mesh_image[MS_MAX_PATH];
          msMaterial_GetDiffuseTexture(_mat,mesh_image,MS_MAX_PATH);
			 if (strcmp(mesh_image,"")==0)
			 {
			 	 errorMessage("All materials must have a texture");
				 return 0;
			 } 

		   // Now ensure that the texture we referenced is valid (a tga file, with optionally embedded lightmap as an alpha channel)
			char newtexture[MS_MAX_PATH];
			strcpy(newtexture,mesh_image);
			newtexture[strlen(newtexture)-4]='\0';
			strcat(newtexture,".tga");
			ilInit();
			if (ilLoadImage(mesh_image))
			{
				char lightmap[MS_MAX_PATH];
				msMaterial_GetAlphaTexture (_mat, lightmap, 128);
				if (strcmp(lightmap,"")!=0)
				{
					// Make the destination (main texture) into a proper RGBA
					if (!ilConvertImage(IL_RGBA,IL_UNSIGNED_BYTE)) 
					{
						errorMessage("Error resampling texture");
						return 0;
					}

					// Get a handle to the image
					int dest_width=ilGetInteger(IL_IMAGE_WIDTH);
					int dest_height=ilGetInteger(IL_IMAGE_HEIGHT);
					ILubyte *dest=(ILubyte *)malloc(dest_width*dest_height*4);
					ilCopyPixels(0,0,0,dest_width,dest_height,1,IL_RGBA,IL_UNSIGNED_BYTE,dest);

					if (ilLoadImage(lightmap))
					{
						// Get a handle to the image
						ILubyte *source=ilGetData();
						int source_width=ilGetInteger(IL_IMAGE_WIDTH);
						int source_height=ilGetInteger(IL_IMAGE_HEIGHT);
						int source_type=ilGetInteger(IL_IMAGE_FORMAT);
						if (source_type!=IL_COLOR_INDEX) 
						{
							ilConvertImage(IL_COLOUR_INDEX,IL_UNSIGNED_BYTE);
							source=ilGetData();
						}
						if ((source_width!=dest_width) || (source_height!=dest_height)) 
						{
							iluScale(dest_width,dest_height,1);
							source_width=dest_width;
							source_height=dest_height;
							source=ilGetData();
						}
						ILubyte *pal=ilGetPalette();

						int x,y;
						for (y=0;y<source_height;y++)
						{
							for (x=0;x<source_width;x++)
							{
								unsigned char alpha=*(source+y*source_width+x);
								*(dest+y*source_width*4+x*4+3)=pal[alpha*3];
							}
						}

						if (!ilConvertImage(IL_RGBA,IL_UNSIGNED_BYTE)) 
						{
							errorMessage("Error resampling image");
							return 0;
						}
						ilSetData(dest);
					}

					free(dest);
				}

				ilSaveImage(newtexture);
			}

          MakeShortFileName(newtexture,_mesh_image);
       }
       insert_NiImage(_mesh_image,myfile);

       // Material
       float shininess=0;
       float alpha=1;
       float ambient[4]={0,0,0};
       float diffuse[4]={1,1,1};
       char mat_name[MS_MAX_NAME];
       strcpy(mat_name,"");
       if (_mat)
       {
          msMaterial_GetAmbient(_mat,ambient);
          msMaterial_GetDiffuse(_mat,diffuse);
          shininess=msMaterial_GetShininess(_mat);
          alpha=msMaterial_GetTransparency(_mat);
          msMaterial_GetName(_mat,mat_name,MS_MAX_NAME);
       }
       insert_NiMaterialProperty(mat_name,ambient,diffuse,shininess,alpha,myfile);

       // Actual mesh
       // ===========

       insert_header(myfile,"NiTriShapeData");
       unsigned short nov=msMesh_GetVertexCount(pMesh);
       fwrite(&nov,2,1,myfile);

       // Vertices
       unsigned int silly_id=11+i;
       fwrite(&silly_id,4,1,myfile);
       int j;
       for (j=0;j<nov;j++)
       {
          msVertex * v=msMesh_GetVertexAt(pMesh,j);
          float _v[3];
          msVertex_GetVertex(v,_v);
			 _v[0]*=SCALE;
			 _v[1]*=SCALE;
			 _v[2]*=SCALE;
          fwrite(&_v[0],4,1,myfile);
          fwrite(&_v[2],4,1,myfile);
          fwrite(&_v[1],4,1,myfile);
       }

       // Normals
       silly_id=33+i;
       fwrite(&silly_id,4,1,myfile);
       int k;
       for (j=0;j<nov;j++)
       {
          float n[3]={0,0,0};

          // Find a polygon that uses this vertex, so we can get the normal
          for (k=0;k<msMesh_GetTriangleCount(pMesh);k++)
          {
             msTriangle * tri=msMesh_GetTriangleAt(pMesh,k);
             unsigned short vi[3];
             unsigned short normals[3];
             msTriangle_GetVertexIndices(tri,vi);
             msTriangle_GetNormalIndices(tri,normals);
             int l;
             for (l=0;l<3;l++)
             {
                if (vi[l]==j) 
                {
                   msMesh_GetVertexNormalAt(pMesh,normals[l],n);
                   break;
                }
             }
             if (l!=3) break;
          }
          fwrite(&n[0],4,1,myfile);
          fwrite(&n[2],4,1,myfile);
          fwrite(&n[1],4,1,myfile);
       }

       // Unknown inter-stuff
       unsigned int temp=0;
       fwrite(&temp,4,1,myfile);
       fwrite(&temp,4,1,myfile);
       float temp3;
       temp3=(float)15.70985;
       fwrite(&temp3,4,1,myfile);
       temp3=(float)33.33814;
       fwrite(&temp3,4,1,myfile);
       fwrite(&temp,4,1,myfile);

       // UV
       unsigned short temp2=1;
       fwrite(&temp2,2,1,myfile);
       silly_id=55+i;
       fwrite(&silly_id,4,1,myfile);
       for (j=0;j<nov;j++)
       {
          msVertex * v=msMesh_GetVertexAt(pMesh,j);
          float uv[2];
          msVertex_GetTexCoords(v,uv);
          fwrite(uv,8,1,myfile);
       }

       // Triangles
       unsigned short nop=msMesh_GetTriangleCount(pMesh);
       fwrite(&nop,2,1,myfile);
       temp=nop*3;
       fwrite(&temp,4,1,myfile);
       for (j=0;j<nop;j++)
       {
          msTriangle * tri=msMesh_GetTriangleAt(pMesh,j);
          unsigned short vi[3];
          msTriangle_GetVertexIndices(tri,vi);
          fwrite(&vi[2],2,1,myfile);
          fwrite(&vi[1],2,1,myfile);
          fwrite(&vi[0],2,1,myfile);
       }

       // ?. But needs to be zero to finish off
       temp2=0;
       fwrite(&temp2,2,1,myfile);
    }

    // 
    // Tail
    // 
    insert_header(myfile,"End Of File",true);

    //
    // Finish
    //

    fclose (myfile);

    // dont' forget to destroy the model
    msModel_Destroy (pModel);

    return 0;
}

void insert_header(FILE * myfile, char header[],bool skip)
{
   int len=strlen(header);
   fwrite(&len,4,1,myfile);
   fwrite(header,len,1,myfile);
   if (!skip)
   {
      fwrite(&no_chunks,4,1,myfile);
   }
   no_chunks++;
}

void insert_NiImage(char mesh_image[],FILE *myfile)
{
   insert_header(myfile,"NiImage");

   unsigned char temp=1;
   fwrite(&temp,1,1,myfile);
   unsigned int len=strlen(mesh_image);
   fwrite(&len,4,1,myfile);
   fwrite(mesh_image,len,1,myfile);
   unsigned int temp2=7;
   fwrite(&temp2,4,1,myfile);
   float temp3=(float)128.5;
   fwrite(&temp3,4,1,myfile);
}

void insert_NiTextureModeProperty(FILE *myfile, unsigned short flags, unsigned int value)
{
   insert_header(myfile,"NiTextureModeProperty");

   unsigned int temp=0;
   fwrite(&temp,4,1,myfile);
   fwrite(&temp,4,1,myfile);
   fwrite(&temp,4,1,myfile);
   fwrite(&flags,2,1,myfile);
   fwrite(&value,4,1,myfile);
}

void insert_NiTextureProperty(FILE *myfile, unsigned int img_id)
{
   insert_header(myfile,"NiTextureProperty");

   unsigned int temp=0;
   fwrite(&temp,4,1,myfile);
   fwrite(&temp,4,1,myfile);
   fwrite(&temp,4,1,myfile);
   fwrite(&temp,2,1,myfile);
   fwrite(&img_id,4,1,myfile);
}

void insert_NiVertexColorProperty(FILE *myfile)
{
   insert_header(myfile,"NiVertexColorProperty");

   unsigned int temp=0;
   fwrite(&temp,4,1,myfile);
   fwrite(&temp,4,1,myfile);
   fwrite(&temp,4,1,myfile);
   fwrite(&temp,4,1,myfile);
   fwrite(&temp,2,1,myfile);
   temp=1;
   fwrite(&temp,4,1,myfile);
}

void insert_NiZBufferProperty(FILE *myfile)
{
   insert_header(myfile,"NiZBufferProperty");

   unsigned int temp=0;
   fwrite(&temp,4,1,myfile);
   fwrite(&temp,4,1,myfile);
   fwrite(&temp,4,1,myfile);
   unsigned short temp2=3;
   fwrite(&temp2,2,1,myfile);
}

void insert_NiNode(char node_name[],int no_properties,unsigned int *properties,int no_nodes,unsigned int *nodes,int no_blocks,unsigned int *blocks,FILE *myfile)
{
   insert_header(myfile,"NiNode");

   unsigned int len=strlen(node_name);
   fwrite(&len,4,1,myfile);
   fwrite(node_name,len,1,myfile);

   unsigned int temp=0;
   fwrite(&temp,4,1,myfile);
   fwrite(&temp,4,1,myfile);
   unsigned short temp2=12;
   fwrite(&temp2,2,1,myfile);

   float zero=0;
   float one=1;

   fwrite(&zero,4,1,myfile);
   fwrite(&zero,4,1,myfile);
   fwrite(&zero,4,1,myfile);

   fwrite(&one,4,1,myfile);
   fwrite(&zero,4,1,myfile);
   fwrite(&zero,4,1,myfile);

   fwrite(&zero,4,1,myfile);
   fwrite(&one,4,1,myfile);
   fwrite(&zero,4,1,myfile);

   fwrite(&zero,4,1,myfile);
   fwrite(&zero,4,1,myfile);
   fwrite(&one,4,1,myfile);

   fwrite(&one,4,1,myfile);
   fwrite(&zero,4,1,myfile);
   fwrite(&zero,4,1,myfile);

   fwrite(&zero,4,1,myfile);

   fwrite(&no_properties,4,1,myfile);
   fwrite(properties,4*no_properties,1,myfile);

   fwrite(&zero,4,1,myfile);

   fwrite(&no_nodes,4,1,myfile);
   fwrite(nodes,4*no_nodes,1,myfile);

   fwrite(&no_blocks,4,1,myfile);
   fwrite(blocks,4*no_blocks,1,myfile);
}

void insert_NiMaterialProperty(char mat_name[],float ambient[3],float diffuse[3],float shininess,float alpha,FILE *myfile)
{
   insert_header(myfile,"NiMaterialProperty");

   unsigned int len=strlen(mat_name);
   fwrite(&len,4,1,myfile);
   fwrite(mat_name,len,1,myfile);
   unsigned int temp=0;
   fwrite(&temp,4,1,myfile);
   fwrite(&temp,4,1,myfile);
   unsigned short temp2=1;
   fwrite(&temp2,2,1,myfile);
   fwrite(ambient,12,1,myfile);
   fwrite(diffuse,12,1,myfile);
   float temp3=0;
   fwrite(&temp3,4,1,myfile);
   fwrite(&temp3,4,1,myfile);
   fwrite(&temp3,4,1,myfile);
   fwrite(&temp,4,1,myfile);
   fwrite(&temp,4,1,myfile);
   fwrite(&temp,4,1,myfile);
   fwrite(&shininess,4,1,myfile);
   fwrite(&alpha,4,1,myfile);
}

void insert_NiTriShape(char mesh_name[],int no_properties,unsigned int *properties,unsigned int data_id,FILE *myfile)
{
   insert_header(myfile,"NiTriShape");

   unsigned int len=strlen(mesh_name);
   fwrite(&len,4,1,myfile);
   fwrite(mesh_name,len,1,myfile);
   unsigned int temp=0;
   fwrite(&temp,4,1,myfile);
   fwrite(&temp,4,1,myfile);
   unsigned short temp2=4;
   fwrite(&temp2,2,1,myfile);

   float zero=0;
   float one=1;

   fwrite(&zero,4,1,myfile);
   fwrite(&zero,4,1,myfile);
   fwrite(&zero,4,1,myfile);

   fwrite(&one,4,1,myfile);
   fwrite(&zero,4,1,myfile);
   fwrite(&zero,4,1,myfile);

   fwrite(&zero,4,1,myfile);
   fwrite(&one,4,1,myfile);
   fwrite(&zero,4,1,myfile);

   fwrite(&zero,4,1,myfile);
   fwrite(&zero,4,1,myfile);
   fwrite(&one,4,1,myfile);

   fwrite(&one,4,1,myfile);
   fwrite(&zero,4,1,myfile);
   fwrite(&zero,4,1,myfile);

   fwrite(&zero,4,1,myfile);

   fwrite(&no_properties,4,1,myfile);
   fwrite(properties,4*no_properties,1,myfile);

   fwrite(&temp,4,1,myfile);

   fwrite(&data_id,4,1,myfile);
}
