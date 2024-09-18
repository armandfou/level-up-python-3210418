
import os
import urllib.request

def make_url_with_num(url, num):
  filename, ext = os.path.splitext(url)
  numStr =  str(num)
  return filename[0: len(filename) - 3] + (((3 - len(numStr)) * "0") + numStr) + ext

def get_filename_from_url(url):
  for i in range(len(url) - 1, -1,-1):
    if (url[i] == "/"):
      return url[i + 1:len(url)]
  return ""

def download_files(url, kiki):
  filename, ext = os.path.splitext(url)
  cpt =  int(filename[len(filename) - 3: len(filename)])
  lastRequestDidNotFailed = True
  os.mkdir(kiki)
  while(lastRequestDidNotFailed):
    try:
      urle = make_url_with_num(url, cpt)
      req = urllib.request.Request(url=make_url_with_num(urle, cpt))
      with urllib.request.urlopen(req) as f:
        with open(os.path.join(kiki, get_filename_from_url(urle)),'wb+') as output:
          output.write(f.read())
      cpt = cpt + 1
    except  Exception as inst:
      print (inst)
      lastRequestDidNotFailed = False

    

# print(download_files('http://699340.youcanlearnit.net/image001.jpg', './images'))




print(download_files('http://699340.youcanlearnit.net/image001.jpg', './images'))