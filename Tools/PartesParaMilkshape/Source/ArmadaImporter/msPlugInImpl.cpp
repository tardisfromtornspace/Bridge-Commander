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

#define MAX_SOD_LIGHTING_MATERIALS 100
#define MAX_VERTICES_PER_OBJECT 64000
#define MAX_NODES 300

bool ass_file_exists(char * filename);
void calculate_normal(float ax, float ay, float az, float bx, float by, float bz, float cx, float cy, float cz, float *nx, float *ny, float *nz);

#define SCALE 0.388

#define UINT8 unsigned char
#define UINT16 unsigned short

class sod_lighting_material
{
public:
   char identifier[30];
   float ambient[4],diffuse[4],specular[4];
	float specular_exponent;
	UINT8 lighting_model;

   sod_lighting_material()
   {
		ambient[3]=1;
		diffuse[3]=1;
		specular[3]=1;
		specular_exponent=1;
   }
};

class sod_node
{
public:
	char name[30];
	ass_matrix matrix;
};

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
    strcpy (szTitle, "Star Trek Armada (SOD)...");
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
	  fclose(temp);
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

// Make us an error message
void errorMessage(char * message);
void errorMessage(char * message)
{
    MessageBox (NULL,message,NULL,MB_OK);
}

bool validate(char * filename, int size)
{
	char searchstring[20000];
	strcpy(searchstring,"33450 Bbase.SOD-21947 Bbattle.SOD-2707 Bbee.SOD-173 Bcolect1.SOD-173 Bcolect2.SOD-173 Bcolect3.SOD-35156 Bconst.SOD-13946 Bcruise1.SOD-13251 Bcruise2.SOD-25322 Bdestroy.SOD-33503 Bfreight.SOD-25252 Bmining.SOD-37998 Bomega.SOD-12872 Borpod1.SOD-1193 Borpod10.SOD-12525 Borpod2.SOD-1502 Borpod3.SOD-1551 Borpod4.SOD-1580 Borpod5.SOD-11051 Borpod6.SOD-1217 Borpod7.SOD-1174 Borpod8.SOD-1730 Borpod9.SOD-14748 Bresear.SOD-22119 Bresear2.SOD-12726 Bscout.SOD-14191 Bsensor.SOD-36540 Bspecial.SOD-15354 Bsuperbl.SOD-3896 Bturret.SOD-14948 Bturret2.SOD-23021 Byard.SOD-8176 Byard2.SOD-516 Default.SOD-1898 dlight.SOD-29269 Favenger.SOD-36844 Fbase.sod-21477 FbaseHQ.SOD-46520 Fbattle.sod-4718 Fbee.SOD-43769 fconst.sod-35785 Fcruise1.sod-34257 Fcruise2.sod-31072 Fdestroy.SOD-13460 Fedpod1.SOD-3148 Fedpod10.SOD-6479 Fedpod2.SOD-3135 Fedpod3.SOD-691 Fedpod4.SOD-3379 Fedpod5.SOD-17790 Fedpod6.SOD-7398 Fedpod7.SOD-7780 Fedpod8.SOD-4616 Fedpod9.SOD-32066 Fentd.SOD-44683 Fente.SOD-35186 Ffreight.sod-32010 Fgalaxy.SOD-57343 Fmining.sod-124771 font.sod-32042 Fprem.sod-28396 FpremNew.SOD-45674 Fresear.sod-33937 Fresear2.SOD-15510 Fscout.sod-12229 Fsensor.sod-35361 Fspecial.SOD-32462 Fsuperbl.SOD-7208 Fturret.sod-6269 Fturret2.sod-21372 Fyard.sod-31799 Fyard2.sod-39070 Kbase.SOD-33908 Kbattle.SOD-2890 Kbee.SOD-76358 kconst.SOD-");
	strcat(searchstring,"35005 Kcruise1.SOD-40883 Kcruise2.SOD-29553 Kdestroy.sod-39600 Kfreight.SOD-1871 Klipod1.SOD-5604 Klipod10.SOD-1648 Klipod2.SOD-1868 Klipod3.SOD-730 Klipod4.SOD-1575 Klipod5.SOD-1063 Klipod6.SOD-5151 Klipod7.SOD-2535 Klipod8.SOD-1648 Klipod9.SOD-59526 Kmining.SOD-21042 Kresear.SOD-26574 Kresear2.SOD-34437 Kscout.SOD-96240 Ksensor.SOD-38281 Kspecial.SOD-34203 Ksuper.SOD-32034 Ksuperbl.SOD-4612 Kturret.SOD-4799 Kturret2.SOD-44960 Kyard.SOD-22929 Kyard2.SOD-2378 Master.SOD-1988 Master1.SOD-2393 Master2.SOD-2489 Master3.SOD-2107 Master4.SOD-2516 Master5.SOD-2292 Master6.SOD-2483 Master7.SOD-2378 Master8.SOD-25610 Material.SOD-29442 Mbaku.SOD-28284 MBarisa.SOD-8621 Mbg01.SOD-1657 Mbg02.SOD-1693 MbgBaku.SOD-482 MbgBlack.SOD-1657 MbgBlue.SOD-1693 MbgBorg.SOD-10301 MbgCard.SOD-1693 MbgDom1.SOD-10301 MbgDom2.SOD-10701 MbgEarth.SOD-11024 MbgGlxy.SOD-10301 MbgIkol.SOD-10319 MbgKlin2.SOD-10319 MbgKlin3.SOD-10335 MbgKlin4.SOD-1711 MbgKling.SOD-10319 MbgOmega.SOD-10301 MbgRom1.SOD-10301 MbgRom2.SOD-10301 MbgRom3.SOD-9084 MbgStars.SOD-17498 MbgX.SOD-26404 Mblackh.SOD-28559 Mborgpl.SOD-19521 Mcomet.SOD-12055 Mdmoon.SOD-12055 Mdmoon2.SOD-12055 Mdmoon3.SOD-28283 Mearth.SOD-28728 Mearthbg.SOD-6432 Mearthmn.SOD-28268 MEridon.SOD-5318 Mgalaxy.SOD-302 Mgate.SOD-27609 MKrios.SOD-28284 MLankal.SOD-173 MLblustr.SOD-173 MLpurstr.SOD-161 Mmoon.SOD-12166 Mmooninf.SOD-994 Mnebula1.sod-1711 Mnebula2.sod-800 Mnebula3.sod-1264 Mnebula4.sod-678 Mnebula5.sod-9463 Momega.SOD-6698 Mplanet.SOD-4927 Mplasma.SOD-28283 MQonos.SOD-28283 MRemus.SOD-28285 MRomulus.SOD-173 MSblustr.SOD-173 MSorastr.SOD-173 MSpurstr.SOD-170 MSredstr.SOD-14276 Mstars.SOD-161 Msun1.SOD-");
	strcat(searchstring,"161 Msun2.SOD-161 Msun3.SOD-60312 Mwormh.SOD-32360 Mwreck.SOD-37149 Rbase.SOD-35771 Rbattle.SOD-4113 Rbee.SOD-33296 Rconst.SOD-29933 Rcruise1.SOD-25946 Rcruise2.SOD-31716 Rdestroy.SOD-40053 Rfreight.SOD-80422 Rmining.SOD-24903 Romega.SOD-34223 RomegaOn.SOD-1657 Rompod1.SOD-1634 Rompod10.SOD-1668 Rompod2.SOD-6057 Rompod3.SOD-1630 Rompod4.SOD-1112 Rompod5.SOD-1386 Rompod6.SOD-3599 Rompod7.SOD-8509 Rompod8.SOD-1994 Rompod9.SOD-29789 Rresear.SOD-34334 Rresear2.SOD-26225 Rscout.SOD-23687 Rsensor.SOD-30630 Rspecial.SOD-41812 Rsuper.SOD-55523 Rsuperbl.SOD-7122 Rturret.SOD-6857 Rturret2.SOD-47605 Ryard.SOD-42558 Ryard2.SOD-103445 stalogo.SOD-103374 stalogoSW.SOD-1655 Wantmine.SOD-10600 Wbassim.SOD-22207 wbholegen.SOD-3456 Wborgate.SOD-11350 Wborgbor.SOD-3893 Wcobdet.SOD-6722 Wcorbrfr.SOD-2313 Wgravmin.SOD-2208 Whobber.SOD-11176 Wholdbm.SOD-14291 Wionstrm.SOD-1045 Wklincom.SOD-21135 Wmanhiem.SOD-4077 Wmastran.SOD-11132 Wmbeam.SOD-94 Wmicremit.SOD-2946 Wmicrorg.SOD-1698 Wmyotron.SOD-2603 Wnanites.SOD-614 Wotractr.SOD-94 Wovremit.SOD-5519 Wprobe.SOD-5277 Wrift.SOD-9654 Wshldadd.SOD-3993 Wshldinv.SOD-784 Wshldisr.SOD-6716 Wshldmod.SOD-9593 Wshldrmd.SOD-6267 Wshldsub.SOD-4857 Wstoptim.SOD-437 Wtetrion.SOD-610 Wtractor.SOD-4319 Wtranwrp.SOD-3079 Wuitrbal.SOD-1462 Wuitrbm.SOD-5052 Wviracod.SOD-21226 Xmanheim.SOD-1038 Xplode.sod-5448 Xprmgate.SOD-21135 Xshlddie.SOD-15916 Xshldx01.SOD-16193 Zbreen.SOD-");
	strcat(searchstring,"24030 Zcardbat.SOD-21131 Zcarddes.SOD-37685 Zclonfac.SOD-80449 Zentity.SOD-20500 Zferengi.SOD-24505 Zjembat.SOD-28957 Zjemdest.SOD-43260 Zjemyard.SOD-13134 Zkahless.SOD-80642 Zmama.SOD-33708 Zneubase.SOD-22207 Zomega.SOD-20599 Zsonbat.SOD-24457 Zsondest.SOD-81415 8472_BasicResearch.SOD-65994 8472_AdvancedResearch.SOD-48744 8472_mother.SOD-44818 8472_collector.sod-37396 8472_HeroMother.SOD-27871 8472_frigate.SOD-25745 8472_passive.SOD-25693 8472Bee.SOD-25614 8472_battle.SOD-23310 8472_ShipUpgradeResearch.SOD-21666 8472_cruise1.SOD-21398 8472_behemoth.SOD-21243 8472_destroy.SOD-20574 8472_transmuter.sod-20386 8472_defender.SOD-20149 8472_active.SOD-18044 8472_scout.SOD-18026 8472_cocoon.SOD-17734 8472_cruise2.SOD-14098 8472_FluidicGate.SOD-7488 8472_Sentinel.SOD-5592 8472_Mine.SOD-4994 8472_PodBasic2.SOD-4994 8472_PodBasic4.SOD-4994 8472_PodBasic0.SOD-4994 8472_PodBasic1.SOD-4994 8472_PodBasic3.SOD-2331 8472_PodShipResearch1.SOD-2331 8472_PodShipResearch2.SOD-2331 8472_PodShipResearch22.SOD-2331 8472_PodShipResearch21.SOD-2331 8472_PodShipResearch24.SOD-2331 8472_PodShipResearch23.SOD-2331 8472_PodShipResearch3.SOD-2331 8472_PodShipResearch0.SOD-2331 8472_PodShipResearch4.SOD-1591 8472_PodAdvanced1.SOD-1591 8472_PodAdvanced3.SOD-1591 8472_PodAdvanced2.SOD-1591 8472_PodAdvanced0.SOD-35782 bassault.SOD-59937 Bbase.SOD-50190 bbattle4.SOD-47596 bbattle3.SOD-17915 bbattle2.SOD-14065 bbattle1.SOD-3722 Bbee.SOD-104689 bcolony.SOD-173 Bcolect3.SOD-173 Bcolect1.SOD-173 Bcolect2.SOD-53208 Bconst.SOD-40602 Bcruise3.SOD-15025 Bcruise1.SOD-9222 Bcruise2.SOD-10033 Bdestroy.SOD-39298 Bfreight.SOD-127485 bfrigate.SOD-");
	strcat(searchstring,"13455 bhub.SOD-11844 bmama.SOD-62741 Bmining.SOD-37998 Bomega.SOD-124370 borg_portal_effect.sod-29184 Borpod16.SOD-12872 Borpod1.SOD-12525 Borpod2.SOD-8180 Borpod6.SOD-6412 Borpod3.SOD-2718 Borpod9.SOD-1580 Borpod5.SOD-1551 Borpod4.SOD-1288 borpod15.SOD-1288 borpod11.SOD-1288 borpod13.SOD-1288 borpod21.SOD-1288 borpod23.SOD-1288 borpod25.SOD-1256 borpod22.SOD-1256 Borpod10.SOD-1256 borpod14.SOD-1256 borpod24.SOD-1256 borpod12.SOD-1217 Borpod7.SOD-1174 Borpod8.SOD-202731 bportal.SOD-42152 Bqueen.SOD-19616 brecycle.SOD-41150 Bresear.SOD-40271 Bresear2.SOD-15696 Bscout.SOD-60727 Bsensor.SOD-42152 Bspecial.SOD-15354 Bsuperbl.SOD-16623 btechass.SOD-42837 Bturret2.SOD-19654 Bturret.SOD-188538 bupgrade.SOD-126553 Byard2.SOD-45637 Byard.SOD-47368 cardassian_super_station.sod-24541 carpod16.SOD-4635 carpod1.SOD-3360 carpod5.SOD-2979 carpod6.SOD-2945 carpod2.SOD-2633 carpod3.SOD-2628 carpod9.SOD-2530 carpod7.SOD-2432 carpod8.SOD-2179 carpod4.SOD-1129 carpod22.SOD-1129 carpod14.SOD-1129 carpod13.SOD-1129 carpod15.SOD-1129 carpod12.SOD-1129 carpod25.SOD-1129 carpod24.SOD-1129 carpod23.SOD-1129 carpod11.SOD-1129 carpod21.SOD-1129 carpod10.SOD-14435 cassault.SOD-49072 cbase.SOD-26871 cbattle2.SOD-23922 cbattle.SOD-2441 cbee.SOD-20939 ccargo.SOD-13240 ccolony.SOD-2153 CcolonyPod.SOD-19688 cconst.SOD-27289 ccruise1.SOD-13944 ccruise3.SOD-12138 ccruise2.SOD-14255 cdestroy2.SOD-12840 cdestroy.SOD-11278 cfreight.sod-15513 cfrigate.SOD-16758 ckentar.SOD-23149 cmining.sod-23514 corbital.sod-15772 cquantum.SOD-61546 cresear.SOD-27706 cresear2.SOD-10198 cscout.SOD-16614 csensor.SOD-29541 cspecial.SOD-25380 csrepair.SOD-6572 csuper.SOD-");
	strcat(searchstring,"37898 ctrading.sod-30988 cturret2.SOD-26840 cturret.SOD-41240 cupgrade.SOD-60974 cyard.SOD-51205 cyard2.SOD-516 Default.SOD-1898 dlight.SOD-1662 drones.SOD-4318 dummy.sod-25137 fassault.SOD-28146 Fbase.sod-21477 FbaseHQ.SOD-34046 Fbattle.sod-13748 fbbridge.SOD-4718 Fbee.SOD-19183 fcargo.sod-22936 fcolony.SOD-2159 FcolonyPod.SOD-43769 fconst.sod-26126 Fcruise3.SOD-24610 Fcruise1.sod-18274 Fcruise2.sod-34596 fdata.SOD-22897 Fdestroy.SOD-17990 Fdestroy2.SOD-51132 fedpod16.SOD-17790 Fedpod6.SOD-13460 Fedpod1.SOD-7780 Fedpod8.SOD-7398 Fedpod7.SOD-6479 Fedpod2.SOD-4616 Fedpod9.SOD-3379 Fedpod5.SOD-3135 Fedpod3.SOD-2169 Fedpod10.SOD-1118 Fedpod14.SOD-1118 Fedpod24.SOD-1118 Fedpod25.SOD-1118 Fedpod13.SOD-1118 Fedpod15.SOD-1118 Fedpod11.SOD-1118 Fedpod23.SOD-1118 Fedpod21.SOD-1118 Fedpod22.SOD-1118 Fedpod12.SOD-691 Fedpod4.SOD-34020 Fente.SOD-35186 Ffreight.sod-22431 ffrigate.sod-22430 Fgalaxy.SOD-32247 fincursion.sod-124428 fluidicrift.SOD-124428 Fluidicrift2.SOD-978 fluidicnebula.SOD-57343 Fmining.sod-124771 font.sod-27806 forbital.sod-32042 Fprem.sod-45679 Fresear.sod-33937 Fresear2.SOD-12416 fsaucer.SOD-13786 Fscout.sod-11414 Fsensor.sod-29242 Fspecial.SOD-20965 fsrepair.sod-32462 Fsuperbl.SOD-35674 ftrading.sod-16425 ftransco.SOD-6436 Fturret.sod-5990 Fturret2.sod-43408 fupgrade.sod-31799 Fyard2.sod-21372 Fyard.sod-14472 Kassault.SOD-28034 Kbase.SOD-36793 Kbattle2.SOD-");
	strcat(searchstring,"33984 Kbattle.SOD-2890 Kbee.SOD-24400 Kbekta.SOD-13812 Kcargo.SOD-25167 kcolony.SOD-1347 KcolonyPod.SOD-76358 kconst.SOD-42953 Kcruise2.SOD-30040 Kcruise1.SOD-27364 Kcruise3.SOD-27975 Kdestroy.sod-39600 Kfreight.SOD-28348 Kfrigate.SOD-5151 Klipod7.SOD-3053 Klipod5.SOD-2909 Klipod16.SOD-2535 Klipod8.SOD-2337 klipod21.SOD-2337 klipod22.SOD-2337 klipod11.SOD-2337 klipod24.SOD-2337 klipod15.SOD-2337 klipod14.SOD-2337 klipod13.SOD-2337 klipod12.SOD-2337 klipod23.SOD-2337 Klipod10.SOD-2337 klipod25.SOD-1871 Klipod1.SOD-1868 Klipod3.SOD-1648 Klipod2.SOD-1648 Klipod9.SOD-1063 Klipod6.SOD-730 Klipod4.SOD-59526 Kmining.SOD-35170 korbital.sod-26574 Kresear2.SOD-11888 Kresear.SOD-26613 Kscout.SOD-43748 Ksensor.SOD-33985 Kspecial.SOD-14915 Ksrepair.SOD-35371 Ksuper.SOD-32034 Ksuperbl.SOD-39093 ktrading.sod-4866 Kturret2.SOD-4061 Kturret.SOD-22101 Kupgrade.SOD-44960 Kyard.SOD-22929 Kyard2.SOD-1304 latinum.SOD-1784 logo.SOD-3054 Master6.SOD-2378 Master.SOD-2198 Master7.SOD-2023 Master3.SOD-2006 Master8.SOD-1694 Master5.SOD-1303 Master4.SOD-1303 Master1.SOD-1287 Master2.SOD-25610 Material.SOD-8621 Mbg01.SOD-1128 Mbg02.SOD-1693 MbgBorg.SOD-1693 MbgBaku.SOD-1128 MbgBlue.SOD-1693 MbgDom1.SOD-1711 MbgKling.SOD-17498 MbgX.SOD-26404 Mblackh.SOD-19521 Mcomet.SOD-12055 Mdmoon2.SOD-12055 Mdmoon3.SOD-12055 Mdmoon.SOD-6432 Mearthmn.SOD-5318 Mgalaxy.SOD-302 Mgate.SOD-");
	strcat(searchstring,"1680 microorganism.SOD-173 MLblustr.SOD-173 MLpurstr.SOD-12166 Mmooninf.SOD-1801 Mnebula7.sod-1711 Mnebula2.sod-1354 Mnebula9.sod-1264 Mnebula4.sod-1076 Mnebula12.sod-1066 Mnebula6.sod-994 Mnebula1.sod-854 Mnebula8.sod-800 Mnebula3.sod-702 Mnebula11.sod-702 Mnebula10.sod-678 Mnebula5.sod-9463 Momega.SOD-6698 Mplanet.SOD-4927 Mplasma.SOD-173 MSblustr.SOD-173 MSorastr.SOD-173 MSpurstr.SOD-170 MSredstr.SOD-14276 Mstars.SOD-161 Msun2.SOD-161 Msun3.SOD-161 Msun1.SOD-60312 Mwormh.SOD-32360 Mwreck.SOD-8839 PB_CLSSD.SOD-7497 PB_CLSSM.sod-7487 PB_CLSSL.sod-7431 PB_CLSSH.sod-7431 PB_CLSSJ.sod-7423 PB_CLSSK.sod-168 psionicdisruption.SOD-89040 quantumsingularity.sod-22651 Rassault.SOD-37149 Rbase.SOD-29503 Rbattle.SOD-22556 Rbattle2.SOD-4113 Rbee.SOD-12893 Rcargo.SOD-14700 Rcolony.SOD-1677 RcolonyPod.SOD-33296 Rconst.SOD-26977 Rcruise1.SOD-15508 Rcruise2.SOD-14552 Rcruise3.SOD-");
	strcat(searchstring,"24430 Rdestroy.SOD-40053 Rfreight.SOD-21280 Rfrigate.SOD-80422 Rmining.SOD-12347 RomPod16.SOD-8509 Rompod8.SOD-6057 Rompod3.SOD-3599 Rompod7.SOD-1994 Rompod9.SOD-1668 Rompod2.SOD-1657 Rompod1.SOD-1630 Rompod4.SOD-1386 Rompod6.SOD-1112 Rompod5.SOD-668 Rompod10.SOD-667 ROMpod13.SOD-667 ROMpod15.SOD-667 ROMpod11.SOD-667 ROMpod12.SOD-667 ROMpod14.SOD-667 ROMpod25.SOD-667 ROMpod21.SOD-667 ROMpod22.SOD-667 ROMpod23.SOD-667 ROMpod24.SOD-35849 Rorbital.SOD-39889 Rresear.SOD-34334 Rresear2.SOD-23293 Rscout.SOD-14471 Rsensor.SOD-24311 Rspecial.SOD-23404 Rsrepair.SOD-41812 Rsuper.SOD-41450 Rsuperbl.SOD-91409 Rtrading.SOD-8157 Rturret.SOD-7655 Rturret2.SOD-24750 Rupgrade.SOD-47605 Ryard.SOD-42558 Ryard2.SOD-5982 select.sod-1655 Wantmine.SOD-10600 Wbassim.SOD-22207 wbholegen.SOD-11350 Wborgbor.SOD-3456 Wborgate.SOD-3893 Wcobdet.SOD-1045 wColPod.SOD-6722 Wcorbrfr.SOD-27193 WEclairlink1.SOD-");
	strcat(searchstring,"10180 wfluxwave.SOD-2313 Wgravmin.SOD-2208 Whobber.SOD-11176 Wholdbm.SOD-14291 Wionstrm.SOD-1400 Wklincom.SOD-21135 Wmanhiem.SOD-4077 Wmastran.SOD-11132 Wmbeam.SOD-2946 Wmicror2.SOD-2946 Wmicrorg.SOD-94 Wmicremit.SOD-94 Wmicremi2.SOD-11176 wMineLatinum.SOD-11176 wMinePlanet.SOD-1698 Wmyotron.SOD-2603 Wnanites.SOD-36827 wOrbitalBeam.SOD-614 Wotractr.SOD-94 Wovremit.SOD-5519 Wprobe.SOD-1483 wREBeam.SOD-36090 wRepairOther.SOD-5277 Wrift.SOD-9654 Wshldadd.SOD-9593 Wshldrmd.SOD-6716 Wshldmod.SOD-6267 Wshldsub.SOD-3993 Wshldinv.SOD-1472 wShldDis.SOD-784 Wshldisr.SOD-4857 Wstoptim.SOD-37133 wtechassimbm.SOD-437 Wtetrion.SOD-4319 Wtranwrp.SOD-610 Wtractor.SOD-3079 Wuitrbal.SOD-1462 Wuitrbm.SOD-5052 Wviracod.SOD-21226 Xmanheim.SOD-1038 Xplode.sod-5448 Xprmgate.SOD-21135 Xshlddie.SOD-15916 Xshldx01.SOD-20500 Zferengi.SOD-11477 Zfercarg.SOD-6406 ZFlag.SOD-33708 Zneubase.SOD-22207 Zomega.SOD-");
	_strlwr(searchstring);
	char substring[100];
	sprintf(substring,"%d %s-",size,filename);
	_strlwr(substring);

	if (strstr(searchstring,substring)!=NULL) return true;

	return false;
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
    char szDefExt[32] = "sod";
    char szFilter[128] = "SOD Files (*.sod)\0*.sod\0All Files (*.*)\0*.*\0\0";
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
    ofn.lpstrTitle = "Import Armada SOD -- assimsoft.com";

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

	// Are we allowed to do this
#ifdef LOCKED
	struct _stat buf;
	int result = _stat( szFile, &buf );
	int filesize=buf.st_size;
	if (!validate(szFile+strlen(filepath),filesize))
	{
		errorMessage("This importer may only be used on stock models");
		return 0;
	}
#endif

	// Initialise some variables
   int junk;
	UINT8 temp;
   sod_lighting_material * lighting_material[MAX_SOD_LIGHTING_MATERIALS];
   sod_node * nodes[MAX_NODES];
   int no_lighting_materials=0;

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
         char rubbish_bin[30];
		   length=0;
		   ass_fread((void *)&length,sizeof(UINT16),1,&myfile);
		   ass_fread(&rubbish_bin,length,1,&myfile);
		   length=0;
		   ass_fread((void *)&length,sizeof(UINT16),1,&myfile);
		   ass_fread(&rubbish_bin,length,1,&myfile);

         // Junk
         ass_fread(&junk,sizeof(float),1,&myfile);
         ass_fread(&junk,3,1,&myfile);
      }
   }

   // Load lighting information
	ass_fread((void *)&count,sizeof(UINT16),1,&myfile);
	for (counter=0;counter<count;counter++)
	{
      lighting_material[no_lighting_materials]=new sod_lighting_material();

      // Name
		length=0;
		ass_fread((void *)&length,sizeof(UINT16),1,&myfile);
		ass_fread(&lighting_material[no_lighting_materials]->identifier,length,1,&myfile);
      lighting_material[no_lighting_materials]->identifier[length]='\0';

      // Useful lighting stuff
		ass_fread(lighting_material[no_lighting_materials]->ambient,sizeof(float)*3,1,&myfile);
		ass_fread(lighting_material[no_lighting_materials]->diffuse,sizeof(float)*3,1,&myfile);
		ass_fread(lighting_material[no_lighting_materials]->specular,sizeof(float)*3,1,&myfile);
		ass_fread(&lighting_material[no_lighting_materials]->specular_exponent,sizeof(float),1,&myfile);

      // Type of lighting
		ass_fread(&lighting_material[no_lighting_materials]->lighting_model,sizeof(UINT8),1,&myfile);
		if ((lighting_material[no_lighting_materials]->lighting_model!=0) && (lighting_material[no_lighting_materials]->lighting_model!=1) && (lighting_material[no_lighting_materials]->lighting_model!=2)) 
		{
			errorMessage("Sod lighting model info error");
			return 0;
		}
//		if (type!=2)
		{
			lighting_material[no_lighting_materials]->specular[0]=1;
			lighting_material[no_lighting_materials]->specular[1]=1;
			lighting_material[no_lighting_materials]->specular[2]=1;
		}

		if (version>1.80+0.01) 
      {
         ass_fread(&temp,1,1,&myfile);
      }

      no_lighting_materials++;
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
			strcpy(parent,parent2);
		} else msBone_SetParentName(myBone,parent);

		// Read in matrix
		nodes[main_counter]=new sod_node();
		ass_vector right,up,front,pos;
		ass_fread(right.v,sizeof(float)*3,1,&myfile);
		ass_fread(up.v,sizeof(float)*3,1,&myfile);
		ass_fread(front.v,sizeof(float)*3,1,&myfile);
		ass_fread(pos.v,sizeof(float)*3,1,&myfile);
		right.v[0]*=-1;
		up.v[0]*=-1;
		front.v[0]*=-1;
		pos.v[0]*=-SCALE;
		pos.v[1]*=SCALE;
		pos.v[2]*=SCALE;
		nodes[main_counter]->matrix.from_vectors(&right,&up,&front,&pos);
		msBone_SetPosition(myBone,pos.v);
		float rot[3];
		nodes[main_counter]->matrix.to_euler(&rot[0],&rot[1],&rot[2]);
		msBone_SetRotation(myBone,rot);

		bool flip=false;

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
			msMesh * myMesh=msModel_GetMeshAt(pModel,msModel_AddMesh(pModel));
			msMesh_SetName(myMesh,node_name);
			strcpy(nodes[main_counter]->name,newNodeName);

			// Texture type (hard coded strings)
         char texture_type[30];
         strcpy(texture_type,"default");
		   if (version>1.60+0.01) 
			{
			   length=0;
			   ass_fread((void *)&length,sizeof(UINT16),1,&myfile);
			   ass_fread(&texture_type,length,1,&myfile);
			   texture_type[length]='\0';
         }

         // Load textures
         UINT32 textures=1;
		   if (version>1.91+0.01) 
			{
				ass_fread(&textures,sizeof(UINT32),1,&myfile);
				ass_fread(&junk,1,4,&myfile);
			}
         char mytexture[30];
			length=0;
			ass_fread((void *)&length,sizeof(UINT16),1,&myfile);
			ass_fread(&mytexture,length,1,&myfile);
			mytexture[length]='\0';
			int matIndex=msModel_AddMaterial(pModel);
			msMaterial* myMat=msModel_GetMaterialAt(pModel,matIndex);
			msMesh_SetMaterialIndex(myMesh,matIndex);
			char texture_name[60];
			char light_type[20];
		   if (version>1.91+0.01) 
			{
				ass_fread(&junk,1,4,&myfile);
				if (junk==0) strcpy(texture_type,"noalpha");
			}

         // Bump map
         if (textures&2)
         {
            char bump[30];
			   length=0;
			   ass_fread((void *)&length,sizeof(UINT16),1,&myfile);
			   ass_fread(&bump,length,1,&myfile);
			   bump[length]='\0';
  				ass_fread(&junk,1,4,&myfile);
         }

			// Unknown junk
		   if (version>1.91+0.01) 
			{
				ass_fread(&junk,1,4,&myfile);
			}
		   if ((version>1.80+0.01) && (version<1.93-0.01))
			{
				ass_fread(&junk,1,2,&myfile);
			}

			// Find the texture file
			char ass_texture_path[MS_MAX_PATH*2];
			char file_path[MS_MAX_PATH*2];
			int finder;
			strcpy(file_path,szFile);
			for (finder=strlen(file_path)-1;finder>=0;finder--)
			{
				if ((file_path[finder]=='\\') || (file_path[finder]=='/')) break;
			}
			file_path[finder+1]='\0';
			int bad=0;
			for (counter=0;counter<=9;counter++)
			{
				int subcounter;
				for (subcounter=0;subcounter<=2;subcounter++)
				{
					bad=0;
					strcpy(ass_texture_path,file_path);
/*					if (subcounter>0)
					{
						for (finder=strlen(ass_texture_path)-2;finder>=0;finder--)
						{
							if ((ass_texture_path[finder]=='\\') || (ass_texture_path[finder]=='/')) break;
						}
						ass_texture_path[finder+1]='\0';
					}*/
					if (subcounter==1) strcat(ass_texture_path,"..\\textures\\");
					if (subcounter==2) strcat(ass_texture_path,"..\\textures\\RGB\\");
					strcat(ass_texture_path,mytexture);
					if (counter==0)
					{
						strcat(ass_texture_path,".tga");
					} else {
						strcat(ass_texture_path,".");
						ass_texture_path[strlen(ass_texture_path)+1]=0;
						ass_texture_path[strlen(ass_texture_path)]=counter+48;
						bad=1;
					}
					if (!ass_file_exists(ass_texture_path)) 
					{
						strcat(ass_texture_path,".high");
						bad=4;
					}
					if (ass_file_exists(ass_texture_path)) break;
				}
				if (ass_file_exists(ass_texture_path)) break;
			}
			if (bad>0)
			{
				char old_ass_texture_path[MS_MAX_PATH*2];
				strcpy(old_ass_texture_path,ass_texture_path);
				*(ass_texture_path+strlen(ass_texture_path)-bad-1)='\0';
				rename(old_ass_texture_path,ass_texture_path);
			}
			// If it wasn't found then lets just assign default
			if (counter==10) strcpy(ass_texture_path,"");
			msMaterial_SetDiffuseTexture(myMat,ass_texture_path+strlen(file_path));

			// Load other header info
			UINT16 t_coords=0,light_groups=0,light_counter;

			// Setup vertex numbering info
			UINT16 _no_v=0,temp2=0;
			ass_fread((void *)&_no_v,sizeof(UINT16),1,&myfile);

			// Load other header info
			ass_fread((void *)&t_coords,sizeof(UINT16),1,&myfile);
			ass_fread((void *)&light_groups,sizeof(UINT16),1,&myfile);

			// Load vertex info
			bool *unused_v=(bool *)malloc(sizeof(bool)*_no_v);
			float *originalv=(float *)malloc(sizeof(float)*_no_v*3);
 			for (counter=0;counter<_no_v;counter++)
			{
				unused_v[counter]=true;

				ass_vector coords;
				ass_fread((void *)&coords.v,sizeof(float)*3,1,&myfile);
				coords.v[0]*=SCALE;
				coords.v[1]*=SCALE;
				coords.v[2]*=SCALE;
				originalv[counter*3+0]=coords.v[0];
				originalv[counter*3+1]=coords.v[1];
				originalv[counter*3+2]=coords.v[2];
				nodes[main_counter]->matrix.apply_to_vector(&coords);

				msVertex* myvert=msMesh_GetVertexAt(myMesh,msMesh_AddVertex(myMesh));
				msVertex_SetVertex(myvert,coords.v);
			}

			// Load the texture co-ordinates
			float sod_u[MAX_VERTICES_PER_OBJECT],sod_v[MAX_VERTICES_PER_OBJECT];
			for (counter=0;counter<t_coords;counter++)
			{
				ass_fread(&sod_u[counter],sizeof(float),1,&myfile);
				ass_fread(&sod_v[counter],sizeof(float),1,&myfile);
			}

         // Load up polygon sets ("lighting groups")
         int p_base=0;
			for (light_counter=0;light_counter<light_groups;light_counter++)
			{
				// Setup polygon numbering info
				UINT16 _no_p=0;
				ass_fread((void *)&_no_p,sizeof(UINT16),1,&myfile);

				// Get lighting identifier
            char lighting_identifier[30];
				length=0;
				ass_fread((void *)&length,sizeof(UINT16),1,&myfile);
				ass_fread(&lighting_identifier,length,1,&myfile);
            lighting_identifier[length]='\0';

            // Look up lighting index
            int lighting_index;
            for (lighting_index=0;lighting_index<no_lighting_materials;lighting_index++)
            {
               if (strcmp(lighting_material[lighting_index]->identifier,lighting_identifier)==0) break;
            }
            if (lighting_index!=no_lighting_materials)
            {
               // Lighting info
				msMaterial_SetAmbient(myMat,lighting_material[lighting_index]->ambient);
				msMaterial_SetDiffuse(myMat,lighting_material[lighting_index]->diffuse);
				msMaterial_SetEmissive(myMat,lighting_material[lighting_index]->specular);
				msMaterial_SetShininess(myMat,lighting_material[lighting_index]->specular_exponent);

				if (lighting_material[lighting_index]->lighting_model==0)
					strcpy(light_type,"constant");
				if (lighting_material[lighting_index]->lighting_model==1)
					strcpy(light_type,"lambert");
				if (lighting_material[lighting_index]->lighting_model==2)
					strcpy(light_type,"phong");
				sprintf(texture_name,"!%s_%s_!%s",light_type,node_name,texture_type);
				msMaterial_SetName(myMat,texture_name);
            } else
			if (no_lighting_materials==0)
			{
               // Lighting info
				float diffuse[]={0.8,0.8,0.8};
				msMaterial_SetDiffuse(myMat,diffuse);

				msMaterial_SetName(myMat,node_name);
			}

				// Load polygon info
				unsigned int subcounter;
				for (counter=0;counter<_no_p;counter++)
				{
					msTriangle* myTri=msMesh_GetTriangleAt(myMesh,msMesh_AddTriangle(myMesh));

					// There are 3 vertices per sod polygon (triangles)
					word vind[3];
					for (subcounter=0;subcounter<3;subcounter++)
					{
						temp2=0;
						ass_fread((void *)&temp2,sizeof(UINT16),1,&myfile);

						UINT16 uv_index;
						ass_fread(&uv_index,sizeof(UINT16),1,&myfile);

						// Copy in texture co-ords (we don't decide to make multiple vertex copies in order to preserve this every-polygon-every-vertex copying, so we simply pick an arbitary one to use from those available)
						float uv[2];
						uv[0]=sod_u[uv_index];
						uv[1]=sod_v[uv_index];
						msVertex * originalV=msMesh_GetVertexAt(myMesh,temp2);
						if (unused_v[temp2]) // First time
						{
							originalV->u=uv[0];
							originalV->v=uv[1];
							vind[subcounter]=temp2;
							unused_v[temp2]=false;
						} else
						if ((originalV->u!=uv[0]) || (originalV->v!=uv[1])) // Been here before, and this time UV is different
						{
							vind[subcounter]=msMesh_AddVertex(myMesh);
							msVertex* myVertex=msMesh_GetVertexAt(myMesh,vind[subcounter]);
							originalV=msMesh_GetVertexAt(myMesh,temp2);
							float originalVertex[3];
							msVertex_GetVertex (originalV, originalVertex);
							msVertex_SetVertex(myVertex,originalVertex);
							msVertex_SetTexCoords(myVertex,uv);
						} else { // been here before and its the same
							vind[subcounter]=temp2;
						}
					}

					// See if we need to do a flip on it
					if (flip)
					{
						word temp=vind[0];
						vind[0]=vind[2];
						vind[2]=temp;
					}

					msTriangle_SetVertexIndices(myTri,vind);
				}

            p_base+=_no_p;
			}

			// Backface culling?
			ass_fread((void *)&temp,sizeof(UINT8),1,&myfile);
			if (temp==0)
			{
				// Not yet implemented: make two sided
			}

         // Throw away =0 padding
			ass_fread(&junk,sizeof(UINT16),1,&myfile);

			free(unused_v);
			free(originalv);
		}

   }

	// Animation    Milkshape can't do this
/*	unsigned short no_animations=0;
	if (!ass_feof(myfile)) ass_fread(&no_animations,2,1,&myfile);
	for (counter=0;counter<no_animations;counter++)
	{
		// What node this applies to
		unsigned short len;
		ass_fread(&len,2,1,&myfile);
		char ani_link[20];
		ass_fread(ani_link,len,1,&myfile);
		ani_link[len]='\0';

		// Setup animation space
		msMesh * ani_node=msModel_GetMeshAt(pModel,msModel_FindMeshByName(pModel,ani_link));

		// Some ani info
		ass_fread(&seq->no_frames,2,1,&myfile);
		ass_fread(&seq->frame_delay_length,4,1,&myfile);
		seq->frame_delay_length/=100;
		ass_fseek(myfile,2,SEEK_CUR);

		// Create static vertex positions for each keyframe
		int i;
		ass_matrix transupdate;
		ass_vector right,up,front,pos;
		for (i=0;i<seq->no_frames;i++)
		{
			// Allocate
			seq->frames[i]=new ass_static_animation_frame();
			ass_static_animation_frame * frame=seq->frames[i];

			// Load in transform matrix
			ass_fread(&right,sizeof(float)*3,1,&myfile);
			ass_fread(&up,sizeof(float)*3,1,&myfile);
			ass_fread(&front,sizeof(float)*3,1,&myfile);
			ass_fread(&pos,sizeof(float)*3,1,&myfile);
			transupdate.from_vectors(&right,&up,&front,&pos);

			// Create each vertex
			int j=0;
			while (ani_node->geometry->vertexlist[j])
			{
				frame->vertexlist[j]=new ass_vertex();
				frame->vertexlist[j]->x=ani_node->geometry->vertexlist[j]->x;
				frame->vertexlist[j]->y=ani_node->geometry->vertexlist[j]->y;
				frame->vertexlist[j]->z=ani_node->geometry->vertexlist[j]->z;
				transupdate.apply_to_vector(frame->vertexlist[j]);
				j++;
			}
		}
	}*/

   // Get rid of lighting materials
   for (counter=0;counter<no_lighting_materials;counter++)
   {
      delete lighting_material[counter];
   }


   return 0;
}

bool ass_file_exists(char * filename)
{
   WIN32_FIND_DATA FindFileData;
   HANDLE hFind;
   hFind = FindFirstFile(filename, &FindFileData);
   FindFileData.cFileName;
	return ((signed)hFind)!=-1;
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
