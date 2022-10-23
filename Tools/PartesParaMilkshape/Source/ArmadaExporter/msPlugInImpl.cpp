// =========================================================
// | Assimilation Software presents...                     |
// |                                                       |
// |  Milkshape Plugins  - (c) Graham (gameRevolt)         |
// =========================================================

#include "stdafx.h"
#include "msPlugInImpl.h"
#include "msLib.h"
#include <math.h>
#include "../common/include/il/il.h"
#include "../common/include/il/ilu.h"
#include "../common/include/maths.h"

void write_mesh(msModel * pModel, msMesh * pMesh, FILE * file,ass_matrix * matrix);
bool start_recursion(msModel * pModel, const char * parent, FILE * file, ass_matrix * current);
void AngleMatrix (const msVec3 angles, float matrix[4][4]);

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

#define SCALE 2.577


cMsPlugIn*
CreatePlugIn ()
{
    return new cPlugIn ();
}



cPlugIn::cPlugIn ()
{
    strcpy (szTitle, "Armada SOD...");
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

// Make us an error message
void errorMessage(char * message)
{
    MessageBox (NULL,message,NULL,MB_OK);
}

char texture_type[30][30];
int armadaVersion;
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
        ::MessageBox (NULL, "The model is empty!  Nothing exported!", "Armada SOD Export", MB_OK | MB_ICONWARNING);
        return 0;
    }

    //
    // choose filename
    //
    OPENFILENAME ofn;
    memset (&ofn, 0, sizeof (OPENFILENAME));
    
    char szFile[MS_MAX_PATH];
    char szFileTitle[MS_MAX_PATH];
    char szDefExt[32] = "sod";
    char szFilter[128] = "Armada 1 SOD Files (*.sod)\0*.sod\0Armada 2 SOD Files (*.sod)\0*.sod\0\0";
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
    ofn.lpstrTitle = "Export Armada SOD -- assimsoft.com";

    if (!::GetSaveFileName (&ofn))
        return 0;

	 armadaVersion=ofn.nFilterIndex;

    //
    // export
    //
    FILE *file = fopen (szFile, "wb");
    if (!file)
        return -1;

    int i;
    char szName[MS_MAX_PATH];

    //
    // header
    //
    float one=1,zero=0;
    char header[20];
    strcpy(header,"Storm3D_SW");
	 float version;
	 if (armadaVersion==2)
		version=(float)1.93;
    else version=(float)1.8;
    fwrite(header,strlen(header),1,file);
    fwrite(&version,4,1,file);

    //
    // materials
    //
    unsigned short mat=msModel_GetMaterialCount (pModel);
    fwrite(&mat,2,1,file);
    for (i = 0; i < msModel_GetMaterialCount (pModel); i++)
    {
        // Start
        msMaterial *pMaterial = msModel_GetMaterialAt (pModel, i);
        msMaterial_GetName (pMaterial, szName, MS_MAX_NAME);
        unsigned short len=strlen(szName);
        fwrite (&len,2,1,file);
        fwrite (szName,len,1,file);

        // Colors
        msVec4 vec4;
        msMaterial_GetAmbient (pMaterial, vec4);
        fwrite(&vec4[0],4,1,file);
        fwrite(&vec4[1],4,1,file);
        fwrite(&vec4[2],4,1,file);
        msMaterial_GetDiffuse (pMaterial, vec4);
        fwrite(&vec4[0],4,1,file);
        fwrite(&vec4[1],4,1,file);
        fwrite(&vec4[2],4,1,file);
        msMaterial_GetSpecular (pMaterial, vec4);
        fwrite(&vec4[0],4,1,file);
        fwrite(&vec4[1],4,1,file);
        fwrite(&vec4[2],4,1,file);
        float s=4;
        fwrite(&s,4,1,file);

        // Light model
        unsigned char light_model=1; // default is lambert
        if (strnicmp(szName,"!constant_",10)==0) light_model=0;
         else if (strnicmp(szName,"!lambert_",9)==0) light_model=1;
         else if (strnicmp(szName,"!phong_",7)==0) light_model=2;
        fwrite(&light_model,1,1,file);
		  if (armadaVersion==2)
		  {
           unsigned char unknown=0;
           fwrite(&unknown,1,1,file);
		  }

        // Texture type
        strcpy(texture_type[i],"default");
		  if (armadaVersion==2) strcpy(texture_type[i],"default");
        char * place=strrchr(szName,'_');
        if ((place) && (*(place+1)=='!') && (strlen(place+1)>3)) strcpy(texture_type[i],place+2);
    }

	 if (msModel_GetBoneCount(pModel)==0)
	 {
		 //
		 // hierachy
		 //
		 short nodes=11+msModel_GetMeshCount (pModel);
		 fwrite(&nodes,2,1,file);
		 for (i=0;i<11;i++)
		 {
			  // Node type
			  unsigned short node_type=0;

			  // Hierachy position
			  char identifier[30];
			  char parent[30];
			  strcpy(identifier,"");
			  strcpy(parent,"");
			  if (i==0)
			  {
					strcpy(identifier,"root");
			  }
			  if (i==1)
			  {
					strcpy(identifier,"hardpoints");
					strcpy(parent,"root");
			  }
			  if (i==2)
			  {
					strcpy(identifier,"damage");
					strcpy(parent,"root");
			  }
			  if (i==3)
			  {
					strcpy(identifier,"borg");
					strcpy(parent,"damage");
			  }
			  if (i==4)
			  {
					strcpy(identifier,"crew");
					strcpy(parent,"damage");
			  }
			  if (i==5)
			  {
					strcpy(identifier,"target");
					strcpy(parent,"damage");
			  }
			  if (i==6)
			  {
					strcpy(identifier,"engines");
					strcpy(parent,"damage");
			  }
			  if (i==7)
			  {
					strcpy(identifier,"life");
					strcpy(parent,"damage");
			  }
			  if (i==8)
			  {
					strcpy(identifier,"sensors");
					strcpy(parent,"damage");
			  }
			  if (i==9)
			  {
					strcpy(identifier,"shield");
					strcpy(parent,"damage");
			  }
			  if (i==10)
			  {
					strcpy(identifier,"lights");
					strcpy(parent,"root");
			  }

			  // Write in data
			  fwrite(&node_type,2,1,file);
			  unsigned short len=strlen(identifier);
			  fwrite(&len,2,1,file);
			  fwrite(identifier,len,1,file);
			  len=strlen(parent);
			  fwrite(&len,2,1,file);
			  fwrite(&parent,len,1,file);
			  fwrite(&one,4,1,file);
			  fwrite(&zero,4,1,file);
			  fwrite(&zero,4,1,file);
			  fwrite(&zero,4,1,file);
			  fwrite(&one,4,1,file);
			  fwrite(&zero,4,1,file);
			  fwrite(&zero,4,1,file);
			  fwrite(&zero,4,1,file);
			  fwrite(&one,4,1,file);
			  fwrite(&zero,4,1,file);
			  fwrite(&zero,4,1,file);
			  fwrite(&zero,4,1,file);
		 }

		 //
		 // mesh nodes
		 //
		 for (i = 0; i < msModel_GetMeshCount (pModel); i++)
		 {
			  msMesh *pMesh = msModel_GetMeshAt (pModel, i);

			  // 
			  // node stuff
			  // 

			  // Node type
			  unsigned short node_type=1;

			  // Hierachy position
			  char identifier[128];
			  msMesh_GetName (pMesh, identifier, 128);
			  char parent[30];
			  strcpy(parent,"root");

			  // Write in data
			  fwrite(&node_type,2,1,file);
			  unsigned short len=strlen(identifier);
			  fwrite(&len,2,1,file);
			  fwrite(identifier,len,1,file);
			  len=strlen(parent);
			  fwrite(&len,2,1,file);
			  fwrite(&parent,len,1,file);
			  float one=1,zero=0;
			  fwrite(&one,4,1,file);
			  fwrite(&zero,4,1,file);
			  fwrite(&zero,4,1,file);
			  fwrite(&zero,4,1,file);
			  fwrite(&one,4,1,file);
			  fwrite(&zero,4,1,file);
			  fwrite(&zero,4,1,file);
			  fwrite(&zero,4,1,file);
			  fwrite(&one,4,1,file);
			  fwrite(&zero,4,1,file);
			  fwrite(&zero,4,1,file);
			  fwrite(&zero,4,1,file);

			  ass_matrix identity;
 			 write_mesh(pModel,pMesh,file,&identity);
		 }
	 } else
	 {
		 short nodes=msModel_GetBoneCount (pModel);
		 fwrite(&nodes,2,1,file);

		 // Do all root nodes on the first recursion level
		 ass_matrix identity;
		 if (!start_recursion(pModel,"",file,&identity)) return 0;
	 }
 
    int zeroint=0;
    fwrite(&zeroint,4,1,file);

    fclose (file);

    // dont' forget to destroy the model
    msModel_Destroy (pModel);

    return 0;
}

bool start_recursion(msModel * pModel, const char * parent, FILE * file, ass_matrix * current)
{
	 int i;
	 for (i = 0; i < msModel_GetBoneCount (pModel); i++)
	 {
		 msBone * myBone=msModel_GetBoneAt(pModel,i);
		 bool child=false;
		 if ((strcmp(myBone->szParentName,parent)==0) && (myBone->szParentName[1]!='_')) child=true;
		 if ((myBone->szParentName[1]=='_') && (strcmp(myBone->szParentName+2,parent)==0)) child=true;
		 if (child)
		 {
			 unsigned short node_type;

			 if ((myBone->szName[1]!='_') || (myBone->szName[0]=='h')) // Standard node
			 {
				 node_type=0;
			 } else
			 if (myBone->szName[0]=='s') // Sprite
			 {
				 node_type=3;
			 } else
			 if (myBone->szName[0]=='e') // Emitter
			 {
				 node_type=12;
			 } else
			 if (myBone->szName[0]=='m') // Mesh
			 {
				 node_type=1;
			 } else
			 if (myBone->szName[0]=='l') // LOD Control
			 {
				 node_type=11;
			 }

			 // Write in data
			 fwrite(&node_type,2,1,file);
			 char newname[30];
			 if (myBone->szName[1]!='_')
			 {
				 strcpy(newname,myBone->szName);
			 } else strcpy(newname,myBone->szName+2);
			 unsigned short len=strlen(newname);
			 fwrite(&len,2,1,file);
			 fwrite(newname,len,1,file);
			 len=strlen(parent);
			 fwrite(&len,2,1,file);
			 fwrite(parent,len,1,file);
			
			 // Transform matrix
			 ass_matrix newmatrix;
			 AngleMatrix(myBone->Rotation,newmatrix.m);
			 newmatrix.pos_x=-myBone->Position[0]*SCALE;
			 newmatrix.pos_y=myBone->Position[1]*SCALE;
			 newmatrix.pos_z=myBone->Position[2]*SCALE;
			 newmatrix.multiply_by(current->calculate_inverse());
			 fwrite(&newmatrix.right_x,4,1,file);
			 fwrite(&newmatrix.right_y,4,1,file);
			 fwrite(&newmatrix.right_z,4,1,file);
			 fwrite(&newmatrix.up_x,4,1,file);
			 fwrite(&newmatrix.up_y,4,1,file);
			 fwrite(&newmatrix.up_z,4,1,file);
			 fwrite(&newmatrix.front_x,4,1,file);
			 fwrite(&newmatrix.front_y,4,1,file);
			 fwrite(&newmatrix.front_z,4,1,file);
			 fwrite(&newmatrix.pos_x,4,1,file);
			 fwrite(&newmatrix.pos_y,4,1,file);
			 fwrite(&newmatrix.pos_z,4,1,file);

			 // Special data
			 if (node_type==12)
			 {
				 unsigned short len=strlen(newname);
				 fwrite(&len,2,1,file);
				 fwrite(newname,len,1,file);
			 } else
			 if (node_type==1)
			 {
				 // Find the matching mesh
				 int j;
				 msMesh * myMesh=NULL;
				 for (j = 0; j < msModel_GetMeshCount (pModel); j++)
				 {
					 myMesh=msModel_GetMeshAt(pModel,j);
					 if (strcmp(myMesh->szName,newname)==0)
					 {
						 break;
					 }
				 }
				 if (j==msModel_GetMeshCount (pModel))
				 {
					 errorMessage("Couldn't match a mesh node with a mesh");
					 return false;
				 } else write_mesh(pModel,myMesh,file,&newmatrix);
			 }

			 // Recurse
			 if (myBone->szName[1]!='_') start_recursion(pModel,myBone->szName,file,&newmatrix);
				else start_recursion(pModel,myBone->szName+2,file,&newmatrix);
		 }
	 }

	 return true;
}

void write_mesh(msModel * pModel,msMesh * pMesh, FILE * file, ass_matrix * matrix)
{
     //
     // material related stuff
     //
     int m=msMesh_GetMaterialIndex (pMesh);
     if (m>=0)
     {
        if (strcmp(texture_type[m],"noalpha")==0)
        {
           char default_type[30];
           strcpy(default_type,"default");
           unsigned short temp=strlen(default_type);
           fwrite(&temp,2,1,file);
           fwrite(default_type,strlen(default_type),1,file);
        }
        else {
           unsigned short temp=strlen(texture_type[m]);
           fwrite(&temp,2,1,file);
           fwrite(texture_type[m],strlen(texture_type[m]),1,file);
        }
     } else
     {
		  errorMessage("All meshes must be bound to a material");
		  return;
     }
	  unsigned int unknown;
	  if (armadaVersion==2)
	  {
		  unknown=4;
		  if ((m>=0) && (strcmp(texture_type[m],"noalpha")==0)) unknown=0;
		  fwrite(&unknown,4,1,file); // Alpha
		  unknown=1;
		  fwrite(&unknown,4,1,file); // Textures
	  }
     msMaterial * pMaterial=NULL;
     pMaterial = msModel_GetMaterialAt (pModel, m);

     char szName[MS_MAX_PATH];
     msMaterial_GetDiffuseTexture (pMaterial, szName, 128);
	  if (strcmp(szName,"")==0)
	  {
		  errorMessage("All materials must have a texture");
		  return;
	  }
	  int j;
     for (j=strlen(szName)-1;j>=0;j--)
     {
         if (szName[j]=='.') szName[j]='\0';
         if ((szName[j]=='\\') || (szName[j]=='/')) 
         {
             j++;
             break;
         }
     }
     if (j==-1) j=0;
     int len=strlen(szName+j);
     fwrite(&len,2,1,file);
     fwrite(szName+j,len,1,file);
	  if (armadaVersion==2)
	  {
		  unknown=0;
		  fwrite(&unknown,4,1,file);
		  fwrite(&unknown,4,1,file);
	  }

	  // Now ensure that the texture we referenced is valid (a tga file, with optionally embedded lightmap as an alpha channel)
	   msMaterial_GetDiffuseTexture (pMaterial, szName, 128);
		char newtexture[MS_MAX_PATH];
		strcpy(newtexture,szName);
		newtexture[strlen(newtexture)-4]='\0';
		strcat(newtexture,".tga");
		ilInit();
		if (ilLoadImage(szName))
		{
			char lightmap[MS_MAX_PATH];
			msMaterial_GetAlphaTexture (pMaterial, lightmap, 128);
			if (strcmp(lightmap,"")!=0)
			{
				// Make the destination (main texture) into a proper RGBA
				if (!ilConvertImage(IL_RGBA,IL_UNSIGNED_BYTE)) 
				{
					errorMessage("Error resampling texture");
					return;
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
						return;
					}
					ilSetData(dest);
				}

				free(dest);
			}

			ilSaveImage(newtexture);
		}

     //
     // counts
     //
     unsigned short v=msMesh_GetVertexCount (pMesh);
     fwrite(&v,2,1,file);
     fwrite(&v,2,1,file); // This is for number of tex coords
     unsigned short temp;
     temp=1; // one lighting group
     fwrite(&temp,2,1,file);

     //
     // vertices
     //
     for (j = 0; j < msMesh_GetVertexCount (pMesh); j++)
     {
         msVertex *pVertex = msMesh_GetVertexAt (pMesh, j);
         ass_vector Vertex;

         msVertex_GetVertex (pVertex, Vertex.v);
			Vertex.v[0]*=-SCALE;
			Vertex.v[1]*=SCALE;
			Vertex.v[2]*=SCALE;

			matrix->calculate_inverse()->apply_to_vector(&Vertex);	

         fwrite(&Vertex.v[0],4,1,file);
         fwrite(&Vertex.v[1],4,1,file);
         fwrite(&Vertex.v[2],4,1,file);
     }

     //
     // texture coords
     //
     for (j = 0; j < msMesh_GetVertexCount (pMesh); j++)
     {
         msVertex *pVertex = msMesh_GetVertexAt (pMesh, j);
         msVec2 uv;

         msVertex_GetTexCoords (pVertex, uv);

         fwrite(&uv[0],4,1,file);
         fwrite(&uv[1],4,1,file);
     }

     //
     // number of faces
     //
     unsigned short tri=msMesh_GetTriangleCount (pMesh);
     fwrite(&tri,2,1,file);

     //
     // lighting material
     //
     if (pMaterial) msMaterial_GetName (pMaterial, szName, MS_MAX_NAME);
      else strcpy(szName,"");
     len=strlen(szName);
     fwrite(&len,2,1,file);
     fwrite(&szName,len,1,file);

     //
     // triangles
     //
     for (j = 0; j < msMesh_GetTriangleCount (pMesh); j++)
     {
         msTriangle *pTriangle = msMesh_GetTriangleAt (pMesh, j);
         
         word nIndices[3];
         msTriangle_GetVertexIndices (pTriangle, nIndices);

         unsigned short a,b,c; 
         a=nIndices[0];
         b=nIndices[1];
         c=nIndices[2];

         fwrite(&a,2,1,file);
         fwrite(&a,2,1,file);
         fwrite(&b,2,1,file);
         fwrite(&b,2,1,file);
         fwrite(&c,2,1,file);
         fwrite(&c,2,1,file);
     }

     //
     // finish off
     //
     unsigned char cull=1; // =backface cull
     unsigned short junk=0;
     fwrite(&cull,1,1,file);
     fwrite(&junk,2,1,file);
}

void AngleMatrix (const msVec3 angles, float matrix[4][4])
{
	float		sr, sp, sy, cr, cp, cy;
	
	sy = sin(angles[2]);
	cy = cos(angles[2]);
	sp = sin(angles[1]);
	cp = cos(angles[1]);
	sr = sin(angles[0]);
	cr = cos(angles[0]);

	// matrix = (Z * Y) * X
	matrix[0][0] = cp*cy;
	matrix[0][1] = cp*sy;
	matrix[0][2] = -sp;
	matrix[0][3] = 0.0;
	matrix[1][0] = sr*sp*cy+cr*-sy;
	matrix[1][1] = sr*sp*sy+cr*cy;
	matrix[1][2] = sr*cp;
	matrix[1][3] = 0.0;
	matrix[2][0] = (cr*sp*cy+-sr*-sy);
	matrix[2][1] = (cr*sp*sy+-sr*cy);
	matrix[2][2] = cr*cp;
	matrix[2][3] = 0.0;
	matrix[3][0] = 0.0;
	matrix[3][1] = 0.0;
	matrix[3][2] = 0.0;
	matrix[3][3] = 1.0;
}
