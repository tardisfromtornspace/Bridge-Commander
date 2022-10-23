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

char * make_texture_id(char szName[]);
void calculate_normal(float ax, float ay, float az, float bx, float by, float bz, float cx, float cy, float cz, float *nx, float *ny, float *nz);

#define SCALE 0.444

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
    strcpy (szTitle, "Star Fleet Command MOD...");
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

char temp_texture[30];
char * make_texture_id(char szName[])
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

	 strcpy(temp_texture,szName+j);
    for (j=strlen(temp_texture)-1;j>=0;j--)
    {
		 if (temp_texture[j]=='.') temp_texture[j]='\0';
	 }
    return temp_texture;
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
        ::MessageBox (NULL, "The model is empty!  Nothing exported!", "SFC Export", MB_OK | MB_ICONWARNING);
        return 0;
    }

    //
    // choose filename
    //
    OPENFILENAME ofn;
    memset (&ofn, 0, sizeof (OPENFILENAME));
    
    char szFile[MS_MAX_PATH];
    char szFileTitle[MS_MAX_PATH];
    char szDefExt[32] = "txt";
    char szFilter[128] = "Starfleet Command MOD Files (*.mod)\0*.mod\0All Files (*.*)\0*.*\0\0";
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
    ofn.lpstrTitle = "Export SFC MOD -- assimsoft.com";

    if (!::GetSaveFileName (&ofn))
        return 0;

    //
    // export
    //
    FILE *file = fopen (szFile, "wb");
    if (!file)
        return -1;

    int i, j;
    char szName[MS_MAX_PATH];
    unsigned int standby=666;

    //
    // header
    //
    char header[20];
    strcpy(header,"MDLS");
    unsigned int version=2<<8;
    fwrite(header,strlen(header),1,file);
    fwrite(&standby,4,1,file); // Later: file size
    fwrite(&version,4,1,file);
    fwrite(&standby,4,1,file); // Later: radius around ship
    unsigned int lods=1;
    fwrite(&lods,4,1,file);
    float lod_number=5;
    fwrite(&lod_number,4,1,file);
    lod_number=0;
    fwrite(&lod_number,4,1,file);
    lod_number=100;
    fwrite(&lod_number,4,1,file);
    lod_number=200;
    fwrite(&lod_number,4,1,file);
    lod_number=300;
    fwrite(&lod_number,4,1,file);
    lod_number=400;
    fwrite(&lod_number,4,1,file);

    //
    // strings
    //
    unsigned int string_len=0;
    for (i = 0; i < msModel_GetMaterialCount (pModel); i++)
    {
        msMaterial *pMaterial = msModel_GetMaterialAt (pModel, i);
        strcpy(szName,"");
        if (pMaterial) msMaterial_GetDiffuseTexture (pMaterial, szName, MS_MAX_PATH);
        string_len+=1+strlen(make_texture_id(szName));
        strcpy(szName,"");
        if (pMaterial) msMaterial_GetAlphaTexture (pMaterial, szName, MS_MAX_PATH);
        if (strlen(szName)>0) string_len+=1+strlen(make_texture_id(szName));
         else 
			{
	         if (pMaterial)
				{
					msMaterial_GetDiffuseTexture (pMaterial, szName, MS_MAX_PATH);
					string_len+=1+strlen(make_texture_id(szName))+1;
				}
			}
    }
	 for (i=0;i<msModel_GetBoneCount(pModel);i++)
	 {
		 msBone* myBone=msModel_GetBoneAt(pModel,i);
		 char boneName[31];
		 msBone_GetName(myBone,boneName,30);
       string_len+=1+strlen(boneName);
	 }
    int u=4-(string_len%4);
    if (u==4) u=0;
    string_len+=u;
    char * string_data=(char *)malloc(string_len);
    memset(string_data,0,string_len);
    unsigned int pos=0;
    for (i = 0; i < msModel_GetMaterialCount (pModel); i++)
    {
        msMaterial *pMaterial = msModel_GetMaterialAt (pModel, i);
        strcpy(szName,"");
        if (pMaterial) msMaterial_GetDiffuseTexture (pMaterial, szName, MS_MAX_PATH);
        char id[MS_MAX_NAME];
        strcpy(id,make_texture_id(szName));
        strcpy(string_data+pos,id);
        pos+=1+strlen(id);
        strcpy(szName,"");

		  // Add the lightmap to the string table. If there is none defined, we might be generating
		  // one so stuff a self-generated name in anyway
        if (pMaterial) msMaterial_GetAlphaTexture (pMaterial, szName, MS_MAX_PATH);
        if (strlen(szName)>0)
		  {
	        strcpy(id,make_texture_id(szName));
		  } else strcat(id,"i"); // Just dump an "i" for "illumination-map" on it
        strcpy(string_data+pos,id);
        pos+=1+strlen(id);
    }
	 for (i=0;i<msModel_GetBoneCount(pModel);i++)
	 {
		 msBone* myBone=msModel_GetBoneAt(pModel,i);
		 char boneName[31];
		 msBone_GetName(myBone,boneName,30);
		 strcat(string_data+pos,boneName);
       pos+=1+strlen(boneName);
	 }
    strcpy(header,"STRS");
    fwrite(header,4,1,file);
    fwrite(&string_len,4,1,file);
    fwrite(string_data,string_len,1,file);

    //
    // materials
    //
    strcpy(header,"MATS");
    fwrite(header,4,1,file);
    fpos_t mat_size_offset;
    fgetpos(file,&mat_size_offset);
    fwrite(&standby,4,1,file); // Later: size of this section
    unsigned int mat_size=0;
    for (i = 0; i < msModel_GetMaterialCount (pModel); i++)
    {
        char texture[MS_MAX_PATH],lightmap[MS_MAX_PATH];
        char _texture[30],_lightmap[30];

        msMaterial *pMaterial = msModel_GetMaterialAt (pModel, i);
        msMaterial_GetDiffuseTexture (pMaterial, texture, 128);
        if (strcmp(texture,"")==0) 
		  {
			  errorMessage("All materials must have textures");
			  return 0;
		  }
        strcpy(_texture,make_texture_id(texture));
        msMaterial_GetAlphaTexture (pMaterial, lightmap, 128);
        strcpy(_lightmap,make_texture_id(lightmap));

        // Flags
        unsigned int flags=0x2+0x1;
        if (strcmp(lightmap,"")!=0) flags=flags | 0x20;

		  // Ensure texture is a bmp or pcx
			char newtexture[MS_MAX_PATH];
			strcpy(newtexture,texture);
			newtexture[strlen(newtexture)-4]='\0';
			strcat(newtexture,".bmp");
			ilInit();
			if (ilLoadImage(texture))
			{
				ilSaveImage(newtexture);
			}
			if (strcmp(lightmap,"")!=0)
			{
				strcpy(newtexture,lightmap);
				newtexture[strlen(newtexture)-4]='\0';
				strcat(newtexture,".bmp");
				ilInit();
				if (ilLoadImage(lightmap))
				{
					ilSaveImage(newtexture);
				}
			} else
			{
				// We will have to split the texture to form a lightmap
				int depth=ilGetInteger(IL_IMAGE_BITS_PER_PIXEL);
				int width=ilGetInteger(IL_IMAGE_WIDTH);
				int height=ilGetInteger(IL_IMAGE_HEIGHT);
				if (depth==32)
				{
					bool blank=true;
					ILubyte *data=ilGetAlpha(IL_UNSIGNED_BYTE);
					ILuint newImage;
					ilGenImages(1,&newImage);
					ilBindImage(newImage);
					ilTexImage(width,height,1,1,IL_COLOR_INDEX,IL_UNSIGNED_BYTE,data);
					unsigned char Pal[256*3];
					int x,y;
					for (x=0;x<256;x++)
					{
						Pal[x*3+0]=x;
						Pal[x*3+1]=x;
						Pal[x*3+2]=x;
					}
					ilRegisterPal(Pal,256*3,IL_PAL_RGB24);
					for (y=0;y<height;y++)
					{
						for (x=0;x<width;x++)
						{
							unsigned char alpha=*(data+y*width+x);
							if (alpha!=255) blank=false;
						}
					}

					// Apparently this was a real alpha channel, so export it
					if (!blank)
					{
						flags=flags | 0x20;
						char newlightmap[MS_MAX_PATH];
						strcpy(newlightmap,newtexture);
						strcpy(newlightmap+strlen(newlightmap)-4,"i.bmp");
						ilSaveImage(newlightmap);
						strcpy(_lightmap,make_texture_id(newlightmap));
					}
				}
			}

			fwrite(&flags,4,1,file);

        // Colours
        float s;
        int _s=0x00FFFFFF;
        fwrite(&_s,4,1,file);
        msVec4 vec4;
        msMaterial_GetAmbient (pMaterial, vec4);
        s=(vec4[0]+vec4[1]+vec4[2])/3;
        fwrite(&s,4,1,file);
        msMaterial_GetDiffuse (pMaterial, vec4);
        s=(vec4[0]+vec4[1]+vec4[2])/3;
        fwrite(&s,4,1,file);
        msMaterial_GetEmissive (pMaterial, vec4);
        s=(vec4[0]+vec4[1]+vec4[2])/3;
        fwrite(&s,4,1,file);

        mat_size+=5*4;
    
        // Texture
        unsigned int temp=0;
        fwrite(&temp,4,1,file);
        unsigned int j=0;
        while (j<string_len) // Find out where we've put this string
        {
            if (strcmp(_texture,string_data+j)==0) break;
            j+=strlen(string_data+j)+1;
        }
        fwrite(&j,4,1,file);

        mat_size+=2*4;

        // Lightmap
        if (flags&32)
        {
            j=0;
            fwrite(&temp,4,1,file);
            while (j<string_len) // Find out where we've put this string
            {
                if (strcmp(_lightmap,string_data+j)==0) break;
                j+=strlen(string_data+j)+1;
            }
            fwrite(&j,4,1,file);

            mat_size+=2*4;
        }
    }

    //
    // points section
    //
    strcpy(header,"PNTS");
    fwrite(header,4,1,file);
    pos=16*msModel_GetBoneCount(pModel);
    fwrite(&pos,4,1,file);
	 for (i=0;i<msModel_GetBoneCount(pModel);i++)
	 {
		 msBone* myBone=msModel_GetBoneAt(pModel,i);
		 float v[3];
		 msBone_GetPosition(myBone,v);
		 v[0]*=SCALE;
		 v[1]*=SCALE;
		 v[2]*=SCALE;
	    fwrite(&v[2],4,1,file);
	    fwrite(&v[1],4,1,file);
	    fwrite(&v[0],4,1,file);
		 char boneName[31];
		 msBone_GetName(myBone,boneName,30);
		 int j=0;
       while (j<string_len) // Find out where we've put this string
       {
          if (strcmp(boneName,string_data+j)==0) break;
          j+=strlen(string_data+j)+1;
       }
       fwrite(&j,4,1,file);
	 }


    //
    // MOD0 section
    //
    strcpy(header,"MOD0");
    fwrite(header,4,1,file);
    fpos_t mod0_size_offset;
    fgetpos(file,&mod0_size_offset);
    fwrite(&standby,4,1,file); // Later: size of this section
    fpos_t mod0_vertex_offset;
    fgetpos(file,&mod0_vertex_offset);
    fwrite(&standby,4,1,file); // Later: vertices
    fpos_t mod0_polygon_offset;
    fgetpos(file,&mod0_polygon_offset);
    fwrite(&standby,4,1,file); // Later: polygons
    int mod_size=8;

    //
    // vertices
    //
    unsigned int no_vertices=0;
    float max_radius=0;
    strcpy(header,"VTXS");
    fwrite(header,4,1,file);
    mod_size+=4;
    for (i = 0; i < msModel_GetMeshCount (pModel); i++)
    {
        msMesh *pMesh = msModel_GetMeshAt (pModel, i);
        no_vertices+=msMesh_GetVertexCount (pMesh);
    }
    unsigned int vtx_size=no_vertices*12;
    fwrite(&vtx_size,4,1,file);
    mod_size+=4;
    for (i = 0; i < msModel_GetMeshCount (pModel); i++)
    {
        msMesh *pMesh = msModel_GetMeshAt (pModel, i);

        for (j = 0; j < msMesh_GetVertexCount (pMesh); j++)
        {
            msVertex *pVertex = msMesh_GetVertexAt (pMesh, j);
            msVec3 Vertex;

            msVertex_GetVertex (pVertex, Vertex);

				Vertex[0]*=SCALE;
				Vertex[1]*=SCALE;
				Vertex[2]*=SCALE;
            fwrite(&Vertex[2],4,1,file);
            fwrite(&Vertex[1],4,1,file);
            fwrite(&Vertex[0],4,1,file);
            mod_size+=12;

            float radius=(float)sqrt(Vertex[0]*Vertex[0]+Vertex[1]*Vertex[1]+Vertex[2]*Vertex[2]);
            if (radius>max_radius) max_radius=radius;
        }
    }

    //
    // triangles
    //
    unsigned int v_base=0;
    unsigned int no_polygons=0;
    for (i = 0; i < msModel_GetMeshCount (pModel); i++)
    {
        msMesh *pMesh = msModel_GetMeshAt (pModel, i);
        int m=msMesh_GetMaterialIndex (pMesh);
        if (m==-1) m=0;

        for (j = 0; j < msMesh_GetTriangleCount (pMesh); j++)
        {
            msTriangle* mytri=msMesh_GetTriangleAt (pMesh,j);

            strcpy(header,"POLY");
            fwrite(header,4,1,file);
            unsigned int temp_size=5*4+7*3*4;
            fwrite(&temp_size,4,1,file);
            unsigned int tri=3;
            fwrite(&tri,4,1,file);
            fwrite(&m,4,1,file);
            unsigned short normals[3];
            msTriangle_GetNormalIndices (mytri, normals);
            float mynormal[3][3];
            msMesh_GetVertexNormalAt (pMesh, normals[0],mynormal[0]);
            msMesh_GetVertexNormalAt (pMesh, normals[1],mynormal[1]);
            msMesh_GetVertexNormalAt (pMesh, normals[2],mynormal[2]);

            unsigned short myverts[3];
            msTriangle_GetVertexIndices (mytri, myverts);

            msVertex* verta=msMesh_GetVertexAt (pMesh, myverts[0]);
            msVec3 va;
            msVertex_GetVertex (verta, va);
            verta=msMesh_GetVertexAt (pMesh, myverts[1]);
            msVec3 vb;
            msVertex_GetVertex (verta, vb);
            verta=msMesh_GetVertexAt (pMesh, myverts[2]);
            msVec3 vc;
            msVertex_GetVertex (verta, vc);
            float nx=0,ny=0,nz=1;
            calculate_normal(va[0],va[1],va[2],vb[0],vb[1],vb[2],vc[0],vc[1],vc[2],&nx,&ny,&nz);
            fwrite(&nz,4,1,file);
            fwrite(&ny,4,1,file);
            fwrite(&nx,4,1,file);

            int k;
            for (k=0;k<3;k++)
            {
                unsigned int tempv=myverts[k]+v_base;
                fwrite(&tempv,4,1,file);
                if ((mynormal[k][0]==0) && (mynormal[k][1]==0) && (mynormal[k][2]==0))
                {
                   fwrite(&nz,4,1,file);
                   fwrite(&ny,4,1,file);
                   fwrite(&nx,4,1,file);
                } else
                {
                   fwrite(&mynormal[k][2],4,1,file);
                   fwrite(&mynormal[k][1],4,1,file);
                   fwrite(&mynormal[k][0],4,1,file);
                }
                msVertex* myvert=msMesh_GetVertexAt (pMesh, myverts[k]);
                float uv[2];
                msVertex_GetTexCoords (myvert,uv);
                uv[1]=1-uv[1];
                fwrite(&uv[0],4,1,file);
                fwrite(&uv[1],4,1,file);
                unsigned int junk=0;
                fwrite(&junk,4,1,file);
            }

            mod_size+=8+temp_size;

            no_polygons++;
        }

        v_base+=msMesh_GetVertexCount (pMesh);
    }

    // Fix up any bits not done yet
    fpos_t file_size;
    fgetpos(file,&file_size);
    file_size-=8;
    fseek(file,4,SEEK_SET);
    fwrite(&file_size,4,1,file);
    fseek(file,12,SEEK_SET);
    fwrite(&max_radius,4,1,file);
    fsetpos(file,&mat_size_offset);
    fwrite(&mat_size,4,1,file);
    fsetpos(file,&mod0_size_offset);
    fwrite(&mod_size,4,1,file);
    fsetpos(file,&mod0_vertex_offset);
    fwrite(&no_vertices,4,1,file);
    fsetpos(file,&mod0_polygon_offset);
    fwrite(&no_polygons,4,1,file);

    fclose (file);

    // don't forget to destroy the model
    free(string_data);
    msModel_Destroy (pModel);

    return 0;
}

void calculate_normal(float ax, float ay, float az, float bx, float by, float bz, float cx, float cy, float cz, float *nx, float *ny, float *nz)
{
	// Calculate two vectors on the plane of the polygon
	float vax,vay,vaz,vbx,vby,vbz;
	vax=bx-ax;
	vay=by-ay;
	vaz=bz-az;
	vbx=cx-bx;
	vby=cy-by;
	vbz=cz-bz;

	// Calculate the cross-product of the vectors to get the normal
	*nx=vay*vbz-vaz*vby;
	*ny=vaz*vbx-vax*vbz;
	*nz=vax*vby-vay*vbx;

	// Okay, now we have to make our normals unit length
	float len=(float)sqrt((*nx)*(*nx)+(*ny)*(*ny)+(*nz)*(*nz));
   *nx/=len;
   *ny/=len;
   *nz/=len;
}
