import os, shutil
path = "C:/Users/balintgucsi/Documents/test/origin/doc.txt"
moveto = "V:/Dokumentumok/dest/doc.txt"
print "File moved successfully!"

shutil.copy2(path,moveto)


