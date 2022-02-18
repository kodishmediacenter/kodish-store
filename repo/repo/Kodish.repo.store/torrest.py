# Python 3 code
import urllib.request, urllib.parse, urllib.error
import zipfile
import os,xbmcvfs,shutil,xbmcplugin,xbmcgui,xbmcaddon,xbmc
import sys
import re


ADDON_ID      = 'Kodish.repo.store'
REAL_SETTINGS = xbmcaddon.Addon(id=ADDON_ID)
ADDON_NAME    = REAL_SETTINGS.getAddonInfo('name')
ICON          = REAL_SETTINGS.getAddonInfo('icon')
FANART        = REAL_SETTINGS.getAddonInfo('fanart')


def addon_instalado():

    for a in ['special://home/addons/plugin.video.torrest']:
        existe = xbmcvfs.translatePath(a)
        
        if os.path.exists(existe)==True:
            shutil.rmtree(existe)


def torrest_android_verso():
    dialog = xbmcgui.Dialog()
    versao = dialog.select('Kodish Store - Neo', ['Arm','Arm 64','x64','x86'])
    
    if versao == 0:
        url = "https://raw.githubusercontent.com/kodishmediacenter/torrest/main/Android/arm/plugin.video.torrest.zip"
        torrest_android(url)
    
    if versao == 1:
        url = "https://raw.githubusercontent.com/kodishmediacenter/torrest/main/Android/arm64/plugin.video.torrest.zip"
        torrest_android(url)   
        
    if versao == 2:
        url = "https://raw.githubusercontent.com/kodishmediacenter/torrest/main/Android/x64/plugin.video.torrest.zip"
        torrest_android(url)
    
    if versao == 3:
        url = "https://raw.githubusercontent.com/kodishmediacenter/torrest/main/Android/x86/plugin.video.torrest.zip"
        torrest_android(url)
        
        
def torrest_android(link):    
    param2 = ''
    zip_file = "special://home/media/"
    api_file  = os.path.join(xbmcvfs.translatePath(zip_file))
    filezip = re.sub('plugin://kodish.repo.store/', r'', param2)
    filezip2 = str(filezip.replace("?file=",""))
    tam = len(filezip2)
    filezip21 = "plugin.video.torrest"
    ids = filezip21
    addon_instalado()
    url = link
    filezip2 = "plugin.video.torrest.zip" 
    print("baixando addon ....")
    os.chdir (api_file) 
    urllib.request.urlretrieve(url, ""+filezip2+"")
    exemploZIP = zipfile.ZipFile (""+filezip2+"")
    exemploZIP.extractall()
    exemploZIP.close()
    source = ""+api_file+"/"+filezip21+""
    destination = "special://home/addons"
    destination2 = os.path.join(xbmcvfs.translatePath(destination))
    shutil.move(source, destination2)
    dialog = xbmcgui.Dialog()
    dialog.ok('Kodish Store', 'Addon Instalado com sucesso !!!')
    database.insert_id(filezip21)


def torrest_apple():

    param2 = ""
    zip_file = "special://home/media/"
    api_file  = os.path.join(xbmcvfs.translatePath(zip_file))
    filezip = re.sub('plugin://kodish.repo.store/', r'', param2)
    filezip2 = str(filezip.replace("?file=",""))
    tam = len(filezip2)
    filezip21 = "plugin.video.torrest"
    url = 'https://raw.githubusercontent.com/kodishmediacenter/torrest/main/Apple/plugin.video.torrest.zip'
    filezip2 = "plugin.video.torrest.zip" 
    print("baixando addon ....")
    os.chdir (api_file) 
    urllib.request.urlretrieve(url, ""+filezip2+"")
    exemploZIP = zipfile.ZipFile (""+filezip2+"")
    exemploZIP.extractall()
    exemploZIP.close()
    source = ""+api_file+"/"+filezip21+""
    destination = "special://home/addons"
    destination2 = os.path.join(xbmcvfs.translatePath(destination))
    shutil.move(source, destination2)
    dialog = xbmcgui.Dialog()
    dialog.ok('Kodish Store', 'Addon Instalado com sucesso !!!')
    database.insert_id(filezip21)



def torrest_linux_verso():
    dialog = xbmcgui.Dialog()
    versao = dialog.select('Kodish Store - Neo', ['Arm 64','Arm 7','x64','x86'])
    
    if versao == 0:
        url = "https://raw.githubusercontent.com/kodishmediacenter/torrest/main/Linux/arm64/plugin.video.torrest.zip"
        torrest_linux(url)
    
    if versao == 1:
        url = "https://raw.githubusercontent.com/kodishmediacenter/torrest/main/Linux/armv7/plugin.video.torrest.zip"
        torrest_linux(url)   
        
    if versao == 2:
        url = "https://raw.githubusercontent.com/kodishmediacenter/torrest/main/Linux/x64/plugin.video.torrest.zip"
        torrest_linux(url)
    
    if versao == 3:
        url = "https://raw.githubusercontent.com/kodishmediacenter/torrest/main/Linux/x86/plugin.video.torrest.zip"
        torrest_linux(url)

def torrest_linux(link):

    param2 = ""
    zip_file = "special://home/media/"
    api_file  = os.path.join(xbmcvfs.translatePath(zip_file))
    filezip = re.sub('plugin://kodish.repo.store/', r'', param2)
    filezip2 = str(filezip.replace("?file=",""))
    tam = len(filezip2)
    filezip21 = "plugin.video.torrest"
    url = link
    filezip2 = "plugin.video.torrest.zip" 
    print("baixando addon ....")
    os.chdir (api_file) 
    urllib.request.urlretrieve(url, ""+filezip2+"")
    exemploZIP = zipfile.ZipFile (""+filezip2+"")
    exemploZIP.extractall()
    exemploZIP.close()
    source = ""+api_file+"/"+filezip21+""
    destination = "special://home/addons"
    destination2 = os.path.join(xbmcvfs.translatePath(destination))
    shutil.move(source, destination2)
    dialog = xbmcgui.Dialog()
    dialog.ok('Kodish Store', 'Addon Instalado com sucesso !!!')
    database.insert_id(filezip21)


def torrest_windows_verso():
    dialog = xbmcgui.Dialog()
    versao = dialog.select('Kodish Store - Neo', ['x64','x86'])
    
    if versao == 0:
        url = "https://raw.githubusercontent.com/kodishmediacenter/torrest/main/Windows/x64/plugin.video.torrest.zip"
        torrest_windows(url)
    
    if versao == 1:
        url = "https://raw.githubusercontent.com/kodishmediacenter/torrest/main/Windows/x86/plugin.video.torrest.zip"
        torrest_windows(url)   
        

def torrest_windows(link):

    param2 = ""
    zip_file = "special://home/media/"
    api_file  = os.path.join(xbmcvfs.translatePath(zip_file))
    filezip = re.sub('plugin://kodish.repo.store/', r'', param2)
    filezip2 = str(filezip.replace("?file=",""))
    tam = len(filezip2)
    filezip21 = "plugin.video.torrest"
    url = link
    filezip2 = "plugin.video.torrest.zip" 
    print("baixando addon ....")
    os.chdir (api_file) 
    urllib.request.urlretrieve(url, ""+filezip2+"")
    exemploZIP = zipfile.ZipFile (""+filezip2+"")
    exemploZIP.extractall()
    exemploZIP.close()
    source = ""+api_file+"/"+filezip21+""
    destination = "special://home/addons"
    destination2 = os.path.join(xbmcvfs.translatePath(destination))
    shutil.move(source, destination2)
    dialog = xbmcgui.Dialog()
    dialog.ok('Kodish Store', 'Addon Instalado com sucesso !!!')
    database.insert_id(filezip21)

def torrest_dep(nome):

    param2 = nome
    zip_file = "special://home/media/"
    api_file  = os.path.join(xbmcvfs.translatePath(zip_file))
    filezip = re.sub('plugin://kodish.repo.store/', r'', param2)
    filezip2 = str(filezip.replace("?file=",""))
    tam = len(filezip2)
    filezip21 = "context.torrest"
    filezip22 = "script.torrest.burst"
    url = 'https://raw.githubusercontent.com/kodishmediacenter/torrest/main/dep.zip'
    filezip2 = "dep.zip" 
    print("baixando addon ....")
    os.chdir (api_file) 
    urllib.request.urlretrieve(url, ""+filezip2+"")
    exemploZIP = zipfile.ZipFile (""+filezip2+"")
    exemploZIP.extractall()
    exemploZIP.close()
    source = ""+api_file+"/"+filezip21+""
    source2 = ""+api_file+"/"+filezip22+""
    destination = "special://home/addons"
    destination2 = os.path.join(xbmcvfs.translatePath(destination))
    shutil.move(source, destination2)
    shutil.move(source2, destination2)
    dialog = xbmcgui.Dialog()
    dialog.ok('Kodish Store', 'Addon Instalado com sucesso !!!')
    database.insert_id(filezip21)




def main_torrest():
    addon_instalado()
    dialog = xbmcgui.Dialog()
    link = dialog.select('Kodish Store - Neo', ['Android','Apple','Linux','Windows'])

    if link == 0:
        torrest_android_verso()
    if link == 1:
        torrest_apple()
    if link == 2:
        torrest_linux_verso()
    if link == 3:
        torrest_windows_verso()


#torrest.main_torrest()
