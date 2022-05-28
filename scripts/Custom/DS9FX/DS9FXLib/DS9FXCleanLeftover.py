# Cleans leftover models which don't belong to some sets

import App
import MissionLib
import DS9FXSets

sVortex = "Vortex "
lBadlands = []
for i in range(0, 61):
        s = sVortex + str(i)
        lBadlands.append(s)
        
lWormhole =  ["Bajoran Wormhole", "Bajoran Wormhole Navpoint"]
        
lDS9 = ["Deep_Space_9", "Comet Alpha", "Attacker 1", "Attacker 2", "Attacker 3", "Attacker 4", "Attacker 5", 
        "USS Excalibur", "USS Defiant", "USS Oregon", "USS_Lakota", "Verde", "Guadiana", "Lankin", 
        "Maroni", "Kuban", "Paraguay", "Tigris"]

lFounderHomeworld = ["Dreadnought", "Bugship 1", "Bugship 2", "Bugship 3", "Bugship Patrol 1", "Bugship Patrol 2", "Bugship Patrol 3", "Bugship Patrol 4", 
                     "Bugship Patrol 5", "Bugship Patrol 6", "Bugship Patrol 7", "Bugship Patrol 8", "Bugship Patrol 9", "Bugship Patrol 10", "Bugship Patrol 11"]

lKaremma = ["Dreadnought 1", "Dreadnought 2"]

lKurill = ["Bugship 1", "Bugship 2", "Bugship 3", "Bugship 4", "Dreadnought"]

lNewBajor = ["USS Majestic", "USS Bonchune"]

lGamma = ["Bugship 1", "Bugship 2", "Bugship 3"]

lQonos = ["IKS K'mpec", "IKS Amar", "IKS Ki'Tang"]

lCardassia = ["Hutet 1", "Keldon 1", "Keldon 2", "Galor 1", "Galor 2"]

def Clean():
        pSequence = App.TGSequence_Create()
        pAction = App.TGScriptAction_Create(__name__, "CleanDelay")
        pSequence.AddAction(pAction, None, 3)
        pSequence.Play()       

def CleanDelay(pAction):
        pPlayer = MissionLib.GetPlayer()
        if not pPlayer:
                return 0

        pSet = pPlayer.GetContainingSet()
        if not pSet:
                return 0

        pName = pSet.GetName()
        if not pName:
                return 0

        if pName == "DeepSpace91":
                for s in lBadlands:
                        pSet.DeleteObjectFromSet(s)

                for s in lFounderHomeworld:
                        pSet.DeleteObjectFromSet(s)
                                             
                for s in lKaremma:
                        pSet.DeleteObjectFromSet(s)
                
                for s in lKurill:
                        pSet.DeleteObjectFromSet(s)   

                for s in lNewBajor:
                        pSet.DeleteObjectFromSet(s)
                        
                for s in lGamma:
                        pSet.DeleteObjectFromSet(s)
                        
                for s in lQonos:
                        pSet.DeleteObjectFromSet(s)  

                for s in lCardassia:
                        pSet.DeleteObjectFromSet(s)                 
                         
        elif pName == "DS9FXBadlands1":
                for s in lDS9:
                        pSet.DeleteObjectFromSet(s)

                for s in lFounderHomeworld:
                        pSet.DeleteObjectFromSet(s)
                                             
                for s in lKaremma:
                        pSet.DeleteObjectFromSet(s)
                
                for s in lKurill:
                        pSet.DeleteObjectFromSet(s)   

                for s in lNewBajor:
                        pSet.DeleteObjectFromSet(s)
                        
                for s in lGamma:
                        pSet.DeleteObjectFromSet(s)
                        
                for s in lWormhole:
                        pSet.DeleteObjectFromSet(s)  
                        
                for s in lQonos:
                        pSet.DeleteObjectFromSet(s)  
                        
                for s in lCardassia:
                        pSet.DeleteObjectFromSet(s)                         
        
        elif pName == "DS9FXFoundersHomeworld1":
                for s in lBadlands:
                        pSet.DeleteObjectFromSet(s)

                for s in lDS9:
                        pSet.DeleteObjectFromSet(s)
                                             
                for s in lKaremma:
                        pSet.DeleteObjectFromSet(s)

                for s in lNewBajor:
                        pSet.DeleteObjectFromSet(s)
                
                for s in lWormhole:
                        pSet.DeleteObjectFromSet(s)  
                        
                for s in lQonos:
                        pSet.DeleteObjectFromSet(s)                            
        
                pSet.DeleteObjectFromSet("Bugship 4")
                
                for s in lCardassia:
                        pSet.DeleteObjectFromSet(s)                 
                
        elif pName == "DS9FXKaremma1":
                for s in lBadlands:
                        pSet.DeleteObjectFromSet(s)

                for s in lDS9:
                        pSet.DeleteObjectFromSet(s)

                for s in lFounderHomeworld:
                        pSet.DeleteObjectFromSet(s)
                                                             
                for s in lKurill:
                        pSet.DeleteObjectFromSet(s)   

                for s in lNewBajor:
                        pSet.DeleteObjectFromSet(s)
                        
                for s in lGamma:
                        pSet.DeleteObjectFromSet(s)
                        
                for s in lWormhole:
                        pSet.DeleteObjectFromSet(s) 
                        
                for s in lQonos:
                        pSet.DeleteObjectFromSet(s)  
                        
                for s in lCardassia:
                        pSet.DeleteObjectFromSet(s)                         
        
        elif pName == "DS9FXKurill1":
                for s in lBadlands:
                        pSet.DeleteObjectFromSet(s)

                for s in lDS9:
                        pSet.DeleteObjectFromSet(s)
                                             
                for s in lKaremma:
                        pSet.DeleteObjectFromSet(s)
                
                for s in lNewBajor:
                        pSet.DeleteObjectFromSet(s)
                                                
                for s in lWormhole:
                        pSet.DeleteObjectFromSet(s)
                        
                lConflict = lFounderHomeworld[:]
                for s in lKurill:
                        try:
                                lConflict.remove(s)
                        except:
                                pass
                for s in lConflict:
                        pSet.DeleteObjectFromSet(s)  
                        
                for s in lQonos:
                        pSet.DeleteObjectFromSet(s)   
                        
                for s in lCardassia:
                        pSet.DeleteObjectFromSet(s)                         
                        
        elif pName == "DS9FXNewBajor1":
                for s in lBadlands:
                        pSet.DeleteObjectFromSet(s)

                for s in lDS9:
                        pSet.DeleteObjectFromSet(s)

                for s in lFounderHomeworld:
                        pSet.DeleteObjectFromSet(s)
                                             
                for s in lKaremma:
                        pSet.DeleteObjectFromSet(s)
                
                for s in lKurill:
                        pSet.DeleteObjectFromSet(s)   
                        
                for s in lGamma:
                        pSet.DeleteObjectFromSet(s)
                        
                for s in lWormhole:
                        pSet.DeleteObjectFromSet(s)  
                        
                for s in lQonos:
                        pSet.DeleteObjectFromSet(s)  
                        
                for s in lCardassia:
                        pSet.DeleteObjectFromSet(s)                         
        
        elif pName == "GammaQuadrant1":
                for s in lBadlands:
                        pSet.DeleteObjectFromSet(s)

                for s in lDS9:
                        pSet.DeleteObjectFromSet(s)
                                             
                for s in lKaremma:
                        pSet.DeleteObjectFromSet(s)
                
                for s in lNewBajor:
                        pSet.DeleteObjectFromSet(s)
                                                
                pSet.DeleteObjectFromSet("Bugship 4")
                
                lConflict = lFounderHomeworld[:]
                for s in lGamma:
                        try:
                                lConflict.remove(s)
                        except:
                                pass
                for s in lConflict:
                        pSet.DeleteObjectFromSet(s)  
                        
                for s in lQonos:
                        pSet.DeleteObjectFromSet(s) 
                        
                for s in lCardassia:
                        pSet.DeleteObjectFromSet(s)                         
                        
        elif pName == "DS9FXQonos1":
                for s in lBadlands:
                        pSet.DeleteObjectFromSet(s)

                for s in lDS9:
                        pSet.DeleteObjectFromSet(s)

                for s in lFounderHomeworld:
                        pSet.DeleteObjectFromSet(s)
                                             
                for s in lKaremma:
                        pSet.DeleteObjectFromSet(s)
                
                for s in lKurill:
                        pSet.DeleteObjectFromSet(s)   

                for s in lNewBajor:
                        pSet.DeleteObjectFromSet(s)
                        
                for s in lGamma:
                        pSet.DeleteObjectFromSet(s)
                        
                for s in lWormhole:
                        pSet.DeleteObjectFromSet(s) 
                        
                for s in lCardassia:
                        pSet.DeleteObjectFromSet(s) 
                        
        elif pName == "DS9FXCardassia1":
                for s in lBadlands:
                        pSet.DeleteObjectFromSet(s)

                for s in lDS9:
                        pSet.DeleteObjectFromSet(s)

                for s in lFounderHomeworld:
                        pSet.DeleteObjectFromSet(s)
                                             
                for s in lKaremma:
                        pSet.DeleteObjectFromSet(s)
                
                for s in lKurill:
                        pSet.DeleteObjectFromSet(s)   

                for s in lNewBajor:
                        pSet.DeleteObjectFromSet(s)
                        
                for s in lGamma:
                        pSet.DeleteObjectFromSet(s)
                        
                for s in lWormhole:
                        pSet.DeleteObjectFromSet(s)  
                        
                for s in lQonos:
                        pSet.DeleteObjectFromSet(s)   
                                       
        else:
                for s in lBadlands:
                        pSet.DeleteObjectFromSet(s)

                for s in lDS9:
                        pSet.DeleteObjectFromSet(s)

                for s in lFounderHomeworld:
                        pSet.DeleteObjectFromSet(s)
                                             
                for s in lKaremma:
                        pSet.DeleteObjectFromSet(s)
                
                for s in lKurill:
                        pSet.DeleteObjectFromSet(s)   

                for s in lNewBajor:
                        pSet.DeleteObjectFromSet(s)
                        
                for s in lGamma:
                        pSet.DeleteObjectFromSet(s)
                        
                for s in lWormhole:
                        pSet.DeleteObjectFromSet(s)  
                        
                for s in lQonos:
                        pSet.DeleteObjectFromSet(s)   
                        
                for s in lCardassia:
                        pSet.DeleteObjectFromSet(s)

        return 0