import shutil 
import xbmcvfs,os,xbmcgui


def pvr_control_disable():
    pvra = os.path.join(xbmcvfs.translatePath("special://home/userdata/addon_data/pvr.iptvsimple"))
    pvrb = os.path.join(xbmcvfs.translatePath("special://home/userdata/addon_data/pvr.iptvsimple"))
    shutil.move(pvra,pvrb)


def pvr_control_enable():
    pvra = os.path.join(xbmcvfs.translatePath("special://home/userdata/addon_data/pvr.iptvsimple"))
    pvrb = os.path.join(xbmcvfs.translatePath("special://home/userdata/addon_data/pvr.iptvsimple"))
    shutil.move(pvrb,pvra)



def pvr_menu():
    dialog = xbmcgui.Dialog()
    link = dialog.select('Kodish Store - PVR Simple Controle', ['Desabilitar','Habilitar'])

    if link == 0:
        pvr_control_disable()
    if link == 1:
        pvr_control_enable()

