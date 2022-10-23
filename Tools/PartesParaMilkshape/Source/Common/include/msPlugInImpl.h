#ifndef __MS_PLUGIN_IMPL_H__
#define __MS_PLUGIN_IMPL_H__



struct msModel;
class cMsPlugIn
{
public:
    enum
    {
        eTypeImport = 1,
        eTypeExport = 2,
        eTypeTool   = 3,
    };

public:
    cMsPlugIn () {};
    virtual ~cMsPlugIn () {};

public:
    virtual int             GetType () = 0;
    virtual const char *    GetTitle () = 0;
    virtual int             Execute (msModel* pModel) = 0;
};



typedef cMsPlugIn* (*FN_CREATE_PLUGIN)();

__declspec(dllexport) cMsPlugIn *CreatePlugIn ();



struct msModel;
class cPlugIn : public cMsPlugIn
{
    char szTitle[64];

public:
	cPlugIn ();
    virtual ~cPlugIn ();

public:
    int             GetType ();
    const char *    GetTitle ();
    int             Execute (msModel* pModel);
};



#endif // __MS_PLUGIN_IMPL_H__