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

#define SCALE 0.0149

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
    strcpy (szTitle, "Star Trek Invasion (TRK)...");
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

void convert_tim(ass_file * timfile, char * outfile);
void trk_load_polygons(int num, msMesh * obj, ass_file * myfile,int polygon_type);

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
    // choose filename
    //
    OPENFILENAME ofn;
    memset (&ofn, 0, sizeof (OPENFILENAME));
    
    char szFile[MS_MAX_PATH];
    char szFileTitle[MS_MAX_PATH];
    char szDefExt[32] = "trk";
    char szFilter[128] = "TRK Files (*.trk)\0*.trk\0All Files (*.*)\0*.*\0\0";
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
    ofn.lpstrTitle = "Import Star Trek Invasion TRK -- assimsoft.com";

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

   // Read in header
	char magic[5];
	magic[4]='\0';
	ass_fread(magic,4,1,&myfile);
   if (strcmp(magic,"TREK")!=0)
   {
      errorMessage("Not a real TREK file");
		return 0;
   }
	int filesize;
   ass_fread(&filesize,4,1,&myfile);
   myfile.pointer+=4; // Skip unknown value

   // Variables
   int count=0;
	int no_tex=0;
	int no_meshes=0;

   // Read in chunks
   char chunk[5];
	do
	{
		chunk[4]='\0';
		ass_fread(chunk,4,1,&myfile);
		int size;
		ass_fread(&size,4,1,&myfile);
//      ass_trace("Reading chunk ");
//      ass_trace(chunk);
//      ass_trace(run_name(" of size ",size,"\n"));

      int pos=myfile.pointer;

      if (strcmp(chunk,"MODL")==0)
      {
         // Model header
         int offset_vertices,offset_normals;
         ass_fread(&offset_vertices,4,1,&myfile);
         ass_fread(&offset_normals,4,1,&myfile);
         short no_vertices,no_normals;
         ass_fread(&no_vertices,2,1,&myfile);
         ass_fread(&no_normals,2,1,&myfile);
         int unknown_a;
         ass_fread(&unknown_a,4,1,&myfile);
         short no_proto_triangles,no_proto_quads,no_triangles,no_quads,no_long_triangles,no_long_quads;
         ass_fread(&no_proto_triangles,2,1,&myfile);
         ass_fread(&no_proto_quads,2,1,&myfile);
         ass_fread(&no_triangles,2,1,&myfile);
         ass_fread(&no_quads,2,1,&myfile);
         ass_fread(&no_long_triangles,2,1,&myfile);
         ass_fread(&no_long_quads,2,1,&myfile);
         int offset_proto_triangles,offset_proto_quads,offset_triangles,offset_quads,offset_long_triangles,offset_long_quads;
         ass_fread(&offset_proto_triangles,4,1,&myfile);
         ass_fread(&offset_proto_quads,4,1,&myfile);
         ass_fread(&offset_triangles,4,1,&myfile);
         ass_fread(&offset_quads,4,1,&myfile);
         ass_fread(&offset_long_triangles,4,1,&myfile);
         ass_fread(&offset_long_quads,4,1,&myfile);

			// Create mesh
			msMesh *myMesh=msModel_GetMeshAt(pModel,msModel_AddMesh(pModel));
			msMesh_SetMaterialIndex(myMesh,0);
			char name[10];
			sprintf(name,"%d",no_meshes);
			strcat(name,"_mesh");
			msMesh_SetName(myMesh,name);
			no_meshes++;

			// Read in vertices
         myfile.pointer=pos+offset_vertices;
         int i;
         for (i=0;i<no_vertices;i++)
         {
            short a,b,c;
            ass_fread(&a,2,1,&myfile);
            ass_fread(&b,2,1,&myfile);
            ass_fread(&c,2,1,&myfile);
				msVertex * myVert=msMesh_GetVertexAt(myMesh,msMesh_AddVertex(myMesh));
				float v[3];
            v[0]=a*SCALE;
            v[1]=-b*SCALE;
            v[2]=c*SCALE;
				msVertex_SetVertex(myVert,v);
            short unknown_t;
            ass_fread(&unknown_t,2,1,&myfile);
//            ass_trace(run_name("unknown_t=",unknown_t,"\n"));
         }

			// Read in proto triangles
         myfile.pointer=pos+offset_proto_triangles;
         trk_load_polygons(no_proto_triangles,myMesh,&myfile,4);

			// Read in proto quads
         myfile.pointer=pos+offset_proto_quads;
         trk_load_polygons(no_proto_quads,myMesh,&myfile,5);

			// Read in triangles
         myfile.pointer=pos+offset_triangles;
         trk_load_polygons(no_triangles,myMesh,&myfile,0);

			// Read in quads
         myfile.pointer=pos+offset_quads;
         trk_load_polygons(no_quads,myMesh,&myfile,1);

			// Read in Long triangles
         myfile.pointer=pos+offset_long_triangles;
         trk_load_polygons(no_long_triangles,myMesh,&myfile,2);

			// Read in Long quads
         myfile.pointer=pos+offset_long_quads;
         trk_load_polygons(no_long_quads,myMesh,&myfile,3);
          
         myfile.pointer=pos+size;

      } else
      if (strcmp(chunk,"TIMS")==0)
      {
			char filename[10];
			sprintf(filename,"%d",no_tex);
			strcat(filename,"_texture.tga");
			convert_tim(&myfile,filename);
			msMaterial *myMat=msModel_GetMaterialAt(pModel,msModel_AddMaterial(pModel));
			msMaterial_SetName(myMat,filename);
			msMaterial_SetDiffuseTexture(myMat,filename);
			float diffuse[]={1,1,1,1};
			msMaterial_SetDiffuse(myMat,diffuse);
			no_tex++;
		} else
		{
         if (strcmp(chunk,"FINI")!=0)
			   myfile.pointer+=size;
		}

      count++;
	}
	while ((myfile.pointer<myfile.size) && (strcmp(chunk,"FINI")!=0));

    return 0;
}

void trk_load_polygons(int num, msMesh * obj, ass_file * myfile,int polygon_type)
{
   // Load all of num polygons in
   int i;
   for (i=0;i<num;i++)
   {
      unsigned short a,b,c,d;
		bool flip=false;
//		if (polygon_type>=2) obj->polygonlist[i+pbase]->two_sided=true;
      if ((polygon_type==1) || (polygon_type==3) || (polygon_type==5))
      {
         ass_fread(&d,2,1,myfile);
         ass_fread(&a,2,1,myfile);
         ass_fread(&c,2,1,myfile);
         ass_fread(&b,2,1,myfile);
         if (polygon_type==5) myfile->pointer+=4; else myfile->pointer+=8;
      } else
      {
         ass_fread(&a,2,1,myfile);
         ass_fread(&b,2,1,myfile);
         ass_fread(&c,2,1,myfile);
         if (polygon_type==4) myfile->pointer+=2; else myfile->pointer+=6;
      }

//		if ((!obj->vertexlist[a]) || (!obj->vertexlist[b]) || (!obj->vertexlist[c]))
//			bailout_error("Corrupt .trk file");
		word vs[3];
		vs[0]=a;
		vs[1]=b;
		vs[2]=c;
		msTriangle * myTri=msMesh_GetTriangleAt(obj,msMesh_AddTriangle(obj));
		msTriangle_SetVertexIndices(myTri,vs);
		msTriangle * myTri2;
      if ((polygon_type==1) || (polygon_type==3) || (polygon_type==5))
		{
			vs[0]=c;
			vs[1]=d;
			vs[2]=a;
			myTri2=msMesh_GetTriangleAt(obj,msMesh_AddTriangle(obj));
			msTriangle_SetVertexIndices(myTri2,vs);
		}

      unsigned short unknown_p_a;
      unsigned char unknown_p_b;
		unsigned char tex_seq;
		unsigned char u[4],v[4];
      if ((polygon_type==1) || (polygon_type==3))
      {
         ass_fread(&u[3],1,1,myfile);
         ass_fread(&v[3],1,1,myfile);
         ass_fread(&unknown_p_a,2,1,myfile);
         ass_fread(&u[0],1,1,myfile);
         ass_fread(&v[0],1,1,myfile);
         ass_fread(&tex_seq,1,1,myfile);
         ass_fread(&unknown_p_b,1,1,myfile);
         ass_fread(&u[2],1,1,myfile);
         ass_fread(&v[2],1,1,myfile);
         ass_fread(&u[1],1,1,myfile);
         ass_fread(&v[1],1,1,myfile);
      }
      if ((polygon_type==0) || (polygon_type==2))
      {
         ass_fread(&u[0],1,1,myfile);
         ass_fread(&v[0],1,1,myfile);
         ass_fread(&unknown_p_a,2,1,myfile);
         ass_fread(&u[1],1,1,myfile);
         ass_fread(&v[1],1,1,myfile);
         ass_fread(&tex_seq,1,1,myfile);
         ass_fread(&unknown_p_b,1,1,myfile);
         ass_fread(&u[2],1,1,myfile);
         ass_fread(&v[2],1,1,myfile);
      }
      if (polygon_type==4)
      {
         ass_fread(&u[0],1,1,myfile);
         ass_fread(&v[0],1,1,myfile);
         ass_fread(&u[1],1,1,myfile);
         ass_fread(&v[1],1,1,myfile);
         ass_fread(&unknown_p_a,2,1,myfile);
         ass_fread(&u[2],1,1,myfile);
         ass_fread(&v[2],1,1,myfile);
      }
      if (polygon_type==5)
      {
         ass_fread(&u[3],1,1,myfile);
         ass_fread(&v[3],1,1,myfile);
         ass_fread(&u[0],1,1,myfile);
         ass_fread(&v[0],1,1,myfile);
         ass_fread(&u[2],1,1,myfile);
         ass_fread(&v[2],1,1,myfile);
         ass_fread(&u[1],1,1,myfile);
         ass_fread(&v[1],1,1,myfile);
      }

		// Copy the UV coordinates into the vertices
		float uv[2];
		uv[0]=u[0]/256.0; uv[1]=v[0]/256.0;
		msVertex_SetTexCoords(msMesh_GetVertexAt(obj,a),uv);
		uv[0]=u[1]/256.0; uv[1]=v[1]/256.0;
		msVertex_SetTexCoords(msMesh_GetVertexAt(obj,b),uv);
		uv[0]=u[2]/256.0; uv[1]=v[2]/256.0;
		msVertex_SetTexCoords(msMesh_GetVertexAt(obj,c),uv);
      if ((polygon_type==1) || (polygon_type==3) || (polygon_type==5))
		{
			uv[0]=u[3]/256.0; uv[1]=v[3]/256.0;
			msVertex_SetTexCoords(msMesh_GetVertexAt(obj,d),uv);
		}

      if (polygon_type==0) myfile->pointer+=14;
      if (polygon_type==1) myfile->pointer+=16;
      if (polygon_type==2) myfile->pointer+=14+24;
      if (polygon_type==3) myfile->pointer+=16+28;
      if (polygon_type==4) myfile->pointer+=8;
      if (polygon_type==5) myfile->pointer+=8;

//		if (flip) obj->polygonlist[i+pbase]->flip();
   }             
}

// Based on tim2tga
void convert_tim(ass_file * timfile, char * outfile)
{
  /* picture buffer */
  int realxsize=0,xsize=0,ysize=0;
  char *scr=NULL;

  /* read/write buffer */
  unsigned char buffer[2048];

  int rc=1;
  int type;
  int clut;
  int depth=24;
  int colors;
  char * theclut=NULL;

    ass_fread(buffer,8,1,timfile);
    /* All TIM-files begin with 0x10! */
      type=buffer[4]&7;
      if (type==0) { depth=4;  colors=16; }
      if (type==1) { depth=8;  colors=256; }
      if (type==2) { depth=16; }
      if (type==3) { depth=24; }
      clut=(buffer[4]&8)>1;
      if ((depth<16) && (!clut))
      {
        errorMessage("paletted image with no palette!");
		  return;
      }
      if ((depth>=16) && (clut))
      {
        errorMessage("clut for real/true color??!");
		  return;
      }
//      ass_trace(run_name("Bitmap of color depth: ",depth,"\n"));
      if (clut)
      {
        unsigned short i,x,r,g,b;
        theclut=(char*)malloc(3*colors);
        if (!theclut)
        {
          errorMessage("error allocating memory for clut!");
			 return;
        }
        ass_fread(buffer,12,1,timfile);
        for (i=0;i<colors;i++)
        {
          ass_fread(&x,2,1,timfile);
          r=((x      ) & 31) << 3;
          g=((x >> 5 ) & 31) << 3;
          b=((x >> 10) & 31) << 3;
          *(theclut+i*3+0)=r;
          *(theclut+i*3+1)=g;
          *(theclut+i*3+2)=b;
        }
      }
      ass_fread(buffer,12,1,timfile);
      xsize=buffer[8]|(buffer[9]<<8);
      ysize=buffer[10]|(buffer[11]<<8);
        realxsize=xsize*16/depth;
//        ass_trace(run_name("Bitmap has size: ",realxsize,run_name_b(" x ",ysize,"\n")));
		unsigned char * mypic=(unsigned char *)malloc(4*realxsize*ysize);
        int x,y;
        for (y=0;y<ysize;y++) {
            ass_fread(buffer,2*xsize,1,timfile);
            for (x=0;x<realxsize;x++) {
                unsigned char pixel, r, g, b;

                if ((depth==4) || (depth==8))
                {
                   if (depth==4)
                   {
                     if (x%2==1) pixel=buffer[x/2]>>4;
                     if (x%2==0) pixel=buffer[x/2]&15;
                   }  else pixel=buffer[x];
                   r=theclut[pixel*3+0];
                   g=theclut[pixel*3+1];
                   b=theclut[pixel*3+2];
                }

                if (depth==16)
                {
                   unsigned short pixel;

                   /* convert 2 byte from the buffer into one word */
                   pixel=buffer[x*2]|(buffer[(x*2)+1]<<8);

                   /* "b" needs "& 31" as well to strip 16th bit used for semi-transparency */
                   b = ((pixel >> 10) & 31) << 3;
                   g = ((pixel >>  5) & 31) << 3;
                   r = ((pixel      ) & 31) << 3;
                }

                if (depth==24)
                {
                   unsigned int pixel;

                   /* convert 2 byte from the buffer into one word */
                   pixel=buffer[x*3]|(buffer[(x*3)+1]<<8)|(buffer[(x*3)+2]<<16);

                   /* "b" needs "& 31" as well to strip 16th bit used for semi-transparency */
                   b = ((pixel >> 16) & 127);
                   g = ((pixel >>  8) & 127);
                   r = ((pixel      ) & 127);
                }
					 mypic[4*y*realxsize+4*x+0]=r;
					 mypic[4*y*realxsize+4*x+1]=g;
					 mypic[4*y*realxsize+4*x+2]=b;
					 mypic[4*y*realxsize+4*x+3]=255;
            }
      }

  if (theclut) free(theclut);


	FILE *tgafile;
	tgafile=fopen(outfile,"wb");
	if (!tgafile) return;
	int c;
	/* create Targa-header */
	buffer[0]=0;                /* No image-ID field */
	buffer[1]=0;                /* no color map */
	buffer[2]=2;                /* rgb-pic uncompressed */
	buffer[3]=0;buffer[4]=0;    /* color map offset */
	buffer[5]=0;buffer[6]=0;    /* 0 entrys */
	buffer[7]=32;               /* 32 Bit color */
	buffer[8]=0;buffer[9]=0;    /* X-Position */
	buffer[10]=0;buffer[11]=0;  /* Y-Position */
	buffer[13]=(realxsize>>8)&255;buffer[12]=realxsize&255;     /* X-Size */
	buffer[15]=(ysize>>8)&255;buffer[14]=ysize&255;     /* Y-Size */
	buffer[16]=32; buffer[17]=0; /* 32 bit Color */
	fwrite(&buffer,18,1,tgafile);
	/* save bitmap (bottom up) */
	for (c=1;c<=ysize;c++)
		fwrite(mypic+((ysize-c)*realxsize*4),realxsize*4,1,tgafile);
	fclose(tgafile);
}
