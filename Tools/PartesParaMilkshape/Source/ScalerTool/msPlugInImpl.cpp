// =========================================================
// | Assimilation Software presents...                     |
// |                                                       |
// |  Milkshape Plugins  - (c) Graham (gameRevolt)         |
// =========================================================

#include "stdafx.h"
#include "resource.h"		// main symbols
#include "msPlugInImpl.h"
#include "msLib.h"

HINSTANCE self;

BOOL APIENTRY DllMain( HINSTANCE hModule, 
                       DWORD  ul_reason_for_call, 
                       LPVOID lpReserved
					 )
{
    switch (ul_reason_for_call)
	{
		case DLL_PROCESS_ATTACH:
			self=hModule;
			break;
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
    strcpy (szTitle, "Assimsoft Scaler Tool");
}



cPlugIn::~cPlugIn ()
{
}



int
cPlugIn::GetType ()
{
    return cMsPlugIn::eTypeTool;
}

void errorMessage(char * message)
{
    MessageBox (NULL,message,NULL,MB_OK);
}


const char*
cPlugIn::GetTitle ()
{
    return szTitle;
}

BOOL CALLBACK MyDialogProc(
  HWND hwndDlg,  // handle to dialog box
  UINT uMsg,     // message
  WPARAM wParam, // first message parameter
  LPARAM lParam  // second message parameter
)
{
	switch (uMsg)
	{
	case WM_INITDIALOG:
		char _length[30];
		float length;
		memcpy(&length,&lParam,4);
		sprintf(_length,"%f",length);
		SetDlgItemText(hwndDlg,IDC_LENGTH,_length);
		break;
	case WM_COMMAND:
		switch (LOWORD(wParam))
		{
		case IDCANCEL:
				EndDialog(hwndDlg,0);
				return TRUE;
				break;
		case IDOK:
				char _length[30];
				GetDlgItemText(hwndDlg,IDC_LENGTH,_length,30);
				float length=(float)atof(_length);
				int lParam;
				memcpy(&lParam,&length,4);
				EndDialog(hwndDlg,lParam);
				return TRUE;
				break;
		}
		break;
	}
	return FALSE;
}

int
cPlugIn::Execute (msModel *pModel)
{
    if (!pModel)
        return -1;

	// Find bounds
	float maxx=-1000000,maxy=-1000000,maxz=-1000000,minx=1000000,miny=1000000,minz=1000000;
	bool empty=true;
	int i;
	for (i=0;i<pModel->nNumMeshes;i++)
	{
		int j;
		for (j=0;j<pModel->pMeshes[i].nNumVertices;j++)
		{
			float x=pModel->pMeshes[i].pVertices[j].Vertex[0];
			float y=pModel->pMeshes[i].pVertices[j].Vertex[1];
			float z=pModel->pMeshes[i].pVertices[j].Vertex[2];
			if (x>maxx) maxx=x;
			if (y>maxy) maxy=y;
			if (z>maxz) maxz=z;
			if (x<minx) minx=x;
			if (y<miny) miny=y;
			if (z<minz) minz=z;
			empty=false;
		}
	}
	if (empty)
	{
		errorMessage("Model is empty");
		return 0;
	}

	// Therefore we know the dimensions
	float length=(maxz-minz)*10;

	// Put this into the form
	int lParam;
	memcpy(&lParam,&length,4);
	int nResponse=DialogBoxParam(
		self,  // handle to module
		(LPCTSTR)IDD_SCALER_TOOL_DIALOG,   // dialog box template name
		NULL,      // handle to owner window
		MyDialogProc,  // dialog box procedure
		lParam
	);
	
	if (nResponse != 0)
	{
		float newlength;
		memcpy(&newlength,&nResponse,4);
		float scale=newlength/length;

		// Do the rescale
		for (i=0;i<pModel->nNumMeshes;i++)
		{
			int j;
			for (j=0;j<pModel->pMeshes[i].nNumVertices;j++)
			{
				pModel->pMeshes[i].pVertices[j].Vertex[0]*=scale;
				pModel->pMeshes[i].pVertices[j].Vertex[1]*=scale;
				pModel->pMeshes[i].pVertices[j].Vertex[2]*=scale;
			}
		}
		for (i=0;i<pModel->nNumBones;i++)
		{
			pModel->pBones[i].Position[0]*=scale;
			pModel->pBones[i].Position[1]*=scale;
			pModel->pBones[i].Position[2]*=scale;
		}
	}
   return 0;
}
