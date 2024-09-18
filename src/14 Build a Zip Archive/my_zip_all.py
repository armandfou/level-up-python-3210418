import os
from zipfile import ZipFile;

def listFile(dir, extensions, arrayFiles):
  for (dirpath, dirnames, filenames) in os.walk(dir):
    for i in filenames:
      h = os.path.join(dirpath, i)
      if  len([ext for ext in extensions if h.endswith(ext)])> 0:
        arrayFiles.append(h)
  return arrayFiles

def zip_all(dir, extensions, archiveFileName):
  filenames = listFile(dir, extensions, [])
  with ZipFile(archiveFileName, 'w') as zip_object:
    for i in filenames:
      zip_object.write(i)

zip_all('my_stuff', ['.jpg','.txt'], 'my_stuff.zip')

# print(listFile("my_stuff", ['.jpg','.txt'], []))