md BinRead
copy plc.bin BinRead\plc.zip
cd BinRead\
tar -xvzf plc.zip
tar -xvzf usual-report.tgz 
cd report\
copy *.dump ..\..\*.xls
cd ..\
del /S /Q *
RMDIR /S /Q *
