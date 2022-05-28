@ECHO OFF
echo _________________________________________________________________
echo     WARNING     WARNING     WARNING     WARNING     WARNING
echo _________________________________________________________________
echo .
echo This will delete all VOX_files and set bc to standard settings.
echo Press ENTER to proceed or close this Window to stop this action.
echo .
echo _________________________________________________________________
echo     WARNING     WARNING     WARNING     WARNING     WARNING
echo _________________________________________________________________
pause

cd ..
del /S /F  *vox*
del scripts\KeyboardBinding.py
del scripts\KeyboardBinding.pyc
del options.cfg


echo DONE!     DONE!     DONE!
pause
