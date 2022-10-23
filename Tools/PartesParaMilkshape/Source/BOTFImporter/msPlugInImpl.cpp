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

#include "../common/include/il/il.h"

#define SCALE 0.07

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
    strcpy (szTitle, "Birth of the Federation (HOB)...");
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

// Make us an error message
void errorMessage(char * message)
{
    MessageBox (NULL,message,NULL,MB_OK);
}

int * data;
float *hob_u,*hob_v;
int *hob_uv_vertex;
msMesh * myMesh;

void hob_get_data( int i )
{
	int j;
	if ( data[i+8] == 0 ) {

		msTriangle* myTri=msMesh_GetTriangleAt(myMesh,msMesh_AddTriangle(myMesh));
		int nov=data[i+11];
		unsigned short *v=(unsigned short *)malloc(2*nov);
		for ( j = 0; j < nov; j++ ) {
			int t=data[i+12+j] / 68;
			v[j]=hob_uv_vertex [ t ];
			float uv[2];
			uv[0]=hob_u[t];
			uv[1]=hob_v[t];
			msVertex_SetTexCoords(msMesh_GetVertexAt(myMesh,v[j]),uv);
		}
		if (nov==3)
		{
			msTriangle* tri=msMesh_GetTriangleAt(myMesh,msMesh_AddTriangle(myMesh));
			msTriangle_SetVertexIndices(tri,v);
		} else
		if (nov==4)
		{
			msTriangle* tri=msMesh_GetTriangleAt(myMesh,msMesh_AddTriangle(myMesh));
			msTriangle_SetVertexIndices(tri,v);
			v[1]=v[2];
			v[2]=v[3];
			tri=msMesh_GetTriangleAt(myMesh,msMesh_AddTriangle(myMesh));
			msTriangle_SetVertexIndices(tri,v);
		} else
		{
			msVertex *a=msMesh_GetVertexAt(myMesh,v[0]);
			msVertex *b=msMesh_GetVertexAt(myMesh,v[nov/2]);

			int i;
			int middle=msMesh_AddVertex(myMesh);
			msVertex * midVert=msMesh_GetVertexAt(myMesh,middle);
			midVert->Vertex[0]=(b->Vertex[0]+a->Vertex[0])/2;
			midVert->Vertex[1]=(b->Vertex[1]+a->Vertex[1])/2;
			midVert->Vertex[2]=(b->Vertex[2]+a->Vertex[2])/2;
			midVert->u=(b->u+a->u)/2;
			midVert->v=(b->v+a->v)/2;
			unsigned short _v[3];
			for (i=0;i<nov;i++)
			{
				int first=i;
				int last=i+1;
				if (last==nov) last=0;
				_v[0]=v[first];
				_v[1]=middle;
				_v[2]=v[last];
				msTriangle* tri=msMesh_GetTriangleAt(myMesh,msMesh_AddTriangle(myMesh));
				msTriangle_SetVertexIndices(tri,_v);
			}
		}
		free(v);
	}
}

void hob_check_data( int i )
{
	switch ( data[i] ) {
		case 0:
		case 1:
		case 2:
		case 10:
		case 12:
		case 13:
			if ( data[i+2] > 0) hob_check_data( data[i+2]/4 );
			if ( data[i+3] > 0) hob_check_data( data[i+3]/4 );
			break;
		case 4:
		case 5:
			hob_get_data( data[i+1]/4 );
			if ( data[i+2] > 0) hob_check_data( data[i+2]/4 );
			if ( data[i+3] > 0) hob_check_data( data[i+3]/4 );
			break;
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
    char szDefExt[32] = "hob";
    char szFilter[128] = "HOB Files (*.hob)\0*.hob\0All Files (*.*)\0*.*\0\0";
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
    ofn.lpstrTitle = "Import Birth of the Federation HOB -- assimsoft.com";

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

	// Texture
	char texture[MS_MAX_PATH];
	char oldtexture[MS_MAX_PATH];
	strcpy(texture,szFile);
	texture[strlen(texture)-4]='\0';
	strcpy(oldtexture,texture);
	strcat(texture,".tga");
	strcat(oldtexture,".gif");
	ilInit();
	if (ilLoadImage(oldtexture))
	{
		ilSaveImage(texture);
	}
	myMesh=msModel_GetMeshAt(pModel,msModel_AddMesh(pModel));
	msMaterial * myMaterial=msModel_GetMaterialAt(pModel,msModel_AddMaterial(pModel));
	msMesh_SetMaterialIndex(myMesh,0);
	msMesh_SetName(myMesh,"import");
	msMaterial_SetName(myMaterial,"import");
	msMaterial_SetDiffuseTexture(myMaterial,texture);
	msVec4 Emissive={1,1,1,1};
	msMaterial_SetEmissive(myMaterial,Emissive);

	// Used for polygon working out
	int data_size;
	ass_fread(&data_size,4,1,&myfile);

	// Read in counts
	myfile.pointer=16;
	int uv_count;
	ass_fread(&uv_count,4,1,&myfile);
	int vertex_count;
	ass_fread(&vertex_count,4,1,&myfile);

	// Read 
	myfile.pointer=60;
	int polygon_position;
	ass_fread(&polygon_position,4,1,&myfile);
	int uv_position;
	ass_fread(&uv_position,4,1,&myfile);
	int vertex_position;
	ass_fread(&vertex_position,4,1,&myfile);

	hob_u=(float*)malloc(uv_count*4);
	hob_v=(float*)malloc(uv_count*4);
	hob_uv_vertex=(int*)malloc(uv_count*4);

	// UV info
	myfile.pointer=uv_position;
	int counter;
	for (counter=0;counter<uv_count;counter++)
	{
		myfile.pointer+=16;
		ass_fread(&hob_u[counter],4,1,&myfile);
		ass_fread(&hob_v[counter],4,1,&myfile);
		myfile.pointer+=4;
		ass_fread(&hob_uv_vertex[counter],4,1,&myfile);
		myfile.pointer+=8;
	}

	// Vertices
	myfile.pointer=vertex_position;
	for (counter=0;counter<vertex_count;counter++)
	{
		msVertex * myVertex=msMesh_GetVertexAt(myMesh,msMesh_AddVertex(myMesh));
		float v[3];
		ass_fread(&v,12,1,&myfile);
		myVertex->Vertex[0]=-v[0]*SCALE;
		myVertex->Vertex[1]=-v[1]*SCALE;
		myVertex->Vertex[2]=-v[2]*SCALE;
		myfile.pointer+=8;
	}

	// Polygons (hack?? just copied code from here on)
	myfile.pointer=0;
	data	= (int *)myfile.data;
	hob_check_data(polygon_position/4);

	free(hob_u);
	free(hob_v);
	free(hob_uv_vertex);


    return 0;
}
