import xbmc
import xbmcgui

def web_browser(urlcn):
        import webbrowser
        if xbmc . getCondVisibility ( 'system.platform.android' ) :
                ost = xbmc . executebuiltin ( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( ''+urlcn+'' ) )
        else:
                ost = webbrowser . open ( ''+urlcn+'' )

def donation():
        url = "https://uploaddeimagens.com.br/images/001/572/022/original/mercadopago.png"
        url2 = "https://goo.gl/ArZ2Gx"
        url3 = "https://raw.githubusercontent.com/kodishmediacenter/omega/master/pix.txt"
        
        dialog = xbmcgui.Dialog()
        link = dialog.select('Forma de Doacao', ['App do Mercado Pago/Livre', 'PayPal','Pix'])

        if link == 0:
        
                import webbrowser
                if xbmc . getCondVisibility ( 'system.platform.android' ) :
                    ost = xbmc . executebuiltin ( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( ''+url+'' ) )
                else:
                    ost = webbrowser . open ( ''+url+'' )

        if link == 1:
        
                import webbrowser
                if xbmc . getCondVisibility ( 'system.platform.android' ) :
                    ost = xbmc . executebuiltin ( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( ''+url2+'' ) )
                else:
                    ost = webbrowser . open ( ''+url2+'' )

        if link == 2:
        
                import webbrowser
                if xbmc . getCondVisibility ( 'system.platform.android' ) :
                    ost = xbmc . executebuiltin ( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( ''+url3+'' ) )
                else:
                    ost = webbrowser . open ( ''+url3+'' )
