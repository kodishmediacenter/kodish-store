# Python 3 code
import urllib.request, urllib.parse, urllib.error
import zipfile
import os,xbmcvfs,shutil,xbmcplugin,xbmcgui,xbmcaddon,xbmc
import sys
import re
import runter
import donation

ADDON_ID      = 'Kodish.repo.store'
REAL_SETTINGS = xbmcaddon.Addon(id=ADDON_ID)
ADDON_NAME    = REAL_SETTINGS.getAddonInfo('name')
ICON          = REAL_SETTINGS.getAddonInfo('icon')
FANART        = REAL_SETTINGS.getAddonInfo('fanart')


logexite = "special://home/media/kodi.txt"
filewk = os.path.join(xbmcvfs.translatePath(logexite))


def super_log_fix():
    f = os.path.join(xbmcvfs.translatePath("special://logpath/kodi.log"))
    file = open(f,"w") 
    file.write("Super Log Fixed")
    file.write("\n")
    #main_kodish()

def addon_instalado(ids):
    tamz = len(ids)
    for a in ['special://home/addons/'+ids[0:tamz-4]+'']:
        existe = xbmcvfs.translatePath(a)
        
        if os.path.exists(existe)==True:
            shutil.rmtree(existe)
    return ids

    

def limpacache():
    for a in ['special://home/cache']:
        existe = xbmcvfs.translatePath(a)
        if os.path.exists(existe)==True:
            shutil.rmtree(existe)
		
def updatefix(ids):
    for a in ['special://home/addons/'+ids+'']:
        existe = xbmcvfs.translatePath(a)
        if os.path.exists(existe)==True:
            shutil.rmtree(existe)


def limpaelementum():
    for a in ['special://home/addons/plugin.video.elementum','special://home/addons/script.elementum.burst','special://home/addons/context.elementum','special://home/userdata/addon_data/plugin.video.elementum']:
        existe = xbmcvfs.translatePath(a)
        if os.path.exists(existe)==True:
            shutil.rmtree(existe)
		
    


def execc(nome):

    param2 = nome
    zip_file = "special://home/media/"
    api_file  = os.path.join(xbmcvfs.translatePath(zip_file))
    filezip = re.sub('plugin://kodish.repo.store/', r'', param2)
    
    filezip2 = str(filezip.replace("?file=",""))
    tam = len(filezip2)
    filezip21 = filezip2[0:tam-4]
    url = 'https://raw.githubusercontent.com/kodishmediacenter/kodi19/master/addons/'+filezip2+''


     
    pDialog = xbmcgui.DialogProgress()
    pDialog.create('Kodi', 'Iniciando o Download')
    os.chdir (api_file) 
    urllib.request.urlretrieve(url, ""+filezip2+"")
    pDialog.update(100, 'Terminando de Instalar')
    exemploZIP = zipfile.ZipFile (""+filezip2+"")
    exemploZIP.extractall()
    exemploZIP.close()
    source = ""+api_file+"/"+filezip21+""
    destination = "special://home/addons"
    destination2 = os.path.join(xbmcvfs.translatePath(destination))
    shutil.move(source, destination2)
    dialog = xbmcgui.Dialog()
    ativaaddon(filezip21)
    file = open(filewk,"w") 
    file.write(filezip21)
    pDialog.close()
    dialog.ok('Kodish Store', 'Addon Instalado com sucesso !!!')
    

    
    main_kodish()
    
def execc2(nome):

    param2 = nome
    zip_file = "special://home/media/"
    api_file  = os.path.join(xbmcvfs.translatePath(zip_file))
    filezip = re.sub('plugin://kodish.repo.store/', r'', param2)
    filezip2 = str(filezip.replace("?file=",""))
    tam = len(filezip2)
    filezip21 = "xbmc.python2"
    url = 'https://raw.githubusercontent.com/kodishmediacenter/kodi19/master/fix/xbmc.python2.zip'
    pDialog = xbmcgui.DialogProgress()
    pDialog.create('Kodi', 'Iniciando o Download')
    filezip2 = "xbmc.python2.zip" 
    print("baixando addon ....")
    os.chdir (api_file) 
    urllib.request.urlretrieve(url, ""+filezip2+"")
    pDialog.update(100, 'Terminando de Instalar')
    exemploZIP = zipfile.ZipFile (""+filezip2+"")
    exemploZIP.extractall()
    exemploZIP.close()
    source = ""+api_file+"/"+filezip21+""
    destination = "special://home/addons"
    destination2 = os.path.join(xbmcvfs.translatePath(destination))
    shutil.move(source, destination2)
    dialog = xbmcgui.Dialog()
    pDialog.close()
    dialog.ok('Kodish Store', 'Addon Instalado com sucesso !!!')
    ativaaddon(filezip21)

    main_kodish()



def execc3(nome):

    param2 = nome
    zip_file = "special://home/media/"
    api_file  = os.path.join(xbmcvfs.translatePath(zip_file))
    filezip = re.sub('plugin://kodish.repo.store/', r'', param2)
    
    filezip2 = str(filezip.replace("?file=","").replace('https://kodishmediacenter.github.io/kodi19/repos/repos/',''))
    tam = len(filezip2)
    filezip21 = filezip2[0:tam-4]
    
    url = 'https://raw.githubusercontent.com/kodishmediacenter/kodi19/master/addons/'+filezip2+''
    url2 = url.replace('repos/repos','repos').replace('https://raw.githubusercontent.com/kodishmediacenter/kodi19/master/addons/','')
    url3 = url2.replace('https://kodishmediacenter.github.io/kodi19/repos/','https://raw.githubusercontent.com/kodishmediacenter/kodi19/master/repos/')

    pDialog = xbmcgui.DialogProgress()
    pDialog.create('Kodi', 'Iniciando o Download')
     
    print("baixando addon ....")
    os.chdir (api_file)
    file = open(filewk,"a")
    file.write('\n')
    file.write(url3)
    file.write('\n')
    file.close()
    #urllib.request.urlretrieve(url3, ""+filezip2+"")
    #urllib.request.urlretrieve(url3)
    import wget 
    wget.download(url3)
    exemploZIP = zipfile.ZipFile (""+filezip2+"")
    exemploZIP.extractall()
    exemploZIP.close()
    source = ""+api_file+"/"+filezip21+""
    destination = "special://home/addons"
    destination2 = os.path.join(xbmcvfs.translatePath(destination))
    shutil.move(source, destination2)
    dialog = xbmcgui.Dialog()
    ativaaddon(filezip21)
    file = open(filewk,"a")
    file.write('\n')
    file.write('Vers??o Instalada\n')
    file.write(filezip21)
    file.write('\n')
    
    f.close()

    file = open(filewk,"a")
    file.write('Vers??o a ser Extraida\n')
    file.write(filezip2)
    file.write('\n')
    f.close()
    pDialog.update(100, 'Terminando de Instalar')
    pDialog.close()
    dialog.ok('Kodish Store', 'Addon Instalado com sucesso !!!')    
    main_kodish()



def execc4(nome):

    param2 = nome
    zip_file = "special://home/media/"
    api_file  = os.path.join(xbmcvfs.translatePath(zip_file))
    filezip = re.sub('plugin://kodish.repo.store/', r'', param2)
    
    filezip2 = str(filezip.replace("?file=",""))
    tam = len(filezip2)
    filezip21 = filezip2[0:tam-4]
    url = 'https://raw.githubusercontent.com/kodishmediacenter/repos19/main/repo/'+filezip2+''
    pDialog = xbmcgui.DialogProgress()
    pDialog.create('Kodi', 'Iniciando o Download')
    


     
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
    pDialog.update(100, 'Terminando de Instalar')
    dialog = xbmcgui.Dialog()
    ativaaddon(filezip21)
    file = open(filewk,"w") 
    file.write(filezip21)
    pDialog.close()
    dialog.ok('Kodish Store', 'Addon Instalado com sucesso !!!')

    
    main_kodish()
    

def ativaaddon(ids):
    import database
    nome = ids
    database.insert_id(nome)
    database.enable_addon(nome)
    xbmc.executebuiltin("Container.Update()")


def addDir(title,url,icon):
    liz=xbmcgui.ListItem(title)
    liz.setProperty('IsPlayable', 'false')
    liz.setInfo(type="Video", infoLabels={"label":title,"title":title} )
    liz.setArt({'thumb':icon,'fanart':FANART})
    nome = url
    execc(nome)
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=True)

def addons_menu():
    link = "https://kodishmediacenter.github.io/kodi19/"
    dialog = xbmcgui.Dialog()
    fn = dialog.browseSingle(1, 'Kodish Store Neo Kodi 19', 'music', '', False, False, link)
    fns = str(fn)
    fns2 = fns.replace('https://kodishmediacenter.github.io/kodi19/addons/','')
    file = open(filewk,"w") 
    file.write(fns2)
    file.close()
    addon_instalado(fns2)
    execc(fns2)
    

def addons_fix():
    link = "http://kodishteam.space/fix/k19/"
    dialog = xbmcgui.Dialog()
    fn = dialog.browseSingle(1, 'Kodish Store Neo Kodi 19', 'music', '', False, False, link)
    fns = str(fn)
    fns2 = fns.replace('http://kodishteam.space/fix/k19/','https://kodishmediacenter.github.io/kodi19/fix/')
    file = open(filewk,"w") 
    file.write(fns2)
    file.close()
    addon_instalado(fns2)
    execc2(fns2)

def addons_repo():
    link3 = "https://kodishmediacenter.github.io/repos19/"
    dialog = xbmcgui.Dialog()
    fn = dialog.browseSingle(1, 'Kodish Store Neo Kodi 19', 'music', '', False, False, link3)
    fns = str(fn)
    fns2 = fns.replace('https://kodishmediacenter.github.io/repos19/repo/','')
    file = open(filewk,"w") 
    file.write(fns2)
    file.close()
    addon_instalado(fns2)
    execc4(fns2)




def loja_kodish():
    dialog = xbmcgui.Dialog()
    linkf = dialog.select('Kodish Store - Loja', ['Colocar Senha em Addon','Criptografar um Addon','Criar um Repositorio','Criar um Addon','Videos Youtube para DVD','Videos Youtube para Bluray','','','','','','',''])

    if linkf == 0:
        dialog = xbmcgui.Dialog()
        linkf = dialog.select('Kodish Store - Loja', ['Esse Servico permite colocar uma senha basica num addon','','Addon Limpo R$ 65 e Addon Sujo R$ 130'])
        
    if linkf == 1:
        dialog = xbmcgui.Dialog()
        linkf = dialog.select('Kodish Store - Loja', ['Esse Servico criptografamos addon default','','Addon Limpo R$ 25 e Addon Sujo R$ 50'])

    if linkf == 2:
        dialog = xbmcgui.Dialog()
        linkf = dialog.select('Kodish Store - Loja', ['Criamos Repositorio para seu addon','','Kodi 18 R$25','Kodi 19 R$35','Kodi 18 e 19 R$50'])

    if linkf == 3:
        dialog = xbmcgui.Dialog()
        linkf = dialog.select('Kodish Store - Loja', ['Criacao de Addon diversos','','Addon Youtube R$25,00','Addon XML e M3U R$35,00','Addon de Canal e Radio Web R$35,00',''])

    if linkf == 4:
        dialog = xbmcgui.Dialog()
        linkf = dialog.select('Kodish Store - Loja', ['Videos Youtube para DVD Criamos DVD com seus Videos Favoritos','','Imagem ISO R$35,00','A Midia DVD R$40,00 + Frete e Caixa'])

    if linkf == 5:
        dialog = xbmcgui.Dialog()
        linkf = dialog.select('Kodish Store - Loja', ['Videos Youtube para Bluray Criamos Bluray com seus Videos Favoritos em alta qualidade','','Imagem ISO R$50,00','A Midia DVD R$60,00 + Frete e Caixa'])
        
def ativaraddon():
    xbmc.executebuiltin("ActivateWindow(addons://sources/video/addons)")

def main_kodish():
    #limpacache()
    #super_log_fix()
    dialog = xbmcgui.Dialog()
    link = dialog.select('Kodish Store - Neomix', ['Doa????o','Loja da Kodish','','Instalar Addons','Remover o Elementun','Instalar o Fix (Obrigatorio)','Repositorios','Instalar o Elementum','Instalar Torrest','Limpar o Super Cache','Instalar F4M Tester'])
    links = str(link)
    file = open(filewk,"a") 
    file.write(links)
    file.close()

    if link == 0:
        donation.donation()
    if link == 1:
        loja_kodish()
        
    if link == 3:
        addons_menu()
    if link == 4:
        limpaelementum()
    if link == 5:
        addons_fix()
    if link == 6:
        addons_repo()
    if link == 7:
        import elementum
        elementum.main_elementum()
    if link == 8:
        import torrest
        torrest.main_torrest()
    if link == 9:
        super_log_fix()

    if link == 10:
        import f4mtester
        f4mtester.execc2()

        


main_kodish()

 
