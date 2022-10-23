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
#include "../common/include/il/ilu.h"

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
    strcpy (szTitle, "Assimsoft Lightmap Flip Tool");
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


	 int i;
    for (i = 0; i < msModel_GetMaterialCount (pModel); i++)
    {
		   char texture[MS_MAX_PATH];
		   char lightmap[MS_MAX_PATH];

         msMaterial *pMaterial = msModel_GetMaterialAt (pModel, i);
         msMaterial_GetDiffuseTexture (pMaterial, texture, 128);
         if (strcmp(texture,"")==0) continue;
         msMaterial_GetAlphaTexture (pMaterial, lightmap, 128);

			// We don't have an alphamap-lightamp thus we are doing Armada/BC->SFC
			if (strcmp(lightmap,"")==0)
			{
				// Ensure texture is a bmp or pcx
				char newtexture[MS_MAX_PATH];
				strcpy(newtexture,texture);
				newtexture[strlen(newtexture)-4]='\0';
				strcat(newtexture,".bmp");
				ilInit();
				if (ilLoadImage(texture))
				{
					ilSaveImage(newtexture);
					msMaterial_SetDiffuseTexture(pMaterial,newtexture);

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
							char newlightmap[MS_MAX_PATH];
							strcpy(newlightmap,newtexture);
							strcpy(newlightmap+strlen(newlightmap)-4,"i.bmp");
							ilSaveImage(newlightmap);
							msMaterial_SetAlphaTexture(pMaterial,newlightmap);
						}
					}
				}
			} else // SFC->BC/Armada
			{
				char newtexture[MS_MAX_PATH];
				strcpy(newtexture,texture);
				newtexture[strlen(newtexture)-4]='\0';
				strcat(newtexture,".tga");
				ilInit();
				if (ilLoadImage(texture))
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

					ilSaveImage(newtexture);
					msMaterial_SetAlphaTexture(pMaterial,"");
					msMaterial_SetDiffuseTexture(pMaterial,newtexture);
				}
			}
    }



    return 0;
}

