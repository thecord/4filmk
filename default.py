#import sys,urllib,,urllib2,re,xbmcplugin,xbmcgui,xbmc,xbmcaddon,os
import urllib, urllib2, re, os.path, sys
import xbmc, xbmcplugin, xbmcgui, xbmcaddon,urlparse
import requests
from addon.common.addon import Addon
import urlresolver

User_Agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36'
addon_id='plugin.video.try001'
selfAddon = xbmcaddon.Addon(id=addon_id)
addon = Addon(addon_id, sys.argv)
art = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id + '/resources/art/'))
icon = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))
fanart = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))
baseurl = 'http://www.4filmk.com'
reload(sys)
sys.setdefaultencoding('utf8')


def CAT():
        addDir('[B][COLOR white]English Movies[/COLOR][/B]',baseurl+'/online/%D8%A7%D9%81%D9%84%D8%A7%D9%85-%D8%A7%D8%AC%D9%86%D8%A8%D9%89-%D8%A7%D9%88%D9%86-%D9%84%D8%A7%D9%8A%D9%86-%D9%85%D8%AA%D8%B1%D8%AC%D9%85%D9%87/',1,icon,fanart)
        addDir('[B][COLOR white]Indian Movies[/COLOR][/B]',baseurl+'/online/%d8%a7%d9%81%d9%84%d8%a7%d9%85-%d9%87%d9%86%d8%af%d9%8a-%d8%a7%d9%88%d9%86-%d9%84%d8%a7%d9%8a%d9%86/',1,icon,fanart)
        addDir('[B][COLOR white]Arabic Movies[/COLOR][/B]',baseurl+'/online/%d8%a7%d9%81%d9%84%d8%a7%d9%85-%d8%b9%d8%b1%d8%a8%d9%89-%d8%a7%d9%88%d9%86-%d9%84%d8%a7%d9%8a%d9%86/',2,icon,fanart)
        addDir('[B][COLOR white]Anime Movies[/COLOR][/B]',baseurl+'/online/%d8%a7%d9%81%d9%84%d8%a7%d9%85-%d8%a7%d9%86%d9%8a%d9%85%d9%89-%d8%a7%d9%88%d9%86-%d9%84%d8%a7%d9%8a%d9%86/',2,icon,fanart)
        addDir('[B][COLOR white]WWE SMAKDOWN & RAW [/COLOR][/B]',baseurl+'/online/%d9%85%d8%b5%d8%a7%d8%b1%d8%b9%d9%87-%d8%ad%d8%b1%d9%87-%d8%a7%d9%88%d9%86-%d9%84%d8%a7%d9%8a%d9%86/',1,icon,fanart)
        addDir('[B][COLOR white]Arabic TVshows[/COLOR][/B]',baseurl+'/online/%d9%85%d8%b3%d9%84%d8%b3%d9%84%d8%a7%d8%aa-%d8%b9%d8%b1%d8%a8%d9%8a-%d8%a7%d9%88%d9%86-%d9%84%d8%a7%d9%8a%d9%86/',2,icon,fanart)
        addDir('[B][COLOR white]English TVshows[/COLOR][/B]',baseurl+'/online/%d9%85%d8%b3%d9%84%d8%b3%d9%84%d8%a7%d8%aa-%d8%a7%d8%ac%d9%86%d8%a8%d9%89-%d8%a7%d9%88%d9%86-%d9%84%d8%a7%d9%8a%d9%86/',1,icon,fanart)
        addDir('[B][COLOR white]Ramadan TVshows[/COLOR][/B]',baseurl+'/online/%d9%85%d8%b3%d9%84%d8%b3%d9%84%d8%a7%d8%aa-%d8%a7%d8%b3%d9%8a%d9%88%d9%8a-%d8%a7%d9%88%d9%86-%d9%84%d8%a7%d9%8a%d9%86/',2,icon,fanart)
        addDir('[B][COLOR white]Turkish TVshows[/COLOR][/B]',baseurl+'/online/%d9%85%d8%b3%d9%84%d8%b3%d9%84%d8%a7%d8%aa-%d8%aa%d8%b1%d9%83%d9%8a-%d8%a7%d9%88%d9%86-%d9%84%d8%a7%d9%8a%d9%86/',2,icon,fanart)
        addDir('[B][COLOR white]Search[/COLOR][/B]','url',3,icon,fanart)
        


def INDEX(url):
        link = OPEN_URL(url)
        all_videos = regex_get_all(link, '<div class="moviefilm">', 'categoryFilm')
        items = len(all_videos)
        for a in all_videos:
                name = regex_from_to(a, 'alt="4filmk.com-', '">')
                name=re.sub(r'[^\x20-\x7e]', '', name)
                name = addon.unescape(name)
                name = name.encode('ascii', 'ignore').decode('ascii')
                #qual = regex_from_to(a, 'class="h3-quality".*?>', '<')#.replace('- Quality:','[COLOR gold]- Quality:[/COLOR]')
                url = regex_from_to(a, 'href="', '"')
                thumb = regex_from_to(a, 'src=', 'class="attachment').replace('"','')
                #epi = regex_from_to(a, '"h4-cat"<a title="Latest episode.*?">', '<')#.replace('Latest episode:','[COLOR gold]Latest episode:[/COLOR]')
                
                if 'view_online' in url:
                        name = name.replace('BluRay','[COLOR blue]BluRay[/COLOR]')
                        name = name.replace('WEB-DL','[COLOR red]WEB-DL[/COLOR]')
                        name = name.replace('HDRip','[COLOR green]HDRip[/COLOR]')
                        name = name.replace('HDTV','[COLOR green]HDTV[/COLOR]')
                        name = name.replace('HD','[COLOR green]HD[/COLOR]')
                        addDir(name,url,4,thumb,fanart)
        try:    
                url = re.compile(ur'<li><a href="(.+?)".+?</a></li>\n</ul></div>').findall(link)[0]
                url = url.replace('/page/', '/?page=')
                addDir('[I][B][COLOR dodgerblue]Go To Next Page>>>[/COLOR][/B][/I]',url,1,icon,fanart)
        except:pass


def INDEX2(url):
        link = OPEN_URL(url)
        all_videos = regex_get_all(link, '<div class="moviefilm">', 'categoryFilm')
        items = len(all_videos)
        for a in all_videos:
                name = regex_from_to(a, 'alt="4filmk.com-', '">')
                # name=re.sub(r'[^\x20-\x7e]', '', name)
                # name = addon.unescape(name)
                # name = name.encode('ascii', 'ignore').decode('ascii')
                #qual = regex_from_to(a, 'class="h3-quality".*?>', '<')#.replace('- Quality:','[COLOR gold]- Quality:[/COLOR]')
                url = regex_from_to(a, 'href="', '"')
                thumb = regex_from_to(a, 'src=', 'class="attachment').replace('"','')
                #epi = regex_from_to(a, '"h4-cat"<a title="Latest episode.*?">', '<')#.replace('Latest episode:','[COLOR gold]Latest episode:[/COLOR]')
                if 'view_online' in url:
                        name = name.replace('BluRay','[COLOR blue]BluRay[/COLOR]')
                        name = name.replace('WEB-DL','[COLOR red]WEB-DL[/COLOR]')
                        name = name.replace('HDRip','[COLOR green]HDRip[/COLOR]')
                        name = name.replace('HDTV','[COLOR green]HDTV[/COLOR]')
                        name = name.replace('HD','[COLOR green]HD[/COLOR]')
                        addDir(name,url,4,thumb,fanart)
        try:    
                url = re.compile(ur'<li><a href="(.+?)".+?</a></li>\n</ul></div>').findall(link)[0]
                url = url.replace('/page/', '/?page=')
                addDir('[I][B][COLOR dodgerblue]Go To Next Page>>>[/COLOR][/B][/I]',url,11,icon,fanart)
        except:pass



def LINK(name,url,iconimage):
    
    link = OPEN_URL(url)
    link = link.encode('UTF-8').decode('utf-8')
    media_url= re.compile('<IFRAME SRC="(.+?)"',re.DOTALL|re.IGNORECASE).findall(link)
    for url in media_url:
        name = url
        addDir2(name,url,5,iconimage,'','')
        # Don't forget to add ok.ru host.
        
def play_video(name,url): 
    
    url = urlresolver.resolve(url)
    liz = xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
    liz.setProperty("IsPlayable","true")
    liz.setPath(url)
    xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)

def getHtml2(url):
    req = Request(url)
    response = urlopen(req, timeout=60)
    data = response.read()
    response.close()
    return data 

def SEARCH():
        keyb = xbmc.Keyboard('', 'Search')
        keyb.doModal()
        if (keyb.isConfirmed()):
                search = keyb.getText().replace(' ','-')
                url = 'http://www.4filmk.com/?s='+search
                INDEX2(url)


def regex_from_to(text, from_string, to_string, excluding=True):
        if excluding:
                try: r = re.search("(?i)" + from_string + "([\S\s]+?)" + to_string, text).group(1)
                except: r = ''
        else:
                try: r = re.search("(?i)(" + from_string + "[\S\s]+?" + to_string + ")", text).group(1)
                except: r = ''
        return r


def regex_get_all(text, start_with, end_with):
        r = re.findall("(?i)(" + start_with + "[\S\s]+?" + end_with + ")", text)
        return r

def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param

def addDir2(name,url,mode,iconimage,fanart,description):
        name = name.replace('()','')
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name,"Plot":description} )
        liz.setProperty('fanart_image', fanart)
        liz.setProperty("IsPlayable","true")
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok

def addDir(name, url, mode, iconimage, fanart):
    u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + urllib.quote_plus(name) + "&iconimage=" + urllib.quote_plus(iconimage)
    ok = True
    liz = xbmcgui.ListItem(name, iconImage = "DefaultFolder.png", thumbnailImage = iconimage)
    liz.setInfo( type = "Video", infoLabels = { "Title": name } )
    liz.setProperty('fanart_image', fanart)
    if ('youtube.com/user/' in url) or ('youtube.com/channel/' in url) or ('youtube/user/' in url) or ('youtube/channel/' in url):
        u = 'plugin://plugin.video.youtube/%s/%s/' % (url.split( '/' )[-2], url.split( '/' )[-1])
        ok = xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url = u, listitem = liz, isFolder = True)
        return ok       
    ok = xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url = u, listitem = liz, isFolder = True)
    return ok

def OPEN_URL(url):
        headers = {}
        headers['User-Agent'] = User_Agent
        link = requests.get(url, headers=headers, allow_redirects=False).text
        link = link.encode('UTF-8')
        return link


params=get_params()
url=None
name=None
mode=None
iconimage=None
description=None
site=None




try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        iconimage=urllib.unquote_plus(params["iconimage"])
except:
        pass
try:        
        mode=int(params["mode"])
except:
        pass
try:
        description=urllib.unquote_plus(params["description"])
except:
        pass


if mode==None or url==None or len(url)<1:
        CAT()

elif mode==1:
        INDEX(url)

elif mode==2:
        INDEX2(url)

elif mode==3:
        SEARCH()

elif mode==4:
        LINK(name,url,iconimage)   

elif mode==5:
        play_video(name,url)

xbmcplugin.endOfDirectory(int(sys.argv[1]))