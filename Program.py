from subprocess import Popen
p = Popen("BinReader.bat", cwd=r"C:\Users\puhov\Desktop\SoftGIT\IDLEtable")
stdout, stderr = p.communicate()
