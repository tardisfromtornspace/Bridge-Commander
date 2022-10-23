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

#define SCALE 0.064

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
    strcpy (szTitle, "Bridge Commander (NIF)...");
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

bool ass_fseek(ass_file * file,int amount,int type)
{
	if (type==SEEK_CUR) file->pointer+=amount; else file->pointer=amount;
	return file->pointer<file->size;
}
bool ass_fsetpos(ass_file * file,int amount)
{
	return ass_fseek(file,amount,SEEK_SET);
}
int ass_fgetpos(ass_file * file)
{
	return file->pointer;
}
bool ass_feof(ass_file * file)
{
	return file->pointer>=file->size;
}


// Make us an error message
void errorMessage(char * message)
{
    MessageBox (NULL,message,NULL,MB_OK);
}

bool ass_file_exists(char * filename)
{
   WIN32_FIND_DATA FindFileData;
   HANDLE hFind;
   hFind = FindFirstFile(filename, &FindFileData);
   FindFileData.cFileName;
	return ((signed)hFind)!=-1;
}

// Some constants
// ==============

#define MAX_CHUNKS 500
#define MAX_NODE_CHILDREN 200
#define MAX_MESH_HOLDER_PROPERTIES 10

// Types of chunk
#define NIF_NULL 0
#define NIF_MESH 1
#define NIF_MESH_HOLDER 2
#define NIF_NODE 3
#define NIF_MATERIAL 4
#define NIF_IMAGE 5
#define NIF_TEXTURE_HOLDER 6
#define NIF_RAW_IMAGE 7

// Types of NiImage
#define TYPE_IMG_INTERNAL 0
#define TYPE_IMG_EXTERNAL 1

// Types used for general use
// ==========================

// Vertex
class _nif_vertex
{
public:
	float x,y,z;    // coordinate
	float u,v;      // texture map pos
	float nx,ny,nz; // normal vector

   _nif_vertex()
   {
      x=y=z=u=v=nx=ny=nz=0;
   }
};

// Triangle
class _nif_triangle
{
public:
	unsigned int v[3];

   _nif_triangle()
   {
      v[0]=v[1]=v[2]=0;
   }
};


// Types to be held in the chunk list
// ==================================

class nif_holder
{
public:
   unsigned int nif_id;
   unsigned int nif_type;
   bool used;
	char node_name_type[30];

   void setup(unsigned int _nif_id, unsigned int _nif_type, char * _node_name_type)
   {
      nif_id=_nif_id;
      nif_type=_nif_type;
      used=false;
		strcpy(node_name_type,_node_name_type);
   }
};

// Material
class nif_material : public nif_holder
{
public:
   char name[30];

   float ambient[4];
   float diffuse[4];
   float specular[4];
   float glossiness;
   float opacity;

   nif_material(unsigned int nif_id)
   {
      strcpy(name,"");
      opacity=1;
      glossiness=0;
      ambient[0]=ambient[1]=ambient[2]=0;
      diffuse[0]=diffuse[1]=diffuse[2]=1;
		ambient[3]=diffuse[3]=specular[3]=1;

      setup(nif_id,NIF_MATERIAL,"Material");
   }
};

// Texture holder
class nif_texture_holder : public nif_holder
{
public:
   unsigned int nif_data_id;

   nif_texture_holder(unsigned int nif_id)
   {
      nif_data_id=0;

      setup(nif_id,NIF_TEXTURE_HOLDER,"Texture Holder");
   }
};

// Texture
class nif_image : public nif_holder
{
public:
   unsigned char type;

   char filename[MS_MAX_PATH*2];
   unsigned int raw_image_id;

   nif_image(unsigned int nif_id)
   {
      type=TYPE_IMG_EXTERNAL;
      strcpy(filename,"");
      raw_image_id=0;

      setup(nif_id,NIF_IMAGE,"Image Reference");
   }
};

// Raw Image
class nif_raw_image : public nif_holder
{
public:
   unsigned int width,height,type;
   unsigned char * color_data;

   nif_raw_image(unsigned int nif_id)
   {
      width=height=type=0;
      color_data=NULL;

      setup(nif_id,NIF_RAW_IMAGE,"Raw Image");
   }

   ~nif_raw_image()
   {
      if (color_data) free(color_data);
   }
};

// Holds a mesh
class nif_mesh_holder : public nif_holder
{
public:
   char name[30];

   unsigned int no_children;
   unsigned int nif_child[MAX_MESH_HOLDER_PROPERTIES];
   unsigned int nif_mesh_id;

   ass_matrix transform;

   nif_mesh_holder(unsigned int nif_id)
   {
      nif_mesh_id=no_children=0;
      strcpy(name,"");

      setup(nif_id,NIF_MESH_HOLDER,"Mesh Holder");
   }
};

// Mesh
#define MAX_VERTICES_PER_OBJECT 50000
#define MAX_POLYGONS_PER_OBJECT 50000
class nif_mesh : public nif_holder
{
public:
   unsigned short no_vertices;
   _nif_vertex *vertices[MAX_VERTICES_PER_OBJECT];

   unsigned short no_triangles;
   _nif_triangle *triangles[MAX_POLYGONS_PER_OBJECT];

   nif_mesh(unsigned int nif_id)
   {
      no_vertices=no_triangles=0;

      setup(nif_id,NIF_MESH,"Mesh");
   }

   ~nif_mesh()
   {
      int counter;

      // Free up the vertices
      for (counter;counter<no_vertices;counter++)
      {
         delete vertices[counter];
      }

      // Free up the triangles
      for (counter;counter<no_triangles;counter++)
      {
         delete triangles[counter];
      }
   }
};

// Node
class nif_node : public nif_holder
{
public:
   char name[30];

   unsigned int no_children;
   unsigned int nif_child[MAX_NODE_CHILDREN];

   ass_matrix transform;

   nif_node(unsigned int nif_id)
   {
      no_children=0;
      strcpy(name,"");

      setup(nif_id,NIF_NODE,"Node");
   }
};

// Help functions
// ==============
void nif_read_transform_matrix(ass_file * myfile, ass_matrix * mymatrix);
void convert_nif_texture(char *infile, char *outfile);

// Function we will use at the end
// ===============================

void nif_process_node(nif_node * mynode, msModel * treepos, ass_matrix * oldcompound, int recursions);
nif_holder * find_nif (unsigned int nif_id);
void nif_process_mesh(nif_mesh_holder * my_mesh_holder, msModel * treepos, ass_matrix * oldcompound);

// Some variables
// ==============

unsigned int no_chunks;
nif_holder ** nif_chunks;
char * nif_filename;
unsigned char no_textures_done;
FILE * loadlog;

int method;

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
    char szDefExt[32] = "nif";
    char szFilter[128] = "NIF Files (*.nif)\0*.nif\0All Files (*.*)\0*.*\0\0";
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
    ofn.lpstrTitle = "Import Bridge Commander NIF -- assimsoft.com";

    if (!::GetOpenFileName (&ofn))
        return 0;

    //
    // import
    //
    ass_file _myfile(szFile);
    if (!_myfile.data) return 0;
	 ass_file * myfile=&_myfile;

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

   // Declare
   no_chunks=0;
   nif_chunks=(nif_holder **)malloc(MAX_CHUNKS*sizeof(nif_holder *));
   unsigned int counter;
   char chunk_name[30];
   nif_filename=(char *)malloc(MS_MAX_PATH);
   strcpy(nif_filename,szFile);
   no_textures_done=0;
   bool exit_flag=false;

   // Get the header
   char header[128];
   ass_fread(header,128,1,myfile);
   if (strncmp(header,"NetImmerse File Format, Version 3.1",strlen("NetImmerse File Format, Version 3.1"))!=0)
   {
      errorMessage("Invalid version of the NIF format (if its NIF at all)");
      return 0;
   }

	// Set up the hierachy loading log, so we can see the structure
	char logpath[MS_MAX_PATH];
	strcpy(logpath,filepath);
	strcat(logpath,"structure.txt");
	loadlog=fopen(logpath,"wt");

   // Read in the chunks (finally :)
   do
   {
	   method=0;

      // Get the chunk header
      unsigned int chunk_id=0;
      unsigned int temp_len=0;
      ass_fread(&temp_len,4,1,myfile);
      if (temp_len>=30) temp_len=0;
      ass_fread(chunk_name,temp_len,1,myfile);
      chunk_name[temp_len]=0;
      if ((strcmp(chunk_name,"Top Level Object")!=0) && (strcmp(chunk_name,"End Of File")!=0))
      {
         ass_fread(&chunk_id,4,1,myfile);
         if (strncmp(chunk_name,"Ni",2)!=0) 
			{
				errorMessage("Got lost in the file, finding way back and trying alternative algorithm");
				for (counter=(unsigned)myfile->pointer;counter<myfile->size;counter++)
				{
					if (strncmp(myfile->data+counter+4,"Ni",2)==0) break;
				}
				myfile->pointer=counter;
				method=1-method;
				no_chunks--;
			}
      }
      if (no_chunks>=MAX_CHUNKS) 
      {
         errorMessage("Too many chunks in NIF");
         return 0;
      }

      // Now we have code to process the important chunks
      // ================================================

      // Node
      if (strcmp(chunk_name,"NiNode")==0)
      {
         nif_chunks[no_chunks]=new nif_node(chunk_id);

         // Name
         ass_fread(&temp_len,4,1,myfile);
         ass_fread(((nif_node *)nif_chunks[no_chunks])->name,temp_len,1,myfile);
         ((nif_node *)nif_chunks[no_chunks])->name[temp_len]=0;

         // Skip on
         ass_fseek(myfile,10,SEEK_CUR);

         // Transform matrix
         nif_read_transform_matrix(myfile,&((nif_node *)nif_chunks[no_chunks])->transform);

         // Skip on
         ass_fseek(myfile,16,SEEK_CUR);

         // Read in all properties, children and blocks
         unsigned int no_whatever;
         unsigned int i;
         for (i=0;i<4;i++)
         {
            ass_fread(&no_whatever,4,1,myfile);
            for (counter=0;counter<no_whatever;counter++)
            {
               ass_fread(&
                  ((nif_node *)nif_chunks[no_chunks])->nif_child[((nif_node *)nif_chunks[no_chunks])->no_children]
                  ,4,1,myfile);
               ((nif_node *)nif_chunks[no_chunks])->no_children++;

               if (((nif_node *)nif_chunks[no_chunks])->no_children>=MAX_NODE_CHILDREN) 
               {
                  errorMessage("Too many children/properties for a certain node in NIF");
                  return 0;
               }
            }
         }

         no_chunks++;
      } else

      // Mesh Holder
      if (strcmp(chunk_name,"NiTriShape")==0)
      {
         nif_chunks[no_chunks]=new nif_mesh_holder(chunk_id);

         // Name
         ass_fread(&temp_len,4,1,myfile);
         ass_fread(((nif_mesh_holder *)nif_chunks[no_chunks])->name,temp_len,1,myfile);
         ((nif_mesh_holder *)nif_chunks[no_chunks])->name[temp_len]=0;

         // Skip on
         ass_fseek(myfile,10,SEEK_CUR);

         // Transform matrix
         nif_read_transform_matrix(myfile,&((nif_mesh_holder *)nif_chunks[no_chunks])->transform);

         // Skip on
         ass_fseek(myfile,16,SEEK_CUR);

         // Read in all properties
         unsigned int no_whatever;
         ass_fread(&no_whatever,4,1,myfile);
         for (counter=0;counter<no_whatever;counter++)
         {
            ass_fread(&
               ((nif_mesh_holder *)nif_chunks[no_chunks])->nif_child[((nif_mesh_holder *)nif_chunks[no_chunks])->no_children]
               ,4,1,myfile);
            ((nif_mesh_holder *)nif_chunks[no_chunks])->no_children++;

            if (((nif_mesh_holder *)nif_chunks[no_chunks])->no_children>=MAX_MESH_HOLDER_PROPERTIES) 
            {
               errorMessage("Too many properties for a certain mesh holder in NIF");
               return 0;
            }
         }

         // Skip on
         ass_fseek(myfile,4,SEEK_CUR);

         // Link to Mesh
         ass_fread(&((nif_mesh_holder *)nif_chunks[no_chunks])->nif_mesh_id,4,1,myfile);

         no_chunks++;
      } else

      // Mesh
      if (strcmp(chunk_name,"NiTriShapeData")==0)
      {
         nif_chunks[no_chunks]=new nif_mesh(chunk_id);

         unsigned short no_vertices,no_triangles;

         // Do vertices
         ass_fread(&no_vertices,2,1,myfile);
         if (no_vertices>=MAX_VERTICES_PER_OBJECT) 
         {
            errorMessage("Too many vertices in NIF");
            return 0;
         }
         ((nif_mesh *)nif_chunks[no_chunks])->no_vertices=no_vertices;
         ass_fseek(myfile,4,SEEK_CUR);
         for (counter=0;counter<no_vertices;counter++)
         {
            ((nif_mesh *)nif_chunks[no_chunks])->vertices[counter]=new _nif_vertex();

            ass_fread(&((nif_mesh *)nif_chunks[no_chunks])->vertices[counter]->x,4,1,myfile);
            ass_fread(&((nif_mesh *)nif_chunks[no_chunks])->vertices[counter]->y,4,1,myfile);
            ass_fread(&((nif_mesh *)nif_chunks[no_chunks])->vertices[counter]->z,4,1,myfile);
         }

         // Do normals
         ass_fseek(myfile,4,SEEK_CUR);
         for (counter=0;counter<no_vertices;counter++)
         {
            ass_fread(&((nif_mesh *)nif_chunks[no_chunks])->vertices[counter]->nx,4,1,myfile);
            ass_fread(&((nif_mesh *)nif_chunks[no_chunks])->vertices[counter]->ny,4,1,myfile);
            ass_fread(&((nif_mesh *)nif_chunks[no_chunks])->vertices[counter]->nz,4,1,myfile);
         }

         // Do UV sets
         ass_fseek(myfile,20,SEEK_CUR);
         unsigned short uv_sets;
         ass_fread(&uv_sets,2,1,myfile);
         unsigned short i;
         ass_fseek(myfile,4,SEEK_CUR);
         for (i=0;i<uv_sets;i++)
         {
            for (counter=0;counter<no_vertices;counter++)
            {
               float u,v;
               ass_fread(&u,4,1,myfile);
               ass_fread(&v,4,1,myfile);
               if (i==0)
               {
                  ((nif_mesh *)nif_chunks[no_chunks])->vertices[counter]->u=u;
                  ((nif_mesh *)nif_chunks[no_chunks])->vertices[counter]->v=v;
               }
            }
         }
         if ((uv_sets==0) && (method==0)) ass_fseek(myfile,4,SEEK_CUR);

         // Do triangles
         ass_fread(&no_triangles,2,1,myfile);
         if (no_triangles>=MAX_POLYGONS_PER_OBJECT) 
         {
            errorMessage("Too many triangles in NIF");
            return 0;
         }
         ((nif_mesh *)nif_chunks[no_chunks])->no_triangles=no_triangles;
         ass_fseek(myfile,4,SEEK_CUR);
         for (counter=0;counter<no_triangles;counter++)
         {
            ((nif_mesh *)nif_chunks[no_chunks])->triangles[counter]=new _nif_triangle();

            for (i=0;i<3;i++)
            {
               ass_fread(&((nif_mesh *)nif_chunks[no_chunks])->triangles[counter]->v[i],2,1,myfile);
            }
         }

         // Read in some unknown stuff, which is there
         unsigned short unknown_count;
         ass_fread(&unknown_count,2,1,myfile);
         for (i=0;i<unknown_count;i++)
         {
            unsigned short junk;
            ass_fread(&junk,2,1,myfile);
            ass_fseek(myfile,2*junk,SEEK_CUR);
         }

         no_chunks++;
      } else

      // Material
      if ((strcmp(chunk_name,"NiMaterial")==0) || (strcmp(chunk_name,"NiMaterialProperty")==0))
      {
         nif_chunks[no_chunks]=new nif_material(chunk_id);

         // Name
         ass_fread(&temp_len,4,1,myfile);
         ass_fread(((nif_material *)nif_chunks[no_chunks])->name,temp_len,1,myfile);
         ((nif_material *)nif_chunks[no_chunks])->name[temp_len]=0;

         // Skip on
         ass_fseek(myfile,10,SEEK_CUR);

         // Read colors
         ass_fread(((nif_material *)nif_chunks[no_chunks])->ambient,12,1,myfile);
         ass_fread(((nif_material *)nif_chunks[no_chunks])->diffuse,12,1,myfile);
         ass_fread(((nif_material *)nif_chunks[no_chunks])->specular,12,1,myfile);

         // Skip on
         ass_fseek(myfile,12,SEEK_CUR);

         // Read other properties
         ass_fread(&((nif_material *)nif_chunks[no_chunks])->glossiness,4,1,myfile);
         ass_fread(&((nif_material *)nif_chunks[no_chunks])->opacity,4,1,myfile);

         no_chunks++;
      } else

      // Image
      if (strcmp(chunk_name,"NiImage")==0)
      {
         nif_chunks[no_chunks]=new nif_image(chunk_id);

         // Type
         unsigned char type;
         ass_fread(&type,1,1,myfile);
         ((nif_image *)nif_chunks[no_chunks])->type=type;

         // Embedded image
         if (type==TYPE_IMG_INTERNAL)
         {
            ass_fread(&((nif_image *)nif_chunks[no_chunks])->raw_image_id,4,1,myfile);
         } else
         if (type==TYPE_IMG_EXTERNAL)
         {
            // Filename
            ass_fread(&temp_len,4,1,myfile);
            ass_fread(((nif_image *)nif_chunks[no_chunks])->filename,temp_len,1,myfile);
            ((nif_image *)nif_chunks[no_chunks])->filename[temp_len]=0;
         } else errorMessage("Weird image type");

         // Skip on
         ass_fseek(myfile,8,SEEK_CUR);

         no_chunks++;
      } else

      // Texture holder
      if (strcmp(chunk_name,"NiTextureProperty")==0)
      {
         nif_chunks[no_chunks]=new nif_texture_holder(chunk_id);

         // Skip on
         ass_fseek(myfile,14,SEEK_CUR);

         // Image ID
         ass_fread(&((nif_texture_holder *)nif_chunks[no_chunks])->nif_data_id,4,1,myfile);

         no_chunks++;
      } else

      // Raw image
      if (strcmp(chunk_name,"NiRawImageData")==0)
      {
         nif_chunks[no_chunks]=new nif_raw_image(chunk_id);

         // Dimensions
         unsigned int width,height;
         ass_fread(&width,4,1,myfile);
         ((nif_raw_image *)nif_chunks[no_chunks])->width=width;
         ass_fread(&height,4,1,myfile);
         ((nif_raw_image *)nif_chunks[no_chunks])->height=height;

         // Skip on
         unsigned int type;
         ass_fread(&type,4,1,myfile);
         ((nif_raw_image *)nif_chunks[no_chunks])->type=type;
         int x=3;
         if (type==2) x=4;

         // Read in actual data
         unsigned char * color_data=(unsigned char *)malloc(width*height*x);
         ass_fread(color_data,width*height*x,1,myfile);
         ((nif_raw_image *)nif_chunks[no_chunks])->color_data=color_data;

         no_chunks++;
      } else


      // Oh, we need to skip
      // ===================
      {
         // Search for the next node (they all start Ni)
         for (counter=(unsigned)myfile->pointer;counter<(unsigned)myfile->size-6;counter++)
         {
            if (strncmp(myfile->data+counter+4,"Ni",2)==0) break;
         }
         if (counter==(unsigned)myfile->size-6) exit_flag=true; // Just in case (being very careful)

         // Put pointer to desired location
         myfile->pointer=counter;
      }
   }
   while (!ass_feof(myfile) && (!exit_flag) && (strcmp(chunk_name,"End Of File")!=0));

   // Turn our structure into Milkshape compatible data
	ass_matrix identitymatrix;
   nif_process_node((nif_node *)nif_chunks[0], pModel,&identitymatrix,0);

   // Check we processed all the nodes
   for (counter=0;counter<no_chunks;counter++)
   {
      if (!nif_chunks[counter]->used)
      {
//         ass_trace("A seemingly important NIF chunk wasn't linked into the hierachy right\n");
      }
   }

   // Tidy up
   for (counter=0;counter<no_chunks;counter++)
   {
      delete nif_chunks[counter];
   }
   free(nif_chunks);
   free(nif_filename);
	fclose(loadlog);

	return 0;
}

// Read in the matrix
void nif_read_transform_matrix(ass_file * myfile, ass_matrix * mymatrix)
{
   // Position
   ass_fread(&mymatrix->pos_x,4,1,myfile);
   ass_fread(&mymatrix->pos_y,4,1,myfile);
   ass_fread(&mymatrix->pos_z,4,1,myfile);
	mymatrix->pos_x*=SCALE;
	mymatrix->pos_y*=SCALE;
	mymatrix->pos_z*=SCALE;
	mymatrix->pos_w=1;

   // Axes
   ass_fread(&mymatrix->right_x,4,1,myfile);
   ass_fread(&mymatrix->right_y,4,1,myfile);
   ass_fread(&mymatrix->right_z,4,1,myfile);
	mymatrix->right_w=0;
   ass_fread(&mymatrix->up_x,4,1,myfile);
   ass_fread(&mymatrix->up_y,4,1,myfile);
   ass_fread(&mymatrix->up_z,4,1,myfile);
	mymatrix->up_w=0;
   ass_fread(&mymatrix->front_x,4,1,myfile);
   ass_fread(&mymatrix->front_y,4,1,myfile);
   ass_fread(&mymatrix->front_z,4,1,myfile);
	mymatrix->front_w=0;
}

// Process node (we start with the root, then recurse off it)
void nif_process_node(nif_node * mynode, msModel * treepos, ass_matrix * oldcompound, int recursions=0)
{
   mynode->used=true;

	// Build up matrix
	ass_matrix newcompound;
	newcompound.multiply_by(&mynode->transform);
	newcompound.multiply_by(oldcompound);

	// Log
	int x;
	for (x=0;x<recursions;x++)
		fputs("\t",loadlog);
	fprintf(loadlog,"%s (%s, Transform: [%f %f %f] [%f %f %f] [%f %f %f] [%f %f %f])\n",
		mynode->node_name_type,mynode->name,
		mynode->transform.pos_x,mynode->transform.pos_y,mynode->transform.pos_z,
		mynode->transform.right_x,mynode->transform.right_y,mynode->transform.right_z,
		mynode->transform.up_x,mynode->transform.up_y,mynode->transform.up_z,
		mynode->transform.front_x,mynode->transform.front_y,mynode->transform.front_z);

   // Identifier
//   strcpy(treepos->identifier,mynode->name);

   unsigned int counter,no_children=0;
   for (counter=0;counter<mynode->no_children;counter++)
   {
      nif_holder *mychild=find_nif(mynode->nif_child[counter]);

      if (mychild)
      {
			// Log
			if (mychild->nif_type!=NIF_NODE)
			{
				int x;
				for (x=0;x<recursions+1;x++)
					fputs("\t",loadlog);
				if (mychild->nif_type==NIF_MESH_HOLDER)
					fprintf(loadlog,"%s (%s, Transform: [%f %f %f] [%f %f %f] [%f %f %f] [%f %f %f])\n",
						mychild->node_name_type,((nif_mesh_holder *)mychild)->name,
						((nif_mesh_holder *)mychild)->transform.pos_x,((nif_mesh_holder *)mychild)->transform.pos_y,((nif_mesh_holder *)mychild)->transform.pos_z,
						((nif_mesh_holder *)mychild)->transform.right_x,((nif_mesh_holder *)mychild)->transform.right_y,((nif_mesh_holder *)mychild)->transform.right_z,
						((nif_mesh_holder *)mychild)->transform.up_x,((nif_mesh_holder *)mychild)->transform.up_y,((nif_mesh_holder *)mychild)->transform.up_z,
						((nif_mesh_holder *)mychild)->transform.front_x,((nif_mesh_holder *)mychild)->transform.front_y,((nif_mesh_holder *)mychild)->transform.front_z);
//				else if (mychild->nif_type==NIF_MATERIAL) fprintf(loadlog,"%s (%s)\n",mychild->node_name_type,((nif_material *)mychild)->name);
//				else if (mychild->nif_type==NIF_IMAGE) fprintf(loadlog,"%s (%s)\n",mychild->node_name_type,((nif_image *)mychild)->filename);
				else fprintf(loadlog,"%s\n",mychild->node_name_type);
			}

         if (mychild->nif_type==NIF_NODE) // Subnode
         {
            nif_process_node((nif_node *)mychild,treepos,&newcompound,recursions+1);
            no_children++;
         } else
         if (mychild->nif_type==NIF_MESH_HOLDER) // A destination to a mesh
         {
            nif_mesh_holder * mymesh=(nif_mesh_holder *)mychild;

            nif_process_mesh(mymesh,treepos,&newcompound);
            no_children++;
         }
      }
   }
}

// Find nif chunk with given ID
nif_holder * find_nif (unsigned int nif_id)
{
   unsigned int counter;
   for (counter=0;counter<no_chunks;counter++)
   {
      if (nif_chunks[counter]->nif_id==nif_id) 
      {
         return nif_chunks[counter];
      }
   }

   return NULL;
}

void nif_process_mesh(nif_mesh_holder * my_mesh_holder, msModel * treepos, ass_matrix * oldcompound)
{
   my_mesh_holder->used=true;

	// Build up matrix
	ass_matrix newcompound;
	newcompound.multiply_by(&my_mesh_holder->transform);
	newcompound.multiply_by(oldcompound);

   // Declare
   nif_material * mat=NULL;
   nif_image * img=NULL;

   // Find pointers to chunks holding our material and texture info
   unsigned int counter,subcounter;
   for (counter=0;counter<my_mesh_holder->no_children;counter++)
   {
      nif_holder *mychild=find_nif(my_mesh_holder->nif_child[counter]);

      if (mychild)
      {
         if (mychild->nif_type==NIF_MATERIAL) // A material
         {
            mat=(nif_material *)mychild;
            mat->used=true;
         } else
         if (mychild->nif_type==NIF_TEXTURE_HOLDER) // A destination to a texturemap
         {
            nif_texture_holder * tex=(nif_texture_holder *)mychild;
            tex->used=true;

            nif_image * temp_img=(nif_image *)find_nif(tex->nif_data_id);
            if ((temp_img) && (!img)) 
            {
               img=temp_img;
            }
         }
      }
   }

	// Images must be put/from files base folder
	char tempname[MS_MAX_PATH*2];
	strcpy(tempname,nif_filename);
	unsigned short j;
	for (j=strlen(tempname)-1;j>0;j--)
	{
		if ((tempname[j]=='\\') || (tempname[j]=='/'))
		{
			tempname[j+1]='\0';
			break;
		}
	}

   if ((img) && (!img->used)) // If we have to export a .tga texture
   {
      img->used=true;

		// Must we export to an external .nif first?
      if (img->type==TYPE_IMG_INTERNAL)
      {
         nif_raw_image * raw=(nif_raw_image *)find_nif(img->raw_image_id);
         raw->used=true;

         // Export data to an external nif
         unsigned int _x=3;
         if (raw->type==2) _x=4;

			sprintf(img->filename,"imp_%d.nif",no_textures_done);
			img->nif_type=TYPE_IMG_EXTERNAL;
			FILE * nifout=fopen(img->filename,"wb");
			int depth=3;
			if (raw->type==2) depth=4;
			char header[128]="NetImmerse File Format, Version 3.1\nNumerical Design Limited, Chapel Hill, NC 27514\nCopyright (c) 1996-2000\nAll Rights Reserved";
			fwrite(header,128,1,nifout);
			int size=16;
			fwrite(&size,4,1,nifout);
			char header2[17]="Top Level Object";
			fwrite(header2,16,1,nifout);
			size=14;
			fwrite(&size,4,1,nifout);
			char header3[15]="NiRawImageData";
			fwrite(header3,14,1,nifout);
			size=12345; // Not a size, just a random id
			fwrite(&size,4,1,nifout);
			fwrite(&raw->width,4,1,nifout);
			fwrite(&raw->height,4,1,nifout);
			fwrite(&raw->type,4,1,nifout);
			fwrite(&raw->color_data,raw->width*raw->height*depth,1,nifout);
			size=11;
			fwrite(&size,4,1,nifout);
			char header4[12]="End Of File";
			fwrite(header4,11,1,nifout);
			fclose(nifout);

         // Increment this: we used it to derive the filename remember
         no_textures_done++;
      }

		char tempname2[MS_MAX_PATH*2];
		strcpy(tempname2,tempname);
		strcat(tempname2,img->filename);
		if (!ass_file_exists(tempname2))
		{
			strcpy(tempname2,tempname);
			strcat(tempname2,"high\\");
			strcat(tempname2,img->filename);
		}
		strcpy(img->filename,tempname2);
		if (stricmp(img->filename+strlen(img->filename)-3,"nif")==0)
		{
			strcpy(img->filename+strlen(img->filename)-3,"tga");
			convert_nif_texture(tempname2,img->filename);
		}
   }


   // Now we can finally head for the mesh
   // ====================================

   // Set up basic material and mesh
   msMesh * myMesh=msModel_GetMeshAt(treepos,msModel_AddMesh(treepos));
	msMesh_SetName(myMesh,my_mesh_holder->name);
	int matIndex=msModel_AddMaterial(treepos);
	msMesh_SetMaterialIndex(myMesh,matIndex);
   msMaterial * myMat=msModel_GetMaterialAt(treepos,matIndex);
	if (img) msMaterial_SetDiffuseTexture(myMat,img->filename+strlen(tempname));
	msMaterial_SetName(myMat,my_mesh_holder->name);
	msMaterial_SetAmbient(myMat,mat->ambient);
	msMaterial_SetEmissive(myMat,mat->ambient);
	msMaterial_SetDiffuse(myMat,mat->diffuse);
	msMaterial_SetSpecular(myMat,mat->specular);
	msMaterial_SetShininess(myMat,mat->glossiness);
	msMaterial_SetTransparency(myMat,mat->opacity);

   // Now for the mesh for real
   nif_mesh * mesh=(nif_mesh*)find_nif(my_mesh_holder->nif_mesh_id);
   if (mesh)
   {
      mesh->used=true;

      // Vertices
      for (counter=0;counter<mesh->no_vertices;counter++)
      {
			msVertex* myVertex=msMesh_GetVertexAt(myMesh,msMesh_AddVertex(myMesh));

			ass_vector _v;
			_v.x=mesh->vertices[counter]->x*SCALE;
			_v.y=mesh->vertices[counter]->y*SCALE;
			_v.z=mesh->vertices[counter]->z*SCALE;
			newcompound.apply_to_vector(&_v);
			float temp=_v.z;
			_v.z=_v.y;
			_v.y=temp;
			float _uv[2];
			_uv[0]=mesh->vertices[counter]->u;
			_uv[1]=mesh->vertices[counter]->v;

			msVertex_SetVertex(myVertex,_v.v);
			msVertex_SetTexCoords(myVertex,_uv);
		}

		// Triangles
      for (counter=0;counter<mesh->no_triangles;counter++)
      {
         msTriangle* myTri=msMesh_GetTriangleAt(myMesh,msMesh_AddTriangle(myMesh));

			// Vertices and normals for triangle
			word v[3];
			word n[3];
			for (subcounter=0;subcounter<3;subcounter++)
			{
				v[subcounter]=mesh->triangles[counter]->v[2-subcounter];

				n[subcounter]=msMesh_AddVertexNormal(myMesh);

				float _n[3];
				_n[0]=mesh->vertices[mesh->triangles[counter]->v[subcounter]]->nx;
				_n[2]=mesh->vertices[mesh->triangles[counter]->v[subcounter]]->ny;
				_n[1]=mesh->vertices[mesh->triangles[counter]->v[subcounter]]->nz;

				msMesh_SetVertexNormalAt(myMesh,n[subcounter],_n);
			}
			msTriangle_SetVertexIndices(myTri,v);
			msTriangle_SetNormalIndices(myTri,n);
      }
   } else
   {
      errorMessage("We seem to have lost a mesh in the NIF\n");
   }
}

// This can load up a NIF file as a simple texture
void convert_nif_texture(char *infile, char *outfile)
{
	// Open file
	ass_file myfile(infile);
	if (!myfile.data) return;

	// See if we can find ourselves the raw image data
	bool good=false;
	while (myfile.pointer<myfile.size-strlen("NiRawImageData")-2)
	{
      if (strncmp(myfile.data+myfile.pointer,"NiRawImageData",strlen("NiRawImageData"))==0) 
		{
			myfile.pointer+=strlen("NiRawImageData")+4;
			good=true;
			break;
		}
		myfile.pointer++;
	}

	// Can we go?
	if (good)
	{
      // Dimensions
      unsigned int width,height;
      ass_fread(&width,4,1,&myfile);
      ass_fread(&height,4,1,&myfile);

      // Skip on
      unsigned int type;
      ass_fread(&type,4,1,&myfile);
      int x=3;
      if (type==2) x=4;

      // Read in actual data
      unsigned char * color_data=(unsigned char *)malloc(width*height*x);
      ass_fread(color_data,width*height*x,1,&myfile);

		// Save
		FILE *tgafile;
		tgafile=fopen(outfile,"wb");
		if (!tgafile) return;
		int c;

		/* create Targa-header */
		unsigned char buffer[18];
		buffer[0]=0;                /* No image-ID field */
		buffer[1]=0;                /* no color map */
		buffer[2]=2;                /* rgb-pic uncompressed */
		buffer[3]=0;buffer[4]=0;    /* color map offset */
		buffer[5]=0;buffer[6]=0;    /* 0 entrys */
		buffer[7]=x*8;               /* 32 Bit color */
		buffer[8]=0;buffer[9]=0;    /* X-Position */
		buffer[10]=0;buffer[11]=0;  /* Y-Position */
		buffer[13]=(width>>8)&255;buffer[12]=width&255;     /* X-Size */
		buffer[15]=(height>>8)&255;buffer[14]=height&255;     /* Y-Size */
		buffer[16]=x*8; buffer[17]=0; /* 32 bit Color */
		fwrite(&buffer,18,1,tgafile);
		/* save bitmap (bottom up) */
		for (c=1;c<=height;c++)
			fwrite(color_data+((height-c)*width*x),width*x,1,tgafile);
		fclose(tgafile);
	}
}
