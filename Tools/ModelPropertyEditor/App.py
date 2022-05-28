# This file was created automatically by SWIG.
import Appc
import new
class NiAVObject:
    def __init__(self,this):
        self.this = this

    def __repr__(self):
        return "<C NiAVObject instance at %s>" % (self.this,)
class NiAVObjectPtr(NiAVObject):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = NiAVObject



class NiColor:
    def __init__(self,*args):
        self.this = apply(Appc.new_NiColor,args)
        self.thisown = 1

    __setmethods__ = {
        "r" : Appc.NiColor_r_set,
        "g" : Appc.NiColor_g_set,
        "b" : Appc.NiColor_b_set,
    }
    def __setattr__(self,name,value):
        if (name == "this") or (name == "thisown"): self.__dict__[name] = value; return
        method = NiColor.__setmethods__.get(name,None)
        if method: return method(self,value)
        self.__dict__[name] = value
    __getmethods__ = {
        "r" : Appc.NiColor_r_get,
        "g" : Appc.NiColor_g_get,
        "b" : Appc.NiColor_b_get,
    }
    def __getattr__(self,name):
        method = NiColor.__getmethods__.get(name,None)
        if method: return method(self)
        raise AttributeError,name
    def __repr__(self):
        return "<C NiColor instance at %s>" % (self.this,)
class NiColorPtr(NiColor):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = NiColor



class NiColorA:
    def __init__(self,*args):
        self.this = apply(Appc.new_NiColorA,args)
        self.thisown = 1

    __setmethods__ = {
        "r" : Appc.NiColorA_r_set,
        "g" : Appc.NiColorA_g_set,
        "b" : Appc.NiColorA_b_set,
        "a" : Appc.NiColorA_a_set,
    }
    def __setattr__(self,name,value):
        if (name == "this") or (name == "thisown"): self.__dict__[name] = value; return
        method = NiColorA.__setmethods__.get(name,None)
        if method: return method(self,value)
        self.__dict__[name] = value
    __getmethods__ = {
        "r" : Appc.NiColorA_r_get,
        "g" : Appc.NiColorA_g_get,
        "b" : Appc.NiColorA_b_get,
        "a" : Appc.NiColorA_a_get,
    }
    def __getattr__(self,name):
        method = NiColorA.__getmethods__.get(name,None)
        if method: return method(self)
        raise AttributeError,name
    def __repr__(self):
        return "<C NiColorA instance at %s>" % (self.this,)
class NiColorAPtr(NiColorA):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = NiColorA



class TGStream:
    def __init__(self,this):
        self.this = this

    def __repr__(self):
        return "<C TGStream instance at %s>" % (self.this,)
class TGStreamPtr(TGStream):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = TGStream



class TGBufferStream(TGStream):
    def __init__(self,*args):
        self.this = apply(Appc.new_TGBufferStream,args)
        self.thisown = 1

    def __del__(self,Appc=Appc):
        if self.thisown == 1 :
            Appc.delete_TGBufferStream(self)
    def __repr__(self):
        return "<C TGBufferStream instance at %s>" % (self.this,)
class TGBufferStreamPtr(TGBufferStream):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = TGBufferStream


TGBufferStream.Close = new.instancemethod(Appc.TGBufferStream_Close, None, TGBufferStream)
TGBufferStream.SetWriteMode = new.instancemethod(Appc.TGBufferStream_SetWriteMode, None, TGBufferStream)
TGBufferStream.GetWriteMode = new.instancemethod(Appc.TGBufferStream_GetWriteMode, None, TGBufferStream)
TGBufferStream.Read = new.instancemethod(Appc.TGBufferStream_Read, None, TGBufferStream)
TGBufferStream.Write = new.instancemethod(Appc.TGBufferStream_Write, None, TGBufferStream)
TGBufferStream.ReadCLine = new.instancemethod(Appc.TGBufferStream_ReadCLine, None, TGBufferStream)
TGBufferStream.WriteCLine = new.instancemethod(Appc.TGBufferStream_WriteCLine, None, TGBufferStream)
TGBufferStream.ReadCString = new.instancemethod(Appc.TGBufferStream_ReadCString, None, TGBufferStream)
TGBufferStream.WriteCString = new.instancemethod(Appc.TGBufferStream_WriteCString, None, TGBufferStream)
TGBufferStream.ReadCWLine = new.instancemethod(Appc.TGBufferStream_ReadCWLine, None, TGBufferStream)
TGBufferStream.WriteCWLine = new.instancemethod(Appc.TGBufferStream_WriteCWLine, None, TGBufferStream)
TGBufferStream.ReadWChar = new.instancemethod(Appc.TGBufferStream_ReadWChar, None, TGBufferStream)
TGBufferStream.WriteWChar = new.instancemethod(Appc.TGBufferStream_WriteWChar, None, TGBufferStream)
TGBufferStream.ReadChar = new.instancemethod(Appc.TGBufferStream_ReadChar, None, TGBufferStream)
TGBufferStream.ReadBool = new.instancemethod(Appc.TGBufferStream_ReadBool, None, TGBufferStream)
TGBufferStream.ReadShort = new.instancemethod(Appc.TGBufferStream_ReadShort, None, TGBufferStream)
TGBufferStream.ReadInt = new.instancemethod(Appc.TGBufferStream_ReadInt, None, TGBufferStream)
TGBufferStream.ReadLong = new.instancemethod(Appc.TGBufferStream_ReadLong, None, TGBufferStream)
TGBufferStream.ReadFloat = new.instancemethod(Appc.TGBufferStream_ReadFloat, None, TGBufferStream)
TGBufferStream.ReadDouble = new.instancemethod(Appc.TGBufferStream_ReadDouble, None, TGBufferStream)
TGBufferStream.WriteBool = new.instancemethod(Appc.TGBufferStream_WriteBool, None, TGBufferStream)
TGBufferStream.WriteChar = new.instancemethod(Appc.TGBufferStream_WriteChar, None, TGBufferStream)
TGBufferStream.WriteShort = new.instancemethod(Appc.TGBufferStream_WriteShort, None, TGBufferStream)
TGBufferStream.WriteInt = new.instancemethod(Appc.TGBufferStream_WriteInt, None, TGBufferStream)
TGBufferStream.WriteLong = new.instancemethod(Appc.TGBufferStream_WriteLong, None, TGBufferStream)
TGBufferStream.WriteFloat = new.instancemethod(Appc.TGBufferStream_WriteFloat, None, TGBufferStream)
TGBufferStream.WriteDouble = new.instancemethod(Appc.TGBufferStream_WriteDouble, None, TGBufferStream)
TGBufferStream.ReadID = new.instancemethod(Appc.TGBufferStream_ReadID, None, TGBufferStream)
TGBufferStream.WriteID = new.instancemethod(Appc.TGBufferStream_WriteID, None, TGBufferStream)
TGBufferStream.GetBuffer = new.instancemethod(Appc.TGBufferStream_GetBuffer, None, TGBufferStream)
TGBufferStream.OpenBuffer = new.instancemethod(Appc.TGBufferStream_OpenBuffer, None, TGBufferStream)
TGBufferStream.CloseBuffer = new.instancemethod(Appc.TGBufferStream_CloseBuffer, None, TGBufferStream)
TGBufferStream.GetPos = new.instancemethod(Appc.TGBufferStream_GetPos, None, TGBufferStream)
TGBufferStream.GetLength = new.instancemethod(Appc.TGBufferStream_GetLength, None, TGBufferStream)
TGBufferStream.Eof = new.instancemethod(Appc.TGBufferStream_Eof, None, TGBufferStream)

class TGLocalizationDatabase:
    def __init__(self,this):
        self.this = this

    def GetString(*args):
        val = apply(Appc.TGLocalizationDatabase_GetString,args)
        if val: val = TGStringPtr(val) 
        return val
    def __repr__(self):
        return "<C TGLocalizationDatabase instance at %s>" % (self.this,)
class TGLocalizationDatabasePtr(TGLocalizationDatabase):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = TGLocalizationDatabase


TGLocalizationDatabase.HasString = new.instancemethod(Appc.TGLocalizationDatabase_HasString, None, TGLocalizationDatabase)
TGLocalizationDatabase.GetFilename = new.instancemethod(Appc.TGLocalizationDatabase_GetFilename, None, TGLocalizationDatabase)

class TGLocalizationManager:
    def __init__(self,this):
        self.this = this

    def Load(*args):
        val = apply(Appc.TGLocalizationManager_Load,args)
        if val: val = TGLocalizationDatabasePtr(val) 
        return val
    def GetIfRegistered(*args):
        val = apply(Appc.TGLocalizationManager_GetIfRegistered,args)
        if val: val = TGLocalizationDatabasePtr(val) 
        return val
    def __repr__(self):
        return "<C TGLocalizationManager instance at %s>" % (self.this,)
class TGLocalizationManagerPtr(TGLocalizationManager):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = TGLocalizationManager


TGLocalizationManager.Unload = new.instancemethod(Appc.TGLocalizationManager_Unload, None, TGLocalizationManager)
TGLocalizationManager.DeleteAll = new.instancemethod(Appc.TGLocalizationManager_DeleteAll, None, TGLocalizationManager)
TGLocalizationManager.Purge = new.instancemethod(Appc.TGLocalizationManager_Purge, None, TGLocalizationManager)
TGLocalizationManager.RegisterDatabase = new.instancemethod(Appc.TGLocalizationManager_RegisterDatabase, None, TGLocalizationManager)

class TGObject:
    def __init__(self,this):
        self.this = this

    def __repr__(self):
        return "<C TGObject instance at %s>" % (self.this,)
class TGObjectPtr(TGObject):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = TGObject


TGObject.GetObjType = new.instancemethod(Appc.TGObject_GetObjType, None, TGObject)
TGObject.IsTypeOf = new.instancemethod(Appc.TGObject_IsTypeOf, None, TGObject)
TGObject.GetObjID = new.instancemethod(Appc.TGObject_GetObjID, None, TGObject)
TGObject.Destroy = new.instancemethod(Appc.TGObject_Destroy, None, TGObject)
TGObject.Print = new.instancemethod(Appc.TGObject_Print, None, TGObject)

class TGAttrObject(TGObject):
    def __init__(self,this):
        self.this = this

    def __repr__(self):
        return "<C TGAttrObject instance at %s>" % (self.this,)
class TGAttrObjectPtr(TGAttrObject):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = TGAttrObject


TGAttrObject.LookupAttrValue = new.instancemethod(Appc.TGAttrObject_LookupAttrValue, None, TGAttrObject)
TGAttrObject.GetAttrValue = new.instancemethod(Appc.TGAttrObject_GetAttrValue, None, TGAttrObject)
TGAttrObject.SetAttrValue = new.instancemethod(Appc.TGAttrObject_SetAttrValue, None, TGAttrObject)
TGAttrObject.RemoveAttr = new.instancemethod(Appc.TGAttrObject_RemoveAttr, None, TGAttrObject)
TGAttrObject.LookupAttrInt = new.instancemethod(Appc.TGAttrObject_LookupAttrInt, None, TGAttrObject)
TGAttrObject.GetAttrInt = new.instancemethod(Appc.TGAttrObject_GetAttrInt, None, TGAttrObject)
TGAttrObject.SetAttrInt = new.instancemethod(Appc.TGAttrObject_SetAttrInt, None, TGAttrObject)

class TGTemplatedAttrObject(TGAttrObject):
    def __init__(self,this):
        self.this = this

    def __repr__(self):
        return "<C TGTemplatedAttrObject instance at %s>" % (self.this,)
class TGTemplatedAttrObjectPtr(TGTemplatedAttrObject):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = TGTemplatedAttrObject


TGTemplatedAttrObject.LookupLocalAttrValue = new.instancemethod(Appc.TGTemplatedAttrObject_LookupLocalAttrValue, None, TGTemplatedAttrObject)

class TGString:
    def __init__(self,*args):
        self.this = apply(Appc.new_TGString,args)
        self.thisown = 1

    def __del__(self,Appc=Appc):
        if self.thisown == 1 :
            Appc.delete_TGString(self)
    def Append(*args):
        val = apply(Appc.TGString_Append,args)
        if val: val = TGStringPtr(val) ; val.thisown = 1
        return val
    def __repr__(self):
        return "<C TGString instance at %s>" % (self.this,)
class TGStringPtr(TGString):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = TGString


TGString.GetLength = new.instancemethod(Appc.TGString_GetLength, None, TGString)
TGString.SetString = new.instancemethod(Appc.TGString_SetString, None, TGString)
TGString.FindC = new.instancemethod(Appc.TGString_FindC, None, TGString)
TGString.Find = new.instancemethod(Appc.TGString_Find, None, TGString)
TGString.CompareC = new.instancemethod(Appc.TGString_CompareC, None, TGString)
TGString.Compare = new.instancemethod(Appc.TGString_Compare, None, TGString)

class TGSystemWrapperClass:
    IMAGE_FORMAT_TGA = Appc.TGSystemWrapperClass_IMAGE_FORMAT_TGA
    IMAGE_FORMAT_BMP = Appc.TGSystemWrapperClass_IMAGE_FORMAT_BMP
    def __init__(self,this):
        self.this = this

    def __repr__(self):
        return "<C TGSystemWrapperClass instance at %s>" % (self.this,)
class TGSystemWrapperClassPtr(TGSystemWrapperClass):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = TGSystemWrapperClass


TGSystemWrapperClass.GetTimeSinceFrameStart = new.instancemethod(Appc.TGSystemWrapperClass_GetTimeSinceFrameStart, None, TGSystemWrapperClass)
TGSystemWrapperClass.GetTimeInSeconds = new.instancemethod(Appc.TGSystemWrapperClass_GetTimeInSeconds, None, TGSystemWrapperClass)
TGSystemWrapperClass.GetTimeInMilliseconds = new.instancemethod(Appc.TGSystemWrapperClass_GetTimeInMilliseconds, None, TGSystemWrapperClass)
TGSystemWrapperClass.GetTimeElapsedInSeconds = new.instancemethod(Appc.TGSystemWrapperClass_GetTimeElapsedInSeconds, None, TGSystemWrapperClass)
TGSystemWrapperClass.GetTimeElapsedInMilliseconds = new.instancemethod(Appc.TGSystemWrapperClass_GetTimeElapsedInMilliseconds, None, TGSystemWrapperClass)
TGSystemWrapperClass.GetUpdateNumber = new.instancemethod(Appc.TGSystemWrapperClass_GetUpdateNumber, None, TGSystemWrapperClass)
TGSystemWrapperClass.GetVerticalAspectRatio = new.instancemethod(Appc.TGSystemWrapperClass_GetVerticalAspectRatio, None, TGSystemWrapperClass)
TGSystemWrapperClass.IsForeground = new.instancemethod(Appc.TGSystemWrapperClass_IsForeground, None, TGSystemWrapperClass)
TGSystemWrapperClass.GetRandomNumber = new.instancemethod(Appc.TGSystemWrapperClass_GetRandomNumber, None, TGSystemWrapperClass)
TGSystemWrapperClass.SetRandomSeed = new.instancemethod(Appc.TGSystemWrapperClass_SetRandomSeed, None, TGSystemWrapperClass)
TGSystemWrapperClass.GetIniInt = new.instancemethod(Appc.TGSystemWrapperClass_GetIniInt, None, TGSystemWrapperClass)
TGSystemWrapperClass.GetIniFloat = new.instancemethod(Appc.TGSystemWrapperClass_GetIniFloat, None, TGSystemWrapperClass)
TGSystemWrapperClass.GetIniString = new.instancemethod(Appc.TGSystemWrapperClass_GetIniString, None, TGSystemWrapperClass)
TGSystemWrapperClass.TakeScreenshot = new.instancemethod(Appc.TGSystemWrapperClass_TakeScreenshot, None, TGSystemWrapperClass)
TGSystemWrapperClass.SetDefaultScreenShotPath = new.instancemethod(Appc.TGSystemWrapperClass_SetDefaultScreenShotPath, None, TGSystemWrapperClass)

class TGProfilingInfo:
    def __init__(self,*args):
        self.this = apply(Appc.new_TGProfilingInfo,args)
        self.thisown = 1

    def __del__(self,Appc=Appc):
        if self.thisown == 1 :
            Appc.delete_TGProfilingInfo(self)
    def __repr__(self):
        return "<C TGProfilingInfo instance at %s>" % (self.this,)
class TGProfilingInfoPtr(TGProfilingInfo):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = TGProfilingInfo



class TGConfigMapping:
    def __init__(self,this):
        self.this = this

    def GetTGStringValue(*args):
        val = apply(Appc.TGConfigMapping_GetTGStringValue,args)
        if val: val = TGStringPtr(val) 
        return val
    def __repr__(self):
        return "<C TGConfigMapping instance at %s>" % (self.this,)
class TGConfigMappingPtr(TGConfigMapping):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = TGConfigMapping


TGConfigMapping.GetFloatValue = new.instancemethod(Appc.TGConfigMapping_GetFloatValue, None, TGConfigMapping)
TGConfigMapping.GetIntValue = new.instancemethod(Appc.TGConfigMapping_GetIntValue, None, TGConfigMapping)
TGConfigMapping.GetStringValue = new.instancemethod(Appc.TGConfigMapping_GetStringValue, None, TGConfigMapping)
TGConfigMapping.SetFloatValue = new.instancemethod(Appc.TGConfigMapping_SetFloatValue, None, TGConfigMapping)
TGConfigMapping.SetIntValue = new.instancemethod(Appc.TGConfigMapping_SetIntValue, None, TGConfigMapping)
TGConfigMapping.SetStringValue = new.instancemethod(Appc.TGConfigMapping_SetStringValue, None, TGConfigMapping)
TGConfigMapping.SetTGStringValue = new.instancemethod(Appc.TGConfigMapping_SetTGStringValue, None, TGConfigMapping)
TGConfigMapping.HasValue = new.instancemethod(Appc.TGConfigMapping_HasValue, None, TGConfigMapping)
TGConfigMapping.LoadConfigFile = new.instancemethod(Appc.TGConfigMapping_LoadConfigFile, None, TGConfigMapping)
TGConfigMapping.SaveConfigFile = new.instancemethod(Appc.TGConfigMapping_SaveConfigFile, None, TGConfigMapping)

class TGPoolManager:
    def __init__(self,this):
        self.this = this

    def __repr__(self):
        return "<C TGPoolManager instance at %s>" % (self.this,)
class TGPoolManagerPtr(TGPoolManager):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = TGPoolManager


TGPoolManager.Purge = new.instancemethod(Appc.TGPoolManager_Purge, None, TGPoolManager)
TGPoolManager.PrintPoolSummary = new.instancemethod(Appc.TGPoolManager_PrintPoolSummary, None, TGPoolManager)
TGPoolManager.WalkObjects = new.instancemethod(Appc.TGPoolManager_WalkObjects, None, TGPoolManager)
TGPoolManager.PrintFull = new.instancemethod(Appc.TGPoolManager_PrintFull, None, TGPoolManager)
TGPoolManager.PrintSummary = new.instancemethod(Appc.TGPoolManager_PrintSummary, None, TGPoolManager)
TGPoolManager.DumpFile = new.instancemethod(Appc.TGPoolManager_DumpFile, None, TGPoolManager)
TGPoolManager.DumpBlocks = new.instancemethod(Appc.TGPoolManager_DumpBlocks, None, TGPoolManager)
TGPoolManager.DumpObjects = new.instancemethod(Appc.TGPoolManager_DumpObjects, None, TGPoolManager)
TGPoolManager.DisplayFile = new.instancemethod(Appc.TGPoolManager_DisplayFile, None, TGPoolManager)

class PyEmbed:
    def __init__(self,this):
        self.this = this

    def __repr__(self):
        return "<C PyEmbed instance at %s>" % (self.this,)
class PyEmbedPtr(PyEmbed):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = PyEmbed



class TGModelProperty(TGObject):
    def __init__(self,*args):
        self.this = apply(Appc.new_TGModelProperty,args)
        self.thisown = 1

    def __del__(self,Appc=Appc):
        if self.thisown == 1 :
            Appc.delete_TGModelProperty(self)
    def GetName(*args):
        val = apply(Appc.TGModelProperty_GetName,args)
        if val: val = TGStringPtr(val) ; val.thisown = 1
        return val
    def Duplicate(*args):
        val = apply(Appc.TGModelProperty_Duplicate,args)
        if val: val = TGModelPropertyPtr(val) 
        return val
    def __repr__(self):
        return "<C TGModelProperty instance at %s>" % (self.this,)
class TGModelPropertyPtr(TGModelProperty):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = TGModelProperty


TGModelProperty.GetRefCount = new.instancemethod(Appc.TGModelProperty_GetRefCount, None, TGModelProperty)
TGModelProperty.DecRefCount = new.instancemethod(Appc.TGModelProperty_DecRefCount, None, TGModelProperty)
TGModelProperty.IncRefCount = new.instancemethod(Appc.TGModelProperty_IncRefCount, None, TGModelProperty)
TGModelProperty.WriteInit = new.instancemethod(Appc.TGModelProperty_WriteInit, None, TGModelProperty)
TGModelProperty.Edit = new.instancemethod(Appc.TGModelProperty_Edit, None, TGModelProperty)
TGModelProperty.SetName = new.instancemethod(Appc.TGModelProperty_SetName, None, TGModelProperty)
TGModelProperty.SetNameW = new.instancemethod(Appc.TGModelProperty_SetNameW, None, TGModelProperty)

class TGModelPropertyManager:
    GLOBAL_TEMPLATES = Appc.TGModelPropertyManager_GLOBAL_TEMPLATES
    LOCAL_TEMPLATES = Appc.TGModelPropertyManager_LOCAL_TEMPLATES
    def __init__(self,this):
        self.this = this

    def FindByNameAndType(*args):
        val = apply(Appc.TGModelPropertyManager_FindByNameAndType,args)
        if val: val = TGModelPropertyPtr(val) 
        return val
    def FindByName(*args):
        val = apply(Appc.TGModelPropertyManager_FindByName,args)
        if val: val = TGModelPropertyPtr(val) 
        return val
    def __repr__(self):
        return "<C TGModelPropertyManager instance at %s>" % (self.this,)
class TGModelPropertyManagerPtr(TGModelPropertyManager):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = TGModelPropertyManager


TGModelPropertyManager.IsLocalTemplate = new.instancemethod(Appc.TGModelPropertyManager_IsLocalTemplate, None, TGModelPropertyManager)
TGModelPropertyManager.IsGlobalTemplate = new.instancemethod(Appc.TGModelPropertyManager_IsGlobalTemplate, None, TGModelPropertyManager)
TGModelPropertyManager.RegisterLocalTemplate = new.instancemethod(Appc.TGModelPropertyManager_RegisterLocalTemplate, None, TGModelPropertyManager)
TGModelPropertyManager.RegisterGlobalTemplate = new.instancemethod(Appc.TGModelPropertyManager_RegisterGlobalTemplate, None, TGModelPropertyManager)
TGModelPropertyManager.ClearGlobalTemplates = new.instancemethod(Appc.TGModelPropertyManager_ClearGlobalTemplates, None, TGModelPropertyManager)
TGModelPropertyManager.ClearLocalTemplates = new.instancemethod(Appc.TGModelPropertyManager_ClearLocalTemplates, None, TGModelPropertyManager)
TGModelPropertyManager.ClearRegisteredFilters = new.instancemethod(Appc.TGModelPropertyManager_ClearRegisteredFilters, None, TGModelPropertyManager)
TGModelPropertyManager.RegisterFilter = new.instancemethod(Appc.TGModelPropertyManager_RegisterFilter, None, TGModelPropertyManager)
TGModelPropertyManager.AddFilter = new.instancemethod(Appc.TGModelPropertyManager_AddFilter, None, TGModelPropertyManager)
TGModelPropertyManager.ApplyFilters = new.instancemethod(Appc.TGModelPropertyManager_ApplyFilters, None, TGModelPropertyManager)
TGModelPropertyManager.ClearCurrentFilters = new.instancemethod(Appc.TGModelPropertyManager_ClearCurrentFilters, None, TGModelPropertyManager)
TGModelPropertyManager.RemoveFilter = new.instancemethod(Appc.TGModelPropertyManager_RemoveFilter, None, TGModelPropertyManager)
TGModelPropertyManager.RemoveTemplate = new.instancemethod(Appc.TGModelPropertyManager_RemoveTemplate, None, TGModelPropertyManager)

class TGModelPropertySet(TGObject):
    def __init__(self,*args):
        self.this = apply(Appc.new_TGModelPropertySet,args)
        self.thisown = 1

    def __del__(self,Appc=Appc):
        if self.thisown == 1 :
            Appc.delete_TGModelPropertySet(self)
    def GetPropertyList(*args):
        val = apply(Appc.TGModelPropertySet_GetPropertyList,args)
        if val: val = TGModelPropertyListPtr(val) 
        return val
    def GetPropertiesByType(*args):
        val = apply(Appc.TGModelPropertySet_GetPropertiesByType,args)
        if val: val = TGModelPropertyListPtr(val) 
        return val
    def __repr__(self):
        return "<C TGModelPropertySet instance at %s>" % (self.this,)
class TGModelPropertySetPtr(TGModelPropertySet):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = TGModelPropertySet


TGModelPropertySet.AddToSet = new.instancemethod(Appc.TGModelPropertySet_AddToSet, None, TGModelPropertySet)

class TGModelPropertyInstance:
    def __init__(self,*args):
        self.this = apply(Appc.new_TGModelPropertyInstance,args)
        self.thisown = 1

    def __del__(self,Appc=Appc):
        if self.thisown == 1 :
            Appc.delete_TGModelPropertyInstance(self)
    def GetProperty(*args):
        val = apply(Appc.TGModelPropertyInstance_GetProperty,args)
        if val: val = TGModelPropertyPtr(val) 
        return val
    def GetOriginalTemplate(*args):
        val = apply(Appc.TGModelPropertyInstance_GetOriginalTemplate,args)
        if val: val = TGModelPropertyPtr(val) 
        return val
    def __repr__(self):
        return "<C TGModelPropertyInstance instance at %s>" % (self.this,)
class TGModelPropertyInstancePtr(TGModelPropertyInstance):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = TGModelPropertyInstance


TGModelPropertyInstance.UseOriginalTemplate = new.instancemethod(Appc.TGModelPropertyInstance_UseOriginalTemplate, None, TGModelPropertyInstance)
TGModelPropertyInstance.GetHardpointName = new.instancemethod(Appc.TGModelPropertyInstance_GetHardpointName, None, TGModelPropertyInstance)

class TGModelPropertyList:
    def __init__(self,*args):
        self.this = apply(Appc.new_TGModelPropertyList,args)
        self.thisown = 1

    def __del__(self,Appc=Appc):
        if self.thisown == 1 :
            Appc.delete_TGModelPropertyList(self)
    def TGGetNext(*args):
        val = apply(Appc.TGModelPropertyList_TGGetNext,args)
        if val: val = TGModelPropertyInstancePtr(val) 
        return val
    def __repr__(self):
        return "<C TGModelPropertyList instance at %s>" % (self.this,)
class TGModelPropertyListPtr(TGModelPropertyList):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = TGModelPropertyList


TGModelPropertyList.TGBeginIteration = new.instancemethod(Appc.TGModelPropertyList_TGBeginIteration, None, TGModelPropertyList)
TGModelPropertyList.TGDoneIterating = new.instancemethod(Appc.TGModelPropertyList_TGDoneIterating, None, TGModelPropertyList)
TGModelPropertyList.TGDestroy = new.instancemethod(Appc.TGModelPropertyList_TGDestroy, None, TGModelPropertyList)
TGModelPropertyList.TGGetNumItems = new.instancemethod(Appc.TGModelPropertyList_TGGetNumItems, None, TGModelPropertyList)

class TGPoint3:
    def __init__(self,*args):
        self.this = apply(Appc.new_TGPoint3,args)
        self.thisown = 1

    def __del__(self,Appc=Appc):
        if self.thisown == 1 :
            Appc.delete_TGPoint3(self)
    def Cross(*args):
        val = apply(Appc.TGPoint3_Cross,args)
        if val: val = TGPoint3Ptr(val) ; val.thisown = 1
        return val
    def UnitCross(*args):
        val = apply(Appc.TGPoint3_UnitCross,args)
        if val: val = TGPoint3Ptr(val) ; val.thisown = 1
        return val
    def GetAlignedComponent(*args):
        val = apply(Appc.TGPoint3_GetAlignedComponent,args)
        if val: val = TGPoint3Ptr(val) ; val.thisown = 1
        return val
    def GetPerpendicularComponent(*args):
        val = apply(Appc.TGPoint3_GetPerpendicularComponent,args)
        if val: val = TGPoint3Ptr(val) ; val.thisown = 1
        return val
    def __repr__(self):
        return "<C TGPoint3 instance at %s>" % (self.this,)
class TGPoint3Ptr(TGPoint3):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = TGPoint3


TGPoint3.GetX = new.instancemethod(Appc.TGPoint3_GetX, None, TGPoint3)
TGPoint3.GetY = new.instancemethod(Appc.TGPoint3_GetY, None, TGPoint3)
TGPoint3.GetZ = new.instancemethod(Appc.TGPoint3_GetZ, None, TGPoint3)
TGPoint3.SetX = new.instancemethod(Appc.TGPoint3_SetX, None, TGPoint3)
TGPoint3.SetY = new.instancemethod(Appc.TGPoint3_SetY, None, TGPoint3)
TGPoint3.SetZ = new.instancemethod(Appc.TGPoint3_SetZ, None, TGPoint3)
TGPoint3.SetXYZ = new.instancemethod(Appc.TGPoint3_SetXYZ, None, TGPoint3)
TGPoint3.MultMatrix = new.instancemethod(Appc.TGPoint3_MultMatrix, None, TGPoint3)
TGPoint3.MultMatrixLeft = new.instancemethod(Appc.TGPoint3_MultMatrixLeft, None, TGPoint3)
TGPoint3.Add = new.instancemethod(Appc.TGPoint3_Add, None, TGPoint3)
TGPoint3.Subtract = new.instancemethod(Appc.TGPoint3_Subtract, None, TGPoint3)
TGPoint3.Scale = new.instancemethod(Appc.TGPoint3_Scale, None, TGPoint3)
TGPoint3.Set = new.instancemethod(Appc.TGPoint3_Set, None, TGPoint3)
TGPoint3.LoadBinary = new.instancemethod(Appc.TGPoint3_LoadBinary, None, TGPoint3)
TGPoint3.SaveBinary = new.instancemethod(Appc.TGPoint3_SaveBinary, None, TGPoint3)

class TGColorA(NiColorA):
    def __init__(self,*args):
        self.this = apply(Appc.new_TGColorA,args)
        self.thisown = 1

    def __del__(self,Appc=Appc):
        if self.thisown == 1 :
            Appc.delete_TGColorA(self)
    __setmethods__ = {
        "r" : Appc.TGColorA_r_set,
        "g" : Appc.TGColorA_g_set,
        "b" : Appc.TGColorA_b_set,
        "a" : Appc.TGColorA_a_set,
    }
    def __setattr__(self,name,value):
        if (name == "this") or (name == "thisown"): self.__dict__[name] = value; return
        method = TGColorA.__setmethods__.get(name,None)
        if method: return method(self,value)
        self.__dict__[name] = value
    __getmethods__ = {
        "r" : Appc.TGColorA_r_get,
        "g" : Appc.TGColorA_g_get,
        "b" : Appc.TGColorA_b_get,
        "a" : Appc.TGColorA_a_get,
    }
    def __getattr__(self,name):
        method = TGColorA.__getmethods__.get(name,None)
        if method: return method(self)
        raise AttributeError,name
    def __repr__(self):
        return "<C TGColorA instance at %s>" % (self.this,)
class TGColorAPtr(TGColorA):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = TGColorA


TGColorA.GetR = new.instancemethod(Appc.TGColorA_GetR, None, TGColorA)
TGColorA.GetG = new.instancemethod(Appc.TGColorA_GetG, None, TGColorA)
TGColorA.GetB = new.instancemethod(Appc.TGColorA_GetB, None, TGColorA)
TGColorA.GetA = new.instancemethod(Appc.TGColorA_GetA, None, TGColorA)
TGColorA.SetR = new.instancemethod(Appc.TGColorA_SetR, None, TGColorA)
TGColorA.SetG = new.instancemethod(Appc.TGColorA_SetG, None, TGColorA)
TGColorA.SetB = new.instancemethod(Appc.TGColorA_SetB, None, TGColorA)
TGColorA.SetA = new.instancemethod(Appc.TGColorA_SetA, None, TGColorA)
TGColorA.SetRGBA = new.instancemethod(Appc.TGColorA_SetRGBA, None, TGColorA)
TGColorA.Copy = new.instancemethod(Appc.TGColorA_Copy, None, TGColorA)
TGColorA.ScaleRGB = new.instancemethod(Appc.TGColorA_ScaleRGB, None, TGColorA)

class PositionOrientationProperty(TGModelProperty):
    def __init__(self,*args):
        self.this = apply(Appc.new_PositionOrientationProperty,args)
        self.thisown = 1

    def __del__(self,Appc=Appc):
        if self.thisown == 1 :
            Appc.delete_PositionOrientationProperty(self)
    def GetForward(*args):
        val = apply(Appc.PositionOrientationProperty_GetForward,args)
        if val: val = TGPoint3Ptr(val) ; val.thisown = 1
        return val
    def GetUp(*args):
        val = apply(Appc.PositionOrientationProperty_GetUp,args)
        if val: val = TGPoint3Ptr(val) ; val.thisown = 1
        return val
    def GetRight(*args):
        val = apply(Appc.PositionOrientationProperty_GetRight,args)
        if val: val = TGPoint3Ptr(val) ; val.thisown = 1
        return val
    def GetPosition(*args):
        val = apply(Appc.PositionOrientationProperty_GetPosition,args)
        if val: val = TGPoint3Ptr(val) ; val.thisown = 1
        return val
    def __repr__(self):
        return "<C PositionOrientationProperty instance at %s>" % (self.this,)
class PositionOrientationPropertyPtr(PositionOrientationProperty):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = PositionOrientationProperty


PositionOrientationProperty.SetOrientation = new.instancemethod(Appc.PositionOrientationProperty_SetOrientation, None, PositionOrientationProperty)
PositionOrientationProperty.SetPosition = new.instancemethod(Appc.PositionOrientationProperty_SetPosition, None, PositionOrientationProperty)

class SubsystemProperty(TGModelProperty):
    def __init__(self,*args):
        self.this = apply(Appc.new_SubsystemProperty,args)
        self.thisown = 1

    def __del__(self,Appc=Appc):
        if self.thisown == 1 :
            Appc.delete_SubsystemProperty(self)
    def GetPositionTG(*args):
        val = apply(Appc.SubsystemProperty_GetPositionTG,args)
        if val: val = TGPoint3Ptr(val) ; val.thisown = 1
        return val
    def __repr__(self):
        return "<C SubsystemProperty instance at %s>" % (self.this,)
class SubsystemPropertyPtr(SubsystemProperty):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = SubsystemProperty


SubsystemProperty.GetMaxCondition = new.instancemethod(Appc.SubsystemProperty_GetMaxCondition, None, SubsystemProperty)
SubsystemProperty.IsCritical = new.instancemethod(Appc.SubsystemProperty_IsCritical, None, SubsystemProperty)
SubsystemProperty.IsTargetable = new.instancemethod(Appc.SubsystemProperty_IsTargetable, None, SubsystemProperty)
SubsystemProperty.IsPrimary = new.instancemethod(Appc.SubsystemProperty_IsPrimary, None, SubsystemProperty)
SubsystemProperty.GetRepairComplexity = new.instancemethod(Appc.SubsystemProperty_GetRepairComplexity, None, SubsystemProperty)
SubsystemProperty.GetDisabledPercentage = new.instancemethod(Appc.SubsystemProperty_GetDisabledPercentage, None, SubsystemProperty)
SubsystemProperty.GetRadius = new.instancemethod(Appc.SubsystemProperty_GetRadius, None, SubsystemProperty)
SubsystemProperty.SetMaxCondition = new.instancemethod(Appc.SubsystemProperty_SetMaxCondition, None, SubsystemProperty)
SubsystemProperty.SetCritical = new.instancemethod(Appc.SubsystemProperty_SetCritical, None, SubsystemProperty)
SubsystemProperty.SetTargetable = new.instancemethod(Appc.SubsystemProperty_SetTargetable, None, SubsystemProperty)
SubsystemProperty.SetPrimary = new.instancemethod(Appc.SubsystemProperty_SetPrimary, None, SubsystemProperty)
SubsystemProperty.SetRepairComplexity = new.instancemethod(Appc.SubsystemProperty_SetRepairComplexity, None, SubsystemProperty)
SubsystemProperty.SetDisabledPercentage = new.instancemethod(Appc.SubsystemProperty_SetDisabledPercentage, None, SubsystemProperty)
SubsystemProperty.SetRadius = new.instancemethod(Appc.SubsystemProperty_SetRadius, None, SubsystemProperty)
SubsystemProperty.GetPosition = new.instancemethod(Appc.SubsystemProperty_GetPosition, None, SubsystemProperty)
SubsystemProperty.GetPosition2D = new.instancemethod(Appc.SubsystemProperty_GetPosition2D, None, SubsystemProperty)
SubsystemProperty.SetPosition = new.instancemethod(Appc.SubsystemProperty_SetPosition, None, SubsystemProperty)
SubsystemProperty.SetPosition2D = new.instancemethod(Appc.SubsystemProperty_SetPosition2D, None, SubsystemProperty)

class PoweredSubsystemProperty(SubsystemProperty):
    def __init__(self,*args):
        self.this = apply(Appc.new_PoweredSubsystemProperty,args)
        self.thisown = 1

    def __del__(self,Appc=Appc):
        if self.thisown == 1 :
            Appc.delete_PoweredSubsystemProperty(self)
    def __repr__(self):
        return "<C PoweredSubsystemProperty instance at %s>" % (self.this,)
class PoweredSubsystemPropertyPtr(PoweredSubsystemProperty):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = PoweredSubsystemProperty


PoweredSubsystemProperty.GetNormalPowerPerSecond = new.instancemethod(Appc.PoweredSubsystemProperty_GetNormalPowerPerSecond, None, PoweredSubsystemProperty)
PoweredSubsystemProperty.SetNormalPowerPerSecond = new.instancemethod(Appc.PoweredSubsystemProperty_SetNormalPowerPerSecond, None, PoweredSubsystemProperty)

class ShipProperty(TGModelProperty):
    def __init__(self,*args):
        self.this = apply(Appc.new_ShipProperty,args)
        self.thisown = 1

    def __del__(self,Appc=Appc):
        if self.thisown == 1 :
            Appc.delete_ShipProperty(self)
    def __repr__(self):
        return "<C ShipProperty instance at %s>" % (self.this,)
class ShipPropertyPtr(ShipProperty):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = ShipProperty


ShipProperty.GetGenus = new.instancemethod(Appc.ShipProperty_GetGenus, None, ShipProperty)
ShipProperty.GetSpecies = new.instancemethod(Appc.ShipProperty_GetSpecies, None, ShipProperty)
ShipProperty.GetMass = new.instancemethod(Appc.ShipProperty_GetMass, None, ShipProperty)
ShipProperty.GetRotationalInertia = new.instancemethod(Appc.ShipProperty_GetRotationalInertia, None, ShipProperty)
ShipProperty.GetShipName = new.instancemethod(Appc.ShipProperty_GetShipName, None, ShipProperty)
ShipProperty.GetModelFilename = new.instancemethod(Appc.ShipProperty_GetModelFilename, None, ShipProperty)
ShipProperty.GetDamageResolution = new.instancemethod(Appc.ShipProperty_GetDamageResolution, None, ShipProperty)
ShipProperty.GetAffiliation = new.instancemethod(Appc.ShipProperty_GetAffiliation, None, ShipProperty)
ShipProperty.IsStationary = new.instancemethod(Appc.ShipProperty_IsStationary, None, ShipProperty)
ShipProperty.GetAIString = new.instancemethod(Appc.ShipProperty_GetAIString, None, ShipProperty)
ShipProperty.GetDeathExplosionSound = new.instancemethod(Appc.ShipProperty_GetDeathExplosionSound, None, ShipProperty)
ShipProperty.SetGenus = new.instancemethod(Appc.ShipProperty_SetGenus, None, ShipProperty)
ShipProperty.SetSpecies = new.instancemethod(Appc.ShipProperty_SetSpecies, None, ShipProperty)
ShipProperty.SetMass = new.instancemethod(Appc.ShipProperty_SetMass, None, ShipProperty)
ShipProperty.SetRotationalInertia = new.instancemethod(Appc.ShipProperty_SetRotationalInertia, None, ShipProperty)
ShipProperty.SetShipName = new.instancemethod(Appc.ShipProperty_SetShipName, None, ShipProperty)
ShipProperty.SetModelFilename = new.instancemethod(Appc.ShipProperty_SetModelFilename, None, ShipProperty)
ShipProperty.SetDamageResolution = new.instancemethod(Appc.ShipProperty_SetDamageResolution, None, ShipProperty)
ShipProperty.SetAffiliation = new.instancemethod(Appc.ShipProperty_SetAffiliation, None, ShipProperty)
ShipProperty.SetStationary = new.instancemethod(Appc.ShipProperty_SetStationary, None, ShipProperty)
ShipProperty.SetAIString = new.instancemethod(Appc.ShipProperty_SetAIString, None, ShipProperty)
ShipProperty.SetDeathExplosionSound = new.instancemethod(Appc.ShipProperty_SetDeathExplosionSound, None, ShipProperty)

class WeaponSystemProperty(PoweredSubsystemProperty):
    WST_UNKNOWN = Appc.WeaponSystemProperty_WST_UNKNOWN
    WST_PHASER = Appc.WeaponSystemProperty_WST_PHASER
    WST_TORPEDO = Appc.WeaponSystemProperty_WST_TORPEDO
    WST_PULSE = Appc.WeaponSystemProperty_WST_PULSE
    WST_TRACTOR = Appc.WeaponSystemProperty_WST_TRACTOR
    def __init__(self,*args):
        self.this = apply(Appc.new_WeaponSystemProperty,args)
        self.thisown = 1

    def __del__(self,Appc=Appc):
        if self.thisown == 1 :
            Appc.delete_WeaponSystemProperty(self)
    def GetFiringChainString(*args):
        val = apply(Appc.WeaponSystemProperty_GetFiringChainString,args)
        if val: val = TGStringPtr(val) ; val.thisown = 1
        return val
    def __repr__(self):
        return "<C WeaponSystemProperty instance at %s>" % (self.this,)
class WeaponSystemPropertyPtr(WeaponSystemProperty):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = WeaponSystemProperty


WeaponSystemProperty.GetWeaponSystemType = new.instancemethod(Appc.WeaponSystemProperty_GetWeaponSystemType, None, WeaponSystemProperty)
WeaponSystemProperty.SetWeaponSystemType = new.instancemethod(Appc.WeaponSystemProperty_SetWeaponSystemType, None, WeaponSystemProperty)
WeaponSystemProperty.IsSingleFire = new.instancemethod(Appc.WeaponSystemProperty_IsSingleFire, None, WeaponSystemProperty)
WeaponSystemProperty.SetSingleFire = new.instancemethod(Appc.WeaponSystemProperty_SetSingleFire, None, WeaponSystemProperty)
WeaponSystemProperty.IsAimedWeapon = new.instancemethod(Appc.WeaponSystemProperty_IsAimedWeapon, None, WeaponSystemProperty)
WeaponSystemProperty.SetAimedWeapon = new.instancemethod(Appc.WeaponSystemProperty_SetAimedWeapon, None, WeaponSystemProperty)
WeaponSystemProperty.SetFiringChainString = new.instancemethod(Appc.WeaponSystemProperty_SetFiringChainString, None, WeaponSystemProperty)

class WeaponProperty(SubsystemProperty):
    def __init__(self,*args):
        self.this = apply(Appc.new_WeaponProperty,args)
        self.thisown = 1

    def __del__(self,Appc=Appc):
        if self.thisown == 1 :
            Appc.delete_WeaponProperty(self)
    def __repr__(self):
        return "<C WeaponProperty instance at %s>" % (self.this,)
class WeaponPropertyPtr(WeaponProperty):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = WeaponProperty


WeaponProperty.IsDumbfire = new.instancemethod(Appc.WeaponProperty_IsDumbfire, None, WeaponProperty)
WeaponProperty.SetDumbfire = new.instancemethod(Appc.WeaponProperty_SetDumbfire, None, WeaponProperty)
WeaponProperty.GetWeaponID = new.instancemethod(Appc.WeaponProperty_GetWeaponID, None, WeaponProperty)
WeaponProperty.SetWeaponID = new.instancemethod(Appc.WeaponProperty_SetWeaponID, None, WeaponProperty)
WeaponProperty.IsMemberOfGroup = new.instancemethod(Appc.WeaponProperty_IsMemberOfGroup, None, WeaponProperty)
WeaponProperty.GetGroups = new.instancemethod(Appc.WeaponProperty_GetGroups, None, WeaponProperty)
WeaponProperty.SetGroups = new.instancemethod(Appc.WeaponProperty_SetGroups, None, WeaponProperty)
WeaponProperty.GetDamageRadiusFactor = new.instancemethod(Appc.WeaponProperty_GetDamageRadiusFactor, None, WeaponProperty)
WeaponProperty.SetDamageRadiusFactor = new.instancemethod(Appc.WeaponProperty_SetDamageRadiusFactor, None, WeaponProperty)
WeaponProperty.GetIconNum = new.instancemethod(Appc.WeaponProperty_GetIconNum, None, WeaponProperty)
WeaponProperty.SetIconNum = new.instancemethod(Appc.WeaponProperty_SetIconNum, None, WeaponProperty)
WeaponProperty.GetIconPositionX = new.instancemethod(Appc.WeaponProperty_GetIconPositionX, None, WeaponProperty)
WeaponProperty.SetIconPositionX = new.instancemethod(Appc.WeaponProperty_SetIconPositionX, None, WeaponProperty)
WeaponProperty.GetIconPositionY = new.instancemethod(Appc.WeaponProperty_GetIconPositionY, None, WeaponProperty)
WeaponProperty.SetIconPositionY = new.instancemethod(Appc.WeaponProperty_SetIconPositionY, None, WeaponProperty)
WeaponProperty.IsIconAboveShip = new.instancemethod(Appc.WeaponProperty_IsIconAboveShip, None, WeaponProperty)
WeaponProperty.SetIconAboveShip = new.instancemethod(Appc.WeaponProperty_SetIconAboveShip, None, WeaponProperty)

class EnergyWeaponProperty(WeaponProperty):
    def __init__(self,*args):
        self.this = apply(Appc.new_EnergyWeaponProperty,args)
        self.thisown = 1

    def __del__(self,Appc=Appc):
        if self.thisown == 1 :
            Appc.delete_EnergyWeaponProperty(self)
    def __repr__(self):
        return "<C EnergyWeaponProperty instance at %s>" % (self.this,)
class EnergyWeaponPropertyPtr(EnergyWeaponProperty):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = EnergyWeaponProperty


EnergyWeaponProperty.GetRechargeRate = new.instancemethod(Appc.EnergyWeaponProperty_GetRechargeRate, None, EnergyWeaponProperty)
EnergyWeaponProperty.GetNormalDischargeRate = new.instancemethod(Appc.EnergyWeaponProperty_GetNormalDischargeRate, None, EnergyWeaponProperty)
EnergyWeaponProperty.GetMaxCharge = new.instancemethod(Appc.EnergyWeaponProperty_GetMaxCharge, None, EnergyWeaponProperty)
EnergyWeaponProperty.GetMinFiringCharge = new.instancemethod(Appc.EnergyWeaponProperty_GetMinFiringCharge, None, EnergyWeaponProperty)
EnergyWeaponProperty.GetFireSound = new.instancemethod(Appc.EnergyWeaponProperty_GetFireSound, None, EnergyWeaponProperty)
EnergyWeaponProperty.GetMaxDamage = new.instancemethod(Appc.EnergyWeaponProperty_GetMaxDamage, None, EnergyWeaponProperty)
EnergyWeaponProperty.GetMaxDamageDistance = new.instancemethod(Appc.EnergyWeaponProperty_GetMaxDamageDistance, None, EnergyWeaponProperty)
EnergyWeaponProperty.GetIndicatorIconNum = new.instancemethod(Appc.EnergyWeaponProperty_GetIndicatorIconNum, None, EnergyWeaponProperty)
EnergyWeaponProperty.GetIndicatorIconPositionX = new.instancemethod(Appc.EnergyWeaponProperty_GetIndicatorIconPositionX, None, EnergyWeaponProperty)
EnergyWeaponProperty.GetIndicatorIconPositionY = new.instancemethod(Appc.EnergyWeaponProperty_GetIndicatorIconPositionY, None, EnergyWeaponProperty)
EnergyWeaponProperty.SetFireSound = new.instancemethod(Appc.EnergyWeaponProperty_SetFireSound, None, EnergyWeaponProperty)
EnergyWeaponProperty.SetMaxDamage = new.instancemethod(Appc.EnergyWeaponProperty_SetMaxDamage, None, EnergyWeaponProperty)
EnergyWeaponProperty.SetMaxDamageDistance = new.instancemethod(Appc.EnergyWeaponProperty_SetMaxDamageDistance, None, EnergyWeaponProperty)
EnergyWeaponProperty.SetMinFiringCharge = new.instancemethod(Appc.EnergyWeaponProperty_SetMinFiringCharge, None, EnergyWeaponProperty)
EnergyWeaponProperty.SetMaxCharge = new.instancemethod(Appc.EnergyWeaponProperty_SetMaxCharge, None, EnergyWeaponProperty)
EnergyWeaponProperty.SetNormalDischargeRate = new.instancemethod(Appc.EnergyWeaponProperty_SetNormalDischargeRate, None, EnergyWeaponProperty)
EnergyWeaponProperty.SetRechargeRate = new.instancemethod(Appc.EnergyWeaponProperty_SetRechargeRate, None, EnergyWeaponProperty)
EnergyWeaponProperty.SetIndicatorIconNum = new.instancemethod(Appc.EnergyWeaponProperty_SetIndicatorIconNum, None, EnergyWeaponProperty)
EnergyWeaponProperty.SetIndicatorIconPositionX = new.instancemethod(Appc.EnergyWeaponProperty_SetIndicatorIconPositionX, None, EnergyWeaponProperty)
EnergyWeaponProperty.SetIndicatorIconPositionY = new.instancemethod(Appc.EnergyWeaponProperty_SetIndicatorIconPositionY, None, EnergyWeaponProperty)

class PhaserProperty(EnergyWeaponProperty):
    def __init__(self,*args):
        self.this = apply(Appc.new_PhaserProperty,args)
        self.thisown = 1

    def __del__(self,Appc=Appc):
        if self.thisown == 1 :
            Appc.delete_PhaserProperty(self)
    def GetOrientationForward(*args):
        val = apply(Appc.PhaserProperty_GetOrientationForward,args)
        if val: val = TGPoint3Ptr(val) ; val.thisown = 1
        return val
    def GetOrientationUp(*args):
        val = apply(Appc.PhaserProperty_GetOrientationUp,args)
        if val: val = TGPoint3Ptr(val) ; val.thisown = 1
        return val
    def GetOuterShellColor(*args):
        val = apply(Appc.PhaserProperty_GetOuterShellColor,args)
        if val: val = NiColorAPtr(val) ; val.thisown = 1
        return val
    def GetInnerShellColor(*args):
        val = apply(Appc.PhaserProperty_GetInnerShellColor,args)
        if val: val = NiColorAPtr(val) ; val.thisown = 1
        return val
    def GetOuterCoreColor(*args):
        val = apply(Appc.PhaserProperty_GetOuterCoreColor,args)
        if val: val = NiColorAPtr(val) ; val.thisown = 1
        return val
    def GetInnerCoreColor(*args):
        val = apply(Appc.PhaserProperty_GetInnerCoreColor,args)
        if val: val = NiColorAPtr(val) ; val.thisown = 1
        return val
    def __repr__(self):
        return "<C PhaserProperty instance at %s>" % (self.this,)
class PhaserPropertyPtr(PhaserProperty):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = PhaserProperty


PhaserProperty.SetOrientation = new.instancemethod(Appc.PhaserProperty_SetOrientation, None, PhaserProperty)
PhaserProperty.SetWidth = new.instancemethod(Appc.PhaserProperty_SetWidth, None, PhaserProperty)
PhaserProperty.SetLength = new.instancemethod(Appc.PhaserProperty_SetLength, None, PhaserProperty)
PhaserProperty.SetPhaserTextureStart = new.instancemethod(Appc.PhaserProperty_SetPhaserTextureStart, None, PhaserProperty)
PhaserProperty.SetPhaserTextureEnd = new.instancemethod(Appc.PhaserProperty_SetPhaserTextureEnd, None, PhaserProperty)
PhaserProperty.SetPhaserWidth = new.instancemethod(Appc.PhaserProperty_SetPhaserWidth, None, PhaserProperty)
PhaserProperty.SetArcWidthAngles = new.instancemethod(Appc.PhaserProperty_SetArcWidthAngles, None, PhaserProperty)
PhaserProperty.SetArcHeightAngles = new.instancemethod(Appc.PhaserProperty_SetArcHeightAngles, None, PhaserProperty)
PhaserProperty.SetOuterShellColor = new.instancemethod(Appc.PhaserProperty_SetOuterShellColor, None, PhaserProperty)
PhaserProperty.SetInnerShellColor = new.instancemethod(Appc.PhaserProperty_SetInnerShellColor, None, PhaserProperty)
PhaserProperty.SetOuterCoreColor = new.instancemethod(Appc.PhaserProperty_SetOuterCoreColor, None, PhaserProperty)
PhaserProperty.SetInnerCoreColor = new.instancemethod(Appc.PhaserProperty_SetInnerCoreColor, None, PhaserProperty)
PhaserProperty.SetNumSides = new.instancemethod(Appc.PhaserProperty_SetNumSides, None, PhaserProperty)
PhaserProperty.SetMainRadius = new.instancemethod(Appc.PhaserProperty_SetMainRadius, None, PhaserProperty)
PhaserProperty.SetTaperRadius = new.instancemethod(Appc.PhaserProperty_SetTaperRadius, None, PhaserProperty)
PhaserProperty.SetCoreScale = new.instancemethod(Appc.PhaserProperty_SetCoreScale, None, PhaserProperty)
PhaserProperty.SetTaperRatio = new.instancemethod(Appc.PhaserProperty_SetTaperRatio, None, PhaserProperty)
PhaserProperty.SetTaperMinLength = new.instancemethod(Appc.PhaserProperty_SetTaperMinLength, None, PhaserProperty)
PhaserProperty.SetTaperMaxLength = new.instancemethod(Appc.PhaserProperty_SetTaperMaxLength, None, PhaserProperty)
PhaserProperty.SetLengthTextureTilePerUnit = new.instancemethod(Appc.PhaserProperty_SetLengthTextureTilePerUnit, None, PhaserProperty)
PhaserProperty.SetPerimeterTile = new.instancemethod(Appc.PhaserProperty_SetPerimeterTile, None, PhaserProperty)
PhaserProperty.SetTextureSpeed = new.instancemethod(Appc.PhaserProperty_SetTextureSpeed, None, PhaserProperty)
PhaserProperty.SetTextureName = new.instancemethod(Appc.PhaserProperty_SetTextureName, None, PhaserProperty)
PhaserProperty.GetWidth = new.instancemethod(Appc.PhaserProperty_GetWidth, None, PhaserProperty)
PhaserProperty.GetLength = new.instancemethod(Appc.PhaserProperty_GetLength, None, PhaserProperty)
PhaserProperty.GetPhaserTextureStart = new.instancemethod(Appc.PhaserProperty_GetPhaserTextureStart, None, PhaserProperty)
PhaserProperty.GetPhaserTextureEnd = new.instancemethod(Appc.PhaserProperty_GetPhaserTextureEnd, None, PhaserProperty)
PhaserProperty.GetPhaserWidth = new.instancemethod(Appc.PhaserProperty_GetPhaserWidth, None, PhaserProperty)
PhaserProperty.GetArcWidthAngles = new.instancemethod(Appc.PhaserProperty_GetArcWidthAngles, None, PhaserProperty)
PhaserProperty.GetArcHeightAngles = new.instancemethod(Appc.PhaserProperty_GetArcHeightAngles, None, PhaserProperty)
PhaserProperty.GetArcWidthAngleMin = new.instancemethod(Appc.PhaserProperty_GetArcWidthAngleMin, None, PhaserProperty)
PhaserProperty.GetArcWidthAngleMax = new.instancemethod(Appc.PhaserProperty_GetArcWidthAngleMax, None, PhaserProperty)
PhaserProperty.GetArcHeightAngleMin = new.instancemethod(Appc.PhaserProperty_GetArcHeightAngleMin, None, PhaserProperty)
PhaserProperty.GetArcHeightAngleMax = new.instancemethod(Appc.PhaserProperty_GetArcHeightAngleMax, None, PhaserProperty)
PhaserProperty.GetNumSides = new.instancemethod(Appc.PhaserProperty_GetNumSides, None, PhaserProperty)
PhaserProperty.GetMainRadius = new.instancemethod(Appc.PhaserProperty_GetMainRadius, None, PhaserProperty)
PhaserProperty.GetTaperRadius = new.instancemethod(Appc.PhaserProperty_GetTaperRadius, None, PhaserProperty)
PhaserProperty.GetCoreScale = new.instancemethod(Appc.PhaserProperty_GetCoreScale, None, PhaserProperty)
PhaserProperty.GetTaperRatio = new.instancemethod(Appc.PhaserProperty_GetTaperRatio, None, PhaserProperty)
PhaserProperty.GetTaperMinLength = new.instancemethod(Appc.PhaserProperty_GetTaperMinLength, None, PhaserProperty)
PhaserProperty.GetTaperMaxLength = new.instancemethod(Appc.PhaserProperty_GetTaperMaxLength, None, PhaserProperty)
PhaserProperty.GetLengthTextureTilePerUnit = new.instancemethod(Appc.PhaserProperty_GetLengthTextureTilePerUnit, None, PhaserProperty)
PhaserProperty.GetPerimeterTile = new.instancemethod(Appc.PhaserProperty_GetPerimeterTile, None, PhaserProperty)
PhaserProperty.GetTextureSpeed = new.instancemethod(Appc.PhaserProperty_GetTextureSpeed, None, PhaserProperty)
PhaserProperty.GetTextureName = new.instancemethod(Appc.PhaserProperty_GetTextureName, None, PhaserProperty)

class EngineGlowProperty(TGModelProperty):
    def __init__(self,this):
        self.this = this

    def __del__(self,Appc=Appc):
        if self.thisown == 1 :
            Appc.delete_TGModelProperty(self)
    def __repr__(self):
        return "<C EngineGlowProperty instance at %s>" % (self.this,)
class EngineGlowPropertyPtr(EngineGlowProperty):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = EngineGlowProperty



class TorpedoTubeProperty(WeaponProperty):
    def __init__(self,*args):
        self.this = apply(Appc.new_TorpedoTubeProperty,args)
        self.thisown = 1

    def __del__(self,Appc=Appc):
        if self.thisown == 1 :
            Appc.delete_TorpedoTubeProperty(self)
    def GetDirection(*args):
        val = apply(Appc.TorpedoTubeProperty_GetDirection,args)
        if val: val = TGPoint3Ptr(val) ; val.thisown = 1
        return val
    def GetRight(*args):
        val = apply(Appc.TorpedoTubeProperty_GetRight,args)
        if val: val = TGPoint3Ptr(val) ; val.thisown = 1
        return val
    def __repr__(self):
        return "<C TorpedoTubeProperty instance at %s>" % (self.this,)
class TorpedoTubePropertyPtr(TorpedoTubeProperty):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = TorpedoTubeProperty


TorpedoTubeProperty.GetImmediateDelay = new.instancemethod(Appc.TorpedoTubeProperty_GetImmediateDelay, None, TorpedoTubeProperty)
TorpedoTubeProperty.GetReloadDelay = new.instancemethod(Appc.TorpedoTubeProperty_GetReloadDelay, None, TorpedoTubeProperty)
TorpedoTubeProperty.GetMaxReady = new.instancemethod(Appc.TorpedoTubeProperty_GetMaxReady, None, TorpedoTubeProperty)
TorpedoTubeProperty.SetDirection = new.instancemethod(Appc.TorpedoTubeProperty_SetDirection, None, TorpedoTubeProperty)
TorpedoTubeProperty.SetRight = new.instancemethod(Appc.TorpedoTubeProperty_SetRight, None, TorpedoTubeProperty)
TorpedoTubeProperty.SetImmediateDelay = new.instancemethod(Appc.TorpedoTubeProperty_SetImmediateDelay, None, TorpedoTubeProperty)
TorpedoTubeProperty.SetReloadDelay = new.instancemethod(Appc.TorpedoTubeProperty_SetReloadDelay, None, TorpedoTubeProperty)
TorpedoTubeProperty.SetMaxReady = new.instancemethod(Appc.TorpedoTubeProperty_SetMaxReady, None, TorpedoTubeProperty)

class ShieldProperty(PoweredSubsystemProperty):
    FRONT_SHIELDS = Appc.ShieldProperty_FRONT_SHIELDS
    REAR_SHIELDS = Appc.ShieldProperty_REAR_SHIELDS
    TOP_SHIELDS = Appc.ShieldProperty_TOP_SHIELDS
    BOTTOM_SHIELDS = Appc.ShieldProperty_BOTTOM_SHIELDS
    LEFT_SHIELDS = Appc.ShieldProperty_LEFT_SHIELDS
    RIGHT_SHIELDS = Appc.ShieldProperty_RIGHT_SHIELDS
    NUM_SHIELDS = Appc.ShieldProperty_NUM_SHIELDS
    def __init__(self,*args):
        self.this = apply(Appc.new_ShieldProperty,args)
        self.thisown = 1

    def __del__(self,Appc=Appc):
        if self.thisown == 1 :
            Appc.delete_ShieldProperty(self)
    def GetShieldGlowColor(*args):
        val = apply(Appc.ShieldProperty_GetShieldGlowColor,args)
        if val: val = TGColorAPtr(val) ; val.thisown = 1
        return val
    def __repr__(self):
        return "<C ShieldProperty instance at %s>" % (self.this,)
class ShieldPropertyPtr(ShieldProperty):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = ShieldProperty


ShieldProperty.GetShieldGlowDecay = new.instancemethod(Appc.ShieldProperty_GetShieldGlowDecay, None, ShieldProperty)
ShieldProperty.GetMaxShields = new.instancemethod(Appc.ShieldProperty_GetMaxShields, None, ShieldProperty)
ShieldProperty.GetShieldChargePerSecond = new.instancemethod(Appc.ShieldProperty_GetShieldChargePerSecond, None, ShieldProperty)
ShieldProperty.SetShieldGlowColor = new.instancemethod(Appc.ShieldProperty_SetShieldGlowColor, None, ShieldProperty)
ShieldProperty.SetShieldGlowDecay = new.instancemethod(Appc.ShieldProperty_SetShieldGlowDecay, None, ShieldProperty)
ShieldProperty.SetMaxShields = new.instancemethod(Appc.ShieldProperty_SetMaxShields, None, ShieldProperty)
ShieldProperty.SetShieldChargePerSecond = new.instancemethod(Appc.ShieldProperty_SetShieldChargePerSecond, None, ShieldProperty)

class HullProperty(SubsystemProperty):
    def __init__(self,*args):
        self.this = apply(Appc.new_HullProperty,args)
        self.thisown = 1

    def __del__(self,Appc=Appc):
        if self.thisown == 1 :
            Appc.delete_HullProperty(self)
    def __repr__(self):
        return "<C HullProperty instance at %s>" % (self.this,)
class HullPropertyPtr(HullProperty):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = HullProperty



class SensorProperty(PoweredSubsystemProperty):
    def __init__(self,*args):
        self.this = apply(Appc.new_SensorProperty,args)
        self.thisown = 1

    def __del__(self,Appc=Appc):
        if self.thisown == 1 :
            Appc.delete_SensorProperty(self)
    def __repr__(self):
        return "<C SensorProperty instance at %s>" % (self.this,)
class SensorPropertyPtr(SensorProperty):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = SensorProperty


SensorProperty.GetBaseSensorRange = new.instancemethod(Appc.SensorProperty_GetBaseSensorRange, None, SensorProperty)
SensorProperty.SetBaseSensorRange = new.instancemethod(Appc.SensorProperty_SetBaseSensorRange, None, SensorProperty)
SensorProperty.GetMaxProbes = new.instancemethod(Appc.SensorProperty_GetMaxProbes, None, SensorProperty)
SensorProperty.SetMaxProbes = new.instancemethod(Appc.SensorProperty_SetMaxProbes, None, SensorProperty)

class PulseWeaponProperty(EnergyWeaponProperty):
    def __init__(self,*args):
        self.this = apply(Appc.new_PulseWeaponProperty,args)
        self.thisown = 1

    def __del__(self,Appc=Appc):
        if self.thisown == 1 :
            Appc.delete_PulseWeaponProperty(self)
    def GetOrientationForward(*args):
        val = apply(Appc.PulseWeaponProperty_GetOrientationForward,args)
        if val: val = TGPoint3Ptr(val) ; val.thisown = 1
        return val
    def GetOrientationUp(*args):
        val = apply(Appc.PulseWeaponProperty_GetOrientationUp,args)
        if val: val = TGPoint3Ptr(val) ; val.thisown = 1
        return val
    def GetOrientationRight(*args):
        val = apply(Appc.PulseWeaponProperty_GetOrientationRight,args)
        if val: val = TGPoint3Ptr(val) ; val.thisown = 1
        return val
    def __repr__(self):
        return "<C PulseWeaponProperty instance at %s>" % (self.this,)
class PulseWeaponPropertyPtr(PulseWeaponProperty):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = PulseWeaponProperty


PulseWeaponProperty.SetOrientation = new.instancemethod(Appc.PulseWeaponProperty_SetOrientation, None, PulseWeaponProperty)
PulseWeaponProperty.SetArcWidthAngles = new.instancemethod(Appc.PulseWeaponProperty_SetArcWidthAngles, None, PulseWeaponProperty)
PulseWeaponProperty.SetArcHeightAngles = new.instancemethod(Appc.PulseWeaponProperty_SetArcHeightAngles, None, PulseWeaponProperty)
PulseWeaponProperty.SetCooldownTime = new.instancemethod(Appc.PulseWeaponProperty_SetCooldownTime, None, PulseWeaponProperty)
PulseWeaponProperty.SetModuleName = new.instancemethod(Appc.PulseWeaponProperty_SetModuleName, None, PulseWeaponProperty)
PulseWeaponProperty.GetArcWidthAngles = new.instancemethod(Appc.PulseWeaponProperty_GetArcWidthAngles, None, PulseWeaponProperty)
PulseWeaponProperty.GetArcHeightAngles = new.instancemethod(Appc.PulseWeaponProperty_GetArcHeightAngles, None, PulseWeaponProperty)
PulseWeaponProperty.GetArcWidthAngleMin = new.instancemethod(Appc.PulseWeaponProperty_GetArcWidthAngleMin, None, PulseWeaponProperty)
PulseWeaponProperty.GetArcWidthAngleMax = new.instancemethod(Appc.PulseWeaponProperty_GetArcWidthAngleMax, None, PulseWeaponProperty)
PulseWeaponProperty.GetArcHeightAngleMin = new.instancemethod(Appc.PulseWeaponProperty_GetArcHeightAngleMin, None, PulseWeaponProperty)
PulseWeaponProperty.GetArcHeightAngleMax = new.instancemethod(Appc.PulseWeaponProperty_GetArcHeightAngleMax, None, PulseWeaponProperty)
PulseWeaponProperty.GetCooldownTime = new.instancemethod(Appc.PulseWeaponProperty_GetCooldownTime, None, PulseWeaponProperty)
PulseWeaponProperty.GetModuleName = new.instancemethod(Appc.PulseWeaponProperty_GetModuleName, None, PulseWeaponProperty)

class ImpulseEngineProperty(PoweredSubsystemProperty):
    def __init__(self,*args):
        self.this = apply(Appc.new_ImpulseEngineProperty,args)
        self.thisown = 1

    def __del__(self,Appc=Appc):
        if self.thisown == 1 :
            Appc.delete_ImpulseEngineProperty(self)
    def __repr__(self):
        return "<C ImpulseEngineProperty instance at %s>" % (self.this,)
class ImpulseEnginePropertyPtr(ImpulseEngineProperty):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = ImpulseEngineProperty


ImpulseEngineProperty.GetMaxSpeed = new.instancemethod(Appc.ImpulseEngineProperty_GetMaxSpeed, None, ImpulseEngineProperty)
ImpulseEngineProperty.GetMaxAccel = new.instancemethod(Appc.ImpulseEngineProperty_GetMaxAccel, None, ImpulseEngineProperty)
ImpulseEngineProperty.GetMaxAngularVelocity = new.instancemethod(Appc.ImpulseEngineProperty_GetMaxAngularVelocity, None, ImpulseEngineProperty)
ImpulseEngineProperty.GetMaxAngularAccel = new.instancemethod(Appc.ImpulseEngineProperty_GetMaxAngularAccel, None, ImpulseEngineProperty)
ImpulseEngineProperty.GetEngineSound = new.instancemethod(Appc.ImpulseEngineProperty_GetEngineSound, None, ImpulseEngineProperty)
ImpulseEngineProperty.SetMaxSpeed = new.instancemethod(Appc.ImpulseEngineProperty_SetMaxSpeed, None, ImpulseEngineProperty)
ImpulseEngineProperty.SetMaxAccel = new.instancemethod(Appc.ImpulseEngineProperty_SetMaxAccel, None, ImpulseEngineProperty)
ImpulseEngineProperty.SetMaxAngularVelocity = new.instancemethod(Appc.ImpulseEngineProperty_SetMaxAngularVelocity, None, ImpulseEngineProperty)
ImpulseEngineProperty.SetMaxAngularAccel = new.instancemethod(Appc.ImpulseEngineProperty_SetMaxAngularAccel, None, ImpulseEngineProperty)
ImpulseEngineProperty.SetEngineSound = new.instancemethod(Appc.ImpulseEngineProperty_SetEngineSound, None, ImpulseEngineProperty)

class WarpEngineProperty(PoweredSubsystemProperty):
    def __init__(self,*args):
        self.this = apply(Appc.new_WarpEngineProperty,args)
        self.thisown = 1

    def __del__(self,Appc=Appc):
        if self.thisown == 1 :
            Appc.delete_WarpEngineProperty(self)
    def __repr__(self):
        return "<C WarpEngineProperty instance at %s>" % (self.this,)
class WarpEnginePropertyPtr(WarpEngineProperty):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = WarpEngineProperty



class PowerProperty(SubsystemProperty):
    def __init__(self,*args):
        self.this = apply(Appc.new_PowerProperty,args)
        self.thisown = 1

    def __del__(self,Appc=Appc):
        if self.thisown == 1 :
            Appc.delete_PowerProperty(self)
    def __repr__(self):
        return "<C PowerProperty instance at %s>" % (self.this,)
class PowerPropertyPtr(PowerProperty):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = PowerProperty


PowerProperty.GetMainBatteryLimit = new.instancemethod(Appc.PowerProperty_GetMainBatteryLimit, None, PowerProperty)
PowerProperty.GetBackupBatteryLimit = new.instancemethod(Appc.PowerProperty_GetBackupBatteryLimit, None, PowerProperty)
PowerProperty.GetMainConduitCapacity = new.instancemethod(Appc.PowerProperty_GetMainConduitCapacity, None, PowerProperty)
PowerProperty.GetBackupConduitCapacity = new.instancemethod(Appc.PowerProperty_GetBackupConduitCapacity, None, PowerProperty)
PowerProperty.GetPowerOutput = new.instancemethod(Appc.PowerProperty_GetPowerOutput, None, PowerProperty)
PowerProperty.SetMainBatteryLimit = new.instancemethod(Appc.PowerProperty_SetMainBatteryLimit, None, PowerProperty)
PowerProperty.SetBackupBatteryLimit = new.instancemethod(Appc.PowerProperty_SetBackupBatteryLimit, None, PowerProperty)
PowerProperty.SetMainConduitCapacity = new.instancemethod(Appc.PowerProperty_SetMainConduitCapacity, None, PowerProperty)
PowerProperty.SetBackupConduitCapacity = new.instancemethod(Appc.PowerProperty_SetBackupConduitCapacity, None, PowerProperty)
PowerProperty.SetPowerOutput = new.instancemethod(Appc.PowerProperty_SetPowerOutput, None, PowerProperty)

class RepairSubsystemProperty(PoweredSubsystemProperty):
    def __init__(self,*args):
        self.this = apply(Appc.new_RepairSubsystemProperty,args)
        self.thisown = 1

    def __del__(self,Appc=Appc):
        if self.thisown == 1 :
            Appc.delete_RepairSubsystemProperty(self)
    def __repr__(self):
        return "<C RepairSubsystemProperty instance at %s>" % (self.this,)
class RepairSubsystemPropertyPtr(RepairSubsystemProperty):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = RepairSubsystemProperty


RepairSubsystemProperty.GetMaxRepairPoints = new.instancemethod(Appc.RepairSubsystemProperty_GetMaxRepairPoints, None, RepairSubsystemProperty)
RepairSubsystemProperty.GetNumRepairTeams = new.instancemethod(Appc.RepairSubsystemProperty_GetNumRepairTeams, None, RepairSubsystemProperty)
RepairSubsystemProperty.SetMaxRepairPoints = new.instancemethod(Appc.RepairSubsystemProperty_SetMaxRepairPoints, None, RepairSubsystemProperty)
RepairSubsystemProperty.SetNumRepairTeams = new.instancemethod(Appc.RepairSubsystemProperty_SetNumRepairTeams, None, RepairSubsystemProperty)

class TractorBeamProperty(EnergyWeaponProperty):
    def __init__(self,*args):
        self.this = apply(Appc.new_TractorBeamProperty,args)
        self.thisown = 1

    def __del__(self,Appc=Appc):
        if self.thisown == 1 :
            Appc.delete_TractorBeamProperty(self)
    def GetOrientationForward(*args):
        val = apply(Appc.TractorBeamProperty_GetOrientationForward,args)
        if val: val = TGPoint3Ptr(val) ; val.thisown = 1
        return val
    def GetOrientationUp(*args):
        val = apply(Appc.TractorBeamProperty_GetOrientationUp,args)
        if val: val = TGPoint3Ptr(val) ; val.thisown = 1
        return val
    def GetOrientationRight(*args):
        val = apply(Appc.TractorBeamProperty_GetOrientationRight,args)
        if val: val = TGPoint3Ptr(val) ; val.thisown = 1
        return val
    def GetOuterShellColor(*args):
        val = apply(Appc.TractorBeamProperty_GetOuterShellColor,args)
        if val: val = NiColorAPtr(val) ; val.thisown = 1
        return val
    def GetInnerShellColor(*args):
        val = apply(Appc.TractorBeamProperty_GetInnerShellColor,args)
        if val: val = NiColorAPtr(val) ; val.thisown = 1
        return val
    def GetOuterCoreColor(*args):
        val = apply(Appc.TractorBeamProperty_GetOuterCoreColor,args)
        if val: val = NiColorAPtr(val) ; val.thisown = 1
        return val
    def GetInnerCoreColor(*args):
        val = apply(Appc.TractorBeamProperty_GetInnerCoreColor,args)
        if val: val = NiColorAPtr(val) ; val.thisown = 1
        return val
    def __repr__(self):
        return "<C TractorBeamProperty instance at %s>" % (self.this,)
class TractorBeamPropertyPtr(TractorBeamProperty):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = TractorBeamProperty


TractorBeamProperty.SetArcWidthAngles = new.instancemethod(Appc.TractorBeamProperty_SetArcWidthAngles, None, TractorBeamProperty)
TractorBeamProperty.SetArcHeightAngles = new.instancemethod(Appc.TractorBeamProperty_SetArcHeightAngles, None, TractorBeamProperty)
TractorBeamProperty.SetOrientation = new.instancemethod(Appc.TractorBeamProperty_SetOrientation, None, TractorBeamProperty)
TractorBeamProperty.GetArcWidthAngles = new.instancemethod(Appc.TractorBeamProperty_GetArcWidthAngles, None, TractorBeamProperty)
TractorBeamProperty.GetArcHeightAngles = new.instancemethod(Appc.TractorBeamProperty_GetArcHeightAngles, None, TractorBeamProperty)
TractorBeamProperty.GetArcWidthAngleMin = new.instancemethod(Appc.TractorBeamProperty_GetArcWidthAngleMin, None, TractorBeamProperty)
TractorBeamProperty.GetArcWidthAngleMax = new.instancemethod(Appc.TractorBeamProperty_GetArcWidthAngleMax, None, TractorBeamProperty)
TractorBeamProperty.GetArcHeightAngleMin = new.instancemethod(Appc.TractorBeamProperty_GetArcHeightAngleMin, None, TractorBeamProperty)
TractorBeamProperty.GetArcHeightAngleMax = new.instancemethod(Appc.TractorBeamProperty_GetArcHeightAngleMax, None, TractorBeamProperty)
TractorBeamProperty.GetNumSides = new.instancemethod(Appc.TractorBeamProperty_GetNumSides, None, TractorBeamProperty)
TractorBeamProperty.GetMainRadius = new.instancemethod(Appc.TractorBeamProperty_GetMainRadius, None, TractorBeamProperty)
TractorBeamProperty.GetTaperRadius = new.instancemethod(Appc.TractorBeamProperty_GetTaperRadius, None, TractorBeamProperty)
TractorBeamProperty.GetCoreScale = new.instancemethod(Appc.TractorBeamProperty_GetCoreScale, None, TractorBeamProperty)
TractorBeamProperty.GetTaperRatio = new.instancemethod(Appc.TractorBeamProperty_GetTaperRatio, None, TractorBeamProperty)
TractorBeamProperty.GetTaperMinLength = new.instancemethod(Appc.TractorBeamProperty_GetTaperMinLength, None, TractorBeamProperty)
TractorBeamProperty.GetTaperMaxLength = new.instancemethod(Appc.TractorBeamProperty_GetTaperMaxLength, None, TractorBeamProperty)
TractorBeamProperty.GetLengthTextureTilePerUnit = new.instancemethod(Appc.TractorBeamProperty_GetLengthTextureTilePerUnit, None, TractorBeamProperty)
TractorBeamProperty.GetPerimeterTile = new.instancemethod(Appc.TractorBeamProperty_GetPerimeterTile, None, TractorBeamProperty)
TractorBeamProperty.GetTextureSpeed = new.instancemethod(Appc.TractorBeamProperty_GetTextureSpeed, None, TractorBeamProperty)
TractorBeamProperty.GetTextureName = new.instancemethod(Appc.TractorBeamProperty_GetTextureName, None, TractorBeamProperty)
TractorBeamProperty.GetTextureStart = new.instancemethod(Appc.TractorBeamProperty_GetTextureStart, None, TractorBeamProperty)
TractorBeamProperty.GetTextureEnd = new.instancemethod(Appc.TractorBeamProperty_GetTextureEnd, None, TractorBeamProperty)
TractorBeamProperty.GetTractorBeamWidth = new.instancemethod(Appc.TractorBeamProperty_GetTractorBeamWidth, None, TractorBeamProperty)
TractorBeamProperty.SetOuterShellColor = new.instancemethod(Appc.TractorBeamProperty_SetOuterShellColor, None, TractorBeamProperty)
TractorBeamProperty.SetInnerShellColor = new.instancemethod(Appc.TractorBeamProperty_SetInnerShellColor, None, TractorBeamProperty)
TractorBeamProperty.SetOuterCoreColor = new.instancemethod(Appc.TractorBeamProperty_SetOuterCoreColor, None, TractorBeamProperty)
TractorBeamProperty.SetInnerCoreColor = new.instancemethod(Appc.TractorBeamProperty_SetInnerCoreColor, None, TractorBeamProperty)
TractorBeamProperty.SetNumSides = new.instancemethod(Appc.TractorBeamProperty_SetNumSides, None, TractorBeamProperty)
TractorBeamProperty.SetMainRadius = new.instancemethod(Appc.TractorBeamProperty_SetMainRadius, None, TractorBeamProperty)
TractorBeamProperty.SetTaperRadius = new.instancemethod(Appc.TractorBeamProperty_SetTaperRadius, None, TractorBeamProperty)
TractorBeamProperty.SetCoreScale = new.instancemethod(Appc.TractorBeamProperty_SetCoreScale, None, TractorBeamProperty)
TractorBeamProperty.SetTaperRatio = new.instancemethod(Appc.TractorBeamProperty_SetTaperRatio, None, TractorBeamProperty)
TractorBeamProperty.SetTaperMinLength = new.instancemethod(Appc.TractorBeamProperty_SetTaperMinLength, None, TractorBeamProperty)
TractorBeamProperty.SetTaperMaxLength = new.instancemethod(Appc.TractorBeamProperty_SetTaperMaxLength, None, TractorBeamProperty)
TractorBeamProperty.SetLengthTextureTilePerUnit = new.instancemethod(Appc.TractorBeamProperty_SetLengthTextureTilePerUnit, None, TractorBeamProperty)
TractorBeamProperty.SetPerimeterTile = new.instancemethod(Appc.TractorBeamProperty_SetPerimeterTile, None, TractorBeamProperty)
TractorBeamProperty.SetTextureSpeed = new.instancemethod(Appc.TractorBeamProperty_SetTextureSpeed, None, TractorBeamProperty)
TractorBeamProperty.SetTextureName = new.instancemethod(Appc.TractorBeamProperty_SetTextureName, None, TractorBeamProperty)
TractorBeamProperty.SetTextureStart = new.instancemethod(Appc.TractorBeamProperty_SetTextureStart, None, TractorBeamProperty)
TractorBeamProperty.SetTextureEnd = new.instancemethod(Appc.TractorBeamProperty_SetTextureEnd, None, TractorBeamProperty)
TractorBeamProperty.SetTractorBeamWidth = new.instancemethod(Appc.TractorBeamProperty_SetTractorBeamWidth, None, TractorBeamProperty)

class EffectEmitterProperty(PositionOrientationProperty):
    def __init__(self,this):
        self.this = this

    def __del__(self,Appc=Appc):
        if self.thisown == 1 :
            Appc.delete_PositionOrientationProperty(self)
    def __repr__(self):
        return "<C EffectEmitterProperty instance at %s>" % (self.this,)
class EffectEmitterPropertyPtr(EffectEmitterProperty):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = EffectEmitterProperty



class SmokeEmitterProperty(EffectEmitterProperty):
    def __init__(self,this):
        self.this = this

    def __del__(self,Appc=Appc):
        if self.thisown == 1 :
            Appc.delete_PositionOrientationProperty(self)
    def __repr__(self):
        return "<C SmokeEmitterProperty instance at %s>" % (self.this,)
class SmokeEmitterPropertyPtr(SmokeEmitterProperty):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = SmokeEmitterProperty



class ExplodeEmitterProperty(EffectEmitterProperty):
    def __init__(self,this):
        self.this = this

    def __del__(self,Appc=Appc):
        if self.thisown == 1 :
            Appc.delete_PositionOrientationProperty(self)
    def __repr__(self):
        return "<C ExplodeEmitterProperty instance at %s>" % (self.this,)
class ExplodeEmitterPropertyPtr(ExplodeEmitterProperty):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = ExplodeEmitterProperty



class SparkEmitterProperty(EffectEmitterProperty):
    def __init__(self,this):
        self.this = this

    def __del__(self,Appc=Appc):
        if self.thisown == 1 :
            Appc.delete_PositionOrientationProperty(self)
    def __repr__(self):
        return "<C SparkEmitterProperty instance at %s>" % (self.this,)
class SparkEmitterPropertyPtr(SparkEmitterProperty):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = SparkEmitterProperty



class CloakingSubsystemProperty(PoweredSubsystemProperty):
    def __init__(self,*args):
        self.this = apply(Appc.new_CloakingSubsystemProperty,args)
        self.thisown = 1

    def __del__(self,Appc=Appc):
        if self.thisown == 1 :
            Appc.delete_CloakingSubsystemProperty(self)
    def __repr__(self):
        return "<C CloakingSubsystemProperty instance at %s>" % (self.this,)
class CloakingSubsystemPropertyPtr(CloakingSubsystemProperty):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = CloakingSubsystemProperty


CloakingSubsystemProperty.GetCloakStrength = new.instancemethod(Appc.CloakingSubsystemProperty_GetCloakStrength, None, CloakingSubsystemProperty)
CloakingSubsystemProperty.SetCloakStrength = new.instancemethod(Appc.CloakingSubsystemProperty_SetCloakStrength, None, CloakingSubsystemProperty)

class EngineProperty(SubsystemProperty):
    EP_IMPULSE = Appc.EngineProperty_EP_IMPULSE
    EP_WARP = Appc.EngineProperty_EP_WARP
    def __init__(self,*args):
        self.this = apply(Appc.new_EngineProperty,args)
        self.thisown = 1

    def __del__(self,Appc=Appc):
        if self.thisown == 1 :
            Appc.delete_EngineProperty(self)
    def __repr__(self):
        return "<C EngineProperty instance at %s>" % (self.this,)
class EnginePropertyPtr(EngineProperty):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = EngineProperty


EngineProperty.GetEngineType = new.instancemethod(Appc.EngineProperty_GetEngineType, None, EngineProperty)
EngineProperty.SetEngineType = new.instancemethod(Appc.EngineProperty_SetEngineType, None, EngineProperty)

class TorpedoAmmoType:
    def __init__(self,*args):
        self.this = apply(Appc.new_TorpedoAmmoType,args)
        self.thisown = 1

    def __del__(self,Appc=Appc):
        if self.thisown == 1 :
            Appc.delete_TorpedoAmmoType(self)
    __setmethods__ = {
        "m_iMaxTorpedoes" : Appc.TorpedoAmmoType_m_iMaxTorpedoes_set,
        "m_pcModule" : Appc.TorpedoAmmoType_m_pcModule_set,
        "m_fLaunchSpeed" : Appc.TorpedoAmmoType_m_fLaunchSpeed_set,
        "m_pcLaunchSound" : Appc.TorpedoAmmoType_m_pcLaunchSound_set,
    }
    def __setattr__(self,name,value):
        if (name == "this") or (name == "thisown"): self.__dict__[name] = value; return
        method = TorpedoAmmoType.__setmethods__.get(name,None)
        if method: return method(self,value)
        self.__dict__[name] = value
    __getmethods__ = {
        "m_iMaxTorpedoes" : Appc.TorpedoAmmoType_m_iMaxTorpedoes_get,
        "m_pcModule" : Appc.TorpedoAmmoType_m_pcModule_get,
        "m_fLaunchSpeed" : Appc.TorpedoAmmoType_m_fLaunchSpeed_get,
        "m_pcLaunchSound" : Appc.TorpedoAmmoType_m_pcLaunchSound_get,
    }
    def __getattr__(self,name):
        method = TorpedoAmmoType.__getmethods__.get(name,None)
        if method: return method(self)
        raise AttributeError,name
    def __repr__(self):
        return "<C TorpedoAmmoType instance at %s>" % (self.this,)
class TorpedoAmmoTypePtr(TorpedoAmmoType):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = TorpedoAmmoType


TorpedoAmmoType.GetLaunchSpeed = new.instancemethod(Appc.TorpedoAmmoType_GetLaunchSpeed, None, TorpedoAmmoType)
TorpedoAmmoType.GetLaunchSound = new.instancemethod(Appc.TorpedoAmmoType_GetLaunchSound, None, TorpedoAmmoType)
TorpedoAmmoType.GetPowerCost = new.instancemethod(Appc.TorpedoAmmoType_GetPowerCost, None, TorpedoAmmoType)
TorpedoAmmoType.GetAmmoName = new.instancemethod(Appc.TorpedoAmmoType_GetAmmoName, None, TorpedoAmmoType)
TorpedoAmmoType.GetMaxTorpedoes = new.instancemethod(Appc.TorpedoAmmoType_GetMaxTorpedoes, None, TorpedoAmmoType)
TorpedoAmmoType.SetMaxTorpedoes = new.instancemethod(Appc.TorpedoAmmoType_SetMaxTorpedoes, None, TorpedoAmmoType)
TorpedoAmmoType.GetTorpedoScript = new.instancemethod(Appc.TorpedoAmmoType_GetTorpedoScript, None, TorpedoAmmoType)
TorpedoAmmoType.SetTorpedoScript = new.instancemethod(Appc.TorpedoAmmoType_SetTorpedoScript, None, TorpedoAmmoType)

class TorpedoSystemProperty(WeaponSystemProperty):
    def __init__(self,*args):
        self.this = apply(Appc.new_TorpedoSystemProperty,args)
        self.thisown = 1

    def __del__(self,Appc=Appc):
        if self.thisown == 1 :
            Appc.delete_TorpedoSystemProperty(self)
    def __repr__(self):
        return "<C TorpedoSystemProperty instance at %s>" % (self.this,)
class TorpedoSystemPropertyPtr(TorpedoSystemProperty):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = TorpedoSystemProperty


TorpedoSystemProperty.SetMaxTorpedoes = new.instancemethod(Appc.TorpedoSystemProperty_SetMaxTorpedoes, None, TorpedoSystemProperty)
TorpedoSystemProperty.GetMaxTorpedoes = new.instancemethod(Appc.TorpedoSystemProperty_GetMaxTorpedoes, None, TorpedoSystemProperty)
TorpedoSystemProperty.SetTorpedoScript = new.instancemethod(Appc.TorpedoSystemProperty_SetTorpedoScript, None, TorpedoSystemProperty)
TorpedoSystemProperty.GetTorpedoScript = new.instancemethod(Appc.TorpedoSystemProperty_GetTorpedoScript, None, TorpedoSystemProperty)
TorpedoSystemProperty.SetNumAmmoTypes = new.instancemethod(Appc.TorpedoSystemProperty_SetNumAmmoTypes, None, TorpedoSystemProperty)
TorpedoSystemProperty.GetNumAmmoTypes = new.instancemethod(Appc.TorpedoSystemProperty_GetNumAmmoTypes, None, TorpedoSystemProperty)

class BlinkingLightProperty(EffectEmitterProperty):
    def __init__(self,this):
        self.this = this

    def GetColor(*args):
        val = apply(Appc.BlinkingLightProperty_GetColor,args)
        if val: val = TGColorAPtr(val) ; val.thisown = 1
        return val
    def __del__(self,Appc=Appc):
        if self.thisown == 1 :
            Appc.delete_PositionOrientationProperty(self)
    def __repr__(self):
        return "<C BlinkingLightProperty instance at %s>" % (self.this,)
class BlinkingLightPropertyPtr(BlinkingLightProperty):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = BlinkingLightProperty


BlinkingLightProperty.GetRadius = new.instancemethod(Appc.BlinkingLightProperty_GetRadius, None, BlinkingLightProperty)
BlinkingLightProperty.GetPeriod = new.instancemethod(Appc.BlinkingLightProperty_GetPeriod, None, BlinkingLightProperty)
BlinkingLightProperty.GetDuration = new.instancemethod(Appc.BlinkingLightProperty_GetDuration, None, BlinkingLightProperty)
BlinkingLightProperty.GetTextureName = new.instancemethod(Appc.BlinkingLightProperty_GetTextureName, None, BlinkingLightProperty)
BlinkingLightProperty.SetColor = new.instancemethod(Appc.BlinkingLightProperty_SetColor, None, BlinkingLightProperty)
BlinkingLightProperty.SetRadius = new.instancemethod(Appc.BlinkingLightProperty_SetRadius, None, BlinkingLightProperty)
BlinkingLightProperty.SetPeriod = new.instancemethod(Appc.BlinkingLightProperty_SetPeriod, None, BlinkingLightProperty)
BlinkingLightProperty.SetDuration = new.instancemethod(Appc.BlinkingLightProperty_SetDuration, None, BlinkingLightProperty)
BlinkingLightProperty.SetTextureName = new.instancemethod(Appc.BlinkingLightProperty_SetTextureName, None, BlinkingLightProperty)

class ObjectEmitterProperty(PositionOrientationProperty):
    OEP_UNKNOWN = Appc.ObjectEmitterProperty_OEP_UNKNOWN
    OEP_SHUTTLE = Appc.ObjectEmitterProperty_OEP_SHUTTLE
    OEP_PROBE = Appc.ObjectEmitterProperty_OEP_PROBE
    OEP_DECOY = Appc.ObjectEmitterProperty_OEP_DECOY
    def __init__(self,*args):
        self.this = apply(Appc.new_ObjectEmitterProperty,args)
        self.thisown = 1

    def __del__(self,Appc=Appc):
        if self.thisown == 1 :
            Appc.delete_ObjectEmitterProperty(self)
    def __repr__(self):
        return "<C ObjectEmitterProperty instance at %s>" % (self.this,)
class ObjectEmitterPropertyPtr(ObjectEmitterProperty):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
        self.__class__ = ObjectEmitterProperty


ObjectEmitterProperty.GetEmittedObjectType = new.instancemethod(Appc.ObjectEmitterProperty_GetEmittedObjectType, None, ObjectEmitterProperty)
ObjectEmitterProperty.SetEmittedObjectType = new.instancemethod(Appc.ObjectEmitterProperty_SetEmittedObjectType, None, ObjectEmitterProperty)



#-------------- FUNCTION WRAPPERS ------------------

TGLocDBWrapperSerialize = Appc.TGLocDBWrapperSerialize

TGLocDBWrapperUnserialize = Appc.TGLocDBWrapperUnserialize

IsNull = Appc.IsNull

DeleteBuffer = Appc.DeleteBuffer

Breakpoint = Appc.Breakpoint

SerializeGetState = Appc.SerializeGetState

UnserializeSetState = Appc.UnserializeSetState

def TGLocalizationDatabase_Create(*args, **kwargs):
    val = apply(Appc.TGLocalizationDatabase_Create,args,kwargs)
    if val: val = TGLocalizationDatabasePtr(val)
    return val

TGLocalizationDatabase_WriteSample = Appc.TGLocalizationDatabase_WriteSample

TGObject_GetIndentString = Appc.TGObject_GetIndentString

TGObject_SetIncrementID = Appc.TGObject_SetIncrementID

TGObject_IsIncrementID = Appc.TGObject_IsIncrementID

def TGObject_GetTGObjectPtr(*args, **kwargs):
    val = apply(Appc.TGObject_GetTGObjectPtr,args,kwargs)
    if val: val = TGObjectPtr(val)
    return val

TGProfilingInfo_EnableProfiling = Appc.TGProfilingInfo_EnableProfiling

TGProfilingInfo_DisableProfiling = Appc.TGProfilingInfo_DisableProfiling

TGProfilingInfo_StartTiming = Appc.TGProfilingInfo_StartTiming

TGProfilingInfo_StopTiming = Appc.TGProfilingInfo_StopTiming

TGProfilingInfo_SetTimingData = Appc.TGProfilingInfo_SetTimingData

TGProfilingInfo_SaveRawData = Appc.TGProfilingInfo_SaveRawData

TGProfilingInfo_Terminate = Appc.TGProfilingInfo_Terminate

PyEmbed_SerializeModule = Appc.PyEmbed_SerializeModule

PyEmbed_UnserializeModule = Appc.PyEmbed_UnserializeModule

PyEmbed_StartSave = Appc.PyEmbed_StartSave

PyEmbed_FinishSave = Appc.PyEmbed_FinishSave

PyEmbed_StartLoad = Appc.PyEmbed_StartLoad

PyEmbed_FinishLoad = Appc.PyEmbed_FinishLoad

def TGModelProperty_Cast(*args, **kwargs):
    val = apply(Appc.TGModelProperty_Cast,args,kwargs)
    if val: val = TGModelPropertyPtr(val)
    return val

def TGModelProperty_Create(*args, **kwargs):
    val = apply(Appc.TGModelProperty_Create,args,kwargs)
    if val: val = TGModelPropertyPtr(val)
    return val

def TGModelPropertySet_Create(*args, **kwargs):
    val = apply(Appc.TGModelPropertySet_Create,args,kwargs)
    if val: val = TGModelPropertySetPtr(val)
    return val

def TGPoint3_GetRandomUnitVector(*args, **kwargs):
    val = apply(Appc.TGPoint3_GetRandomUnitVector,args,kwargs)
    if val: val = TGPoint3Ptr(val); val.thisown = 1
    return val

def TGPoint3_GetModelForward(*args, **kwargs):
    val = apply(Appc.TGPoint3_GetModelForward,args,kwargs)
    if val: val = TGPoint3Ptr(val); val.thisown = 1
    return val

def TGPoint3_GetModelBackward(*args, **kwargs):
    val = apply(Appc.TGPoint3_GetModelBackward,args,kwargs)
    if val: val = TGPoint3Ptr(val); val.thisown = 1
    return val

def TGPoint3_GetModelUp(*args, **kwargs):
    val = apply(Appc.TGPoint3_GetModelUp,args,kwargs)
    if val: val = TGPoint3Ptr(val); val.thisown = 1
    return val

def TGPoint3_GetModelDown(*args, **kwargs):
    val = apply(Appc.TGPoint3_GetModelDown,args,kwargs)
    if val: val = TGPoint3Ptr(val); val.thisown = 1
    return val

def TGPoint3_GetModelRight(*args, **kwargs):
    val = apply(Appc.TGPoint3_GetModelRight,args,kwargs)
    if val: val = TGPoint3Ptr(val); val.thisown = 1
    return val

def TGPoint3_GetModelLeft(*args, **kwargs):
    val = apply(Appc.TGPoint3_GetModelLeft,args,kwargs)
    if val: val = TGPoint3Ptr(val); val.thisown = 1
    return val

TGPoint3_UnitizeVectors = Appc.TGPoint3_UnitizeVectors

TGPoint3_UnitizeVector = Appc.TGPoint3_UnitizeVector

TGPoint3_VectorLength = Appc.TGPoint3_VectorLength

def PositionOrientationProperty_Cast(*args, **kwargs):
    val = apply(Appc.PositionOrientationProperty_Cast,args,kwargs)
    if val: val = PositionOrientationPropertyPtr(val)
    return val

def PositionOrientationProperty_Create(*args, **kwargs):
    val = apply(Appc.PositionOrientationProperty_Create,args,kwargs)
    if val: val = PositionOrientationPropertyPtr(val)
    return val

def SubsystemProperty_Cast(*args, **kwargs):
    val = apply(Appc.SubsystemProperty_Cast,args,kwargs)
    if val: val = SubsystemPropertyPtr(val)
    return val

def SubsystemProperty_Create(*args, **kwargs):
    val = apply(Appc.SubsystemProperty_Create,args,kwargs)
    if val: val = SubsystemPropertyPtr(val)
    return val

def PoweredSubsystemProperty_Cast(*args, **kwargs):
    val = apply(Appc.PoweredSubsystemProperty_Cast,args,kwargs)
    if val: val = PoweredSubsystemPropertyPtr(val)
    return val

def PoweredSubsystemProperty_Create(*args, **kwargs):
    val = apply(Appc.PoweredSubsystemProperty_Create,args,kwargs)
    if val: val = PoweredSubsystemPropertyPtr(val)
    return val

def ShipProperty_Cast(*args, **kwargs):
    val = apply(Appc.ShipProperty_Cast,args,kwargs)
    if val: val = ShipPropertyPtr(val)
    return val

def ShipProperty_Create(*args, **kwargs):
    val = apply(Appc.ShipProperty_Create,args,kwargs)
    if val: val = ShipPropertyPtr(val)
    return val

def WeaponSystemProperty_Cast(*args, **kwargs):
    val = apply(Appc.WeaponSystemProperty_Cast,args,kwargs)
    if val: val = WeaponSystemPropertyPtr(val)
    return val

def WeaponSystemProperty_Create(*args, **kwargs):
    val = apply(Appc.WeaponSystemProperty_Create,args,kwargs)
    if val: val = WeaponSystemPropertyPtr(val)
    return val

def WeaponProperty_Cast(*args, **kwargs):
    val = apply(Appc.WeaponProperty_Cast,args,kwargs)
    if val: val = WeaponPropertyPtr(val)
    return val

def WeaponProperty_Create(*args, **kwargs):
    val = apply(Appc.WeaponProperty_Create,args,kwargs)
    if val: val = WeaponPropertyPtr(val)
    return val

def EnergyWeaponProperty_Cast(*args, **kwargs):
    val = apply(Appc.EnergyWeaponProperty_Cast,args,kwargs)
    if val: val = EnergyWeaponPropertyPtr(val)
    return val

def EnergyWeaponProperty_Create(*args, **kwargs):
    val = apply(Appc.EnergyWeaponProperty_Create,args,kwargs)
    if val: val = EnergyWeaponPropertyPtr(val)
    return val

def PhaserProperty_Cast(*args, **kwargs):
    val = apply(Appc.PhaserProperty_Cast,args,kwargs)
    if val: val = PhaserPropertyPtr(val)
    return val

def PhaserProperty_Create(*args, **kwargs):
    val = apply(Appc.PhaserProperty_Create,args,kwargs)
    if val: val = PhaserPropertyPtr(val)
    return val

def EngineGlowProperty_Cast(*args, **kwargs):
    val = apply(Appc.EngineGlowProperty_Cast,args,kwargs)
    if val: val = EngineGlowPropertyPtr(val)
    return val

def EngineGlowProperty_Create(*args, **kwargs):
    val = apply(Appc.EngineGlowProperty_Create,args,kwargs)
    if val: val = EngineGlowPropertyPtr(val)
    return val

def TorpedoTubeProperty_Cast(*args, **kwargs):
    val = apply(Appc.TorpedoTubeProperty_Cast,args,kwargs)
    if val: val = TorpedoTubePropertyPtr(val)
    return val

def TorpedoTubeProperty_Create(*args, **kwargs):
    val = apply(Appc.TorpedoTubeProperty_Create,args,kwargs)
    if val: val = TorpedoTubePropertyPtr(val)
    return val

def ShieldProperty_Cast(*args, **kwargs):
    val = apply(Appc.ShieldProperty_Cast,args,kwargs)
    if val: val = ShieldPropertyPtr(val)
    return val

def ShieldProperty_Create(*args, **kwargs):
    val = apply(Appc.ShieldProperty_Create,args,kwargs)
    if val: val = ShieldPropertyPtr(val)
    return val

def HullProperty_Cast(*args, **kwargs):
    val = apply(Appc.HullProperty_Cast,args,kwargs)
    if val: val = HullPropertyPtr(val)
    return val

def HullProperty_Create(*args, **kwargs):
    val = apply(Appc.HullProperty_Create,args,kwargs)
    if val: val = HullPropertyPtr(val)
    return val

def SensorProperty_Cast(*args, **kwargs):
    val = apply(Appc.SensorProperty_Cast,args,kwargs)
    if val: val = SensorPropertyPtr(val)
    return val

def SensorProperty_Create(*args, **kwargs):
    val = apply(Appc.SensorProperty_Create,args,kwargs)
    if val: val = SensorPropertyPtr(val)
    return val

def PulseWeaponProperty_Cast(*args, **kwargs):
    val = apply(Appc.PulseWeaponProperty_Cast,args,kwargs)
    if val: val = PulseWeaponPropertyPtr(val)
    return val

def PulseWeaponProperty_Create(*args, **kwargs):
    val = apply(Appc.PulseWeaponProperty_Create,args,kwargs)
    if val: val = PulseWeaponPropertyPtr(val)
    return val

def ImpulseEngineProperty_Cast(*args, **kwargs):
    val = apply(Appc.ImpulseEngineProperty_Cast,args,kwargs)
    if val: val = ImpulseEnginePropertyPtr(val)
    return val

def ImpulseEngineProperty_Create(*args, **kwargs):
    val = apply(Appc.ImpulseEngineProperty_Create,args,kwargs)
    if val: val = ImpulseEnginePropertyPtr(val)
    return val

def WarpEngineProperty_Cast(*args, **kwargs):
    val = apply(Appc.WarpEngineProperty_Cast,args,kwargs)
    if val: val = WarpEnginePropertyPtr(val)
    return val

def WarpEngineProperty_Create(*args, **kwargs):
    val = apply(Appc.WarpEngineProperty_Create,args,kwargs)
    if val: val = WarpEnginePropertyPtr(val)
    return val

def PowerProperty_Cast(*args, **kwargs):
    val = apply(Appc.PowerProperty_Cast,args,kwargs)
    if val: val = PowerPropertyPtr(val)
    return val

def PowerProperty_Create(*args, **kwargs):
    val = apply(Appc.PowerProperty_Create,args,kwargs)
    if val: val = PowerPropertyPtr(val)
    return val

def RepairSubsystemProperty_Cast(*args, **kwargs):
    val = apply(Appc.RepairSubsystemProperty_Cast,args,kwargs)
    if val: val = RepairSubsystemPropertyPtr(val)
    return val

def RepairSubsystemProperty_Create(*args, **kwargs):
    val = apply(Appc.RepairSubsystemProperty_Create,args,kwargs)
    if val: val = RepairSubsystemPropertyPtr(val)
    return val

def TractorBeamProperty_Cast(*args, **kwargs):
    val = apply(Appc.TractorBeamProperty_Cast,args,kwargs)
    if val: val = TractorBeamPropertyPtr(val)
    return val

def TractorBeamProperty_Create(*args, **kwargs):
    val = apply(Appc.TractorBeamProperty_Create,args,kwargs)
    if val: val = TractorBeamPropertyPtr(val)
    return val

def EffectEmitterProperty_Cast(*args, **kwargs):
    val = apply(Appc.EffectEmitterProperty_Cast,args,kwargs)
    if val: val = EffectEmitterPropertyPtr(val)
    return val

def EffectEmitterProperty_Create(*args, **kwargs):
    val = apply(Appc.EffectEmitterProperty_Create,args,kwargs)
    if val: val = EffectEmitterPropertyPtr(val)
    return val

def SmokeEmitterProperty_Cast(*args, **kwargs):
    val = apply(Appc.SmokeEmitterProperty_Cast,args,kwargs)
    if val: val = SmokeEmitterPropertyPtr(val)
    return val

def SmokeEmitterProperty_Create(*args, **kwargs):
    val = apply(Appc.SmokeEmitterProperty_Create,args,kwargs)
    if val: val = SmokeEmitterPropertyPtr(val)
    return val

def ExplodeEmitterProperty_Cast(*args, **kwargs):
    val = apply(Appc.ExplodeEmitterProperty_Cast,args,kwargs)
    if val: val = ExplodeEmitterPropertyPtr(val)
    return val

def ExplodeEmitterProperty_Create(*args, **kwargs):
    val = apply(Appc.ExplodeEmitterProperty_Create,args,kwargs)
    if val: val = ExplodeEmitterPropertyPtr(val)
    return val

def SparkEmitterProperty_Cast(*args, **kwargs):
    val = apply(Appc.SparkEmitterProperty_Cast,args,kwargs)
    if val: val = SparkEmitterPropertyPtr(val)
    return val

def SparkEmitterProperty_Create(*args, **kwargs):
    val = apply(Appc.SparkEmitterProperty_Create,args,kwargs)
    if val: val = SparkEmitterPropertyPtr(val)
    return val

def CloakingSubsystemProperty_Cast(*args, **kwargs):
    val = apply(Appc.CloakingSubsystemProperty_Cast,args,kwargs)
    if val: val = CloakingSubsystemPropertyPtr(val)
    return val

def CloakingSubsystemProperty_Create(*args, **kwargs):
    val = apply(Appc.CloakingSubsystemProperty_Create,args,kwargs)
    if val: val = CloakingSubsystemPropertyPtr(val)
    return val

def EngineProperty_Cast(*args, **kwargs):
    val = apply(Appc.EngineProperty_Cast,args,kwargs)
    if val: val = EnginePropertyPtr(val)
    return val

def EngineProperty_Create(*args, **kwargs):
    val = apply(Appc.EngineProperty_Create,args,kwargs)
    if val: val = EnginePropertyPtr(val)
    return val

def TorpedoSystemProperty_Cast(*args, **kwargs):
    val = apply(Appc.TorpedoSystemProperty_Cast,args,kwargs)
    if val: val = TorpedoSystemPropertyPtr(val)
    return val

def TorpedoSystemProperty_Create(*args, **kwargs):
    val = apply(Appc.TorpedoSystemProperty_Create,args,kwargs)
    if val: val = TorpedoSystemPropertyPtr(val)
    return val

def BlinkingLightProperty_Cast(*args, **kwargs):
    val = apply(Appc.BlinkingLightProperty_Cast,args,kwargs)
    if val: val = BlinkingLightPropertyPtr(val)
    return val

def BlinkingLightProperty_Create(*args, **kwargs):
    val = apply(Appc.BlinkingLightProperty_Create,args,kwargs)
    if val: val = BlinkingLightPropertyPtr(val)
    return val

def ObjectEmitterProperty_Cast(*args, **kwargs):
    val = apply(Appc.ObjectEmitterProperty_Cast,args,kwargs)
    if val: val = ObjectEmitterPropertyPtr(val)
    return val

def ObjectEmitterProperty_Create(*args, **kwargs):
    val = apply(Appc.ObjectEmitterProperty_Create,args,kwargs)
    if val: val = ObjectEmitterPropertyPtr(val)
    return val



#-------------- VARIABLE WRAPPERS ------------------

NULL_STRING_INDEX = Appc.NULL_STRING_INDEX
globals = Appc.globals
g_kLocalizationManager = TGLocalizationManagerPtr(Appc.globals.g_kLocalizationManager)
NULL_ID = Appc.NULL_ID
g_kSystemWrapper = TGSystemWrapperClassPtr(Appc.globals.g_kSystemWrapper)
PFID_INVALID = Appc.PFID_INVALID
g_kConfigMapping = TGConfigMappingPtr(Appc.globals.g_kConfigMapping)
g_kPoolManager = TGPoolManagerPtr(Appc.globals.g_kPoolManager)
PY_EXPRESSION = Appc.PY_EXPRESSION
PY_STATEMENT = Appc.PY_STATEMENT
g_kModelPropertyManager = TGModelPropertyManagerPtr(Appc.globals.g_kModelPropertyManager)
UTOPIA_MAJOR_VERSION_NUMBER = Appc.UTOPIA_MAJOR_VERSION_NUMBER
UTOPIA_MINOR_VERSION_NUMBER = Appc.UTOPIA_MINOR_VERSION_NUMBER
CT_TEMP_TYPE = Appc.CT_TEMP_TYPE
CT_BASE_OBJECT = Appc.CT_BASE_OBJECT
CT_OBJECT = Appc.CT_OBJECT
CT_PLANET = Appc.CT_PLANET
CT_SUN = Appc.CT_SUN
CT_PHYSICS_OBJECT = Appc.CT_PHYSICS_OBJECT
CT_DAMAGEABLE_OBJECT = Appc.CT_DAMAGEABLE_OBJECT
CT_SHIP = Appc.CT_SHIP
CT_TORPEDO = Appc.CT_TORPEDO
CT_DEBRIS = Appc.CT_DEBRIS
CT_BACKDROP = Appc.CT_BACKDROP
CT_BACKDROP_SPHERE = Appc.CT_BACKDROP_SPHERE
CT_STAR_SPHERE = Appc.CT_STAR_SPHERE
CT_NEBULA = Appc.CT_NEBULA
CT_META_NEBULA = Appc.CT_META_NEBULA
CT_RETICLE = Appc.CT_RETICLE
CT_OBJECT_GROUP = Appc.CT_OBJECT_GROUP
CT_OBJECT_GROUP_WITH_INFO = Appc.CT_OBJECT_GROUP_WITH_INFO
CT_WARP_FLASH = Appc.CT_WARP_FLASH
CT_ASTEROID_FIELD = Appc.CT_ASTEROID_FIELD
CT_ASTEROID_TILE = Appc.CT_ASTEROID_TILE
CT_CHARACTER = Appc.CT_CHARACTER
CT_CHARACTER_SPEAKING_QUEUE = Appc.CT_CHARACTER_SPEAKING_QUEUE
CT_CHARACTER_ACTION = Appc.CT_CHARACTER_ACTION
CT_BRIDGE_OBJECT = Appc.CT_BRIDGE_OBJECT
CT_VIEWSCREEN = Appc.CT_VIEWSCREEN
CT_SHIP_SUBSYSTEM = Appc.CT_SHIP_SUBSYSTEM
CT_POWERED_SUBSYSTEM = Appc.CT_POWERED_SUBSYSTEM
CT_WEAPON_SYSTEM = Appc.CT_WEAPON_SYSTEM
CT_TORPEDO_SYSTEM = Appc.CT_TORPEDO_SYSTEM
CT_PHASER_SYSTEM = Appc.CT_PHASER_SYSTEM
CT_PULSE_WEAPON_SYSTEM = Appc.CT_PULSE_WEAPON_SYSTEM
CT_TRACTOR_BEAM_SYSTEM = Appc.CT_TRACTOR_BEAM_SYSTEM
CT_POWER_SUBSYSTEM = Appc.CT_POWER_SUBSYSTEM
CT_SENSOR_SUBSYSTEM = Appc.CT_SENSOR_SUBSYSTEM
CT_CLOAKING_SUBSYSTEM = Appc.CT_CLOAKING_SUBSYSTEM
CT_WARP_ENGINE_SUBSYSTEM = Appc.CT_WARP_ENGINE_SUBSYSTEM
CT_IMPULSE_ENGINE_SUBSYSTEM = Appc.CT_IMPULSE_ENGINE_SUBSYSTEM
CT_HULL_SUBSYSTEM = Appc.CT_HULL_SUBSYSTEM
CT_SHIELD_SUBSYSTEM = Appc.CT_SHIELD_SUBSYSTEM
CT_REPAIR_SUBSYSTEM = Appc.CT_REPAIR_SUBSYSTEM
CT_WEAPON = Appc.CT_WEAPON
CT_ENERGY_WEAPON = Appc.CT_ENERGY_WEAPON
CT_PHASER_BANK = Appc.CT_PHASER_BANK
CT_PULSE_WEAPON = Appc.CT_PULSE_WEAPON
CT_TRACTOR_BEAM_PROJECTOR = Appc.CT_TRACTOR_BEAM_PROJECTOR
CT_TORPEDO_TUBE = Appc.CT_TORPEDO_TUBE
CT_AI = Appc.CT_AI
CT_PLAIN_AI = Appc.CT_PLAIN_AI
CT_PRIORITY_LIST_AI = Appc.CT_PRIORITY_LIST_AI
CT_SEQUENCE_AI = Appc.CT_SEQUENCE_AI
CT_PREPROCESSING_AI = Appc.CT_PREPROCESSING_AI
CT_CONDITIONAL_AI = Appc.CT_CONDITIONAL_AI
CT_CONDITION = Appc.CT_CONDITION
CT_CONDITION_SCRIPT = Appc.CT_CONDITION_SCRIPT
CT_CONDITION_EVENT_CREATOR = Appc.CT_CONDITION_EVENT_CREATOR
CT_SHIP_STATUS_WINDOW = Appc.CT_SHIP_STATUS_WINDOW
CT_OST_EVENT_HANDLER = Appc.CT_OST_EVENT_HANDLER
CT_OPTIMIZED_AI_FIRST = Appc.CT_OPTIMIZED_AI_FIRST
CT_OPTIMIZED_AI_LAST = Appc.CT_OPTIMIZED_AI_LAST
CT_LIGHT_OBJECT = Appc.CT_LIGHT_OBJECT
CT_PULSING_LIGHT = Appc.CT_PULSING_LIGHT
CT_CAMERA_OBJECT = Appc.CT_CAMERA_OBJECT
CT_SPACE_CAMERA = Appc.CT_SPACE_CAMERA
CT_ZOOM_CAMERA_OBJECT = Appc.CT_ZOOM_CAMERA_OBJECT
CT_VIEWSCREEN_CAMERA = Appc.CT_VIEWSCREEN_CAMERA
CT_CAMERA_MODE = Appc.CT_CAMERA_MODE
CT_IDEAL_CONTROLLED_CAMERA_MODE = Appc.CT_IDEAL_CONTROLLED_CAMERA_MODE
CT_CHASE_CAMERA_MODE = Appc.CT_CHASE_CAMERA_MODE
CT_TARGET_CAMERA_MODE = Appc.CT_TARGET_CAMERA_MODE
CT_ZOOM_TARGET_MODE = Appc.CT_ZOOM_TARGET_MODE
CT_MAP_CAMERA_MODE = Appc.CT_MAP_CAMERA_MODE
CT_DROP_AND_WATCH_MODE = Appc.CT_DROP_AND_WATCH_MODE
CT_PLACEMENT_WATCH_MODE = Appc.CT_PLACEMENT_WATCH_MODE
CT_LOCKED_POSITION_MODE = Appc.CT_LOCKED_POSITION_MODE
CT_TORP_CAMERA_MODE = Appc.CT_TORP_CAMERA_MODE
CT_PLACE_BY_DIRECTION_MODE = Appc.CT_PLACE_BY_DIRECTION_MODE
CT_SCRIPT_OBJECT = Appc.CT_SCRIPT_OBJECT
CT_GAME = Appc.CT_GAME
CT_EPISODE = Appc.CT_EPISODE
CT_MISSION = Appc.CT_MISSION
CT_SET = Appc.CT_SET
CT_BRIDGE_SET = Appc.CT_BRIDGE_SET
CT_WARP_SET = Appc.CT_WARP_SET
CT_MULTIPLAYER_GAME = Appc.CT_MULTIPLAYER_GAME
CT_MULTIPLAYER_WINDOW = Appc.CT_MULTIPLAYER_WINDOW
CT_NET_FILE = Appc.CT_NET_FILE
CT_GAMESPY = Appc.CT_GAMESPY
CT_SERVER_LIST_EVENT = Appc.CT_SERVER_LIST_EVENT
CT_SORT_SERVER_LIST_EVENT = Appc.CT_SORT_SERVER_LIST_EVENT
CT_EDITOR = Appc.CT_EDITOR
CT_PLACEMENT_EDITOR = Appc.CT_PLACEMENT_EDITOR
CT_SUB_EDITOR = Appc.CT_SUB_EDITOR
CT_BACKGROUND_EDITOR = Appc.CT_BACKGROUND_EDITOR
CT_PLACEMENT = Appc.CT_PLACEMENT
CT_ASTEROID_FIELD_PLACEMENT = Appc.CT_ASTEROID_FIELD_PLACEMENT
CT_WAYPOINT = Appc.CT_WAYPOINT
CT_LIGHT_PLACEMENT = Appc.CT_LIGHT_PLACEMENT
CT_GRID = Appc.CT_GRID
CT_ST_MENU = Appc.CT_ST_MENU
CT_ST_TOP_LEVEL_MENU = Appc.CT_ST_TOP_LEVEL_MENU
CT_ST_CHARACTER_MENU = Appc.CT_ST_CHARACTER_MENU
CT_ST_FILE_MENU = Appc.CT_ST_FILE_MENU
CT_ST_FILE_DIALOG = Appc.CT_ST_FILE_DIALOG
CT_ST_LOAD_DIALOG = Appc.CT_ST_LOAD_DIALOG
CT_ST_SAVE_DIALOG = Appc.CT_ST_SAVE_DIALOG
CT_ST_SUB_PANE = Appc.CT_ST_SUB_PANE
CT_ST_TARGET_MENU_SUB_PANE = Appc.CT_ST_TARGET_MENU_SUB_PANE
CT_ST_BUTTON = Appc.CT_ST_BUTTON
CT_ST_ROUNDED_BUTTON = Appc.CT_ST_ROUNDED_BUTTON
CT_ST_REPAIR_BUTTON = Appc.CT_ST_REPAIR_BUTTON
CT_ST_TOGGLE = Appc.CT_ST_TOGGLE
CT_ST_FILL_GAUGE = Appc.CT_ST_FILL_GAUGE
CT_ST_NUMERIC_BAR = Appc.CT_ST_NUMERIC_BAR
CT_ST_TARGET_MENU = Appc.CT_ST_TARGET_MENU
CT_ST_SUBSYSTEM_MENU = Appc.CT_ST_SUBSYSTEM_MENU
CT_ST_COMPONENT_MENU = Appc.CT_ST_COMPONENT_MENU
CT_ST_COMPONENT_MENU_ITEM = Appc.CT_ST_COMPONENT_MENU_ITEM
CT_ST_CHECKBOX = Appc.CT_ST_CHECKBOX
CT_ST_STYLIZED_WINDOW = Appc.CT_ST_STYLIZED_WINDOW
CT_ST_MISSION_LOG = Appc.CT_ST_MISSION_LOG
CT_ST_KEYBOARD_REMAPPING = Appc.CT_ST_KEYBOARD_REMAPPING
CT_ST_TILED_ICON = Appc.CT_ST_TILED_ICON
CT_CHANGE_RENDERED_SET_ACTION = Appc.CT_CHANGE_RENDERED_SET_ACTION
CT_SORTED_REGION_MENU = Appc.CT_SORTED_REGION_MENU
CT_ST_WARP_BUTTON = Appc.CT_ST_WARP_BUTTON
CT_WARP_SEQUENCE = Appc.CT_WARP_SEQUENCE
CT_SHIELDS_DISPLAY = Appc.CT_SHIELDS_DISPLAY
CT_DAMAGE_DISPLAY = Appc.CT_DAMAGE_DISPLAY
CT_DAMAGE_ICON = Appc.CT_DAMAGE_ICON
CT_WEAPONS_DISPLAY = Appc.CT_WEAPONS_DISPLAY
CT_RADAR_DISPLAY = Appc.CT_RADAR_DISPLAY
CT_RADAR_SCOPE = Appc.CT_RADAR_SCOPE
CT_RADAR_BLIP = Appc.CT_RADAR_BLIP
CT_TAC_WEAPONS_CTRL = Appc.CT_TAC_WEAPONS_CTRL
CT_ENG_POWER_CTRL = Appc.CT_ENG_POWER_CTRL
CT_ENG_POWER_DISPLAY = Appc.CT_ENG_POWER_DISPLAY
CT_ENG_REPAIR_PANE = Appc.CT_ENG_REPAIR_PANE
CT_RETICLE_MANAGER_WINDOW = Appc.CT_RETICLE_MANAGER_WINDOW
CT_RETICLE_WINDOW = Appc.CT_RETICLE_WINDOW
CT_PLAYER_RETICLE_WINDOW = Appc.CT_PLAYER_RETICLE_WINDOW
CT_NAMED_RETICLE_WINDOW = Appc.CT_NAMED_RETICLE_WINDOW
CT_TOP_WINDOW = Appc.CT_TOP_WINDOW
CT_MAIN_WINDOW = Appc.CT_MAIN_WINDOW
CT_BRIDGE_WINDOW = Appc.CT_BRIDGE_WINDOW
CT_TACTICAL_WINDOW = Appc.CT_TACTICAL_WINDOW
CT_TACTICAL_CONTROL_WINDOW = Appc.CT_TACTICAL_CONTROL_WINDOW
CT_CONSOLE_WINDOW = Appc.CT_CONSOLE_WINDOW
CT_OPTIONS_WINDOW = Appc.CT_OPTIONS_WINDOW
CT_SUBTITLE_WINDOW = Appc.CT_SUBTITLE_WINDOW
CT_MAP_MODE_WINDOW = Appc.CT_MAP_MODE_WINDOW
CT_CINEMATIC_WINDOW = Appc.CT_CINEMATIC_WINDOW
CT_GRAPHICS_MENU_MANAGER = Appc.CT_GRAPHICS_MENU_MANAGER
CT_CD_CHECK_WINDOW = Appc.CT_CD_CHECK_WINDOW
CT_CHARACTER_MENU_WINDOW = Appc.CT_CHARACTER_MENU_WINDOW
CT_MODAL_DIALOG_WINDOW = Appc.CT_MODAL_DIALOG_WINDOW
CT_SUBTITLE_ACTION = Appc.CT_SUBTITLE_ACTION
CT_SHIP_DISPLAY = Appc.CT_SHIP_DISPLAY
CT_VAR_MANAGER = Appc.CT_VAR_MANAGER
CT_SHIP_EVENT = Appc.CT_SHIP_EVENT
CT_WAYPOINT_EVENT = Appc.CT_WAYPOINT_EVENT
CT_SET_FLOAT_VAR_EVENT = Appc.CT_SET_FLOAT_VAR_EVENT
CT_EXIT_SET_EVENT = Appc.CT_EXIT_SET_EVENT
CT_SAY_LINE_EVENT = Appc.CT_SAY_LINE_EVENT
CT_COLLISION_EVENT = Appc.CT_COLLISION_EVENT
CT_PROXIMITY_CHECK = Appc.CT_PROXIMITY_CHECK
CT_PROXIMITY_EVENT = Appc.CT_PROXIMITY_EVENT
CT_WEAPON_HIT_EVENT = Appc.CT_WEAPON_HIT_EVENT
CT_START_FIRING_EVENT = Appc.CT_START_FIRING_EVENT
CT_OBJECT_EXPLODING_EVENT = Appc.CT_OBJECT_EXPLODING_EVENT
CT_WARP_EVENT = Appc.CT_WARP_EVENT
CT_SUBSYSTEM_PROPERTY = Appc.CT_SUBSYSTEM_PROPERTY
CT_POWERED_SUBSYSTEM_PROPERTY = Appc.CT_POWERED_SUBSYSTEM_PROPERTY
CT_POSITION_ORIENTATION_PROPERTY = Appc.CT_POSITION_ORIENTATION_PROPERTY
CT_SHIP_PROPERTY = Appc.CT_SHIP_PROPERTY
CT_WEAPON_SYSTEM_PROPERTY = Appc.CT_WEAPON_SYSTEM_PROPERTY
CT_WEAPON_PROPERTY = Appc.CT_WEAPON_PROPERTY
CT_ENERGY_WEAPON_PROPERTY = Appc.CT_ENERGY_WEAPON_PROPERTY
CT_PHASER_PROPERTY = Appc.CT_PHASER_PROPERTY
CT_TORPEDO_SYSTEM_PROPERTY = Appc.CT_TORPEDO_SYSTEM_PROPERTY
CT_TORPEDO_TUBE_PROPERTY = Appc.CT_TORPEDO_TUBE_PROPERTY
CT_PULSE_WEAPON_PROPERTY = Appc.CT_PULSE_WEAPON_PROPERTY
CT_TRACTOR_BEAM_PROPERTY = Appc.CT_TRACTOR_BEAM_PROPERTY
CT_SHIELD_PROPERTY = Appc.CT_SHIELD_PROPERTY
CT_HULL_PROPERTY = Appc.CT_HULL_PROPERTY
CT_SENSOR_PROPERTY = Appc.CT_SENSOR_PROPERTY
CT_CLOAKING_SUBSYSTEM_PROPERTY = Appc.CT_CLOAKING_SUBSYSTEM_PROPERTY
CT_WARP_ENGINE_PROPERTY = Appc.CT_WARP_ENGINE_PROPERTY
CT_IMPULSE_ENGINE_PROPERTY = Appc.CT_IMPULSE_ENGINE_PROPERTY
CT_ENGINE_PROPERTY = Appc.CT_ENGINE_PROPERTY
CT_POWER_PROPERTY = Appc.CT_POWER_PROPERTY
CT_REPAIR_SUBSYSTEM_PROPERTY = Appc.CT_REPAIR_SUBSYSTEM_PROPERTY
CT_ENGINE_GLOW_PROPERTY = Appc.CT_ENGINE_GLOW_PROPERTY
CT_EFFECT_EMITTER_PROPERTY = Appc.CT_EFFECT_EMITTER_PROPERTY
CT_SMOKE_EMITTER_PROPERTY = Appc.CT_SMOKE_EMITTER_PROPERTY
CT_SPARK_EMITTER_PROPERTY = Appc.CT_SPARK_EMITTER_PROPERTY
CT_EXPLODE_EMITTER_PROPERTY = Appc.CT_EXPLODE_EMITTER_PROPERTY
CT_BLINKING_LIGHT_PROPERTY = Appc.CT_BLINKING_LIGHT_PROPERTY
CT_OBJECT_EMITTER_PROPERTY = Appc.CT_OBJECT_EMITTER_PROPERTY
CT_CHAT_OBJECT = Appc.CT_CHAT_OBJECT
GENUS_UNKNOWN = Appc.GENUS_UNKNOWN
GENUS_SHIP = Appc.GENUS_SHIP
GENUS_STATION = Appc.GENUS_STATION
GENUS_ASTEROID = Appc.GENUS_ASTEROID
SPECIES_UNKNOWN = Appc.SPECIES_UNKNOWN
SPECIES_FEDERATION_START = Appc.SPECIES_FEDERATION_START
SPECIES_GALAXY = Appc.SPECIES_GALAXY
SPECIES_SOVEREIGN = Appc.SPECIES_SOVEREIGN
SPECIES_AKIRA = Appc.SPECIES_AKIRA
SPECIES_AMBASSADOR = Appc.SPECIES_AMBASSADOR
SPECIES_NEBULA = Appc.SPECIES_NEBULA
SPECIES_SHUTTLE = Appc.SPECIES_SHUTTLE
SPECIES_TRANSPORT = Appc.SPECIES_TRANSPORT
SPECIES_FREIGHTER = Appc.SPECIES_FREIGHTER
SPECIES_CARDASSIAN_START = Appc.SPECIES_CARDASSIAN_START
SPECIES_GALOR = Appc.SPECIES_GALOR
SPECIES_KELDON = Appc.SPECIES_KELDON
SPECIES_CARDFREIGHTER = Appc.SPECIES_CARDFREIGHTER
SPECIES_CARDHYBRID = Appc.SPECIES_CARDHYBRID
SPECIES_ROMULAN_START = Appc.SPECIES_ROMULAN_START
SPECIES_WARBIRD = Appc.SPECIES_WARBIRD
SPECIES_KLINGON_START = Appc.SPECIES_KLINGON_START
SPECIES_BIRD_OF_PREY = Appc.SPECIES_BIRD_OF_PREY
SPECIES_VORCHA = Appc.SPECIES_VORCHA
SPECIES_KESSOK_START = Appc.SPECIES_KESSOK_START
SPECIES_KESSOK_HEAVY = Appc.SPECIES_KESSOK_HEAVY
SPECIES_KESSOK_LIGHT = Appc.SPECIES_KESSOK_LIGHT
SPECIES_KESSOKMINE = Appc.SPECIES_KESSOKMINE
SPECIES_FERENGI_START = Appc.SPECIES_FERENGI_START
SPECIES_MARAUDER = Appc.SPECIES_MARAUDER
SPECIES_OTHER_START = Appc.SPECIES_OTHER_START
SPECIES_FED_STARBASE = Appc.SPECIES_FED_STARBASE
SPECIES_FED_OUTPOST = Appc.SPECIES_FED_OUTPOST
SPECIES_CARD_STARBASE = Appc.SPECIES_CARD_STARBASE
SPECIES_CARD_OUTPOST = Appc.SPECIES_CARD_OUTPOST
SPECIES_CARD_STATION = Appc.SPECIES_CARD_STATION
SPECIES_DRYDOCK = Appc.SPECIES_DRYDOCK
SPECIES_SPACE_FACILITY = Appc.SPECIES_SPACE_FACILITY
SPECIES_COMMARRAY = Appc.SPECIES_COMMARRAY
SPECIES_COMMLIGHT = Appc.SPECIES_COMMLIGHT
SPECIES_PROBE = Appc.SPECIES_PROBE
SPECIES_PROBETYPE2 = Appc.SPECIES_PROBETYPE2
SPECIES_ASTEROID = Appc.SPECIES_ASTEROID
SPECIES_SUNBUSTER = Appc.SPECIES_SUNBUSTER
SPECIES_ESCAPEPOD = Appc.SPECIES_ESCAPEPOD
SPECIES_BORG = Appc.SPECIES_BORG
TEAM_UNKNOWN = Appc.TEAM_UNKNOWN
TEAM_FEDERATION = Appc.TEAM_FEDERATION
TEAM_CARDASSIAN = Appc.TEAM_CARDASSIAN
TEAM_KLINGON = Appc.TEAM_KLINGON
TEAM_ROMULAN = Appc.TEAM_ROMULAN
TEAM_FERENGI = Appc.TEAM_FERENGI
TEAM_KESSOK = Appc.TEAM_KESSOK
TEAM_ALPHA = Appc.TEAM_ALPHA
TEAM_BETA = Appc.TEAM_BETA
TEAM_GAMMA = Appc.TEAM_GAMMA
TEAM_DELTA = Appc.TEAM_DELTA
CSP_MISSION_CRITICAL = Appc.CSP_MISSION_CRITICAL
CSP_NORMAL = Appc.CSP_NORMAL
CSP_SPONTANEOUS = Appc.CSP_SPONTANEOUS
TWO_PI = Appc.TWO_PI
PI = Appc.PI
HALF_PI = Appc.HALF_PI
FOURTH_PI = Appc.FOURTH_PI
AT_ONE = Appc.AT_ONE
AT_TWO = Appc.AT_TWO
AT_THREE = Appc.AT_THREE
AT_FOUR = Appc.AT_FOUR
AT_MAX_NUM_AMMO_TYPES = Appc.AT_MAX_NUM_AMMO_TYPES
g_bIsModelPropertyEditor = TGObjectPtr(Appc.globals.g_bIsModelPropertyEditor)
NiColor_WHITE = NiColorPtr(Appc.globals.NiColor_WHITE)
NiColor_BLACK = NiColorPtr(Appc.globals.NiColor_BLACK)
NiColorA_WHITE = NiColorAPtr(Appc.globals.NiColorA_WHITE)
NiColorA_BLACK = NiColorAPtr(Appc.globals.NiColorA_BLACK)
TGColorA_WHITE = NiColorAPtr(Appc.globals.TGColorA_WHITE)
TGColorA_BLACK = NiColorAPtr(Appc.globals.TGColorA_BLACK)
