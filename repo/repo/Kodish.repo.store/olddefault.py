# Python 3 code
import urllib.request, urllib.parse, urllib.error
import zipfile
import os,xbmcvfs,shutil
import sys
import re


def execc(nome):

    param2 = nome
    zip_file = "special://home/media/"
    api_file  = os.path.join(xbmcvfs.translatePath(zip_file))
    filezip = re.sub('plugin://kodish.repo.store/', r'', param2)
    filezip2 = str(filezip.replace("?file=",""))
    tam = len(filezip2)
    filezip21 = filezip2[0:tam-3]
    url = 'https://raw.githubusercontent.com/kodishmediacenter/kodi19/master/addons/'+filezip2+''
     
    print("baixando addon ....")
    os.chdir (api_file) 
    urllib.request.urlretrieve(url, ""+filezip2+"")
    exemploZIP = zipfile.ZipFile (""+filezip2+"")
    exemploZIP.extractall()
    exemploZIP.close()
    source = ""+api_file+"/"+filezip21+""
    destination = "special://home/addons"
    destination2 = os.path.join(xbmcvfs.translatePath(destination))
    dest = shutil.move(source, destination2)





nome = "plugin.video.espiritismo.zip"
execc(nome)
