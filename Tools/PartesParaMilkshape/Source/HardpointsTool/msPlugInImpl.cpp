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

int do_sfc(char * filename, msModel * pModel);
int do_sod(char * filename, msModel * pModel);
int do_pnt(char * filename, msModel * pModel);

class ass_file
{
public:

   char * data;
   int pointer;
   int size;

   ass_file(const char *filename)
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
    strcpy (szTitle, "Assimsoft Hardpoints Tool");
}



cPlugIn::~cPlugIn ()
{
}



int
cPlugIn::GetType ()
{
    return cMsPlugIn::eTypeTool;
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
    char szDefExt[32] = "pnt";
    char szFilter[128] = "Assimview Dumpfile (*.pnt)\0*.pnt\0SFC Model (*.mod)\0*.mod\0Armada Model (*.sod)\0*.sod\0\0";
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
    ofn.lpstrTitle = "Import Hardpoints into current model -- assimsoft.com";

    if (!::GetOpenFileName (&ofn))
        return 0;

	if (ofn.nFilterIndex==1)
		return do_pnt(szFile,pModel);
	else if (ofn.nFilterIndex==2)
		return do_sfc(szFile,pModel);
	else if (ofn.nFilterIndex==3)
		return do_sod(szFile,pModel);

    return 0;
}

int do_sfc(char * szFile, msModel * pModel)
{
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

	char *string_text=NULL;
	int string_size;

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
			myfile.pointer+=36;
		} else
		if (strcmp(chunk,"PNTS")==0)
		{
         int counter=0;
         while (counter<size)
         {
				msVec3 position;
				ass_fread(&position[2],4,1,&myfile);
				ass_fread(&position[1],4,1,&myfile);
				ass_fread(&position[0],4,1,&myfile);
				position[0]*=2.25;
				position[1]*=2.25;
				position[2]*=2.25;
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
        if (strcmp(chunk,"STRS")==0)
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
		{
			myfile.pointer+=size;
		}
	}
	while (myfile.pointer<myfile.size-1);

	// C'est fini!
	free(string_text);

	return 0;
}

#define SOD_SCALE 0.388
#define UINT8 unsigned char
#define UINT16 unsigned short
class sod_node
{
public:
	char name[30];
	ass_matrix matrix;
};

int do_sod(char * szFile, msModel * pModel)
{
   sod_node * nodes[500];

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

   // Test for magic string
   char magic[15];
   ass_fread((void *)&magic,10,1,&myfile);
   magic[10]='\0';
   if (strcmp(magic,"Storm3D_SW")!=0) 
   {
      errorMessage("Magic string for object is not intact: file broken");
	  return 0;
   }

   // Find file version
   float version=0;
   ass_fread((void *)&version,sizeof(float),1,&myfile);
   if (version<1.80-0.01)
   {
      errorMessage("Sod file format is from Mad Doc Software (as it is an old version of the sod format)");
   }

   // Variables
   UINT16 count=0,length;
	int counter,main_counter;

   // Unknown stuff for old versions
   if (version<1.80-0.01)
   {
	   ass_fread((void *)&count,sizeof(UINT16),1,&myfile);
	   for (counter=0;counter<count;counter++)
      {
         // Name * 2
		   length=0;
		   ass_fread((void *)&length,sizeof(UINT16),1,&myfile);
		   myfile.pointer+=length;
		   length=0;
		   ass_fread((void *)&length,sizeof(UINT16),1,&myfile);
		   myfile.pointer+=length;

         // Junk
		   myfile.pointer+=7;
      }
   }

   // Load lighting information
	ass_fread((void *)&count,sizeof(UINT16),1,&myfile);
	for (counter=0;counter<count;counter++)
	{
      // Name
		length=0;
		ass_fread((void *)&length,sizeof(UINT16),1,&myfile);
	   myfile.pointer+=length;

	   myfile.pointer+=41;

	  if (version>1.80+0.01) 
      {
		   myfile.pointer+=1;
      }
	}

   // Read in nodes
	UINT16 type;
   ass_fread((void *)&count,sizeof(UINT16),1,&myfile);
	type=0;

	// Go through nodes
   for (main_counter=0;main_counter<count;main_counter++)
   {
		// Read in node type
	   ass_fread((void *)&type,sizeof(UINT16),1,&myfile);
		if ((type!=0) && (type!=1) && (type!=3) && (type!=11) && (type!=12))
		{
			errorMessage("Sod node type is unknown: let's just finish loading!");
			break;
		}

		// Read in identifier and parent
      length=0;
		char node_name[30];
		char parent[30];
	   ass_fread((void *)&length,sizeof(UINT16),1,&myfile);
		ass_fread(&node_name,length,1,&myfile);
		node_name[length]='\0';
      length=0;
	   ass_fread((void *)&length,sizeof(UINT16),1,&myfile);
		ass_fread(&parent,length,1,&myfile);
		parent[length]='\0';

		// Add the bone
		msBone * myBone=msModel_GetBoneAt(pModel,msModel_AddBone(pModel));
		if (strcmp(parent,"")!=0)
		{
			char parent2[30];
			strcpy(parent2,parent);
			int parentNum=msModel_FindBoneByName(pModel,parent2);
			if (!(parentNum>=0)) 
			{
				strcpy(parent2,"s_");
				strcat(parent2,parent);
				parentNum=msModel_FindBoneByName(pModel,parent2);
			}
			if (!(parentNum>=0)) 
			{
				strcpy(parent2,"l_");
				strcat(parent2,parent);
				parentNum=msModel_FindBoneByName(pModel,parent2);
			}
			if (!(parentNum>=0)) 
			{
				strcpy(parent2,"e_");
				strcat(parent2,parent);
				parentNum=msModel_FindBoneByName(pModel,parent2);
			}
			if (!(parentNum>=0)) 
			{
				strcpy(parent2,"h_");
				strcat(parent2,parent);
				parentNum=msModel_FindBoneByName(pModel,parent2);
			}
			if (!(parentNum>=0)) 
			{
				strcpy(parent2,"m_");
				strcat(parent2,parent);
				parentNum=msModel_FindBoneByName(pModel,parent2);
			}
			if (!(parentNum>=0)) errorMessage("Couldn't find parent");
			msBone_SetParentName(myBone,parent2);
		} else msBone_SetParentName(myBone,parent);

		// Read in matrix
		nodes[main_counter]=new sod_node();
		ass_vector right,up,front,pos;
		ass_fread(right.v,sizeof(float)*3,1,&myfile);
		ass_fread(up.v,sizeof(float)*3,1,&myfile);
		ass_fread(front.v,sizeof(float)*3,1,&myfile);
		ass_fread(pos.v,sizeof(float)*3,1,&myfile);
		pos.v[0]*=-SOD_SCALE;
		pos.v[1]*=SOD_SCALE;
		pos.v[2]*=SOD_SCALE;
		nodes[main_counter]->matrix.from_vectors(&right,&up,&front,&pos);
		msBone_SetPosition(myBone,pos.v);
		float rot[3];
		nodes[main_counter]->matrix.to_euler(&rot[0],&rot[1],&rot[2]);
		msBone_SetRotation(myBone,rot);

		// Node specific stuff
      if (type==0) 
      {
			char newNodeName[30];
			strcpy(newNodeName,"h_");
			strcat(newNodeName,node_name);
			msBone_SetName(myBone,newNodeName);
			strcpy(nodes[main_counter]->name,newNodeName);
      }
      if (type==3) 
      {
			char newNodeName[30];
			strcpy(newNodeName,"s_");
			strcat(newNodeName,node_name);
			msBone_SetName(myBone,newNodeName);
			strcpy(nodes[main_counter]->name,newNodeName);
      }
      if (type==11) 
      {
			char newNodeName[30];
			strcpy(newNodeName,"l_");
			strcat(newNodeName,node_name);
			msBone_SetName(myBone,newNodeName);
			strcpy(nodes[main_counter]->name,newNodeName);
      }
	   if (type==12)   // Emitter information
		{
         char emitter_name[30];
			length=0;
			ass_fread((void *)&length,sizeof(UINT16),1,&myfile);
			ass_fread(&emitter_name,length,1,&myfile);
         emitter_name[length]='\0';
			char newNodeName[30];
			strcpy(newNodeName,"e_");
			strcat(newNodeName,emitter_name);
			msBone_SetName(myBone,newNodeName);
			strcpy(nodes[main_counter]->name,newNodeName);
		}
		if (type==1)   // Polygon mesh information
		{
			char newNodeName[30];
			strcpy(newNodeName,"m_");
			strcat(newNodeName,node_name);
			msBone_SetName(myBone,newNodeName);
			strcpy(nodes[main_counter]->name,newNodeName);

			// Texture type (hard coded strings)
		   if (version>1.60+0.01) 
			{
			   length=0;
			   ass_fread((void *)&length,sizeof(UINT16),1,&myfile);
			   myfile.pointer+=length;
         }

         // Load textures
         UINT32 textures=1;
		   if (version>1.91+0.01) 
			{
				ass_fread(&textures,sizeof(UINT32),1,&myfile);
		   myfile.pointer+=4;
			}
			ass_fread((void *)&length,sizeof(UINT16),1,&myfile);
		   myfile.pointer+=length;
		   if (version>1.91+0.01) 
			{
		   myfile.pointer+=4;
			}

         // Bump map
         if (textures&2)
         {
			   length=0;
			   ass_fread((void *)&length,sizeof(UINT16),1,&myfile);
		   myfile.pointer+=length+4;
         }

			// Unknown junk
		   if (version>1.91+0.01) 
			{
		   myfile.pointer+=4;
			}
		   if ((version>1.80+0.01) && (version<1.93-0.01))
			{
		   myfile.pointer+=2;
			}

			// Load other header info
			UINT16 t_coords=0,light_groups=0,light_counter;

			// Setup vertex numbering info
			UINT16 _no_v=0,temp2=0;
			ass_fread((void *)&_no_v,sizeof(UINT16),1,&myfile);

			// Load other header info
			ass_fread((void *)&t_coords,sizeof(UINT16),1,&myfile);
			ass_fread((void *)&light_groups,sizeof(UINT16),1,&myfile);

			// Load vertex info
		   myfile.pointer+=12*_no_v;

			// Load the texture co-ordinates
		   myfile.pointer+=8*t_coords;

         // Load up polygon sets ("lighting groups")
			for (light_counter=0;light_counter<light_groups;light_counter++)
			{
				// Setup polygon numbering info
				UINT16 _no_p=0;
				ass_fread((void *)&_no_p,sizeof(UINT16),1,&myfile);

				// Get lighting identifier
				length=0;
				ass_fread((void *)&length,sizeof(UINT16),1,&myfile);
			   myfile.pointer+=length;

				// Load polygon info
			   myfile.pointer+=12*_no_p;
			}

			// Backface culling?
		   myfile.pointer+=3;
		}

   }


   return 0;
}

char assreadstring[1024];
char assreadstring2[1024];

const char * ass_read_string(const char *filename, const char * entry, const char * the_default)
{
	ass_file _myfile(filename);
	ass_file * myfile=&_myfile;
	if (!myfile) 
		return the_default;
	int	len = strlen( entry );
	char	*s = myfile->data;
	while( (s = strstr( s , entry )) != NULL )
		if( s == myfile->data && (s[len] == ' ' || s[len] == '=') )
			break;
		else if( s > myfile->data && iscntrl( s[-1] ) && (s[len] == ' ' || s[len] == '=') )
			break;
		else
			s++;

	if( s )
	{
		memset( assreadstring2 , 0 , sizeof( assreadstring2 ) );
		s += strlen( entry );
		while( !iscntrl( *s ) &&  *s )
			if( (*s == ' ' || *s == '=') )
				s++;
			else
				break;
		char	*t = assreadstring2;
		while( !iscntrl( *s ) &&  *s )
			*t++ = *s++;
	}
	else
		strcpy( assreadstring2 , the_default );

	return assreadstring2;
}

char convertedtostring[100];
char runname3[100];

// Converts a float into a string
char * floattostring(float input)
{
   sprintf(convertedtostring,"%f",input);
   return convertedtostring;
}
// Converts an integer into a string
char * inttostring(int input)
{
   sprintf(convertedtostring,"%d",input);
   return convertedtostring;
}
float stringtofloat(const char *mystring)
{
   return atof(mystring);
}
// Allows a name to be created with a varying number within it
char *run_name_int(const char *pre, int mid, const char *post)
{
   strcpy(runname3,pre);
   strcat(runname3,inttostring(mid));
   strcat(runname3,post);
   return runname3;
}

float ass_read_float(const char * filename, const char * entry, float the_default)
{
	return stringtofloat(ass_read_string(filename,entry,floattostring(the_default)));
}


int do_pnt(char * filename, msModel * pModel)
{
	int num=(int)ass_read_float(filename,"no_hardpoints",0);
	float radius=ass_read_float(filename,"radius",0);

	int i;
	for (i=0;i<num;i++)
	{
		// Read in matrix
		ass_vector right,up,front,pos;
		right.x=ass_read_float(filename,run_name_int("hardpoint_",i,"_right_x"),0);
		right.y=ass_read_float(filename,run_name_int("hardpoint_",i,"_right_y"),0);
		right.z=ass_read_float(filename,run_name_int("hardpoint_",i,"_right_z"),0);
		up.x=ass_read_float(filename,run_name_int("hardpoint_",i,"_up_x"),0);
		up.y=ass_read_float(filename,run_name_int("hardpoint_",i,"_up_y"),0);
		up.z=ass_read_float(filename,run_name_int("hardpoint_",i,"_up_z"),0);
		front.x=ass_read_float(filename,run_name_int("hardpoint_",i,"_front_x"),0);
		front.y=ass_read_float(filename,run_name_int("hardpoint_",i,"_front_y"),0);
		front.z=ass_read_float(filename,run_name_int("hardpoint_",i,"_front_z"),0);
		pos.x=ass_read_float(filename,run_name_int("hardpoint_",i,"_x"),0);
		pos.y=ass_read_float(filename,run_name_int("hardpoint_",i,"_y"),0);
		pos.z=ass_read_float(filename,run_name_int("hardpoint_",i,"_z"),0);
		pos.x*=radius;
		pos.y*=radius;
		pos.z*=radius;
		ass_matrix matrix;
		matrix.from_vectors(&right,&up,&front,&pos);
		msBone * myBone=msModel_GetBoneAt(pModel,msModel_AddBone(pModel));
		msBone_SetPosition(myBone,pos.v);
		msBone_SetName(myBone,run_name_int("hp",i,""));
		float rot[3];
		matrix.to_euler(&rot[0],&rot[1],&rot[2]);
		msBone_SetRotation(myBone,rot);
	}

	return 0;
}

