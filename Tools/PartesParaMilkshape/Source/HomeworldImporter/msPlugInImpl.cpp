// =========================================================
// | Assimilation Software presents...                     |
// |                                                       |
// |  Milkshape Plugins  - (c) Graham (gameRevolt)         |
// =========================================================

#include "stdafx.h"
#include "msPlugInImpl.h"
#include "msLib.h"

#include <math.h>
#include "maths.h"
#include <sys/stat.h>

void convert_lif(char *filename);

#define MAX_VERTICES 5000

#define SCALE 0.133

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
    strcpy (szTitle, "Homeworld (GEO/PEO)...");
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


struct
{
	int version; // File version.
	int pName; // Offset to a file name.
	int fileSize; // File size (in bytes), not counting this header.
	int localSize; // Object size (in bytes).
	int nPublicMaterials; // Number of public materials.
	int nLocalMaterials; // Number of local materials.
	int oPublicMaterial; //list of public materials
	int oLocalMaterial; //list of local materials
	int nPolygonObjects; // Number of polygon objects.
	char reserved[24]; // Reserved for future use.
} GeoFileHeader;

struct
{
	int pName; // Offset to name of material (may be a CRC32).
	int ambient; // Ambient color information.
	int diffuse; // Diffuse color information.
	int specular; // Specular color information.
	float kAlpha; // Alpha blending information.
	int texture; // Pointer to texture information (or CRC32).
	short flags; // Flags for this material.
	char nFullAmbient; // Number of self-illuminating colors.
	char bTexturesRegistered; // Set to TRUE when texture registered.
	int textureNameSave; // After the texture has been registered
} materialentry; 

struct
{
	int pName; // Name for animation.
	char flags; // General flags (see above)
	char iObject; // fixed up at load time so we know what object index we have when recursively processing
	short nameCRC; // 16-bit CRC of name 
	int nVertices; // Number of vertices in vertex list for this object.
	int nFaceNormals; // Number of face normals for this object.
	int nVertexNormals; // Number of vertex normals for this object.
	int nPolygons; // Number of polygons in this object.
	int pVertexList; // Offset to the vertex list in this object.
	int pFaceNormalList; // Offset to the normal list in this object.
	int pVertexNormalList; // Offset to the normal list in this object.
	int pPolygonList; // Offset to the polygon list in this object.
	int pMother; // link to parent object
	int pDaughter; // link to child object
	int pSister; // link to sibling object
	float localMatrix[4][4];
} polygonobject; 

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
    char szDefExt[32] = "peo";
    char szFilter[128] = "PEO Files (*.peo)\0*.peo\0GEO Files (*.geo)\0*.geo\0All Files (*.*)\0*.*\0\0";
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
    ofn.lpstrTitle = "Import Homeworld GEO/PEO -- assimsoft.com";

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

	// Check magic string
	char temp[10];
	ass_fread(temp,8,1,&myfile);
	if (!((temp[0]=='R') && (temp[1]=='M') && (temp[2]=='F') && (temp[3]=='9') && (temp[4]=='9') && (temp[5]=='b') && (temp[6]=='a'))) 
	{
		errorMessage("Magic string broken");
		return 0;
	}

	// Read header
	ass_fread(&GeoFileHeader,sizeof(GeoFileHeader),1,&myfile);

	int marker=myfile.pointer;

	// Read materials
	int counter;
	for (counter=0;counter<GeoFileHeader.nPublicMaterials+GeoFileHeader.nLocalMaterials;counter++)
	{
		if (counter<GeoFileHeader.nPublicMaterials) 
			myfile.pointer=GeoFileHeader.oPublicMaterial+counter*sizeof(materialentry);
		else 
			myfile.pointer=GeoFileHeader.oLocalMaterial+(counter-GeoFileHeader.nPublicMaterials)*sizeof(materialentry);

		ass_fread(&materialentry,sizeof(materialentry),1,&myfile);

		myfile.pointer=materialentry.texture;

		msMaterial *myMat=msModel_GetMaterialAt(pModel,msModel_AddMaterial(pModel));

		// Texture
		char temp_string[35];
		int t=0;
		do
		{
			ass_fread(&temp_string[t],1,1,&myfile);
			t++;
		}
		while (temp_string[t-1]!='\0');
		msMaterial_SetName(myMat,temp_string);
		strcat(temp_string,".lif");
		convert_lif(temp_string);
		msMaterial_SetDiffuseTexture(myMat,temp_string);

      // Two sided
//         material_twosided[counter]=(materialentry.flags&8)!=0;

      // Lighting
		float ambient[4],diffuse[4],specular[4];
      ambient[0]=(float)((materialentry.ambient)&256)/256.0;
      ambient[1]=(float)((materialentry.ambient>>8)&256)/256.0;
      ambient[2]=(float)((materialentry.ambient>>16)&256)/256.0;
		ambient[3]=1;
		msMaterial_SetAmbient(myMat,ambient);
      diffuse[0]=(float)((materialentry.diffuse)&256)/256.0;
      diffuse[1]=(float)((materialentry.diffuse>>8)&256)/256.0;
      diffuse[2]=(float)((materialentry.diffuse>>16)&256)/256.0;
		diffuse[3]=1;
		msMaterial_SetDiffuse(myMat,diffuse);
      specular[0]=(float)((materialentry.specular)&256)/256.0;
      specular[1]=(float)((materialentry.specular>>8)&256)/256.0;
      specular[2]=(float)((materialentry.specular>>16)&256)/256.0;
		specular[3]=1;
		msMaterial_SetSpecular(myMat,specular);
		msMaterial_SetTransparency(myMat,materialentry.kAlpha);
	}

	// Objects
	myfile.pointer=marker;
	int p_base=0;
	int v_base=0;
	int junk;
	int prevMat=-1;
	for (counter=0;counter<GeoFileHeader.nPolygonObjects;counter++)
	{
		ass_fread(&polygonobject.pName,sizeof(int),1,&myfile);
		ass_fread(&polygonobject.flags,1,1,&myfile);
		ass_fread(&polygonobject.iObject,1,1,&myfile);
		ass_fread(&polygonobject.nameCRC,sizeof(short),1,&myfile);
		ass_fread(&polygonobject.nVertices,sizeof(int),1,&myfile);
		ass_fread(&polygonobject.nFaceNormals,sizeof(int),1,&myfile);
		ass_fread(&polygonobject.nVertexNormals,sizeof(int),1,&myfile);
		ass_fread(&polygonobject.nPolygons,sizeof(int),1,&myfile);
		ass_fread(&polygonobject.pVertexList,sizeof(int),1,&myfile);
		ass_fread(&polygonobject.pFaceNormalList,sizeof(int),1,&myfile);
		if (GeoFileHeader.version>=1280) ass_fread(&polygonobject.pVertexNormalList,sizeof(int),1,&myfile);
			else polygonobject.pVertexNormalList=polygonobject.pFaceNormalList+16*polygonobject.nFaceNormals;
		ass_fread(&polygonobject.pPolygonList,sizeof(int),1,&myfile);
		ass_fread(&polygonobject.pMother,sizeof(int),1,&myfile);
		ass_fread(&polygonobject.pDaughter,sizeof(int),1,&myfile);
		ass_fread(&polygonobject.pSister,sizeof(int),1,&myfile);
		ass_matrix mymatrix;
		ass_fread(mymatrix.m,sizeof(float)*16,1,&myfile);

		// Set name
		int proper_place=myfile.pointer;
		myfile.pointer=polygonobject.pName;
		char name[30];
		int i=0;
		do
		{
			ass_fread(&name[i],1,1,&myfile);
			i++;
		}
		while (name[i-1]!='\0');

		// Normals
		int normals;
		myfile.pointer=polygonobject.pVertexNormalList;
		float * normalsdef=(float *)malloc(polygonobject.nVertexNormals*12);
		for (normals=0;normals<polygonobject.nVertexNormals;normals++)
		{
			ass_fread(&normalsdef[normals*3],sizeof(float)*3,1,&myfile);
			ass_fread(&junk,sizeof(float),1,&myfile);
		}

		// Vertices
		int vertices;
		myfile.pointer=polygonobject.pVertexList;
		int * normallink=(int *)malloc(polygonobject.nVertices*4);
		float * verticesdef=(float *)malloc(polygonobject.nVertices*12);
		for (vertices=0;vertices<polygonobject.nVertices;vertices++)
		{
			ass_vector myVector;

			ass_fread(myVector.v,sizeof(float)*3,1,&myfile);
			myVector.v[0]*=SCALE;
			myVector.v[1]*=SCALE;
			myVector.v[2]*=SCALE;
			ass_fread(&normallink[vertices],sizeof(int),1,&myfile);

			mymatrix.apply_to_vector(&myVector);

			verticesdef[vertices*3+0]=myVector.v[0];
			verticesdef[vertices*3+1]=myVector.v[1];
			verticesdef[vertices*3+2]=myVector.v[2];
		}

		// Polygons
		int polygons;
		myfile.pointer=polygonobject.pPolygonList;
		msMesh * myMesh2;
		int *vmapping=(int*)malloc(polygonobject.nVertices*4);
		int newMeshes=0;
		for (polygons=0;polygons<polygonobject.nPolygons;polygons++)
		{
			short temp;

			ass_fread(&junk,sizeof(int),1,&myfile);

			// Vertex links
			unsigned short vlink[3];
			ass_fread(vlink,sizeof(short)*3,1,&myfile);

         // Material link (maybe we need to start a new mesh)
			ass_fread(&temp,sizeof(short),1,&myfile);
			if (prevMat!=temp)
			{
				// The material has changed so we must create a new mesh :S
				myMesh2=msModel_GetMeshAt(pModel,msModel_AddMesh(pModel));
				msMesh_SetMaterialIndex(myMesh2,temp);
				char name2[30];
				strcpy(name2,name);
				name2[strlen(name2)+1]='\0';
				name2[strlen(name2)]=newMeshes+48;
				msMesh_SetName(myMesh2,name2);
				newMeshes++;

				for (vertices=0;vertices<polygonobject.nVertices;vertices++)
					vmapping[vertices]=-1;
			}
			prevMat=temp;

			short normals[3];

			// Load uv
			int subcounter;
			float u[3],v[3];
			for (subcounter=0;subcounter<3;subcounter++)
			{
				ass_fread(&u[subcounter],sizeof(float),1,&myfile);
				ass_fread(&v[subcounter],sizeof(float),1,&myfile);
			}

			// Add a copy of the vertices from the vertex holding mesh
			for (subcounter=0;subcounter<3;subcounter++)
			{
				// Check if we need to copy
				bool doit=false;
				if (vmapping[vlink[subcounter]]==-1) doit=true;
				else
				{
					msVertex * _v=msMesh_GetVertexAt(myMesh2,vmapping[vlink[subcounter]]);
					if (_v->u!=u[subcounter]) doit=true;
					if (_v->v!=v[subcounter]) doit=true;
				}

				if (doit)
				{
					// Copy normal
					int old=normals[subcounter];
					normals[subcounter]=msMesh_AddVertexNormal(myMesh2);
					msMesh_SetVertexNormalAt(myMesh2,normals[subcounter],&normalsdef[old*3]);

					// Copy vertex
					old=vlink[subcounter];
					vlink[subcounter]=msMesh_AddVertex(myMesh2);
					msVertex * v2=msMesh_GetVertexAt(myMesh2,vlink[subcounter]);
					v2->Vertex[0]=verticesdef[old*3+0];
					v2->Vertex[1]=verticesdef[old*3+1];
					v2->Vertex[2]=verticesdef[old*3+2];

					vmapping[old]=vlink[subcounter];
				} else
				{
					vlink[subcounter]=vmapping[vlink[subcounter]];
					normals[subcounter]=normallink[vlink[subcounter]];
				}
			}

			// Add triangle
			msTriangle * myTri=msMesh_GetTriangleAt(myMesh2,msMesh_AddTriangle(myMesh2));
			myTri->nVertexIndices[0]=vlink[0];
			myTri->nVertexIndices[1]=vlink[1];
			myTri->nVertexIndices[2]=vlink[2];
			if ((normals[0]!=-1) && (normals[1]!=-1) && (normals[2]!=-1)) msTriangle_SetNormalIndices(myTri,(unsigned short *)normals);

			// UV coordinates
			for (subcounter=0;subcounter<3;subcounter++)
			{
				// Again, dodgy, but I'm not copying the vertices
				if ((myTri->nVertexIndices[subcounter]<0) || (myTri->nVertexIndices[subcounter]>=polygonobject.nVertices))
				{
			///		errorMessage("Missing vertex indexed");
					myTri->nVertexIndices[subcounter]=0;
				} else
				{
					myMesh2->pVertices[myTri->nVertexIndices[subcounter]].u=u[subcounter];
					myMesh2->pVertices[myTri->nVertexIndices[subcounter]].v=v[subcounter];
				}
			}

			// 2-sided
			ass_fread(&temp,sizeof(short),1,&myfile);
			if (temp==1)
			{
				msTriangle * myTri2=msMesh_GetTriangleAt(myMesh2,msMesh_AddTriangle(myMesh2));
				myTri2->nVertexIndices[0]=myTri->nVertexIndices[2];
				myTri2->nVertexIndices[1]=myTri->nVertexIndices[1];
				myTri2->nVertexIndices[2]=myTri->nVertexIndices[0];

				short normals2[3];
				normals2[0]=normals[2];
				normals2[1]=normals[1];
				normals2[2]=normals[0];
				if ((normals2[0]!=-1) && (normals2[1]!=-1) && (normals2[2]!=-1)) msTriangle_SetNormalIndices(myTri,(unsigned short *)normals2);
			}

			ass_fread(&temp,sizeof(short),1,&myfile);
		}

		free(normallink);
		free(verticesdef);
		free(normalsdef);
		free(vmapping);

		myfile.pointer=proper_place;
	}


    return 0;
}

void convert_lif(char *filename)
{
	// Open file
	ass_file myfile(filename);
	if (!myfile.data) return;

	// Check magic string
	char temp[10];
	ass_fread(temp,8,1,&myfile);
	if (!((temp[0]=='W') && (temp[1]=='i') && (temp[2]=='l') && (temp[3]=='l') && (temp[4]=='y') && (temp[5]==' ') && (temp[6]=='7'))) return;

	// Load the header
	int version;
	int flags;
	int width,height;
	int palette_data, image_data, temp_1, temp_2;
	ass_fread(&version,sizeof(int),1,&myfile);
	if (version!=0x104) return;
	ass_fread(&flags,sizeof(int),1,&myfile);
	ass_fread(&width,sizeof(int),1,&myfile);
	ass_fread(&height,sizeof(int),1,&myfile);
	ass_fread(&temp_1,sizeof(int),1,&myfile);
	ass_fread(&temp_2,sizeof(int),1,&myfile);
	ass_fread(&image_data,sizeof(int),1,&myfile);
	if (image_data==0) return;
	ass_fread(&palette_data,sizeof(int),1,&myfile);
	ass_fread(&temp_1,sizeof(int),1,&myfile);
	ass_fread(&temp_2,sizeof(int),1,&myfile);

	// Load the palette
	unsigned char pal[256][4];
	if (palette_data!=0)
	{
		myfile.pointer=palette_data;
		int counter;
		for (counter=0;counter<256;counter++)
		{
			ass_fread(&pal[counter][0],1,1,&myfile);
			ass_fread(&pal[counter][1],1,1,&myfile);
			ass_fread(&pal[counter][2],1,1,&myfile);
			ass_fread(&pal[counter][3],1,1,&myfile);
		}
	}

	// Load image
	myfile.pointer=image_data;
	unsigned char * mypic=(unsigned char *)malloc(4*width*height);
	int x,y;
	for (y=0;y<height;y++)
	{
		for (x=0;x<width;x++)
		{
			// Paletted
			if (palette_data!=0)
			{
				unsigned char pos;
				ass_fread(&pos,1,1,&myfile);
				mypic[4*y*width+4*x+0]=pal[pos][0];
				mypic[4*y*width+4*x+1]=pal[pos][1];
				mypic[4*y*width+4*x+2]=pal[pos][2];
				mypic[4*y*width+4*x+3]=pal[pos][3];
			}

			// RGBA
			else {
				unsigned char r,g,b,a;
				ass_fread(&r,1,1,&myfile);
				ass_fread(&g,1,1,&myfile);
				ass_fread(&b,1,1,&myfile);
				ass_fread(&a,1,1,&myfile);
				mypic[4*y*width+4*x+0]=r;
				mypic[4*y*width+4*x+1]=g;
				mypic[4*y*width+4*x+2]=b;
				mypic[4*y*width+4*x+3]=a;
			}
		}
	}


	FILE *tgafile;
	strcat(filename,".tga");
	tgafile=fopen(filename,"wb");
	int c;
	unsigned char buffer[20];
	/* create Targa-header */
	buffer[0]=0;                /* No image-ID field */
	buffer[1]=0;                /* no color map */
	buffer[2]=2;                /* rgb-pic uncompressed */
	buffer[3]=0;buffer[4]=0;    /* color map offset */
	buffer[5]=0;buffer[6]=0;    /* 0 entrys */
	buffer[7]=32;               /* 32 Bit color */
	buffer[8]=0;buffer[9]=0;    /* X-Position */
	buffer[10]=0;buffer[11]=0;  /* Y-Position */
	buffer[13]=(width>>8)&255;buffer[12]=width&255;     /* X-Size */
	buffer[15]=(height>>8)&255;buffer[14]=height&255;     /* Y-Size */
	buffer[16]=32; buffer[17]=0; /* 32 bit Color */
	fwrite(&buffer,18,1,tgafile);
	/* save bitmap (bottom up) */
	for (c=1;c<=height;c++)
		fwrite(mypic+((height-c)*width*4),width*4,1,tgafile);
	fclose(tgafile);
}
