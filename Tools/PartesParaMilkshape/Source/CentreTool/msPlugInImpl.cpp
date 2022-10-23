// =========================================================
// | Assimilation Software presents...                     |
// |                                                       |
// |  Milkshape Plugins  - (c) Graham (gameRevolt)         |
// =========================================================

#include "stdafx.h"
#include "msPlugInImpl.h"
#include "msLib.h"


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
    strcpy (szTitle, "Centre Selected Points (and re-adjust joints)");
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

int cPlugIn::Execute (msModel *pModel)
{
    if (!pModel)
        return -1;

	// Find average point
	float x=0,y=0,z=0;
	int count=0;
	int i;
	for (i=0;i<pModel->nNumMeshes;i++)
	{
		int j;
		for (j=0;j<pModel->pMeshes[i].nNumVertices;j++)
		{
			float _x=pModel->pMeshes[i].pVertices[j].Vertex[0];
			float _y=pModel->pMeshes[i].pVertices[j].Vertex[1];
			float _z=pModel->pMeshes[i].pVertices[j].Vertex[2];
			if (pModel->pMeshes[i].pVertices[j].nFlags & 1)
			{
				x+=_x;
				y+=_y;
				z+=_z;
				count++;
			}
		}
	}

	if (count==0) return 0;

	x/=count;
	y/=count;
	z/=count;

	for (i=0;i<pModel->nNumMeshes;i++)
	{
		int j;
		for (j=0;j<pModel->pMeshes[i].nNumVertices;j++)
		{
			float *_x=&pModel->pMeshes[i].pVertices[j].Vertex[0];
			float *_y=&pModel->pMeshes[i].pVertices[j].Vertex[1];
			float *_z=&pModel->pMeshes[i].pVertices[j].Vertex[2];
			if (pModel->pMeshes[i].pVertices[j].nFlags & 1)
			{
				(*_x)-=x;
				(*_y)-=y;
				(*_z)-=z;
			}
		}
	}
	for (i=0;i<pModel->nNumBones;i++)
	{
		pModel->pBones[i].Position[0]-=x;
		pModel->pBones[i].Position[1]-=y;
		pModel->pBones[i].Position[2]-=z;
	}

	return 0;
}

