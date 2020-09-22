import os
import shutil

path  = 'C:/Users/Desktop/doc/'  # your directory
names = os.listdir(path)
extension_set = set()

for i in names:
    ext = i.split(sep=".")
    try:
        extension_set.add(ext[1])
    except:
        continue

for x in extension_set:
    print(x)
    if not os.path.exists(path+x):
        os.mkdir(path+x)
    
for file in names:
    ext = file.split(sep='.')
    if len(ext)>1:
        if ext[1] in file and not os.path.exists(path+ext[1]+'/'+file):
            shutil.move(path+file,path+ext[1]+'/'+file)
 
    
