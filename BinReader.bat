echo off
cls
echo Starting BinRead.bat
md BinRead
copy plc.bin BinRead\plc.zip >nul 2>&1
cd BinRead\ >nul 2>&1
tar -xvzf plc.zip >nul 2>&1
tar -xvzf usual-report.tgz >nul 2>&1
cd report\ >nul 2>&1
copy *.dump ..\..\*.csv >nul 2>&1
copy uptime ..\..\uptime.txt >nul 2>&1
cd ..\ >nul 2>&1
del /S /Q * >nul 2>&1
RMDIR /S /Q * >nul 2>&1
echo Successful completion