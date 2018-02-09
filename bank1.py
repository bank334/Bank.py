# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
from bs4 import BeautifulSoup
from googletrans import Translator
from gtts import gTTS
import wikipedia
import html5lib,shutil
import time,random,sys,json,codecs,threading,glob,urllib,urllib2,urllib3,re,ast,os,subprocess,requests,tempfile

#kk = LINETCR.LINE()
#kk.login(qr=True)
#kk.loginResult()

cl = LINETCR.LINE()
cl.login(token="Epi71af9Ht5Ki1kfRUlf.ICpPiGD6lKxQUjAskbI4lW.WmzsyphjRnTP4dc6cqW0tPFed0l+MMvyvEx6TyIHadk=")
cl.loginResult()

satpam = LINETCR.LINE() # Koplaxs # Login Pake Akun Utama Kalian(Gunanya Supaya Akun Utama Ke Kick bisa Terima Undangan dari Bot Otomatis)
satpam.login(token="EpmkPGswRbUwM7tiHdP4.QXYHCXzQnIXP72luipN3Ha.HvNi//mpiR9Wq3M9B6dRTLrtDYPgA5sJNQn95BAg6yU=")
satpam.loginResult()

ki = LINETCR.LINE()
ki.login(token="Ep205ooa2paIlQD4fF36.0ClDQ0XXExcmqznHTHonrG.ePxVhUViVxzDt/MTlVPoHRyXtIjYdFPSBnkQgR+GEEE=")
ki.loginResult()

kk = LINETCR.LINE()
kk.login(token="EpMQ0BlQZFd1V1sh3BWb.56Q6F8HJ0G7hxHXo37fg6W.Czy5Ky+JBDFT6oX1cu8S6tjtBthS2RRIkRLE5exGujg=")
kk.loginResult()

ks = LINETCR.LINE()
ks.login(token="EpPnFYjf8JgeGDjg8iN9.q+GCiS+H2/Jt0U2vphfDcq./x1OuKAPjCkxfbrJ0tJp9+HNmhwIS36urRtv9oxdnc4=")
ks.loginResult()

ka = LINETCR.LINE()
ka.login(token="EpmkwLjzgcNxnWDiq6Zd.K2HqbjOiKELgUqJfBR1jZq.+yQZFHDaUrsRGeHBpjj7Bsk1hg18j/k//34tkC0Jd5Y=")
ka.loginResult()

kc = LINETCR.LINE()
kc.login(token="EpsvFQLyEKWGzfVsNKm2.BM8ZzCvoIdukCQza1HyZGG.wh4j1RRd2Tc1fkaKwThiZIe6e0ty9jx3MDDexyFbZpE=")
kc.loginResult()

kb = LINETCR.LINE()
kb.login(token="EpwWpxc0iAczxj8ieWmf.A48KdZfnSSzOHMavgsN8dW.pFZhl2M4v4kj63+BApWFIPq9EIQiU5Qg1elKDXiEc/s=")
kb.loginResult()

km = LINETCR.LINE()
km.login(token="EpFrt6RnLUmdHBVfbwI7.qSWU/6UEE3rWWs4Pndd5jW.19GrE3gG/jGDsTPm/ZEgUA6z8HHe9Fa0l0APu6nXJ7Q=")
km.loginResult()

cl

ko = ki

ku = kk

ks

ke = ka

kb

kc
print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage= """\n
═╬════════►∆∆
   Help
═╬════════► 
♦Help edit
♦Help demoted
♦Help steal
♦Help secur
♦Help ban
♦Help invite
♦Help grup
♦Help media
♦Help set
♦Help cancel
♦Help gift
♦Help notif
♦Help kiker
♦Help spam
♦Help utility
♦Help bc
═╬════════►
●▬▬▬▬๑۩line.me/ti/p/~geva7۩๑▬▬▬▬▬●
"""

editedMessage= """\n
═╬════════►∆∆
    Edited     
═╬════════► 
🔘 My name    :  |╬|
🔘 Bot2 rename:  |╬|
🔘 Bot3 rename:  |╬|
🔘 Bot4 rename:  |╬|
🔘 Bot5 rename:  |╬|
🔘 Bot6 rename:  |╬|
🔘 All rename:   |╬|
🔘 Allbio:       |╬|
🔘 My clone   @  |╬|
🔘 Bot2 clone @  |╬|
🔘 Bot3 clone @  |╬|
🔘 Bot4 clone @  |╬|
🔘 Bot5 clone @  |╬|
🔘 Bot6 clone @  |╬|
🔘 Comment:      |╬|
🔘 Message:      |╬|
🔘 Bot1-6 backup |╬|
🔘 Bot1-6 backup |╬|
🔘 Group name:   |╬|
═╬════════►∆∆
"""

demotedMessage= """\n
═╬════════►∆∆
   Demoted
═╬════════►
 |╬| Admin on @
 |╬| Expel on @
 |╬| Expel staff @
 |╬| Add staff @
 |╬| Expelal
═╬════════►∆∆
"""

stealMessage= """\n
═╬════════►
   Steal
═╬════════►
 |╬| Steal
 |╬| Steal name    @
 |╬| Getbio     @
 |╬| Getmid     @
 |╬| Steal status  @
 |╬| Steal mid     @
 |╬| Steal contact @
 |╬| Steal cover   @
 |╬| Steal pict    @
 |╬| Steal group pict
 |╬| Midpict:   [mid]
 |╬| Pict group [name]
 |╬| My pict
 |╬| My cover
 |╬| My name
 |╬| My bio
 |╬| Pap set:
 |╬| Pap
 |╬| Image      [Text]
 |╬| Idline
═╬════════►∆∆
"""

securMessage= """\n
═╬════════►
   SECURITY
═╬════════►
 |╬| Protect:low
 |╬| Protect:hight
 |╬| Autokick on/off
═╬════════►∆∆
"""

banMessage= """\n
═╬════════►
   BANNED
═╬════════►
 |╬| Ban            @
 |╬| Unban          @
 |╬| Banned
 |╬| Unbanned
 |╬| Ban repeat     @
 |╬| Add friend     @
 |╬| Clear banlist
═╬════════►∆∆
"""

inviteMessage= """\n
═╬════════►
   INVITE
═╬════════►
 |╬| Invite:[mid]
 |╬| Invite user[contact]
 |╬| Invite
 |╬| Inviteme: [for creator]
═╬════════►∆∆
"""

grupMessage= """\n
═╬════════►
   GRUP
═╬════════►
 |╬| My waifu sini [Bot assist join]
 |╬| Bot2   @bye
 |╬| Bot3   @bye
 |╬| Bot4   @bye
 |╬| Bot5   @bye
 |╬| Bot6   @bye
 |╬| Cl keluarallgrup
 |╬| Recover
 |╬| @Bye
 |╬| Bye allgroups[own]
═╬════════►∆∆
"""

setMessage= """\n
═╬════════►
   SET BOT
═╬════════►
 |╬| Auto reinvite:on/off
 |╬| Auto join:on/off
 |╬| Protect:hight/low
 |╬| Auto leave:on/off
 |╬| Auto like:on/off
 |╬| Like friend:on/off
 |╬| Sambutan on/off
 |╬| Auto notice:on/off
 |╬| Blockinvite:on/off
 |╬| Gr on/off
 |╬| Kicktag on/off
 |╬| Respontag on/off
 |╬| Autokick on/off
 |╬| Cancl on/off
 |╬| Joinn on/off
 |╬| Prot on/off
 |╬| Namelock:on/off
 |╬| Auto add:on/off
 |╬| Ghost on/off
 |╬| Media:on/off
 |╬| Check message
 |╬| Add message:
 |╬| Comment:on/off
 |╬| Add comment:
 |╬| Check comment
 |╬| Backup:on/off
 |╬| Gcancel:
 |╬| Update welcome:
 |╬| Check welcome message
═╬════════►∆∆
"""

cancelMessage= """\n
═╬════════►
   CANCEL
═╬════════►
 |╬| Rejectall
 |╬| Clean invites
 |╬| Clear invites
═╬════════►∆∆
"""

giftMessage= """\n
═╬════════►
   GIFT
═╬════════►
 |╬| gift1-15
 |╬| Spam gift
 |╬| Gift @
═╬════════►∆∆
"""

notifMessage= """\n
═╬════════►
NOTIFICATION
═╬════════►
 |╬| Gruplist
 |╬| Banlist
 |╬| Grupid
 |╬| Adminlist
 |╬| Creatlist
 |╬| Stafflist
 |╬| Settings
 |╬| Ginfo
 |╬| TL:[text]
 |╬| Set member:
 |╬| Micdel          @
 |╬| Micadd          @
═╬════════►∆∆
"""

kikerMessage= """\n
═╬════════►
   KICKER
═╬════════►
 |╬| cleansemua
 |╬| Vkick @
 |╬| Nk [name]
 |╬| Kick:[mid]
 |╬| Purge
═╬════════►∆∆
"""

spamMessage= """\n
═╬════════►
   SPAM
═╬════════►
 |╬| Spamg[on/off]
 |╬| Spam add:
 |╬| Spam change:
 |╬| Spam start:[number]
 |╬| Spam @
 |╬| Cium! [mid]
 |╬| Say a̸͟͞a̸͟͞a̸͟͞
 |╬| Me
 |╬| Speed
 |╬| Debug speed
 |╬| My mid
 |╬| Gcreator
 |╬| Halo
 |╬| Bot contact
 |╬| Bot mid
 |╬| Creator
 |╬| System
 |╬| Iconfig
 |╬| Kernel
 |╬| Cpu
 |╬| Crash
 |╬| Respon/sname
 |╬| Timebot
 |╬| Mc:[mid]
 |╬| runtim
 |╬| show offenders:on/off
═╬════════►∆∆
"""

utilityMessage= """\n
═╬════════►
   UTILITY
═╬════════►
 |╬| Lurking
 |╬| Result
 |╬| Setlastpoint
 |╬| Viewlastseen
 |╬| Open url
 |╬| Close url
 |╬| Gurl
 |╬| Remove chat
 |╬| Bot restart
═╬════════►∆∆
"""

mediaMessage= """\n
═╬════════►
   MEDIA
═╬════════►
 |╬| Lyric 
 |╬| Music 
 |╬| Wiki 
 |╬| Vidio 
 |╬| Youtube 
 |╬| Instagram 
 |╬| Translate-idn   [text]
 |╬| Translate-eng   [text]
 |╬| Translate-thai  [text] 
 |╬| Translate-japan [text]
 |╬| Translate-arab  [text]
 |╬| Translate-korea [text]
 |╬| Translate-chin  [text]
 |╬| Vn-id           [text]
 |╬| Vn-en           [text]
 |╬| Vn-jp           [text]
 |╬| Kalender
 |╬| Vn     [Text]
 |╬| Cek zodiak [Tggl-bulan-tahun]
 |╬| Tag on/off
 |╬| Emoji [expression]
 |╬| Info @[name]
 |╬| Ping
 |╬| Time
 |╬| Dosa [text]
 |╬| Pahala [text]
 |╬| apakah
 |╬| kerang ajaib
 |╬| Sticker [expression]
 |╬|Summon [Tag all
═╬════════►∆∆
"""

bcMessage= """\n
═╬════════►
 BROADCAST
═╬════════►
 |╬| Pm cast   
 |╬| Broadcast 
 |╬| Spam @[name]
═╬════════►
"""

textspeech= """╔═════════════════
║  			TEXT TO SPEECH
╠═════════════════
╠➩ 'af' : 'Afrikaans'
╠➩ 'sq' : 'Albanian'
╠➩ 'ar' : 'Arabic'
╠➩ 'hy' : 'Armenian'
╠➩ 'bn' : 'Bengali'
╠➩ 'ca' : 'Catalan'
╠➩ 'zh' : 'Chinese'
╠➩ 'zhcn' : 'Chinese (Mandarin/China)'
╠➩ 'zhtw' : 'Chinese (Mandarin/Taiwan)'
╠➩ 'zhyue' : 'Chinese (Cantonese)'
╠➩ 'hr' : 'Croatian'
╠➩ 'cs' : 'Czech'
╠➩ 'da' : 'Danish'
╠➩ 'nl' : 'Dutch'
╠➩ 'en' : 'English'
╠➩ 'enau' : 'English (Australia)'
╠➩ 'enuk' : 'English (United Kingdom)'
╠➩ 'enus' : 'English (United States)'
╠➩ 'eo' : 'Esperanto'
╠➩ 'fi' : 'Finnish'
╠➩ 'fr' : 'French'
╠➩ 'de' : 'German'
╠➩ 'el' : 'Greek'
╠➩ 'hi' : 'Hindi'
╠➩ 'hu' : 'Hungarian'
╠➩ 'is' : 'Icelandic'
╠➩ 'id' : 'Indonesian'
╠➩ 'it' : 'Italian'
╠➩ 'jp' : 'Japanese'
╠➩ 'km' : 'Khmer (Cambodian)'
╠➩ 'ko' : 'Korean'
╠➩ 'la' : 'Latin'
╠➩ 'lv' : 'Latvian'
╠➩ 'mk' : 'Macedonian'
╠➩ 'no' : 'Norwegian'
╠➩ 'pl' : 'Polish'
╠➩ 'pt' : 'Portuguese'
╠➩ 'ro' : 'Romanian'
╠➩ 'ru' : 'Russian'
╠➩ 'sr' : 'Serbian'
╠➩ 'si' : 'Sinhala'
╠➩ 'sk' : 'Slovak'
╠➩ 'es' : 'Spanish'
╠➩ 'eses' : 'Spanish (Spain)'
╠➩ 'esus' : 'Spanish (United States)'
╠➩ 'sw' : 'Swahili'
╠➩ 'sv' : 'Swedish'
╠➩ 'ta' : 'Tamil'
╠➩ 'th' : 'Thai'
╠➩ 'tr' : 'Turkish'
╠➩ 'uk' : 'Ukrainian'
╠➩ 'vi' : 'Vietnamese'
╠➩ 'cy' : 'Welsh'
╚═════════════════
"""

Setgroup =""" Privasi Menu V.1 􀔃􀄆red check mark􏿿
[Protect Group]
-- Gr on/off
[Mid Via Contact]
 -- Contact on/off
[Cancel All Invited]
-- Cancl on/off
[No Joinned]
-- Joinn on/off
"""
KAC=[cl,kk,ke,kc,kb,ka]
DEF=[ka,ki,ks,ko,ku,cl,kk,ke,kc,kb,ka]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
Dmid = ks.getProfile().mid
Emid = ka.getProfile().mid
Fmid = kb.getProfile().mid
Gmid = ko.getProfile().mid
Hmid = ke.getProfile().mid
Imid = ku.getProfile().mid
Jmid = km.getProfile().mid
Smid = satpam.getProfile().mid #Akun Utama


Bots=[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Smid,Jmid,"u5427d8047ab127f5e237eaedd1f0b93b","uab1ca173166a362c69ef62d420f9f784","u051cd9062ec1528d9e16cc784efca04b"]
admin=["uab1ca173166a362c69ef62d420f9f784","ue43898158971147528350ad49b5e8df4","u3d27c322e83dac8c6ad9a2adf12dbf92","u8065b0be04ba4f39ea865a23ab6ba20e",mid]
staff=["u37470b87308ba0c907d493205cbe2676","uc6dc9e8314e8fc3e2834631f4b048506","u5c80975703f4c22a6b3a8811bb40d09e","ue5cd76e14ab4783e702df35a29b4ee3c","u542ca87275438b089fffb6d8adc49c07","ud14122efeea90e7354f3619ad86bb1a2","u8fba8c8444fcf7ff8b34f1f0f2cd6db1"]
creator=["u5427d8047ab127f5e237eaedd1f0b93b","uab1ca173166a362c69ef62d420f9f784","u051cd9062ec1528d9e16cc784efca04b"]
peminjam=[]
adminsa=["u5427d8047ab127f5e237eaedd1f0b93b","uab1ca173166a362c69ef62d420f9f784"]
pembuat=["uab1ca173166a362c69ef62d420f9f784"]
wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True,
    'detectMention':True,    
    'kickMention':False,
    'creatorMention':True,
    'message':"cie ngeadd yaa makasihh",
    'message2':"Cuman creator yg bisa inpit grup",
    "lang":"JP",
    "comment1":"Nice kak",
    "comment2":"Wkwkwk ＼（○＾ω＾○）／",
    "comment3":"Lucu Banget!!! ヘ(^_^)ヘ",
    "comment4":"Nice Kak (^_^)",
    "comment5":"ciee",
    "commentOn":True,
    "welmsg":" Selamat Datang di ",
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "Ghost":False,
    "MENTION":True,
    "media":False,
    "cName":" ",
    "blacklist":{},
    "whitelist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Protectgr":True,
    "protect":False,
    "kickblack":True,
    "alwayRead":False,
    "AutoKick":True,
    "likeOn":False,
    "welcomemsg":True,
    "winvite":{},
    "invite":{},
    "autorein":True,
    "Protectjoin":False,
    "Protectcancl":False,
    "Backup":True,
    "protectionOn":False,
    "atjointicket":True,
    "Pap":["https://i.imgflip.com/1bqcxs.jpg","http://kucingpedia.com/wp-content/uploads/2016/06/Gambar-Kucing-Gemuk-Lucu.jpg","https://cdn.brilio.net/news/2015/06/23/6759/750xauto-25-meme-kucing-yang-imut-ngegemesin-dan-bikin-ketawa-150623c.jpg","https://cdn.brilio.net/news/2015/06/23/6759/21164-meme-kucing-7-9.jpg","http://m.memegen.com/kccbqe.jpg","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ--0ihgvcclOlusyzB1I2pVfenjEfkA7emCu_NR-atnyDlLbh0"],
    "SetKey":".",
    "spam":"Hayo gw spamin lu inget lu harus tobat jgn deh lu lakuin yg gk gk smp ngancurin hiduplu hidup cuman sebentar",
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }


settings = {
    "simiSimi":{}
    }

setTime = {}
setTime = wait2['setTime']
mulai = time.time() 

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     #If the Current Version of Python is 3.0 or above
        import urllib,request    #urllib library for Extracting web pages
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        #If the Current Version of Python is 2.x
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"

#Finding 'Next Image' from the given raw page
def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    #If no links are found then give an error!
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+90)
        end_content = s.find(',"ow"',start_content-90)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content

#Getting all links with the help of '_images_get_next_image'
def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      #Append all the links in the list named 'Links'
            time.sleep(0.1)        #Timer could be used to slow down the request for image downloads
            page = page[end_content:]
    return items

def upload_tempimage(client):
     '''
         Upload a picture of a kitten. We don't ship one, so get creative!
     '''
     config = {
         'album': album,
         'name':  'bot auto upload',
         'title': 'bot auto upload',
         'description': 'bot auto upload'
     }

     print("Uploading image... ")
     image = client.upload_from_path(image_path, config=config, anon=False)
     print("Done")
     print()

     return image
     
def sendAudio(self, to_, path):
       M = Message()
       M.text = None
       M.to = to_
       M.contentMetadata = None
       M.contentPreview = None
       M.contentType = 3
       M_id = self._client.sendMessage(0,M).id
       files = {
             'file': open(path,  'rb'),
       }
     
def sendImage(self, to_, path):
      M = Message(to=to_, text=None, contentType = 1)
      M.contentMetadata = None
      M.contentPreview = None
      M2 = self._client.sendMessage(0,M)
      M_id = M2.id
      files = {
         'file': open(path, 'rb'),
      }
      params = {
         'name': 'media',
         'oid': M_id,
         'size': len(open(path, 'rb').read()),
         'type': 'image',
         'ver': '1.0',
      }
      data = {
         'params': json.dumps(params)
      }
      r = self.post_content('https://obs-sg.line-apps.com/talk/m/upload.nhn', data=data, files=files)
      if r.status_code != 201:
         raise Exception('Upload image failure.')
      return True


def sendImageWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download image failure.')
      try:
         self.sendImage(to_, path)
      except:
         try:
            self.sendImage(to_, path)
         except Exception as e:
            raise e

def sendAudio(self, to_, path):
        M = Message()
        M.text = None
        M.to = to_
        M.contentMetadata = None
        M.contentPreview = None
        M.contentType = 3
        M_id = self._client.sendMessage(0,M).id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'media',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'audio',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }
        r = self.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Upload audio failure.')
        return True

def sendAudioWithURL(self, to_, url):
        path = self.downloadFileWithURL(url)
        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise Exception(e)

def sendAudioWithUrl(self, to_, url):
        path = '%s/pythonLine-%1.data' % (tempfile.gettempdir(), randint(0, 9))
        r = requests.get(url, stream=True, verify=False)
        if r.status_code == 200:
           with open(path, 'w') as f:
              shutil.copyfileobj(r.raw, f)
        else:
           raise Exception('Download audio failure.')
        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise e
            
def downloadFileWithURL(self, fileUrl):
        saveAs = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
        r = self.get_content(fileUrl)
        if r.status_code == 200:
            with open(saveAs, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
            return saveAs
        else:
            raise Exception('Download file failure.')

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv) 
	
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d hour %02d minute %02d seconds' % (hours, mins, secs)
	

def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print "Mention"
    try:
       cl.sendMessage(msg)
    except Exception as error:
       print error

def yt(query):
    with requests.session() as s:
         isi = []
         if query == "":
             query = "S1B tanysyz"   
         s.headers['user-agent'] = 'Mozilla/5.0'
         url    = 'http://www.youtube.com/results'
         params = {'search_query': query}
         r    = s.get(url, params=params)
         soup = BeautifulSoup(r.content, 'html5lib')
         for a in soup.select('.yt-lockup-title > a[title]'):
            if '&list=' not in a['href']:
                if 'watch?v' in a['href']:
                    b = a['href'].replace('watch?v=', '')
                    isi += ['youtu.be' + b]
         return isi

def sendText(self, Tomid, text):
        msg = Message()
        msg.to = Tomid
        msg.text = text

        return self.Talk.client.sendMessage(0, msg)
def sendImage(self, to_, path):
        M = Message(to=to_,contentType = 1)
        M.contentMetadata = None
        M.contentPreview = None
        M_id = self._client.sendMessage(M).id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'media',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'image',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }
        r = self._client.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Upload image failure.')
        #r.content
        return True



 
def post_content(self, urls, data=None, files=None):
        return self._session.post(urls, headers=self._headers, data=data, files=files)

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def sendMessage(self, messageObject):
        return self.Talk.client.sendMessage(0,messageObject)

def sendText(self, Tomid, text):
        msg = Message()
        msg.to = Tomid
        msg.text = text
	
def sendMessage(self, messageObject):
        return self.Talk.client.sendMessage(0,messageObject)

def post_content(self, urls, data=None, files=None):
        return self._session.post(urls, headers=self._headers, data=data, files=files)
def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name
                wait2['ROM'][op.param1][op.param2] = "・" + Name
        else:
            pass
    except:
        pass


def autoSta():
    count = 1
    while True:
        try:
           for posts in cl.activity(1)["result"]["posts"]:
             if posts["postInfo"]["liked"] is False:
                if wait["likeOn"] == True:
                   cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   ki.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   kk.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   ka.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   ke.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   km.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   if wait["commentOn"] == True:
                      if posts["userInfo"]["writerMid"] in wait["commentBlack"]:
                         pass
                      else:
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          ki.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          kk.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          km.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          ka.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          ke.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])												  
        except:
            count += 1
            if(count == 50):
                sys.exit(0)
            else:
                pass
												  

def likefriend():
    for zx in range(0,20):
      hasil = cl.activity(limit=20)
      if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
        try:
           cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
           ki.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
           kk.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
           ka.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
           ke.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
           print "Like"
	except:
              pass
      else:
	  pass	
def likeme():
    for zx in range(0,20):
        hasil = cl.activity(limit=20)
        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
            if hasil['result']['posts'][zx]['userInfo']['mid'] in creator:
                try:
                    cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    ki.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    kk.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    ka.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    ke.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
		    print "Like"
                except:
                    pass
            else:
                print "Status Sudah di Like"

def RECEIVE_MESSAGE(op):
    msg = op.message
    try:
        if msg.contentType == 0:
            try:
                if msg.to in wait2['readPoint']:
                    if msg.from_ in wait2["ROM"][msg.to]:
                        del wait2["ROM"][msg.to][msg.from_]
                else:
                    pass
            except:
                pass
        else:
            pass
          
    except KeyboardInterrupt:
				sys.exit(0)

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
                    cl.sendText(op.param1,str(wait["message2"]))
           #------Protect Group Kick start------#
                #------Protect Group Kick start------#
        if op.type == 11:
          if wait["Protectgr"] == True:
            if op.param2 in Bots:
                pass
            elif op.param2 in admin:
                pass
            elif op.param2 in creator + peminjam:
                pass
            elif op.param2 in staff:
                  pass
            else:
               G = random.choice(KAC).getGroup(op.param1)
               G.preventJoinByTicket = False
	       cl.updateGroup(G)
               Ticket = cl.reissueGroupTicket(op.param1)
               km.acceptGroupInvitationByTicket(op.param1,Ticket)
	       G.preventJoinByTicket = True
               km.updateGroup(G)
               km.kickoutFromGroup(op.param1,[op.param2])
               km.leaveGroup(op.param1)
               random.choice(KAC).sendText(op.param1,random.choice(KAC).getContact(op.param2).displayName + " Jangan otak atik  grup Njiiir")
               wait["blacklist"][op.param2] = True
               f=codecs.open('st2__b.json','w','utf-8')
               json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)	
        #------Protect Group Kick finish-----#    

        #------Protect Group Kick finish-----#
        if op.type == 19:
	 if wait["Ghost"] == True:
          if op.param2 in creator:
             if op.param2 in admin:
                if op.param2 in staff:
                  if op.param2 in Bots + peminjam:	
                      pass
                  else:
                      try:
                          G = cl.getGroup(op.param1)
                          G.preventJoinByTicket = False
                          cl.updateGroup(G)
                          Ticket = cl.reissueGroupTicket(op.param1)
                          km.acceptGroupInvitationByTicket(op.param1,Ticket)
                          time.sleep(0.01)
                          km.kickoutFromGroup(op.param1,[op.param2])
                          c = Message(to=op.param1, from_=None, text=None, contentType=13)
                          c.contentMetadata={'mid':op.param2}
                          km.sendMessage(c)
                          km.leaveGroup(op.param1)
                          G.preventJoinByTicket = True
                          cl.updateGroup(G)
                          wait["blacklist"][op.param2] = True
                      except:
                          G = cl.getGroup(op.param1)
                          G.preventJoinByTicket = False
                          cl.updateGroup(G)
                          Ticket = cl.reissueGroupTicket(op.param1)
                          km.acceptGroupInvitationByTicket(op.param1,Ticket)
                          time.sleep(0.01)
                          km.kickoutFromGroup(op.param1,[op.param2])
                          c = Message(to=op.param1, from_=None, text=None, contentType=13)
                          c.contentMetadata={'mid':op.param2}
                          km.sendMessage(c)
                          km.leaveGroup(op.param1)
                          G.preventJoinByTicket = True
                          cl.updateGroup(G)
                          wait["blacklist"][op.param2] = True				
        if op.type == 17:		
          if wait["welcomemsg"] == True:
            if op.param2 in Bots + peminjam:
                return				
            ginfo = cl.getGroup(op.param1)
            contact = cl.getContact(op.param2)
            image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
            cl.sendImageWithURL(op.param1,image)
            cl.sendText(op.param1,"Halo " + cl.getContact(op.param2).displayName  + "\nJones" +  wait["welmsg"] + str(ginfo.name) + " ☜" + "\nBudayakan Cek Note\nDan Semoga Betah Disini ^_^")
            print "MEMBER JOIN TO GROUP"			
			
        if op.type == 15:
          if wait["welcomemsg"] == True:
            if op.param2 in Bots + peminjam:
                return	     	
            cl.sendText(op.param1,"Good Bye " + cl.getContact(op.param2).displayName +  "\nSee You Next Time . . . (p′︵‵。) 🤗")
            print "MEMBER HAS LEFT THE GROUP"	

        #------Cancel Invite User start------#
        if op.type == 13:
          if wait["Protectcancl"] == True:
            group = cl.getGroup(op.param1)
            gMembMids = [contact.mid for contact in group.invitee]
            if op.param2 in Bots + staff + creator + admin  + peminjam:
              pass
            else:
              cl.cancelGroupInvitation(op.param1, gMembMids)
              random.choice(KAC).sendText(op.param1, "Sorry you not admin😛")
   	  if op.param3 in wait["blacklist"]:
              random.choice(KAC).cancelGroupInvitation(op.param1, [op.param3])
              random.choice(KAC).sendText(op.param1, "Blacklist Detected")
  	  else:
	 	pass	    	
        #------Cancel Invite User Finish------#      
		

#--------------NOTIFIED_INVITE_INTO_GROUP----------------
        if op.type == 13:
            if mid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots + peminjam + creator:
                  cl.acceptGroupInvitation(op.param1)
		  cl.sendText(op.param1,"☆Ketik ☞Help☜ Untuk Bantuan☆\n☆Harap Gunakan Dengan Bijak ^_^ ☆")	
		  cl.sendText(op.param1,helpMessage)
                else:
                  cl.rejectGroupInvitation(op.param1)
		
		
            if Amid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots + peminjam + creator:
                  ki.acceptGroupInvitation(op.param1)
                else:
                  ki.rejectGroupInvitation(op.param1)
		
            if Bmid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots + peminjam + creator:
                  kk.acceptGroupInvitation(op.param1)
                else:
                  kk.rejectGroupInvitation(op.param1)
		
            if Cmid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots +  peminjam + creator:
                  kc.acceptGroupInvitation(op.param1)
                else:
                  kc.rejectGroupInvitation(op.param1)
		
            if Dmid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots + peminjam + creator:
                  ks.acceptGroupInvitation(op.param1)
                else:
                  ks.rejectGroupInvitation(op.param1)
		
            if Emid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots + peminjam + creator:
                  ka.acceptGroupInvitation(op.param1)
                else:
                  ka.rejectGroupInvitation(op.param1)
		
            if Fmid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots + peminjam + creator:
                  kb.acceptGroupInvitation(op.param1)
                else:
                  kb.rejectGroupInvitation(op.param1)
                
            if Gmid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots + peminjam +  creator:
                  ko.acceptGroupInvitation(op.param1)
                else:
                  ko.rejectGroupInvitation(op.param1)
                
            if Hmid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots + peminjam + creator:
                  ke.acceptGroupInvitation(op.param1)
                else:
                  ke.rejectGroupInvitation(op.param1)
                    
            if Imid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots + peminjam + creator:
                  ku.acceptGroupInvitation(op.param1)
                else:
                  ku.rejectGroupInvitation(op.param1)   
		
            if Jmid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots + peminjam + crator:
                  km.acceptGroupInvitation(op.param1)
                else:
                  km.rejectGroupInvitation(op.param1)   
		
            if Smid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots + creator:
                  satpam.acceptGroupInvitation(op.param1)
                else:
                  satpam.rejectGroupInvitation(op.param1)   
		                                		
        if op.type == 13:
            print op.param1
            print op.param2
            print op.param3
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)			
 
        if op.type == 17:
          if op.param2 not in Bots:
                if op.param2 in Bots:
                    pass
                elif op.param2 in admin:
                    pass
                elif op.param2 in staff:
                    pass
                elif op.param2 in creator + peminjam:
                    pass	
          if wait["kickblack"] == True:
               if wait["blacklist"][op.param2] == True:
                    try:
                        random.choice(DEF).kickoutFromGroup(op.param1,[op.param2])
			cl.sendText(op.param1,"Blacklist gk pantes disini")
                        G = cl.getGroup(op.param1)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			    cl.sendText(op.param1,"Blacklist gk pantes disini")
                            G = random.choice(KAC).getGroup(op.param1)
                            G.preventJoinByTicket = True
                            cl.updateGroup(G)
                        except:
                            pass
		
        #------Joined User Kick start------#

        #------Joined User Kick start------#

        if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n・ " + Name + datetime.today().strftime(' [%d - %H:%M:%S]')
                        wait2['ROM'][op.param1][op.param2] = "・ " + Name
                        wait2['setTime'][msg.to] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                else:
                    pass
            except:
                pass
		
        if op.type == 26:
            msg = op.message
            if msg.to in settings["simiSimi"]:
                if settings["simiSimi"][msg.to] == True:
                    if msg.text is not None:
                        text = msg.text
                        r = requests.get("http://api.ntcorp.us/chatbot/v1/?text=" + text.replace(" ","+") + "&key=beta1.nt")
                        data = r.text
                        data = json.loads(data)
                        if data['status'] == 200:
                            if data['result']['result'] == 100:
                                cl.sendText(msg.to,data['result']['response'].encode('utf-8'))
            if "MENTION" in msg.contentMetadata.keys() != None:
                 if wait['detectMention'] == True:
                     contact = cl.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["Don't Tag Me! iam Bussy!, ",cName + "Ada perlu apa, ?",cName + " pc aja klo urgent! sedang sibuk,", "kenapa, ", cName + " kangen?","kangen bilang gak usah tag tag, " + cName, "knp?, " + cName, "apasi?, " + cName + "?", "pulang gih, " + cName + "?","aya naon, ?" + cName + "Tersangkut -_-","Ada apa sih mblo?, "]
                     ret_ = "." + random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in mid:
                                  cl.sendText(msg.to,ret_)
                                  break
				
            if "MENTION" in msg.contentMetadata.keys() != None:
                 if wait['creatorMention'] == True:
                     contact = cl.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["Ada apa sih?","ngapain tag gw?","kangen gw?","Lah jones ngapain tag gw?","klo penting pc gw aja?"]
                     ret_ = random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in pembuat:
                                  satpam.sendText(msg.to,ret_)
                                  break				
                    
            if "MENTION" in msg.contentMetadata.keys() != None:
                 if wait['kickMention'] == True:
                     contact = cl.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["Dont Tag Me!! Im Busy, ",cName + " Ngapain Ngetag?, ",cName + " Nggak Usah Tag-Tag! Kalo Penting Langsung Pc Aja, ", "-_-, ","Kris lagi off, ", cName + " Kenapa Tag saya?, ","SPAM PC aja, " + cName, "Jangan Suka Tag gua, " + cName, "Kamu siapa, " + cName + "?", "Ada Perlu apa, " + cName + "?","Tag doang tidak perlu., ","Ada apa sih mblo?, "]
                     ret_ = "[Auto Respond] " + random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)
                                  cl.kickoutFromGroup(msg.to,[msg.from_])
                                  break		
					
            if msg.contentType == 13:
                if wait['winvite'] == True:
                     _name = msg.contentMetadata["displayName"]
                     invite = msg.contentMetadata["mid"]
                     groups = random.choice(KAC).getGroup(msg.to)
                     pending = groups.invitee
                     targets = []
                     for s in groups.members:
                         if _name in s.displayName:
                             ra.sendText(msg.to, _name + " Berada DiGrup Ini")
                         elif invite in wait["blacklist"]:
                           random.choice(KAC).sendText(msg.to,"Maaf, " + _name + " kena Blacklist")
                           random.choice(KAC).sendText(msg.to,"hubungi owner kami ya !, \n➡Unban: " + invite)			  
                         else:
                             targets.append(invite)
                     if targets == []:
                         pass
                     else:
                         for target in targets:
                             try:
                                 random.choice(KAC).findAndAddContactsByMid(target)
                                 random.choice(KAC).inviteIntoGroup(msg.to,[target])
                                 random.choice(KAC).sendText(msg.to,"Invite " + _name)
                                 wait['winvite'] = False
                                 break                              
                             except:             
                                      random.choice(KAC).sendText(msg.to,"Limit invite")
                                      wait['winvite'] = False
                                      break
					
            if msg.text in ["Crash","crash","/crash"]:
              dia = ("CACAT MAINANNYA CRASH","Tercyduck ingin ngecrash","Kamu asu ngecrash terus!")
              ket = random.choice(dia)
              cl.sendText(msg.to,ket)
              random.choice(DEF).kickoutFromGroup(msg.to,[msg.from_])
              cl.sendText(msg.to,"Mampus! gila lu kang crash")
            if msg.contentType == 16:
                if wait['likeOn'] == True:
                     url = msg.contentMetadata["postEndUrl"]
                     cl.like(url[25:58], url[66:], likeType=1005)
                     ki.like(url[25:58], url[66:], likeType=1002)
                     kk.like(url[25:58], url[66:], likeType=1004)
                     kc.like(url[25:58], url[66:], likeType=1003)
                     kb.like(url[25:58], url[66:], likeType=1001)
                     cl.comment(url[25:58], url[66:], wait["comment1"])
                     ki.comment(url[25:58], url[66:], wait["comment2"])
                     kk.comment(url[25:58], url[66:], wait["comment3"])
                     kc.comment(url[25:58], url[66:], wait["comment4"])
                     kb.comment(url[25:58], url[66:], wait["comment5"])
                     cl.sendText(msg.to,"Like Success")                     
                     wait['likeOn'] = False					
            if wait['alwayRead'] == True:
                if msg.toType == 0:
                    cl.sendChatChecked(msg.from_,msg.id)
                    kk.sendChatChecked(msg.from_,msg.id)
                    ke.sendChatChecked(msg.from_,msg.id)
                    ka.sendChatChecked(msg.from_,msg.id)
                    ki.sendChatChecked(msg.from_,msg.id)
                    kc.sendChatChecked(msg.from_,msg.id)			
                else:
                    cl.sendChatChecked(msg.to,msg.id)
                    ka.sendChatChecked(msg.to,msg.id)
                    ke.sendChatChecked(msg.to,msg.id)
                    kk.sendChatChecked(msg.to,msg.id)	
                    ki.sendChatChecked(msg.to,msg.id)
                    kc.sendChatChecked(msg.to,msg.id)			
#------------------

        if op.type == 19:
          try:	      
            if op.param3 in Smid: #Akun Utama Ke Kick
                if op.param2 in creator + peminjam:
                    pass
	        elif op.param2 in Bots:
		    pass
                G = random.choice(KAC).getGroup(op.param1)
                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                G.preventJoinByTicket = False
                random.choice(KAC).updateGroup(G)
                Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                satpam.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                G.preventJoinByTicket = True
                random.choice(KAC).updateGroup(G)
                satpam.updateGroup(G)
                wait["blacklist"][op.param2] = True
	  except:
	         pass
        if op.type == 19:
		if wait["protect"] == True:
		    try:
			if op.param3 in Bots + creator + admin + staff + peminjam:
			    pass
		        if op.param2 in Bots + creator + admin + staff + peminjam:
			    pass
		        else:
		            cl.kickoutFromGroup(op.param1,[op.param2])
                        if op.param2 in wait["blacklist"]:
                            pass
		        else:
		            kc.inviteIntoGroup(op.param1,[op.param3])
		    except:
		        try:
			    if op.param2 not in Bots:
                                random.choice(DEF).kickoutFromGroup(op.param1,[op.param2])
			    if op.param2 in wait["blacklist"]:
			        pass
			    else:
			        random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
		        except:
			    print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True
           			f=codecs.open('st2__b.json','w','utf-8')
              			json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)				
		    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True
          		    f=codecs.open('st2__b.json','w','utf-8')
           		    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
		else:
		    pass			
        if op.type == 19: #Member Ke Kick
         if wait["AutoKick"] == True:
          if op.param2 in Bots:
            pass
          elif op.param2 in admin:
            pass
          elif op.param2 in creator + peminjam:
            pass
          elif op.param2 in staff:
            pass
          else:
            try:
              wait["blacklist"][op.param2] = True		
	      cl.kickoutFromGroup(op.param1,[op.param2])
              f=codecs.open('st2__b.json','w','utf-8')
              json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
            except:
              wait["blacklist"][op.param2] = True			
              random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
              f=codecs.open('st2__b.json','w','utf-8')
              json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)

                  
        if op.type == 19:
                if mid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kc.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(DEF).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    G = random.choice(KAC).getGroup(op.param1)
                    G.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(G)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
 
                if Amid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kc.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(DEF).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki.updateGroup(G)
                    Ticket = ki.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Bmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        kc.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(DEF).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kk.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kk.updateGroup(G)
                    Ticket = kk.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Cmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(DEF).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kc.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kc.updateGroup(G)
                    Ticket = kc.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                        
                        
                if Dmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(DEF).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Because it is not in the group or Because it does not exist in the group \n["+op.param1+"]\nOf\n["+op.param2+"]\n I could not kick \n Add it to the black list.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ks.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ks.updateGroup(G)
                    Ticket = ks.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                        
                if Emid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(DEF).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Because it is not in the group or Because it does not exist in the group \n["+op.param1+"]\nOf\n["+op.param2+"]\n I could not kick \n Add it to the black list.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ka.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ka.updateGroup(G)
                    Ticket = ka.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                        
                if Fmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(DEF).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Because it is not in the group or Because it does not exist in the group \n["+op.param1+"]\nOf\n["+op.param2+"]\n I could not kick \n Add it to the black list.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kb.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kb.updateGroup(G)
                    Ticket = kb.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                        
                if Gmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(DEF).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Because it is not in the group or Because it does not exist in the group \n["+op.param1+"]\nOf\n["+op.param2+"]\n I could not kick \n Add it to the black list.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ko.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ko.updateGroup(G)
                    Ticket = ko.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                        
                if Hmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(DEF).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Because it is not in the group or Because it does not exist in the group \n["+op.param1+"]\nOf\n["+op.param2+"]\n I could not kick \n Add it to the black list.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ke.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ke.updateGroup(G)
                    Ticket = ke.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
		
                if Imid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(DEF).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Because it is not in the group or Because it does not exist in the group \n["+op.param1+"]\nOf\n["+op.param2+"]\n I could not kick \n Add it to the black list.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    ku.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ku.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ku.updateGroup(G)
                    Ticket = ku.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                       		
                    
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
		
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message


            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
		

        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")

               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        ki.sendText(msg.to,"deleted")
                        kk.sendText(msg.to,"deleted")
                        kc.sendText(msg.to,"deleted")
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        ki.sendText(msg.to,"It is not in the black list")
                        kk.sendText(msg.to,"It is not in the black list")
                        kc.sendText(msg.to,"It is not in the black list")
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"already")
                        ki.sendText(msg.to,"already")
                        kk.sendText(msg.to,"already")
                        kc.sendText(msg.to,"already")
                        wait["wblacklist"] = False
			f=codecs.open('st2__b.json','w','utf-8')
              		json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
			f=codecs.open('st2__b.json','w','utf-8')
              		json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)			
                        cl.sendText(msg.to,"aded")
                        ki.sendText(msg.to,"aded")
                        kk.sendText(msg.to,"aded")
                        kc.sendText(msg.to,"aded")

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        ki.sendText(msg.to,"deleted")
                        kk.sendText(msg.to,"deleted")
                        kc.sendText(msg.to,"deleted")
                        wait["dblacklist"] = False
			f=codecs.open('st2__b.json','w','utf-8')
              		json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)				  
                   else:
                        wait["dblacklist"] = False
			f=codecs.open('st2__b.json','w','utf-8')
              		json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)				  
                        cl.sendText(msg.to,"It is not in the black list")
                        ki.sendText(msg.to,"It is not in the black list")
                        kk.sendText(msg.to,"It is not in the black list")
                        kc.sendText(msg.to,"It is not in the black list")
               elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text in ["Gruplistmid"]:
                if msg.from_ in creator:
                    gruplist = cl.getGroupIdsJoined()
                    kontak = cl.getGroups(gruplist)
                    num=1
                    msgs="═════════List GrupMid═════════"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.id)
                        num=(num+1)
                    msgs+="\n═════════List GrupMid═════════\n\nTotal Grup : %i" % len(kontak)
                    cl.sendText(msg.to, msgs)
#--------------------------------------------------------
            elif "Inviteme: " in msg.text:
              if msg.from_ in creator:
                gid = msg.text.replace("Inviteme: ","")
                if gid == "":
                    cl.sendText(msg.to,"Invalid group id")
                else:
                    try:
                        cl.findAndAddContactsByMid(msg.from_)
                        cl.inviteIntoGroup(gid,[msg.from_])
                    except:
                        cl.sendText(msg.to,"Mungkin saya tidak di dalaam grup itu")	
	    elif msg.text.lower() == 'invite:gcreator':
                if msg.from_ in admin + peminjam:
                    if msg.toType == 2:
                           ginfo = cl.getGroup(msg.to)
                           try:
                               gcmid = ginfo.pembuat.mid
                           except:
                               gcmid = "Error"
                           if wait["lang"] == "JP":
                               cl.inviteIntoGroup(msg.to,[gcmid])
                           else:
                               cl.inviteIntoGroup(msg.to,[gcmid])		
            elif "Invite me" in msg.text:
              if msg.from_ in pembuat:
                         gid = cl.getGroupIdsJoined()
		         for i in gid:
			        cl.findAndAddContactsByMid(msg.from_)
                                random.choice(KAC).inviteIntoGroup(i,[msg.from_])
			        cl.sendText(msg.to, "successfully invited you to all groups")
            elif msg.text is None:
                return
            elif msg.text in ["Key","help","Help"]:
              if wait["lang"] == "JP":
                  cl.sendText(msg.to,helpMessage)
              else:
                  cl.sendText(msg.to,helpt)
			
            elif msg.text in ["Key edit","help edit","Help edit"]:
              if wait["lang"] == "JP":		
                  cl.sendText(msg.to,editedMessage)
              else:
                  cl.sendText(msg.to,helpt)		

            elif msg.text in ["Key demoted","help demoted","Help demoted"]:
              if wait["lang"] == "JP":		
                  cl.sendText(msg.to,demotedMessage)
              else:
                  cl.sendText(msg.to,helpt)		

            elif msg.text in ["Key steal","help steal","Help steal"]:
              if wait["lang"] == "JP":		
                  cl.sendText(msg.to,stealMessage)
              else:
                  cl.sendText(msg.to,helpt)		

            elif msg.text in ["Key secur","help secur","Help secur"]:
              if wait["lang"] == "JP":		
                  cl.sendText(msg.to,securMessage)
              else:
                  cl.sendText(msg.to,helpt)		

            elif msg.text in ["Key ban","help ban","Help ban"]:
              if wait["lang"] == "JP":		
                  cl.sendText(msg.to,banMessage)
              else:
                  cl.sendText(msg.to,helpt)		

            elif msg.text in ["Key invite","help invite","Help invite"]:
              if wait["lang"] == "JP":		
                  cl.sendText(msg.to,inviteMessage)
              else:
                  cl.sendText(msg.to,helpt)		

            elif msg.text in ["Key grup","help grup","Help grup"]:
              if wait["lang"] == "JP":		
                  cl.sendText(msg.to,grupMessage)
              else:
                  cl.sendText(msg.to,helpt)		
		
            elif msg.text in ["Key media","help media","Help media"]:
              if wait["lang"] == "JP":		
                  cl.sendText(msg.to,mediaMessage)
              else:
                  cl.sendText(msg.to,helpt)		
                
            elif msg.text in ["Key set","help set","Help set"]:
              if wait["lang"] == "JP":		
                  cl.sendText(msg.to,setMessage)
              else:
                  cl.sendText(msg.to,helpt)		

            elif msg.text in ["Key cancel","help cancel","Help cancel"]:
              if wait["lang"] == "JP":		
                  cl.sendText(msg.to,cancelMessage)
              else:
                  cl.sendText(msg.to,helpt)		

            elif msg.text in ["Key gift","help gift","Help gift"]:
              if wait["lang"] == "JP":		
                  cl.sendText(msg.to,giftMessage)
              else:
                  cl.sendText(msg.to,helpt)		

            elif msg.text in ["Key notif","help notif","Help notif"]:
              if wait["lang"] == "JP":		
                  cl.sendText(msg.to,notifMessage)
              else:
                  cl.sendText(msg.to,helpt)		
                
            elif msg.text in ["Key kiker","help kiker","Help kiker"]:
              if wait["lang"] == "JP":		
                  cl.sendText(msg.to,kikerMessage)  		
              else:
                  cl.sendText(msg.to,helpt)
		
            elif msg.text in ["Key spam","help spam","Help spam"]:
              if wait["lang"] == "JP":		
                  cl.sendText(msg.to,spamMessage)
              else:
                  cl.sendText(msg.to,helpt)	

            elif msg.text in ["Key utility","help utility","Help utility"]:
              if wait["lang"] == "JP":			
                cl.sendText(msg.to,utilityMessage)		
                
            elif msg.text in ["Key bc","help bc","Help bc"]:
              if wait["lang"] == "JP":		
                  cl.sendText(msg.to,bcMessage)  	
              else:
                  cl.sendText(msg.to,helpt)
#===============================================================
            elif msg.text in ["Gruplist"]:
                if msg.from_ in creator + peminjam:
                    gruplist = cl.getGroupIdsJoined()
                    kontak = cl.getGroups(gruplist)
                    num=1
                    msgs="═════════List Grup═════════"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.name)
                        num=(num+1)
                    msgs+="\n═════════List Grup═════════\n\nTotal Grup : %i" % len(kontak)
                    cl.sendText(msg.to, msgs)					               
            elif msg.text in ["List group"]:
              if msg.from_ in pembuat + peminjam:	   		
                    gid = cl.getGroupIdsJoined()
                    h = ""
		    jml = 0
                    for i in gid:
		        gn = cl.getGroup(i).name
                        h += "♦【%s】\n" % (gn)
		        jml += 1
                    cl.sendText(msg.to,"=======[List Group]=======\n"+ h +"\nTotal Group: "+str(jml))						
	    elif "Ghost on" in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:	        
		     wait["Ghost"] = True
		     cl.sendText(msg.to,"Ghost Sudah Aktif")
	      else:
	          cl.sendText(msg.to,"admin yg boleh")	
			
            elif msg.text in ["Cl keluarallgrup"]:
              if msg.from_ in creator:
				gid = cl.getGroupIdsJoined()				
				for i in gid:					
					cl.leaveGroup(i)
	    elif "Ghost off" in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:	 	        
		     wait["Ghost"] = False
		     cl.sendText(msg.to,"Ghost Sudah Di Nonaktifkan")
	      else:
	          cl.sendText(msg.to,"admin yg boleh")			
		
            elif "/invite:" in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:
                midd = msg.text.replace("/invite:"," ")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
#--------------------------------------------------------
	    elif "Recover" in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:		
		thisgroup = cl.getGroups([msg.to])
		Mids = [contact.mid for contact in thisgroup[0].members]
		mi_d = Mids[:33]
		cl.createGroup("Recover", mi_d)
		cl.sendText(msg.to,"Success recover")		
            
            elif msg.text.lower() == 'contact bot':
              if msg.from_ in admin + staff + creator + peminjam:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid}
                ki.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Bmid}
                kk.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Cmid}
                kc.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Dmid}
                ks.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Emid}
                ka.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Fmid}
                kb.sendMessage(msg)		
            elif msg.text in ["Set group"]:
              if msg.from_ in admin + staff + creator + peminjam:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,Setgroup)
                else:
                    cl.sendText(msg.to,Sett)
            elif "Set member: " in msg.text:
		if msg.from_ in creator + peminjam:
		    jml = msg.text.replace("Set member: ","")
		    wait["Members"] = int(jml)
		    cl.sendText(msg.to, "Jumlah minimal member telah di set : "+jml)
		else:
		    cl.sendText(msg.to, "Khusus Admin")
#=======================================================
            elif msg.text.lower() == ".crash":
              if msg.from_ in creator + peminjam:
                msg.contentType = 13
                msg.contentMetadata = {'mid': "uab1ca173166a362c69ef62d420f9f784',"}
                cl.sendMessage(msg)
            elif "Reinvite" in msg.text.split():
              if msg.from_ in admin + staff + creator + peminjam:	
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    if group.invitee is not None:
                        try:
                            grCans = [contact.mid for contact in group.invitee]
                            cl.findAndAddContactsByMid(msg.to, grCans)
                            cl.cancelGroupInvitation(msg.to, grCans)
                            cl.inviteIntoGroup(msg.to, grCans)
                        except Exception as error:
                            print error
                        pass
            elif ("Gn " in msg.text):
              if msg.from_ in admin + staff + creator + peminjam:		
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn ","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
            elif ("Cv1 gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Cv1 gn ","")
                    ki.updateGroup(X)
                else:
                    ki.sendText(msg.to,"It can't be used besides the group.")
            elif ("Cv2 gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Cv2 gn ","")
                    kk.updateGroup(X)
                else:
                    kk.sendText(msg.to,"It can't be used besides the group.")
            elif ("Cv3 gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Cv3 gn ","")
                    kc.updateGroup(X)
                else:
                    kc.sendText(msg.to,"It can't be used besides the group.")
            elif "Getmid @" in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:
                    _name = msg.text.replace("Getmid @","")
                    _nametarget = _name.rstrip(' ')
                    gs = cl.getGroup(msg.to)
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            cl.sendText(msg.to, g.mid)
                        else:
                            pass		
            elif "Kick " in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:
                midd = msg.text.replace("Kick ","")
                cl.kickoutFromGroup(msg.to,[midd])
            elif "_second kick " in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:
                midd = msg.text.replace("_second kick ","")
                ki.kickoutFromGroup(msg.to,[midd])
            elif "_third kick " in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:
                midd = msg.text.replace("_third kick ","")
                kk.kickoutFromGroup(msg.to,[midd])
            elif "_fourth kick " in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:
                midd = msg.text.replace("_fourth kick ","")
                kc.kickoutFromGroup(msg.to,[midd])
            elif "/invite " in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:
                midd = msg.text.replace("Invite ","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
            elif "sinvite " in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:
                midd = msg.text.replace("sinvite ","")
                ki.findAndAddContactsByMid(midd)
                ki.inviteIntoGroup(msg.to,[midd])
            elif "tinvite " in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:
                midd = msg.text.replace("tinvite ","")
                kk.findAndAddContactsByMid(midd)
                kk.inviteIntoGroup(msg.to,[midd])
            elif "finvite " in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:
                midd = msg.text.replace("finvite ","")
                kc.findAndAddContactsByMid(midd)
                kc.inviteIntoGroup(msg.to,[midd])
            elif msg.text in ["Bot?"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid}
                ki.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': Bmid}
                kk.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Emid}
                ka.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': Hmid}
                ke.sendMessage(msg)
		
            elif msg.text in ["Me"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.from_}
                random.choice(KAC).sendMessage(msg)
            elif msg.text in ["Cv2"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Bmid}
                kk.sendMessage(msg)
            elif msg.text in ["æ„›ã�®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text in ["æ„›ã�®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Cv1 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '6'}
                msg.text = None
                ki.sendMessage(msg)
            elif msg.text in ["æ„›ã�®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Cv2 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '8'}
                msg.text = None
                kk.sendMessage(msg)
            elif msg.text in ["æ„›ã�®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Cv3 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '10'}
                msg.text = None
                kc.sendMessage(msg)
            elif msg.text in ["æ„›ã�®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","All gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '12'}
                msg.text = None
                ki.sendMessage(msg)
                kk.sendMessage(msg)
                kc.sendMessage(msg)
            elif msg.text in ["Cancel","cancel"]:
              if msg.from_ in admin + staff + creator + peminjam:   
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No one is inviting")
                        else:
                            cl.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv cancel","Bot cancel"]:
                if msg.toType == 2:
                    G = k3.getGroup(msg.to)
                    if G.invitee is not None:
                        gInviMids = [contact.mid for contact in G.invitee]
                        k3.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            k3.sendText(msg.to,"No one is inviting")
                        else:
                            k3.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        k3.sendText(msg.to,"Can not be used outside the group")
                    else:
                        k3.sendText(msg.to,"Not for use less than group")
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
            elif msg.text in ["Open url","open url"]:
              if msg.from_ in admin + staff + creator + peminjam:		
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Invite by link open")
                    else:
                        cl.sendText(msg.to,"Already open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv1 ourl","Cv1 link on"]:
              if msg.from_ in admin + staff + creator + peminjam:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    ki.updateGroup(X)
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Done Chivas")
                    else:
                        ki.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv2 ourl","Cv2 link on"]:
              if msg.from_ in admin + staff + creator + peminjam: 
                if msg.toType == 2:
                    X = kk.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    kk.updateGroup(X)
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Done Chivas")
                    else:
                        kk.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kk.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv3 ourl","Cv3 link on"]:
              if msg.from_ in admin + staff + creator + peminjam: 	
                if msg.toType == 2:
                    X = kc.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Done Chivas")
                    else:
                        kc.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kc.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Close url","close url"]:
              if msg.from_ in admin + staff + creator + peminjam: 
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Invite by link Close")
                    else:
                        cl.sendText(msg.to,"Already close")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Auto like"]:
              if msg.from_ in admin + staff + creator + peminjam:	 	
                wait["likeOn"] = True
                cl.sendText(msg.to,"Shere Post Kamu Yang Mau Di Like!")	    
            elif msg.text in ["Cv1 curl","Cv1 link off"]:
              if msg.from_ in admin + staff + creator:	
                if msg.toType == 2:
                    X = ki.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    ki.updateGroup(X)
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Done Chivas")
                    else:
                        ki.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ki.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv2 curl","Cv2 link off"]:
              if msg.from_ in admin + staff + creator + peminjam:	 	
                if msg.toType == 2:
                    X = kk.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    kk.updateGroup(X)
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Done Chivas")
                    else:
                        kk.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kk.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv3 curl","Cv3 link off"]:
              if msg.from_ in admin + staff + creator + peminjam: 	
                if msg.toType == 2:
                    X = kc.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    kc.updateGroup(X)
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Done Chivas")
                    else:
                        kc.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kc.sendText(msg.to,"Not for use less than group")
            elif "jointicket " in msg.text.lower():
              if msg.from_ in admin + creator: 
		rplace=msg.text.lower().replace("jointicket ")
		if rplace == "on":
			wait["atjointicket"]=True
		elif rplace == "off":
			wait["atjointicket"]=False
		cl.sendText(msg.to,"Auto Join Group by Ticket is %s" % str(wait["atjointicket"]))
            elif '/ti/g/' in msg.text.lower():
              if msg.from_ in admin + staff + creator + peminjam:	 
		link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
		links = link_re.findall(msg.text)
		n_links=[]
		for l in links:
			if l not in n_links:
				n_links.append(l)
		for ticket_id in n_links:
			if wait["atjointicket"] == True:
				group=cl.findGroupByTicket(ticket_id)
				cl.acceptGroupInvitationByTicket(group.mid,ticket_id)
				cl.sendText(msg.to,"Sukses join ke grup %s" % str(group.name))
            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\nmembers:" + str(len(ginfo.members)) + "members\npending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif "/bio " in msg.text:	
              if msg.from_ in creator:	 		
                    string = msg.text.replace("/bio ","")
                    if len(string.decode('utf-8')) <= 500:
                        profile = cl.getProfile()
                        profile.statusMessage = string
                        cl.updateProfile(profile)
                        ki.updateProfile(profile)
                        kk.updateProfile(profile)
                        ka.updateProfile(profile)
                        ke.updateProfile(profile)
                        cl.sendText(msg.to,"Semua udh di ganti sayang")			
            elif "Id Group" == msg.text:
                kk.sendText(msg.to,msg.to)
            elif "My mid" == msg.text:
                random.choice(KAC).sendText(msg.to, msg.from_)
            elif "Mid RA" == msg.text:
                cl.sendText(msg.to,mid)
                ki.sendText(msg.to,Amid)
                kk.sendText(msg.to,Bmid)
                kc.sendText(msg.to,Cmid)
                ks.sendText(msg.to,Dmid)
                ka.sendText(msg.to,Emid)
                kb.sendText(msg.to,Fmid)
            elif "RA 1" == msg.text:
                cl.sendText(msg.to,mid)
            elif "RA 2" == msg.text:
                ki.sendText(msg.to,Amid)
            elif "RA 3" == msg.text:
                kk.sendText(msg.to,Bmid)
            elif "RA 4" == msg.text:
                kc.sendText(msg.to,Cmid)
            elif msg.text in ["Haha"]:
                msg.contentType = 7
                msg.text = "Jones Ketawa"
		cl.sendText(msg.to,"Jones ketawa")
                msg.contentMetadata = {
                                     "STKID": "100",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                kk.sendMessage(msg)
                ka.sendMessage(msg)
                ks.sendMessage(msg)
                kc.sendMessage(msg)
                kb.sendMessage(msg)		
            elif msg.text in ["Hehehe","Hehe","He","hehehe","hehe","he"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "10",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["@bye","@Bye"]:
              if msg.from_ in creator + peminjam:
		    cl.sendText(msg.to,"Bye sayangku aku sayang kalian")
		    cl.leaveGroup(msg.to)
              else:
		   cl.sendText(msg.to,"Bilang Dulu Sama Admin Ku")
            elif msg.text in ["Galau"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "9",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["You"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "7",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["aduh"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "6",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Please"]:
                msg.contentType = 7
                msg.text = None
		cl.sendText(msg.to,"Bantuin itu")
                msg.contentMetadata = {
                                     "STKID": "4",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Haaa"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "3",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Lol"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "110",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Hmmm","Hmm","Hm","hmmm","hmm","hm"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "101",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif msg.text in ["Welcome"]:
                msg.contentType = 7
                msg.text = None
		cl.sendText(msg.to,"Selamat Datang Di jones room")
                msg.contentMetadata = {
                                     "STKID": "247",
                                     "STKPKGID": "3",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["TL: "]:
                tl_text = msg.text.replace("TL: ","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif msg.text in ["Cn "]:
              if msg.from_ in admin + creator + peminjam:	 
                string = msg.text.replace("Cn ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Cv1 rename "]:
              if msg.from_ in admin + creator + peminjam:
                string = msg.text.replace("Cv1 rename ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = ki.getProfile()
                    profile_B.displayName = string
                    ki.updateProfile(profile_B)
                    ki.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Cv2 rename "]:
              if msg.from_ in admin + creator + peminjam:
                string = msg.text.replace("Cv2 rename ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = kk.getProfile()
                    profile_B.displayName = string
                    kk.updateProfile(profile_B)
                    kk.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Mc "]:
              if msg.from_ in admin + staff + creator + peminjam:
                mmid = msg.text.replace("Mc ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
            elif msg.text in ["Joinn on","joinn on"]:
              if msg.from_ in admin + staff + creator + peminjam:
                if wait["Protectjoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"kick Joined Group On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectjoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"kick Joined Group On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Joinn off","joinn off"]:
              if msg.from_ in admin + staff + creator + peminjam:
                if wait["Protectjoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"kick Joined Group Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectjoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"kick Joined Group Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Cancl on","cancl on"]:
              if msg.from_ in admin + staff + creator + peminjam:	
                if wait["Protectcancl"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel All Invited On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancl"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel All Invited On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Cancl off","cancl off"]:
              if msg.from_ in admin + staff + creator + peminjam:
                if wait["Protectcancl"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel All Invited Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancl"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel All Invited Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Read on","read on"]:
              if msg.from_ in admin + staff + creator + peminjam:
                if wait["alwayRead"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel All Invited On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancl"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel All Invited On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Read off","read off"]:
              if msg.from_ in admin + staff + creator + peminjam:
                if wait["alwayRead"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel All Invited Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["alwayRead"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel All Invited Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Gr on","gr on"]:
              if msg.from_ in admin + staff + creator + peminjam:
                if wait["Protectgr"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Group On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectgr"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Group On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Gr off","gr off"]:
              if msg.from_ in admin + staff + creator + peminjam:
                if wait["Protectgr"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Group Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectgr"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Group Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Contact On","Contact on","contact on"]:
              if msg.from_ in admin + staff + creator + peminjam:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Send Contact On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Send Contact On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Contact Off","Contact off","contact off"]:
              if msg.from_ in admin + staff + creator + peminjam:	
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Send Contact Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Send Contact Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å�‚åŠ :ã‚ªãƒ³","Join on","Auto join:on","è‡ªå‹•å�ƒåŠ ï¼šé–‹"]:
              if msg.from_ in admin + staff + creator + peminjam:	
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å�‚åŠ :ã‚ªãƒ•","Join off","Auto join:off","è‡ªå‹•å�ƒåŠ ï¼šé—œ"]:
              if msg.from_ in admin + staff + creator + peminjam:	
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Gcancel:"]:
              if msg.from_ in admin + staff + creator + peminjam:	
                try:
                    strnum = msg.text.replace("Gcancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                        else:
                            cl.sendText(msg.to,"å…³äº†é‚€è¯·æ‹’ç»�ã€‚è¦�æ—¶å¼€è¯·æŒ‡å®šäººæ•°å�‘é€�")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
                        else:
                            cl.sendText(msg.to,strnum + "ä½¿äººä»¥ä¸‹çš„å°�ç»„ç”¨è‡ªåŠ¨é‚€è¯·æ‹’ç»�")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Value is wrong")
                    else:
                        cl.sendText(msg.to,"Bizarre ratings")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ³","Leave on","Auto leave:on","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé–‹"]:
              if msg.from_ in admin + staff + creator + peminjam:	
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif "Cium! " in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:		
                korban = msg.text.replace("Cium! ","")
                korban2 = korban.split()
                midd = korban2[0]
                jumlah = int(korban2[1])
                if jumlah <= 999:
                    for var in range(0,jumlah):
                        cl.sendText(midd,(wait["spam"]))
                else:
                    cl.sendText(msg.to, "Kebanyakan gblk! ")	
            elif msg.text.lower() == 'timebot':
              if msg.from_ in admin + staff + creator + peminjam:		
                eltime = time.time() - mulai
                van = "Bot Sudah Berjalan Selama :\n"+waktu(eltime)
                cl.sendText(msg.to,van)	
#----------------------
            elif "Dosa @" in msg.text:
                tanya = msg.text.replace("Dosa @","")
                jawab = ("60%","70%","80%","90%","100%","Tak terhingga")
                jawaban = random.choice(jawab)
                cl.sendText(msg.to,"Dosanya " + tanya + "adalah " + jawaban + " Banyak banyak tobat Nak ")
#----------------------
	    elif "Pahala @" in msg.text:
                tanya = msg.text.replace("Pahala @","")
                jawab = ("0%","20%","40%","50%","60%","Tak ada")
                jawaban = random.choice(jawab)
                cl.sendText(msg.to,"Pahalanya " + tanya + "adalah " + jawaban + "\nTobatlah nak")

	#-------------------------------#			
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ•","Leave off","Auto leave:off","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé—œ"]:
              if msg.from_ in admin + staff + creator + peminjam:	
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ³","Share on","Share on"]:
              if msg.from_ in admin + staff + creator + peminjam:	
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ•","Share off","Share off"]:
              if msg.from_ in admin + staff + creator + peminjam:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif "removechat" in msg.text.lower():
              if msg.from_ in admin + creator + peminjam:
                    try:
                        cl.removeAllMessages(op.param2)
                        ki.removeAllMessages(op.param2)
                        kk.removeAllMessages(op.param2)
                        kc.removeAllMessages(op.param2)
                        ka.removeAllMessages(op.param2)
                        ke.removeAllMessages(op.param2)			
                        print "[Command] Remove Chat"
                        cl.sendText(msg.to,"Done")
                    except Exception as error:
                        print error
                        cl.sendText(msg.to,"Error")  
            elif msg.text in ["Settings"]:
                md = ""
                if wait["Protectjoin"] == True: md+="􀔃􀆑lock􏿿  Block Join\n"
                else: md+=" Block Join Off\n"
                if wait["Protectgr"] == True: md+="􀔃􀆑lock􏿿   Block Group\n"
                else: md+=" Block Group Off\n"
                if wait["Protectcancl"] == True: md+="􀔃􀆑lock􏿿 Cancel All Invited\n"
                else: md+=" Cancel All Invited Off\n"
                if wait["contact"] == True: md+=" Contact    : on\n"
                else: md+=" Contact    : off\n"
                if wait["autoJoin"] == True: md+=" Auto join : on\n"
                else: md +=" Auto join : off\n"
                if wait["autoCancel"]["on"] == True:md+="Group cancel :" + str(wait["autoCancel"]["members"]) + "\n"
                else: md+= "Group cancel : off\n"
                if wait["leaveRoom"] == True: md+="Auto leave    : on\n"
                else: md+="Auto leave : off\n"
                if wait["timeline"] == True: md+="Share   : on\n"
                else:md+=" Share   : off\n"
                if wait["autoAdd"] == True: md+="Auto add : on\n"
                else:md+="Auto add : off\n"
                if wait["commentOn"] == True: md+=" Comment : on\n"
                else:md+=" Comment : off\n"
		if wait["likeOn"] == True: md+="Auto like : on\n"
                else:md+="Auto like : off\n"
		if wait["protect"] == True: md+="Protect group : on\n"
                else:md+="Protect group : off\n"		
                if wait["welcomemsg"] == True: md+="Sambutan : on\n"
                else:md+="Sambutan : off\n"
                cl.sendText(msg.to,md)
            elif "album merit " in msg.text:
                gid = msg.text.replace("album merit ","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album")
                    else:
                        cl.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
                    cl.sendText(msg.to,mg)
            elif "album " in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:	
                gid = msg.text.replace("album ","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album")
                    else:
                        cl.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
            elif "album remove " in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:
                gid = msg.text.replace("album remove ","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Deleted albums")
                else:
                    cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["Group id"]:
              if msg.from_ in admin + staff + creator:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:\n%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
            elif "Bcg " in msg.text:
              if msg.from_ in creator + peminjam:
                bctxt = msg.text.replace("Bcg ", "")
                a = cl.getGroupIdsJoined()
                for manusia in a:
                    cl.sendText(manusia, (bctxt))
		
            elif "Bcc " in msg.text:
              if msg.from_ in creator + peminjam:
                bctxt = msg.text.replace("Bcc ", "")
                a = cl.getAllContactIds()
                for manusia in a:
                    cl.sendText(manusia, (bctxt))
            elif msg.text in ["Cancelall"]:
              if msg.from_ in admin + staff + creator + peminjam:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"All invitations have been refused")
                else:
                    cl.sendText(msg.to,"æ‹’ç»�äº†å…¨éƒ¨çš„é‚€è¯·ã€‚")
            elif "album removeat’" in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:	
                gid = msg.text.replace("album removeat’","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Albums deleted")
                else:
                    cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ³","Add on","Auto add:on","è‡ªå‹•è¿½åŠ ï¼šé–‹"]:
              if msg.from_ in admin + creator + peminjam:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ•","Add off","Auto add:off","è‡ªå‹•è¿½åŠ ï¼šé—œ"]:
              if msg.from_ in admin + creator + peminjam:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif "Message change: " in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:
                wait["message"] = msg.text.replace("Message change: ","")
                cl.sendText(msg.to,"message changed")
            elif "Message add: " in msg.text:
                wait["message"] = msg.text.replace("Message add: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message changed")
                else:
                    cl.sendText(msg.to,"doneã€‚")
            elif msg.text in ["Message","è‡ªå‹•è¿½åŠ å•�å€™èªžç¢ºèª�"]:
              if msg.from_ in admin + staff + creator + peminjam:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message change to\n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"The automatic appending information is set as followsã€‚\n\n" + wait["message"])
            elif "Comment:" in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:
                c = msg.text.replace("Comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"message changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
            elif "Add comment:" in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:
                c = msg.text.replace("Add comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"String that can not be changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ³","Comment on","Comment:on","è‡ªå‹•é¦–é �ç•™è¨€ï¼šé–‹"]:
              if msg.from_ in admin + staff + creator + peminjam:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already on")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ•","Comment on","Comment off","è‡ªå‹•é¦–é �ç•™è¨€ï¼šé—œ"]:
              if msg.from_ in admin + staff + creator + peminjam:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif msg.text in ["Comment","ç•™è¨€ç¢ºèª�"]:
              if msg.from_ in admin + staff + creator + peminjam:	
                cl.sendText(msg.to,"message changed to\n\n" + str(wait["comment"]))
            elif msg.text in ["Gurl"]:
              if msg.from_ in admin + staff + creator + peminjam:	
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv1 gurl"]:
              if msg.from_ in admin + staff + creator + peminjam:	
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        ki.updateGroup(x)
                    gurl = ki.reissueGroupTicket(msg.to)
                    ki.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")

            elif msg.text in ["Comment bl "]:
              if msg.from_ in admin + staff + creator + peminjam:	
                wait["wblack"] = True
                cl.sendText(msg.to,"add to comment bl")
            elif msg.text in ["Comment wl "]:
                wait["dblack"] = True
                cl.sendText(msg.to,"wl to comment bl")
            elif msg.text in ["Comment bl confirm"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"confirmed")
                else:
                    cl.sendText(msg.to,"Blacklist")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
		
            elif msg.text in ["Accept invite"]:
                if msg.from_ in creator:
                    gid = cl.getGroupIdsInvited()
                    _list = ""
                    for i in gid:
                        if i is not None:
                            gids = cl.getGroup(i)
                            _list += gids.name
                            cl.acceptGroupInvitation(i)
                        else:
                            break
                    if gid is not None:
                        cl.sendText(msg.to,"Berhasil terima semua undangan dari grup :\n" + _list)
                    else:
                        cl.sendText(msg.to,"Tidak ada grup yang tertunda saat ini")                    
        #-------------Fungsi Jam on/off Start-------------------#            
            elif msg.text in ["Jam on"]:
              if msg.from_ in admin + staff + creator + peminjam:	
                if wait["clock"] == True:
                    kc.sendText(msg.to,"Bot 4 jam on")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = kc.getProfile()
                    profile.displayName = wait["cName4"] + nowT
                    kc.updateProfile(profile)
                    kc.sendText(msg.to,"Jam Selalu On")
            elif msg.text in ["Jam off"]:
              if msg.from_ in admin + staff + creator + peminjam:
                if wait["clock"] == False:
                    kc.sendText(msg.to,"Bot 4 jam off")
                else:
                    wait["clock"] = False
                    kc.sendText(msg.to,"Jam Sedang Off")
			
         #-------------Fungsi Jam on/off Finish-------------------#   
            elif 'Bot mid' in msg.text.lower():
              if msg.from_ in admin + staff + creator + peminjam:	
			cl.sendText(msg.to,mid)
			ki.sendText(msg.to,Amid)
			kk.sendText(msg.to,Bmid)
			ke.sendText(msg.to,Dmid)
			ka.sendText(msg.to,Emid)
 #=======================================================
            elif "Vn-af " in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:
                 psn = msg.text.replace("Vn-af ","")
                 tts = gTTS(psn, lang='af', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-sq " in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:
                 psn = msg.text.replace("Vn-sq ","")
                 tts = gTTS(psn, lang='sq', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-ar " in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:
                 psn = msg.text.replace("Vn-ar ","")
                 tts = gTTS(psn, lang='ar', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-hy " in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:
                 psn = msg.text.replace("Vn-hy ","")
                 tts = gTTS(psn, lang='hy', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-bn " in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:
                 psn = msg.text.replace("Vn-bn ","")
                 tts = gTTS(psn, lang='bn', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-ca " in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:
                 psn = msg.text.replace("Vn-ca ","")
                 tts = gTTS(psn, lang='ca', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-zh " in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:
                 psn = msg.text.replace("Vn-zh ","")
                 tts = gTTS(psn, lang='zh', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-zhcn " in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:
                 psn = msg.text.replace("Vn-zhcn ","")
                 tts = gTTS(psn, lang='zh-cn', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-zhtw " in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:
                 psn = msg.text.replace("Vn-zhtw ","")
                 tts = gTTS(psn, lang='zh-tw', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-zhyue " in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:
                 psn = msg.text.replace("Vn-zhyue ","")
                 tts = gTTS(psn, lang='zh-yue', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif msg.text in ["Protect:hight","protect:hight"]:
              if msg.from_ in admin + staff + creator + peminjam:
                if wait["protectionOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"turned into high protection\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"turned into high protection\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["protectionOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"turned into high protection\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"turned into high protection\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Protect:low","Protect:low"]:
              if msg.from_ in admin + staff + creator + peminjam:
                if wait["protectionOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"turned into low protection\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"turned into low protection\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["protectionOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"turned into low protection\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"turned into low protection\n\n"+ datetime.today().strftime('%H:%M:%S'))			
            elif "Vn-hr " in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:
                 psn = msg.text.replace("Vn-hr ","")
                 tts = gTTS(psn, lang='hr', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-cs " in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:
                 psn = msg.text.replace("Vn-cs ","")
                 tts = gTTS(psn, lang='cs', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-da " in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:
                 psn = msg.text.replace("Vn-da ","")
                 tts = gTTS(psn, lang='da', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-nl " in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:
                 psn = msg.text.replace("Vn-nl ","")
                 tts = gTTS(psn, lang='nl', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-en " in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:
                 psn = msg.text.replace("Vn-en ","")
                 tts = gTTS(psn, lang='en', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-enau " in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:
                 psn = msg.text.replace("Vn-enau ","")
                 tts = gTTS(psn, lang='en-au', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif msg.text in ["Respontag on","Autorespon:on","Respon on","Respon:on"]:
              if msg.from_ in admin + staff + creator + peminjam:	
                wait['detectMention'] = True
                cl.sendText(msg.to,"Auto respon tag On")
                
            elif msg.text in ["Respontag off","Autorespon:off","Respon off","Respon:off"]:
              if msg.from_ in admin + staff + creator + peminjam:	
                wait['detectMention'] = False
                cl.sendText(msg.to,"Auto creator tag Off")
            elif msg.text in ["Creator tag on","Creatortag on","Respon on","Respon:on"]:
              if msg.from_ in admin + staff + creator + peminjam:	
                wait['detectMention'] = True
                cl.sendText(msg.to,"Auto respon tag On")
                
            elif msg.text in ["Creator tag of","Creatortag off","Respon off","Respon:off"]:
              if msg.from_ in admin + staff + creator + peminjam:	
                wait['detectMention'] = False
                cl.sendText(msg.to,"Auto creator tag Off")            
            elif msg.text in ["Kicktag on","Autokick:on","Responkick on","Responkick:on"]:
              if msg.from_ in admin + staff + creator + peminjam:	
                wait['kickMention'] = True
                cl.sendText(msg.to,"Auto Kick tag ON")
                
            elif msg.text in ["Kicktag off","Autokick:off","Responkick off","Responkick:off"]:
              if msg.from_ in admin + staff + creator + peminjam:	
                wait['kickMention'] = False
                cl.sendText(msg.to,"Auto Kick tag OFF")
            elif msg.text in ["Creattag on","Autokick:on","Responkick on","Responkick:on"]:
              if msg.from_ in admin + staff + creator + peminjam:	
                wait['creatorMention'] = True
                cl.sendText(msg.to,"Auto creator tag ON")
                
            elif msg.text in ["Creattag off","Autokick:off","Responkick off","Responkick:off"]:
              if msg.from_ in admin + staff + creator + peminjam:	
                wait['creatorMention'] = False
                cl.sendText(msg.to,"Auto creator tag OFF")
            elif "Time" in msg.text:
              if msg.toType == 2:
                  cl.sendText(msg.to,datetime.today().strftime('%H:%M:%S'))
            elif "Vn-enuk " in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:
                 psn = msg.text.replace("Vn-enuk ","")
                 tts = gTTS(psn, lang='en-uk', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-enus " in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:
                 psn = msg.text.replace("Vn-enus ","")
                 tts = gTTS(psn, lang='en-us', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-eo " in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:
                 psn = msg.text.replace("Vn-eo ","")
                 tts = gTTS(psn, lang='eo', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-fi " in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:
                 psn = msg.text.replace("Vn-fi ","")
                 tts = gTTS(psn, lang='fi', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-fr " in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:
                 psn = msg.text.replace("Vn-fr ","")
                 tts = gTTS(psn, lang='fr', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-de " in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:
                 psn = msg.text.replace("Vn-de ","")
                 tts = gTTS(psn, lang='de', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-el " in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:
                 psn = msg.text.replace("Vn-el ","")
                 tts = gTTS(psn, lang='el', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-hi " in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:
                 psn = msg.text.replace("Vn-hi ","")
                 tts = gTTS(psn, lang='hi', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-hu " in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:
                 psn = msg.text.replace("Vn-hu ","")
                 tts = gTTS(psn, lang='hu', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-is " in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:
                 psn = msg.text.replace("Vn-is ","")
                 tts = gTTS(psn, lang='is', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-id " in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:
                 psn = msg.text.replace("Vn-id ","")
                 tts = gTTS(psn, lang='id', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-it " in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:
                 psn = msg.text.replace("Vn-it ","")
                 tts = gTTS(psn, lang='it', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-jp " in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:
                 psn = msg.text.replace("Vn-jp ","")
                 tts = gTTS(psn, lang='ja', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-km " in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:
                 psn = msg.text.replace("Vn-km ","")
                 tts = gTTS(psn, lang='km', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-ko " in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:
                 psn = msg.text.replace("Vn-ko ","")
                 tts = gTTS(psn, lang='ko', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-la " in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:
                 psn = msg.text.replace("Vn-la ","")
                 tts = gTTS(psn, lang='la', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-lv " in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:
                 psn = msg.text.replace("Vn-lv ","")
                 tts = gTTS(psn, lang='lv', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-mk " in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:
                 psn = msg.text.replace("Vn-mk ","")
                 tts = gTTS(psn, lang='mk', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-no " in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:
                 psn = msg.text.replace("Vn-no ","")
                 tts = gTTS(psn, lang='no', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-pl " in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:
                 psn = msg.text.replace("Vn-pl ","")
                 tts = gTTS(psn, lang='pl', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-pt " in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:
                 psn = msg.text.replace("Vn-pt ","")
                 tts = gTTS(psn, lang='pt', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-ro " in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:
                 psn = msg.text.replace("Vn-ro ","")
                 tts = gTTS(psn, lang='ro', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-ru " in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:
                 psn = msg.text.replace("Vn-ru ","")
                 tts = gTTS(psn, lang='ru', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-sr " in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:
                 psn = msg.text.replace("Vn-sr ","")
                 tts = gTTS(psn, lang='sr', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-si " in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:
                 psn = msg.text.replace("Vn-si ","")
                 tts = gTTS(psn, lang='si', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-sk " in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:
                 psn = msg.text.replace("Vn-sk ","")
                 tts = gTTS(psn, lang='sk', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-es " in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:
                 psn = msg.text.replace("Vn-es ","")
                 tts = gTTS(psn, lang='es', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-eses " in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:
                 psn = msg.text.replace("Vn-eses ","")
                 tts = gTTS(psn, lang='es-es', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-esus " in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:
                 psn = msg.text.replace("Vn-esus ","")
                 tts = gTTS(psn, lang='es-us', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-sw " in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:
                 psn = msg.text.replace("Vn-sv ","")
                 tts = gTTS(psn, lang='sv', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-ta " in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:
                 psn = msg.text.replace("Vn-ta ","")
                 tts = gTTS(psn, lang='ta', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-th " in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:
                 psn = msg.text.replace("Vn-th ","")
                 tts = gTTS(psn, lang='th', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-tr " in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:
                 psn = msg.text.replace("Vn-tr ","")
                 tts = gTTS(psn, lang='tr', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-uk " in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:
                 psn = msg.text.replace("Vn-uk ","")
                 tts = gTTS(psn, lang='uk', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-vi " in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:
                 psn = msg.text.replace("Vn-vi ","")
                 tts = gTTS(psn, lang='vi', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-cy " in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:
                 psn = msg.text.replace("Vn-cy ","")
                 tts = gTTS(psn, lang='cy', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
			
			
 #=======================================================
            elif "Kickall" == msg.text:
		    if msg.from_ in creator + peminjam:
                     if msg.toType == 2:
                        print "Kick all member"
                        _name = msg.text.replace("Kickall","")
                        gs = cl.getGroup(msg.to)
                        cl.sendText(msg.to,"Dadaaah~")
                        targets = []
                        for g in gs.members:
                            if _name in g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to,"Not found.")
                        else:
                            for target in targets:
				if target not in creator:
                                    try:
                                        cl.kickoutFromGroup(msg.to,[target])
                                        ki.kickoutFromGroup(msg.to,[target])
                                        kk.kickoutFromGroup(msg.to,[target])
                                        ke.kickoutFromGroup(msg.to,[target])
                                        ka.kickoutFromGroup(msg.to,[target])
                                        kc.kickoutFromGroup(msg.to,[target])					
                                        print (msg.to,[g.mid])
                                    except Exception as e:
                                        cl.sendText(msg.to,str(e))
			    cl.inviteIntoGroup(msg.to, targets)

            elif msg.text in ["Invite user"]:
              if msg.from_ in admin + staff + creator + peminjam:	
                 wait["winvite"] = True
                 cl.sendText(msg.to,"send contact")
		
            elif msg.text in ["Invite","ดึง"]:
              if msg.from_ in admin + staff + creator + peminjam:
                wait["winvite"] = True
                random.choice(KAC).sendText(msg.to,"send contact 😉")
		
            elif msg.text in ["Myname"]:
                h = cl.getContact(mid)
                cl.sendText(msg.to,"===[DisplayName]===\n" + h.displayName)
            elif msg.text in ["Mybio"]:
                    h = cl.getContact(mid)
                    cl.sendText(msg.to,"===[StatusMessage]===\n" + h.statusMessage)
            elif msg.text in ["Mypict"]:
                    h = cl.getContact(mid)
                    cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in ["Myvid"]:
                    h = cl.getContact(mid)
                    cl.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in ["Urlpict"]:
                    h = cl.getContact(mid)
                    cl.sendText(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in ["Mycover"]:
                    h = cl.getContact(mid)
                    cu = cl.channel.getCover(mid)          
                    path = str(cu)
                    cl.sendImageWithURL(msg.to, path)
            elif msg.text in ["Urlcover"]:
                    h = cl.getContact(mid)
                    cu = cl.channel.getCover(mid)          
                    path = str(cu)
                    cl.sendText(msg.to, path)
 #=======================================================
            elif "Translate-arab " in msg.text:
                txt = msg.text.replace("Translate-arab ","")
                try:
                    translator = Translator()
                    trs = translator.translate(txt,'ar')
                    A = trs.text
                    A = A.encode('utf-8')
                    cl.sendText(msg.to,A)
                except:
                      cl.sendText(msg.to,'Error.')
            elif "Translate-korea " in msg.text:
                txt = msg.text.replace("Translate-korea ","")
                try:
                    translator = Translator()
                    trs = translator.translate(txt,'ko')
                    A = trs.text
                    A = A.encode('utf-8')
                    cl.sendText(msg.to,A)
                except:
                      cl.sendText(msg.to,'Error.')
            elif "Translate-chin " in msg.text:
                txt = msg.text.replace("Translate-chin ","")
                try:
                    translator = Translator()
                    trs = translator.translate(txt,'zh-cn')
                    A = trs.text
                    A = A.encode('utf-8')
                    cl.sendText(msg.to,A)
                except:
                      cl.sendText(msg.to,'Error.')
	    elif "Translate-japan " in msg.text:
                txt = msg.text.replace("Translate-japan ","")
                try:
                    translator = Translator()
                    trs = translator.translate(txt,'ja')
                    A = trs.text
                    A = A.encode('utf-8')
                    cl.sendText(msg.to,A)
                except:
                      cl.sendText(msg.to,'Error.')
   	    elif "Translate-thai " in msg.text:
                txt = msg.text.replace("Translate-thai ","")
                try:
                    translator = Translator()
                    trs = translator.translate(txt,'th')
                    A = trs.text
                    A = A.encode('utf-8')
                    cl.sendText(msg.to,A)
                except:
                      cl.sendText(msg.to,'Error.')
            elif "Translate-idn " in msg.text:
                txt = msg.text.replace("Translate-idn ","")
                try:
                    translator = Translator()
                    trs = translator.translate(txt,'id')
                    A = trs.text
                    A = A.encode('utf-8')
                    cl.sendText(msg.to,A)
                except:
                      cl.sendText(msg.to,'Error.')

            elif "Translate-eng " in msg.text:
                txt = msg.text.replace("Translate-eng ","")
                try:
                    translator = Translator()
                    trs = translator.translate(txt,'en')
                    A = trs.text
                    A = A.encode('utf-8')
                    cl.sendText(msg.to,A)
                except:
                      cl.sendText(msg.to,'Error.')

            elif "Say " in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:
                if msg.from_ in creator:
				bctxt = msg.text.replace("Say ","")
				cl.sendText(msg.to,(bctxt))
				kk.sendText(msg.to,(bctxt))
				kc.sendText(msg.to,(bctxt))
				ki.sendText(msg.to,(bctxt))
				ks.sendText(msg.to,(bctxt))
				ka.sendText(msg.to,(bctxt))
				
            elif "Idline: " in msg.text:
                msgg = msg.text.replace('Idline: ','')
                conn = cl.findContactsByUserid(msgg)
                if True:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': conn.mid}
                    cl.sendText(msg.to,"http://line.me/ti/p/~" + msgg)
                    cl.sendMessage(msg)			
##≠========================&=&==&=&=%=%=%=%==%=%=%=%;%;%;;%;;%;%
            elif msg.text in ["Sambutan on","Welcome message:on"]:
              if msg.from_ in admin + staff + creator + peminjam:
                if wait["welcomemsg"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"welcome message on\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"welcome message on\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["welcomemsg"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"welcome message on\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"welcome message on")
		
            elif msg.text in ["Sambutan off","Welcome message:off"]:
              if msg.from_ in admin + staff + creator + peminjam:
                if wait["welcomemsg"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"welcome message off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"welcome message off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["welcomemsg"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"welcome message off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"welcome message off\n\n"+ datetime.today().strftime('%H:%M:%S'))
			
#============================================================
            elif "Steal mid" in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                cl.sendText(msg.to,"Mc: " + key1)
            elif "Steal contact" in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]                
                mmid = cl.getContact(key1)
                msg.contentType = 13
                msg.contentMetadata = {"mid": key1}
                cl.sendMessage(msg)
            elif "Mc:" in msg.text:
              if msg.from_ in admin:
               if msg.from_ in creator + peminjam:
                mmid = msg.text.replace("Mc:","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)

#===============================================================
            elif msg.text in ["Backup:on"]:
              if msg.from_ in admin + staff + creator + peminjam:
                if wait["Backup"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"backup has been active\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"backup has been enable\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["Backup"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"backup has been active\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"backup has been enable\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Backup:off"]:
              if msg.from_ in admin + staff + creator + peminjam:
                if wait["Backup"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"backup has been unactive\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"backup has been desable\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["Backup"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"backup has been unactive\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"backup has been desable\n\n"+ datetime.today().strftime('%H:%M:%S'))
            
            elif msg.text in ["Auto like:on"]:
              if msg.from_ in admin + staff + creator + peminjam:
                if wait["likeOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done。")
                else:
                    wait["likeOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already。")
            elif msg.text in ["Auto like:off"]:
              if msg.from_ in admin + staff + creator + peminjam:	
                if wait["likeOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done。")
                else:
                    wait["likeOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already。")
            elif msg.text in ["Media:on"]:
              if msg.from_ in creator:
                if wait["media"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done。")
                else:
                    wait["media"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already。")
            elif msg.text in ["Media:off"]:
              if msg.from_ in creator:
                if wait["media"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done。")
                else:
                    wait["media"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already。")
			
            elif msg.text in ["Kickblack on"]:
              if msg.from_ in admin + staff + creator + peminjam:
                if wait["Kickblack"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"GW BILANG UDH COK。")
                else:
                    wait["Kickblack"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah aktif。")
            elif msg.text in ["Kickblack off"]:
              if msg.from_ in admin + staff + creator + peminjam:
                if wait["Kickblack"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"GW BILANG UDH COK。")
                else:
                    wait["Kickblack"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah di nonaktifkan。")
            elif msg.text in ["Prot on"]:
              if msg.from_ in admin + staff + creator + peminjam:	
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"GW BILANG UDH COK。")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah aktif。")
            elif msg.text in ["Prot off"]:
              if msg.from_ in admin + staff + creator + peminjam:	
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"GW BILANG UDH COK。")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah di nonaktifkan。")
#==========================================================
            elif msg.text == "Lurking":	
                    cl.sendText(msg.to, "Set point.")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                           pass
                    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.now().strftime('%Y-%m-%d %H:%M')
                    wait2['ROM'][msg.to] = {}
                    print wait2
            elif msg.text == "Result":           	
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"
                        cl.sendText(msg.to, "╔═══════════════%s\n╠════════════════\n%s╠═══════════════\n║Readig point creation:\n║ [%s]\n╚════════════════"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "anda slah ketik-_-")
			
            elif msg.text in ["Invite:on"]:
              if msg.from_ in admin + staff + creator + peminjam:	
                if wait["autorein"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done。")
                else:
                    wait["autorein"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already。")
            elif msg.text in ["Invite:off"]:
              if msg.from_ in admin + staff + creator + peminjam:	
                if wait["autorein"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done。")
                else:
                    wait["autorein"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already。")
            elif "Besar cinta " in msg.text:
                tanya = msg.text.replace("Besar cinta ","")
                jawab = ("0%","10%","20%","30%","40%","50%","60%","70%","80%","90%","100%")
                jawaban = random.choice(jawab)
                cl.sendText(msg.to,"Besar Cinta " + tanya + " adalah " + jawaban)
            elif ("Vkick" in msg.text):
				if msg.from_ in admin + staff + creator + peminjam:
					targets = []
					key = eval(msg.contentMetadata["MENTION"])
					key["MENTIONEES"][0]["M"]
					for x in key["MENTIONEES"]:
						targets.append(x["M"])
					for target in targets:
						try:
							cl.kickoutFromGroup(msg.to,[target])
						except:
							cl.sendText(msg.to,"Error")			
         #-------------Fungsi Change Clock Start------------------#
            elif msg.text in ["Change clock"]:
                n = msg.text.replace("Change clock","")
                if len(n.decode("utf-8")) > 13:
                    cl.sendText(msg.to,"changed")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"changed to\n\n" + n)
         #-------------Fungsi Change Clock Finish-----------------#  
            elif "Steal group pict" in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:
					group = cl.getGroup(msg.to)
					path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                                        cl.sendImageWithURL(msg.to,path)
            elif "Turn off bots" in msg.text:
               if msg.from_ in creator:
                 try:
                     import sys
                     sys.exit()
                 except:
                     pass
#==================================================================
            elif "Getbio" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)
                except:
                    cl.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)
            elif 'creator' in msg.text.lower():
				msg.contentType = 13
				msg.contentMetadata = {'mid': "uab1ca173166a362c69ef62d420f9f784"}
				cl.sendMessage(msg)
				cl.sendText(msg.to,"Pembuat kami")
            elif "Admin on @" in msg.text:
                if msg.from_ in creator + peminjam:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Admin on @","")
                    _nametarget = _name.rstrip(' ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                admin.append(target)
                                cl.sendText(msg.to,"succes add to adminlist")
                            except:
                                pass
                    print "[Command]Staff add executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"owner permission required.")
            elif msg.text.lower() == 'Admin list':
              if msg.from_ in admin + staff + creator + peminjam:
                if admin == []:
                       cl.sendText(msg.to,"The adminlist is empty")
                else:
                        cl.sendText(msg.to,"loading...")
                        mc = ""
                        gh = ""
                        for mi_d in owner:
                            mc += "->" +cl.getContact(mi_d).displayName + "\n"
		        for mi_d in admin:
			    gh += "->" +cl.getContact(mi_d).displayName + "\n"				
                        cl.sendText(msg.to,"=======OWNER=======\n\n" + mc + "\n=======ADMIN=======\n\n" + gh +"\n=====================\n")
                        print "[Command]Stafflist executed"
            elif "Expel on @" in msg.text:
                if msg.from_ in creator + peminjam:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Expel on @","")
                    _nametarget = _name.rstrip(' ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                admin.remove(target)
                                cl.sendText(msg.to,"Succes remove admin from adminlist")
                            except:
                                pass
                    print "[Command]Staff remove executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"owner permission required.")
            elif msg.text in ["Bye allgroups"]:
              if msg.from_ in creator:
				gid = cl.getGroupIdsJoined()
				for i in gid:
					kc.leaveGroup(i)
                                        ki.leaveGroup(i)
                                        kk.leaveGroup(i)
                                        ka.leaveGroup(i)
					ks.leaveGroup(i)
					kb.leaveGroup(i)					
				if wait["lang"] == "JP":
					cl.sendText(msg.to,"bye-bye")
				else:
					cl.sendText(msg.to,"He declined all invitations")
#-------Cek sider biar mirip kek siri-----------------------------
            elif "Setlastpoint" in msg.text:
                subprocess.Popen("echo '' > dataSeen/"+msg.to+".txt", shell=True, stdout=subprocess.PIPE)
                #cl.sendText(msg.to, "Checkpoint checked!")
                cl.sendText(msg.to, "Set the lastseens' point(｀・ω・´)\n\n" + datetime.now().strftime('%H:%M:%S'))
                print "Setlastpoint"
#--------------------------------------------
            elif "Viewlastseen" in msg.text:
	        lurkGroup = ""
	        dataResult, timeSeen, contacts, userList, timelist, recheckData = [], [], [], [], [], []
                with open('dataSeen/'+msg.to+'.txt','r') as rr:
                    contactArr = rr.readlines()
                    for v in xrange(len(contactArr) -1,0,-1):
                        num = re.sub(r'\n', "", contactArr[v])
                        contacts.append(num)
                        pass
                    contacts = list(set(contacts))
                    for z in range(len(contacts)):
                        arg = contacts[z].split('|')
                        userList.append(arg[0])
                        timelist.append(arg[1])
                    uL = list(set(userList))
                    for ll in range(len(uL)):
                        try:
                            getIndexUser = userList.index(uL[ll])
                            timeSeen.append(time.strftime("%d日 %H:%M:%S", time.localtime(int(timelist[getIndexUser]) / 1000)))
                            recheckData.append(userList[getIndexUser])
                        except IndexError:
                            conName.append('nones')
                            pass
                    contactId = cl.getContacts(recheckData)
                    for v in range(len(recheckData)):
                        dataResult.append(contactId[v].displayName + ' ('+timeSeen[v]+')')
                        pass
                    if len(dataResult) > 0:
                        grp = '\n• '.join(str(f) for f in dataResult)
                        total = '\nThese %iuesrs have seen at the lastseen\npoint(｀・ω・´)\n\n%s' % (len(dataResult), datetime.now().strftime('%H:%M:%S') )
                        cl.sendText(msg.to, "• %s %s" % (grp, total))
                    else:
                        cl.sendText(msg.to, "Sider ga bisa di read cek setpoint dulu bego tinggal ketik\nSetlastpoint\nkalo mau liat sider ketik\nViewlastseen")
                    print "Viewlastseen"
#==========================================
            elif msg.text in ["Purge"]:
              if msg.from_ in creator + peminjam:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        random.choice(KAC).sendText(msg.to,"group purge")
                        return
                    for jj in matched_list:
                        try:
                            klist=[ki,kk,kc,ks,ka]
                            kicker = random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass					
#------------------------------- CHECK SIDER --------------------------------
            if msg.text.lower() in ["/set"]:
                if msg.toType == 2:
                    cl.sendText(msg.to, "Sini Muncul")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                    wait2['ROM'][msg.to] = {}
                    print "[Command] Set"

            if msg.text.lower() in ["/check"]:
                if msg.toType == 2:
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print "[Command] Check"
                                chiya += rom[1] + "\n"
                        cl.sendText(msg.to, "✔ Read : %s\n\n✖ Sider :\n%s\nPoint creation date n time:\n[%s]"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        print "[Command] Set"
                    else:
                        cl.sendText(msg.to,"Read point tidak tersedia, Silahkan ketik /set untuk membuat Read point.")
        
         #-------------Fungsi Jam Update Start---------------------#            
            elif msg.text in ["Jam Update"]:
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = kc.getProfile()
                    profile.displayName = wait["cName4"] + nowT
                    kc.updateProfile(profile)
                    kc.sendText(msg.to,"Sukses update")
                else:
                    kc.sendText(msg.to,"Aktifkan jam terlebih dulu")
         #-------------Fungsi Jam Update Finish-------------------#

            elif msg.text == "Set":
                    cl.sendText(msg.to, "Check sider")
                    ki.sendText(msg.to, "Check sider")
                    kk.sendText(msg.to, "Check sider")
                    kc.sendText(msg.to, "Check sider")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['ROM'][msg.to] = {}
                    print wait2
            elif msg.text == "Read":
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"

                        cl.sendText(msg.to, "People who readed %s\nthat's it\n\nPeople who have ignored reads\n%sIt is abnormal ♪\n\nReading point creation date n time:\n[%s]"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "An already read point has not been set.\n「set」you can send ♪ read point will be created ♪")
#-----------------------------------------------
            elif "Pam @" in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:
                _name = msg.text.replace("Pam @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       satpam.sendText(msg.to,"Yuk dimulai spamnya")
                       cl.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ki.sendText(g.mid,"ASWLO GENTOD!!!!")
                       kc.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ke.sendText(g.mid,"ASWLO GENTOD!!!!")
                       kk.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ka.sendText(g.mid,"ASWLO GENTOD!!!!")
                       cl.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ki.sendText(g.mid,"ASWLO GENTOD!!!!")
                       kc.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ke.sendText(g.mid,"ASWLO GENTOD!!!!")
                       kk.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ka.sendText(g.mid,"ASWLO GENTOD!!!!")
                       cl.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ki.sendText(g.mid,"ASWLO GENTOD!!!!")
                       kc.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ke.sendText(g.mid,"ASWLO GENTOD!!!!")
                       kk.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ka.sendText(g.mid,"ASWLO GENTOD!!!!")
                       cl.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ki.sendText(g.mid,"ASWLO GENTOD!!!!")
                       kc.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ke.sendText(g.mid,"ASWLO GENTOD!!!!")
                       kk.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ka.sendText(g.mid,"ASWLO GENTOD!!!!")
                       cl.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ki.sendText(g.mid,"ASWLO GENTOD!!!!")
                       kc.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ke.sendText(g.mid,"ASWLO GENTOD!!!!")
                       kk.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ka.sendText(g.mid,"ASWLO GENTOD!!!!")
                       cl.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ki.sendText(g.mid,"ASWLO GENTOD!!!!")
                       kc.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ke.sendText(g.mid,"ASWLO GENTOD!!!!")
                       kk.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ka.sendText(g.mid,"ASWLO GENTOD!!!!")
                       cl.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ki.sendText(g.mid,"ASWLO GENTOD!!!!")
                       kc.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ke.sendText(g.mid,"ASWLO GENTOD!!!!")
                       kk.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ka.sendText(g.mid,"ASWLO GENTOD!!!!")
                       cl.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ki.sendText(g.mid,"ASWLO GENTOD!!!!")
                       kc.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ke.sendText(g.mid,"ASWLO GENTOD!!!!")
                       kk.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ka.sendText(g.mid,"ASWLO GENTOD!!!!")
                       cl.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ki.sendText(g.mid,"ASWLO GENTOD!!!!")
                       kc.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ke.sendText(g.mid,"ASWLO GENTOD!!!!")
                       kk.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ka.sendText(g.mid,"ASWLO GENTOD!!!!")
                       cl.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ki.sendText(g.mid,"ASWLO GENTOD!!!!")
                       kc.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ke.sendText(g.mid,"ASWLO GENTOD!!!!")
                       kk.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ka.sendText(g.mid,"ASWLO GENTOD!!!!")
                       cl.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ki.sendText(g.mid,"ASWLO GENTOD!!!!")
                       kc.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ke.sendText(g.mid,"ASWLO GENTOD!!!!")
                       kk.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ka.sendText(g.mid,"ASWLO GENTOD!!!!")
                       cl.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ki.sendText(g.mid,"ASWLO GENTOD!!!!")
                       kc.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ke.sendText(g.mid,"ASWLO GENTOD!!!!")
                       kk.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ka.sendText(g.mid,"ASWLO GENTOD!!!!")
                       cl.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ki.sendText(g.mid,"ASWLO GENTOD!!!!")
                       kc.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ke.sendText(g.mid,"ASWLO GENTOD!!!!")
                       kk.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ka.sendText(g.mid,"ASWLO GENTOD!!!!")
                       cl.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ki.sendText(g.mid,"ASWLO GENTOD!!!!")
                       kc.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ke.sendText(g.mid,"ASWLO GENTOD!!!!")
                       kk.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ka.sendText(g.mid,"ASWLO GENTOD!!!!")
                       cl.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ki.sendText(g.mid,"ASWLO GENTOD!!!!")
                       kc.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ke.sendText(g.mid,"ASWLO GENTOD!!!!")
                       kk.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ka.sendText(g.mid,"ASWLO GENTOD!!!!")
                       cl.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ki.sendText(g.mid,"ASWLO GENTOD!!!!")
                       kc.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ke.sendText(g.mid,"ASWLO GENTOD!!!!")
                       kk.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ka.sendText(g.mid,"ASWLO GENTOD!!!!")
                       cl.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ki.sendText(g.mid,"ASWLO GENTOD!!!!")
                       kc.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ke.sendText(g.mid,"ASWLO GENTOD!!!!")
                       kk.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ka.sendText(g.mid,"ASWLO GENTOD!!!!")
                       cl.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ki.sendText(g.mid,"ASWLO GENTOD!!!!")
                       kc.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ke.sendText(g.mid,"ASWLO GENTOD!!!!")
                       kk.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ka.sendText(g.mid,"ASWLO GENTOD!!!!")
                       cl.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ki.sendText(g.mid,"ASWLO GENTOD!!!!")
                       kc.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ke.sendText(g.mid,"ASWLO GENTOD!!!!")
                       kk.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ka.sendText(g.mid,"ASWLO GENTOD!!!!")
                       cl.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ki.sendText(g.mid,"ASWLO GENTOD!!!!")
                       kc.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ke.sendText(g.mid,"ASWLO GENTOD!!!!")
                       kk.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ka.sendText(g.mid,"ASWLO GENTOD!!!!")
                       cl.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ki.sendText(g.mid,"ASWLO GENTOD!!!!")
                       kc.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ke.sendText(g.mid,"ASWLO GENTOD!!!!")
                       kk.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ka.sendText(g.mid,"ASWLO GENTOD!!!!")
                       cl.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ki.sendText(g.mid,"ASWLO GENTOD!!!!")
                       kc.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ke.sendText(g.mid,"ASWLO GENTOD!!!!")
                       kk.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ka.sendText(g.mid,"ASWLO GENTOD!!!!")
                       cl.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ki.sendText(g.mid,"ASWLO GENTOD!!!!")
                       kc.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ke.sendText(g.mid,"ASWLO GENTOD!!!!")
                       kk.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ka.sendText(g.mid,"ASWLO GENTOD!!!!")
                       cl.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ki.sendText(g.mid,"ASWLO GENTOD!!!!")
                       kc.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ke.sendText(g.mid,"ASWLO GENTOD!!!!")
                       kk.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ka.sendText(g.mid,"ASWLO GENTOD!!!!")
                       cl.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ki.sendText(g.mid,"ASWLO GENTOD!!!!")
                       kc.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ke.sendText(g.mid,"ASWLO GENTOD!!!!")
                       kk.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ka.sendText(g.mid,"ASWLO GENTOD!!!!")
                       cl.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ki.sendText(g.mid,"ASWLO GENTOD!!!!")
                       kc.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ke.sendText(g.mid,"ASWLO GENTOD!!!!")
                       kk.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ka.sendText(g.mid,"ASWLO GENTOD!!!!")
                       cl.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ki.sendText(g.mid,"ASWLO GENTOD!!!!")
                       kc.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ke.sendText(g.mid,"ASWLO GENTOD!!!!")
                       kk.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ka.sendText(g.mid,"ASWLO GENTOD!!!!")
                       cl.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ki.sendText(g.mid,"ASWLO GENTOD!!!!")
                       kc.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ke.sendText(g.mid,"ASWLO GENTOD!!!!")
                       kk.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ka.sendText(g.mid,"ASWLO GENTOD!!!!")
                       cl.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ki.sendText(g.mid,"ASWLO GENTOD!!!!")
                       kc.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ke.sendText(g.mid,"ASWLO GENTOD!!!!")
                       kk.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ka.sendText(g.mid,"ASWLO GENTOD!!!!")
                       cl.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ki.sendText(g.mid,"ASWLO GENTOD!!!!")
                       kc.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ke.sendText(g.mid,"ASWLO GENTOD!!!!")
                       kk.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ka.sendText(g.mid,"ASWLO GENTOD!!!!")
                       cl.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ki.sendText(g.mid,"ASWLO GENTOD!!!!")
                       kc.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ke.sendText(g.mid,"ASWLO GENTOD!!!!")
                       kk.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ka.sendText(g.mid,"ASWLO GENTOD!!!!")
                       cl.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ki.sendText(g.mid,"ASWLO GENTOD!!!!")
                       kc.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ke.sendText(g.mid,"ASWLO GENTOD!!!!")
                       kk.sendText(g.mid,"ASWLO GENTOD!!!!")
                       ka.sendText(g.mid,"ASWLO GENTOD!!!!")
                       cl.sendText(msg.to,"Udah di spam tuh kali aja insyaf")

#-----------------------------------------------
            elif msg.text in ["Rejectall"]:
              if msg.from_ in creator + peminjam:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"All Invites has been Rejected")
                else:
                    cl.sendText(msg.to,"拒绝了全部的邀请。")
            elif 'clean invites' in msg.text.lower():
              if msg.from_ in admin + staff + creator + peminjam:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        random.choice(KAC).cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No one is inviting。")
                        else:
                            cl.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
			
            elif msg.text in ["Summon","kuchiyose","kuchiyose no jutsu","Crit","Crot","Sayang tag"]:
                    group = cl.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                    if jml <= 100:
                        summon(msg.to, nama)
                    if jml > 100 and jml < 200:
                        for i in range(0, 99):
                            nm1 += [nama[i]]
                        summon(msg.to, nm1)
                        for j in range(100, len(nama)-1):
                            nm2 += [nama[j]]
                        summon(msg.to, nm2)
                    if jml > 200  and jml < 700:
                        for i in range(0, 99):
                            nm1 += [nama[i]]
                        summon(msg.to, nm1)
                        for j in range(100, 199):
                            nm2 += [nama[j]]
                        summon(msg.to, nm2)
                        for k in range(200, 299):
                            nm3 += [nama[k]]
                        summon(msg.to, nm3)
                        for l in range(300, 399):
                            nm4 += [nama[l]]
                        summon(msg.to, nm4)
                        for l in range(400, 499):
                            nm4 += [nama[l]]
                        summon(msg.to, nm4)
                        for l in range(500, 599):
                            nm4 += [nama[l]]
                        summon(msg.to, nm4)
                        for l in range(600, 699):
                            nm4 += [nama[l]]
                        summon(msg.to, nm4)			
                        for m in range(700, len(nama)-1):
                            nm5 += [nama[m]]
                        summon(msg.to, nm5)
                    if jml > 700:
                         cl.sendText(msg.to,"Terlalu Banyak Men 700+")
                    cnt = Message()
                    cnt.text = "Jumlah:\n" + str(jml) +  " Members"
                    cnt.to = msg.to
                    kc.sendMessage(cnt)			
#================================================================================
            elif 'clear invites' in msg.text.lower():
              if msg.from_ in admin + staff + creator + peminjam:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        random.choice(KAC).cancelGroupInvitation(msg.to,[_mid])
                        cl.sendText(msg.to,"I pretended to cancel and canceled.")
            elif "Ulti " in msg.text:
              if msg.from_ in creator + peminjam:
                ulti0 = msg.text.replace("Ulti ","")
                ulti1 = ulti0.rstrip()
                ulti2 = ulti1.replace("@","")
                ulti3 = ulti2.rstrip()
                _name = ulti3
                gs = cl.getGroup(msg.to)
                ginfo = cl.getGroup(msg.to)
                gs.preventJoinByTicket = False
                cl.updateGroup(gs)
                invsend = 0
                Ticket = cl.reissueGroupTicket(msg.to)
                km.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.2)
                targets = []
                for s in gs.members:
                        if _name in s.displayName:
                                targets.append(s.mid)
                if targets ==[]:
                        sendMessage(msg.to,"user does not exist")
                        pass
                else:
                        for target in targets:
                                try:
                                        km.kickoutFromGroup(msg.to,[target])
                                        km.leaveGroup(msg.to)
                                        gs = cl.getGroup(msg.to)
                                        gs.preventJoinByTicket = True
                                        cl.updateGroup(gs)
                                        gs.preventJoinByTicket(gs)
                                        cl.updateGroup(gs)
                                        print (msg.to,[g.mid])
                                except:
                                        km.sendText(msg.t,"Ter ELIMINASI....")
                                        km.sendText(msg.to,"WOLES brooo....!!!")
                                        km.leaveGroup(msg.to)
                                        gs = cl.getGroup(msg.to)
                                        gs.preventJoinByTicket = True
                                        cl.updateGroup(gs)
                                        gs.preventJoinByTicket(gs)
                                        cl.updateGroup(gs)
            elif msg.text in ["Nyanyi","Taktuntuang"]:
              if msg.from_ in admin + staff + creator + peminjam:		
                G = cl.getGroup(msg.to)
                G.preventJoinByTicket = False
                cl.updateGroup(G)
                Ticket = cl.reissueGroupTicket(msg.to)
                km.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.2)	
                G = cl.getGroup(msg.to)
                G.preventJoinByTicket = True
                cl.updateGroup(G)		
                G = cl.getGroup(msg.to)	
                km.sendText(msg.to,"Waktunya nyanyi di grup")
                km.sendText(msg.to,"Aku belum mandi")
                km.sendText(msg.to,"Tak tun tuang")
                km.sendText(msg.to,"Tak tun tuang")
                km.sendText(msg.to,"Tapi masih cantik juga")
                km.sendText(msg.to,"Tak tun tuang")
                km.sendText(msg.to,"Tak tun tuang")
                km.sendText(msg.to,"apalagi kalau sudah mandi")
                km.sendText(msg.to,"Tak tun tuang")
                km.sendText(msg.to,"Pasti cantik sekali")
                km.sendText(msg.to,"yiha")
                km.sendText(msg.to,"Kalau orang lain melihatku")
                km.sendText(msg.to,"Tak tun tuang")
                km.sendText(msg.to,"Badak aku taba bana")
                km.sendText(msg.to,"Tak tun tuang")
                km.sendText(msg.to,"Tak tuntuang")
                km.sendText(msg.to,"Tapi kalau langsuang diidu")
                km.sendText(msg.to,"Tak tun tuang")
                km.sendText(msg.to,"Atagfirullah baunya")
                km.sendText(msg.to,"Males lanjutin ah")
                km.sendText(msg.to,"Sepi bat")
                kk.sendText(msg.to,"Iya sepi udah udah")
                cl.sendText(msg.to,"Gaada yang denger juga kita nyanyi")
                kk.sendText(msg.to,"Nah")
                km.sendText(msg.to,"Mending gua makan dulu")
                cl.sendText(msg.to,"Siyap")
                ki.sendText(msg.to,"Okeh")
                km.sendText(msg.to,"Katanya owner kita Jomblo ya")
                cl.sendText(msg.to,"Iya emang")
                km.sendText(msg.to,"Denger denger si lagi nyari pacar doi")
                kk.sendText(msg.to,"Udah ah gosip mulu doain aja biar dapet")
                km.sendText(msg.to,"Aamiin")
                km.sendText(msg.to,"Bye cuman numpang nyanyi doang wkwk")			      
                km.leaveGroup(msg.to)		
            elif "Spamin @" in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:
                _name = msg.text.replace("Spamin @","")
                _nametarget = _name.rstrip(' ')
                G = cl.getGroup(msg.to)
                G.preventJoinByTicket = False
                cl.updateGroup(G)
                Ticket = cl.reissueGroupTicket(msg.to)
                km.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.2)	
                G = cl.getGroup(msg.to)
                G.preventJoinByTicket = True
                cl.updateGroup(G)		
                G = cl.getGroup(msg.to)
                for g in G.members:
                    if _nametarget == g.displayName:
                       km.sendText(msg.to,"Dimulai spamnya ya biar insyaf")				      
                       km.sendText(g.mid,(wait["spam"]))
                       km.sendText(g.mid,(wait["spam"]))
                       km.sendText(g.mid,(wait["spam"]))
                       km.sendText(g.mid,(wait["spam"]))
                       km.sendText(g.mid,(wait["spam"]))
                       km.sendText(g.mid,(wait["spam"]))
                       km.sendText(g.mid,(wait["spam"]))
                       km.sendText(g.mid,(wait["spam"]))
                       km.sendText(g.mid,(wait["spam"]))
                       km.sendText(g.mid,(wait["spam"]))
                       km.sendText(g.mid,(wait["spam"]))
                       km.sendText(g.mid,(wait["spam"]))
                       km.sendText(g.mid,(wait["spam"]))
                       km.sendText(g.mid,(wait["spam"]))
                       km.sendText(g.mid,(wait["spam"]))
                       km.sendText(g.mid,(wait["spam"]))
                       km.sendText(g.mid,(wait["spam"]))
                       km.sendText(g.mid,(wait["spam"]))
                       km.sendText(g.mid,(wait["spam"]))
                       km.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       ki.sendText(g.mid,(wait["spam"]))
                       ka.sendText(g.mid,(wait["spam"]))
                       ks.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       ki.sendText(g.mid,(wait["spam"]))
                       kk.sendText(g.mid,(wait["spam"]))
                       ka.sendText(g.mid,(wait["spam"]))
                       ks.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       ki.sendText(g.mid,(wait["spam"]))
                       ka.sendText(g.mid,(wait["spam"]))
                       ks.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       ki.sendText(g.mid,(wait["spam"]))
                       kk.sendText(g.mid,(wait["spam"]))
                       ka.sendText(g.mid,(wait["spam"]))
                       ks.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       ki.sendText(g.mid,(wait["spam"]))
                       ka.sendText(g.mid,(wait["spam"]))
                       ks.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       ki.sendText(g.mid,(wait["spam"]))
                       kk.sendText(g.mid,(wait["spam"]))
                       ka.sendText(g.mid,(wait["spam"]))
                       ks.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       ki.sendText(g.mid,(wait["spam"]))
                       ka.sendText(g.mid,(wait["spam"]))
                       ks.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       ki.sendText(g.mid,(wait["spam"]))
                       kk.sendText(g.mid,(wait["spam"]))
                       ka.sendText(g.mid,(wait["spam"]))
                       ks.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       ki.sendText(g.mid,(wait["spam"]))
                       ka.sendText(g.mid,(wait["spam"]))
                       ks.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       ki.sendText(g.mid,(wait["spam"]))
                       kk.sendText(g.mid,(wait["spam"]))
                       ka.sendText(g.mid,(wait["spam"]))
                       ks.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       ki.sendText(g.mid,(wait["spam"]))
                       ka.sendText(g.mid,(wait["spam"]))
                       ks.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       ki.sendText(g.mid,(wait["spam"]))
                       kk.sendText(g.mid,(wait["spam"]))
                       ka.sendText(g.mid,(wait["spam"]))
                       ks.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       ki.sendText(g.mid,(wait["spam"]))
                       ka.sendText(g.mid,(wait["spam"]))
                       ks.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       ki.sendText(g.mid,(wait["spam"]))
                       kk.sendText(g.mid,(wait["spam"]))
                       ka.sendText(g.mid,(wait["spam"]))
                       ks.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       ki.sendText(g.mid,(wait["spam"]))
                       ka.sendText(g.mid,(wait["spam"]))
                       ks.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       ki.sendText(g.mid,(wait["spam"]))
                       kk.sendText(g.mid,(wait["spam"]))
                       ka.sendText(g.mid,(wait["spam"]))
                       ks.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       ki.sendText(g.mid,(wait["spam"]))
                       ka.sendText(g.mid,(wait["spam"]))
                       ks.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       ki.sendText(g.mid,(wait["spam"]))
                       kk.sendText(g.mid,(wait["spam"]))
                       ka.sendText(g.mid,(wait["spam"]))
                       ks.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       ki.sendText(g.mid,(wait["spam"]))
                       ka.sendText(g.mid,(wait["spam"]))
                       ks.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       ki.sendText(g.mid,(wait["spam"]))
                       kk.sendText(g.mid,(wait["spam"]))
                       ka.sendText(g.mid,(wait["spam"]))
                       ks.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       ki.sendText(g.mid,(wait["spam"]))
                       ka.sendText(g.mid,(wait["spam"]))
                       ks.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       ki.sendText(g.mid,(wait["spam"]))
                       kk.sendText(g.mid,(wait["spam"]))
                       ka.sendText(g.mid,(wait["spam"]))
                       ks.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       ki.sendText(g.mid,(wait["spam"]))
                       ka.sendText(g.mid,(wait["spam"]))
                       ks.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       ki.sendText(g.mid,(wait["spam"]))
                       kk.sendText(g.mid,(wait["spam"]))
                       ka.sendText(g.mid,(wait["spam"]))
                       ks.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       ki.sendText(g.mid,(wait["spam"]))
                       ka.sendText(g.mid,(wait["spam"]))
                       ks.sendText(g.mid,(wait["spam"]))		
                       km.sendText(msg.to,"Waktunya nyanyi di grup")
                       km.sendText(msg.to,"Aku belum mandi")
                       km.sendText(msg.to,"Tak tun tuang")
                       km.sendText(msg.to,"Tak tun tuang")
                       km.sendText(msg.to,"Tapi masih cantik juga")
                       km.sendText(msg.to,"Tak tun tuang")
                       km.sendText(msg.to,"Tak tun tuang")
                       km.sendText(msg.to,"apalagi kalau sudah mandi")
                       km.sendText(msg.to,"Tak tun tuang")
                       km.sendText(msg.to,"Pasti cantik sekali")
                       km.sendText(msg.to,"yiha")
                       km.sendText(msg.to,"Kalau orang lain melihatku")
                       km.sendText(msg.to,"Tak tun tuang")
                       km.sendText(msg.to,"Badak aku taba bana")
                       km.sendText(msg.to,"Tak tun tuang")
                       km.sendText(msg.to,"Tak tuntuang")
                       km.sendText(msg.to,"Tapi kalau langsuang diidu")
                       km.sendText(msg.to,"Tak tun tuang")
                       km.sendText(msg.to,"Atagfirullah baunya")
                       km.sendText(msg.to,"Males lanjutin ah")
                       km.sendText(msg.to,"Sepi bat")
                       kk.sendText(msg.to,"Iya sepi udah udah")
                       cl.sendText(msg.to,"Gaada yang denger juga kita nyanyi")
                       kk.sendText(msg.to,"Nah")
                       km.sendText(msg.to,"Mending gua makan dulu")
                       cl.sendText(msg.to,"Siyap")
                       ki.sendText(msg.to,"Okeh")
                       km.sendText(msg.to,"Katanya owner kita Jomblo ya")
                       cl.sendText(msg.to,"Iya emang")
                       km.sendText(msg.to,"Denger denger si lagi nyari pacar doi")
                       kk.sendText(msg.to,"Udah ah gosip mulu doain aja biar dapet")
                       km.sendText(msg.to,"Aamiin")
                       km.sendText(msg.to,"Bye cuman spamin doang wkwk")			      
                       km.leaveGroup(msg.to)
         #----------------Fungsi Join Group Start-----------------------#
            elif msg.text in ["Sini dong","Kuy join","Ayo masuk","My waifu sini"]:
              if msg.from_ in creator + peminjam:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
			ki.sendText(msg.to,"hadir sayang")
                        kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
			kk.sendText(msg.to,"aku juga sayang")
                        ks.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        ks.sendText(msg.to,"aku disini yang")
                        ka.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
			ka.sendText(msg.to,"ada apa sayang")
                        kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
			kc.sendText(msg.to,"Aku sayang kamu")	
                        kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
			kb.sendText(msg.to,"Aku cinta kamu")			
                        G = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        print "Bot Complete"
                        G.preventJoinByTicket(G)
                        cl.updateGroup(G)

            elif msg.text in ["_First join"]:
              if msg.form_ in creator + peminjam:
                  x = ki.getGroup(msg.to)
                  x.preventJoinByTicket = False
                  ki.updateGroup(x)
                  invsend = 0
                  Ti = ki.reissueGroupTicket(msg.to)
                  cl.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = ki.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ki.updateGroup(G)
                  Ticket = ki.reissueGroupTicket(msg.to)

            elif msg.text in ["_Second join"]:
              if msg.from_ in creator + peminjam:
                  x = cl.getGroup(msg.to)
                  x.preventJoinByTicket = False
                  cl.updateGroup(x)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  ki.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = cl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(msg.to)

            elif msg.text in ["_Third join"]:
              if msg.from_ in creator + peminjam:
                  x = cl.getGroup(msg.to)
                  x.preventJoinByTicket = False
                  cl.updateGroup(x)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  kk.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = cl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(msg.to)
                  
            elif msg.text in ["_Fourth join"]:
              if msg.from_ in creator + peminjam:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  kc.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = cl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(msg.to)
    #----------------------Fungsi Join Group Finish---------------#
            elif "Bot1 backup" in msg.text:
              if msg.from_ in admin + creator + peminjam:
                        try:
                            h = open('mydn.txt',"r")
                            name = h.read()
                            h.close()
                            x = name
                            profile = cl.getProfile()
                            profile.displayName = x
                            cl.updateProfile(profile)
                            i = open('mysm.txt',"r")
                            sm = i.read()
                            i.close()
                            y = sm
                            cak = cl.getProfile()
                            cak.statusMessage = y
                            cl.updateProfile(cak)
                            j = open('myps.txt',"r")
                            ps = j.read()
                            j.close()
                            p = ps
                            cl.updateProfilePicture(p)
                            cl.sendText(msg.to, "Succes")
                        except Exception as e:
                            cl.sendText(msg.to,"Gagagl!")
                            print e
            elif "Bot2 backup" in msg.text:
              if msg.from_ in admin + creator + peminjam:
                        try:
                            h = open('mgydn.txt',"r")
                            name = h.read()
                            h.close()
                            x = name
                            profile = ki.getProfile()
                            profile.displayName = x
                            ki.updateProfile(profile)
                            i = open('myesm.txt',"r")
                            sm = i.read()
                            i.close()
                            y = sm
                            cak = ki.getProfile()
                            cak.statusMessage = y
                            ki.updateProfile(cak)
                            j = open('mypfs.txt',"r")
                            ps = j.read()
                            j.close()
                            p = ps
                            ki.updateProfilePicture(p)
                            ki.sendText(msg.to, "Succes")
                        except Exception as e:
                            ki.sendText(msg.to,"Gagagl!")
                            print e
            elif "Bot3 backup" in msg.text:
              if msg.from_ in admin + creator + peminjam:
                        try:
                            h = open('msgydn.txt',"r")
                            name = h.read()
                            h.close()
                            x = name
                            profile = kk.getProfile()
                            profile.displayName = x
                            kk.updateProfile(profile)
                            i = open('mysfdgm.txt',"r")
                            sm = i.read()
                            i.close()
                            y = sm
                            cak = kk.getProfile()
                            cak.statusMessage = y
                            kk.updateProfile(cak)
                            j = open('gymyps.txt',"r")
                            ps = j.read()
                            j.close()
                            p = ps
                            kk.updateProfilePicture(p)
                            kk.sendText(msg.to, "Succes")
                        except Exception as e:
                            kk.sendText(msg.to,"Gagagl!")
                            print e
            elif "Bot4 backup" in msg.text:
              if msg.from_ in admin + creator + peminjam:	
                        try:
                            h = open('jhmydn.txt',"r")
                            name = h.read()
                            h.close()
                            x = name
                            profile = kc.getProfile()
                            profile.displayName = x
                            kc.updateProfile(profile)
                            i = open('myhfsm.txt',"r")
                            sm = i.read()
                            i.close()
                            y = sm
                            cak = kc.getProfile()
                            cak.statusMessage = y
                            kc.updateProfile(cak)
                            j = open('mypfhs.txt',"r")
                            ps = j.read()
                            j.close()
                            p = ps
                            kc.updateProfilePicture(p)
                            kc.sendText(msg.to, "Succes")
                        except Exception as e:
                            kc.sendText(msg.to,"Gagagl!")
                            print e
            elif "Bot5 backup" in msg.text:
              if msg.from_ in admin + creator + peminjam:
                        try:
                            h = open('madydn.txt',"r")
                            name = h.read()
                            h.close()
                            x = name
                            profile = ks.getProfile()
                            profile.displayName = x
                            ks.updateProfile(profile)
                            i = open('mysgjm.txt',"r")
                            sm = i.read()
                            i.close()
                            y = sm
                            cak = ks.getProfile()
                            cak.statusMessage = y
                            ks.updateProfile(cak)
                            j = open('myrdps.txt',"r")
                            ps = j.read()
                            j.close()
                            p = ps
                            ks.updateProfilePicture(p)
                            ks.sendText(msg.to, "Succes")
                        except Exception as e:
                            ks.sendText(msg.to,"Gagagl!")
                            print e
            elif "Bot6 backup" in msg.text:
              if msg.from_ in admin + creator + peminjam:
                        try:
                            h = open('mydnsgv.txt',"r")
                            name = h.read()
                            h.close()
                            x = name
                            profile = kt.getProfile()
                            profile.displayName = x
                            kt.updateProfile(profile)
                            i = open('jhmysm.txt',"r")
                            sm = i.read()
                            i.close()
                            y = sm
                            cak = kt.getProfile()
                            cak.statusMessage = y
                            kt.updateProfile(cak)
                            j = open('myiyps.txt',"r")
                            ps = j.read()
                            j.close()
                            p = ps
                            kt.updateProfilePicture(p)
                            kt.sendText(msg.to, "Succes")
                        except Exception as e:
                            kt.sendText(msg.to,"Gagagl!")
                            print e
				
            elif msg.text in ["Bot1 backup run"]:
              if msg.from_ in admin + creator + peminjam:
                    wek = cl.getContact(mid)
                    a = wek.pictureStatus
                    r = wek.displayName
                    i = wek.statusMessage
                    s = open('mydn.txt',"w")
                    s.write(r)
                    s.close()
                    t = open('mysm.txt',"w")
                    t.write(i)
                    t.close()
                    u = open('myps.txt',"w")
                    u.write(a)
                    u.close()
                    cl.sendText(msg.to, "backup has been active")
                    print wek
                    print a
                    print r
                    print i
            elif msg.text in ["Bot2 backup run"]:
              if msg.from_ in admin + creator + peminjam:
                    wek = ki.getContact(Amid)
                    a = wek.pictureStatus
                    r = wek.displayName
                    i = wek.statusMessage
                    s = open('mgydn.txt',"w")
                    s.write(r)
                    s.close()
                    t = open('myesm.txt',"w")
                    t.write(i)
                    t.close()
                    u = open('mypfs.txt',"w")
                    u.write(a)
                    u.close()
                    ki.sendText(msg.to, "backup has been active")
                    print wek
                    print a
                    print r
                    print i
            elif msg.text in ["Bot3 backup run"]:
              if msg.from_ in admin + creator + peminjam:
                    wek = kk.getContact(Bmid)
                    a = wek.pictureStatus
                    r = wek.displayName
                    i = wek.statusMessage
                    s = open('msgydn.txt',"w")
                    s.write(r)
                    s.close()
                    t = open('mysfdgm.txt',"w")
                    t.write(i)
                    t.close()
                    u = open('gymyps.txt',"w")
                    u.write(a)
                    u.close()
                    kk.sendText(msg.to, "backup has been active")
                    print wek
                    print a
                    print r
                    print i
            elif msg.text in ["Bot4 backup run"]:
              if msg.from_ in admin + creator + peminjam:
                    wek = kc.getContact(Cmid)
                    a = wek.pictureStatus
                    r = wek.displayName
                    i = wek.statusMessage
                    s = open('jhmydn.txt',"w")
                    s.write(r)
                    s.close()
                    t = open('myhfsm.txt',"w")
                    t.write(i)
                    t.close()
                    u = open('mypfhs.txt',"w")
                    u.write(a)
                    u.close()
                    kc.sendText(msg.to, "backup has been active")
                    print wek
                    print a
                    print r
                    print i
            elif msg.text in ["Bot5 backup run"]:
              if msg.from_ in admin + creator + peminjam:
                    wek = ks.getContact(Dmid)
                    a = wek.pictureStatus
                    r = wek.displayName
                    i = wek.statusMessage
                    s = open('madydn.txt',"w")
                    s.write(r)
                    s.close()
                    t = open('mysgjm.txt',"w")
                    t.write(i)
                    t.close()
                    u = open('myrdps.txt',"w")
                    u.write(a)
                    u.close()
                    ks.sendText(msg.to, "backup has been active")
                    print wek
                    print a
                    print r
                    print i
            elif msg.text in ["Bot6 backup run"]:
              if msg.from_ in admin + creator + peminjam:
                    wek = kt.getContact(Emid)
                    a = wek.pictureStatus
                    r = wek.displayName
                    i = wek.statusMessage
                    s = open('mydnsgv.txt',"w")
                    s.write(r)
                    s.close()
                    t = open('jhmysm.txt',"w")
                    t.write(i)
                    t.close()
                    u = open('myiyps.txt',"w")
                    u.write(a)
                    u.close()
                    kt.sendText(msg.to, "backup has been active")
                    print wek
                    print a
                    print r
                    print i
			
            elif msg.text.lower() == 'gift1':
              if msg.from_ in admin + staff + creator + peminjam:	
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '1'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text.lower() == 'gift2':
              if msg.from_ in admin + staff + creator + peminjam:	
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '2'}
                msg.text = None
                ki.sendMessage(msg)
            elif msg.text.lower() == 'gift3':
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '3'}
                msg.text = None
                kk.sendMessage(msg)
            elif msg.text.lower() == 'gift4':
              if msg.from_ in admin + staff + creator + peminjam:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '4'}
                msg.text = None
                kc.sendMessage(msg)
            elif msg.text.lower() == 'gift5':
              if msg.from_ in admin + staff + creator + peminjam:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '5'}
                msg.text = None
                kd.sendMessage(msg)
            elif msg.text.lower() == 'gift6':
              if msg.from_ in admin + staff + creator + peminjam:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}
                msg.text = None
                ke.sendMessage(msg)
            elif msg.text.lower() == 'spam gift':
              if msg.from_ in admin + staff + creator + peminjam:	
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '12'}
                msg.text = None
                ki.sendMessage(msg)
                kk.sendMessage(msg)
                kc.sendMessage(msg)
                cl.sendMessage(msg)
                ks.sendMessage(msg)
                ka.sendMessage(msg)
                ke.sendMessage(msg)
                ko.sendMessage(msg)
                ki.sendMessage(msg)
                kk.sendMessage(msg)
                kc.sendMessage(msg)
                cl.sendMessage(msg)
                ks.sendMessage(msg)
                ka.sendMessage(msg)
                ke.sendMessage(msg)
                ko.sendMessage(msg)
                ki.sendMessage(msg)
                kk.sendMessage(msg)
                kc.sendMessage(msg)
                cl.sendMessage(msg)
                ks.sendMessage(msg)
                ka.sendMessage(msg)
                ke.sendMessage(msg)
                kc.sendMessage(msg)												  
#========================================
            elif "Spam @" in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:		
                _name = msg.text.replace("Spam @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       cl.sendText(msg.to,"Start Spam")
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(msg.to, "Spam Succes biar dia Insyaf")
            elif msg.text.lower() == 'responsename':
              if msg.from_ in admin + staff + creator + peminjam:	
                profile = cl.getProfile()
                text = profile.displayName + ""
                cl.sendText(msg.to, text)
                profile = ki.getProfile()
                text = profile.displayName + ""
                ki.sendText(msg.to, text)
                profile = kk.getProfile()
                text = profile.displayName + ""
                kk.sendText(msg.to, text)
                profile = kc.getProfile()
                text = profile.displayName + ""
                kc.sendText(msg.to, text)
                profile = ka.getProfile()
                text = profile.displayName + ""
                ka.sendText(msg.to, text)
                profile = ks.getProfile()
                text = profile.displayName + ""	
                ks.sendText(msg.to, text)
                profile = kb.getProfile()
                text = profile.displayName + ""	
                kb.sendText(msg.to, text)		
	
            elif msg.text in ["Sayang!"]:
                print "EXCUTED -- ABSEN BOT"
                cl.sendText(msg.to,"bebih")
                ki.sendText(msg.to,"Hadir")
                kk.sendText(msg.to,"Sayang")
                kc.sendText(msg.to,"Micuuuuu")
                ks.sendText(msg.to,"Aku cinta")
	   	ka.sendText(msg.to,"😗😗😗😗😗😗")
		
            elif "Steal cover @" in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:	
                print "[Command]dp executing"
                _name = msg.text.replace("Steal cover @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            cu = cl.channel.getCover(target)
                            path = str(cu)
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"
            elif "Midpict:" in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:	
                umid = msg.text.replace("Midpict:","")
                contact = cl.getContact(umid)
                try:
                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                except:
                    image = "https://www.1and1.co.uk/digitalguide/fileadmin/DigitalGuide/Teaser/not-found-t.jpg"
                try:
                    cl.sendImageWithURL(msg.to,image)
                except Exception as error:
                    cl.sendText(msg.to,(error))
                    pass
	    elif msg.text in ["Remove all chat"]:
              if msg.from_ in admin + creator + peminjam:	
		cl.removeAllMessages(op.param2)
		ki.removeAllMessages(op.param2)
		kk.removeAllMessages(op.param2)
		ka.removeAllMessages(op.param2)
		ke.removeAllMessages(op.param2)
		cl.sendText(msg.to,"Removed all chat")
            elif msg.text in ["debug speed","Debug speed"]:
              if msg.from_ in admin + creator + peminjam:	
                cl.sendText(msg.to, "Measuring...")
                start = time.time()
                time.sleep(0.0001)
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sseconds" % (elapsed_time))    
                print "[Command]Speed palsu executed"
            elif "Steal pict " in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:	
                if msg.toType == 2:
                    msg.contentType = 0
                    steal0 = msg.text.replace("Steal pict ","")
                    steal1 = steal0.lstrip()
                    steal2 = steal1.replace("@","")
                    steal3 = steal2.rstrip()
                    _name = steal3
                    group = cl.getGroup(msg.to)
                    targets = []
                    for g in group.members:
                        if _name == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"not found")
                    else:
                        for target in targets:
                            try:
                                contact = cl.getContact(target)
                                try:
                                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                except:
                                    image = "https://www.1and1.co.uk/digitalguide/fileadmin/DigitalGuide/Teaser/not-found-t.jpg"
                                try:
                                    cl.sendImageWithURL(msg.to,image)
                                except Exception as error:
                                    cl.sendText(msg.to,(error))
                                    pass
                            except:
                                cl.sendText(msg.to,"Error!")
                                break
                else:
                    cl.sendText(msg.to,"Tidak bisa dilakukan di luar grup")
            elif "Pict group " in msg.text: 
                saya = msg.text.replace('Pict group ','')
                gid = cl.getGroupIdsJoined()
                for i in gid: 
                    h = cl.getGroup(i).name
                    gna = cl.getGroup(i)
                    if h == saya:
                       cl.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)
            elif msg.text in ["My name"]:
                    h = cl.getContact(mid)
                    cl.sendText(msg.to,"===[DisplayName]===\n" + h.displayName)
            elif msg.text in ["My bio"]:
                    h = cl.getContact(mid)
                    cl.sendText(msg.to,"===[StatusMessage]===\n" + h.statusMessage)
            elif msg.text in ["My pict"]:
                    h = cl.getContact(mid)
                    cl.sendImageWithUrl(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in ["My cover"]:
                    h = cl.getContact(mid)
                    cu = cl.channel.getCover(mid)
                    path = str(cu)
                    cl.sendImageWithUrl(msg.to, path)
	    elif "Pap set " in msg.text:
                wait["Pap"] = msg.text.replace("Pap set ","")
                cl.sendText(msg.to,"Pap Has Ben Set To")

	    elif msg.text in ["pap","Pap"]:
                cl.sendImageWithURL(msg.to,random.choice(wait["Pap"]))
				    
	    elif "Vn" in msg.text:
                say = msg.text.replace("Vn","")
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
	    elif msg.text in ["Kalender","/waktu"]:
                timeNow = datetime.now()
                timeHours = datetime.strftime(timeNow,"(%H:%M)")
                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                inihari = datetime.today()
                hr = inihari.strftime('%A')
                bln = inihari.strftime('%m')
                for i in range(len(day)):
                    if hr == day[i]: hasil = hari[i]
                for k in range(0, len(bulan)):
                    if bln == str(k): blan = bulan[k-1]
                rst = hasil + ", " + inihari.strftime('%d') + " - " + blan + " - " + inihari.strftime('%Y') + "\nJam : [ " + inihari.strftime('%H:%M:%S') + " ]"
                cl.sendText(msg.to, rst)
            elif "Creat group" in msg.text:
              if msg.from_ in admin + creator + peminjam:	
                thisgroup = cl.getGroups([msg.to])
                Mids = [contact.mid for contact in thisgroup[0].members] 
                mi_d = Mids[:33]
                cl.createGroup("New", mi_d)
                cl.sendText(msg.to,"Succes creat new group")
            elif msg.text in ["Like:friend", "Bot like temen"]:
                print "[Command]Like executed"
                cl.sendText(msg.to,"pertamax")
                try:
                  likefriend()
                except:
                  pass

	    elif "Cek zodiak " in msg.text:
                tanggal = msg.text.replace("Cek zodiak ","")
                r=requests.get('https://script.google.com/ macros/exec?service=AKfycbw7gKzP-WYV 2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                data=r.text
                data=json.loads(data)
                lahir = data["data"]["lahir"]
                usia = data["data"]["usia"]
                ultah = data["data"]["ultah"]
                zodiak = data["data"]["zodiak"]
                cl.sendText(msg.to,"Tanggal Lahir: "+lahir+"\n\nUsia:"+usia+"\n\nUltah: "+ultah+"\n\nZodiak: "+zodiak)
            elif "Steal " in msg.text:
              if msg.from_ in admin + creator:	
                    salsa = msg.text.replace("Steal ","")
                    Manis = cl.getContact(salsa)
                    Imoet = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                    try:
                        cover = cl.channel.getCover(Manis)
                    except:
                        cover = ""
                    cl.sendText(msg.to,"Gambar Foto Profilenya")
                    cl.sendImageWithURL(msg.to,Imoet)
                    if cover == "":
                        cl.sendText(msg.to,"User tidak memiliki cover atau sejenisnya")
                    else:
                        cl.sendText(msg.to,"Gambar Covernya")
                        cl.sendImageWithURL(msg.to,cover)
				    
            elif "Spam change:" in msg.text:
              if msg.from_ in admin + creator + peminjam:		
                wait["spam"] = msg.text.replace("Spam change:","")
                cl.sendText(msg.to,"spam changed")

            elif "Spam add:" in msg.text:
              if msg.from_ in admin + creator + peminjam:		
                wait["spam"] = msg.text.replace("Spam add:","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"spam changed")
                else:
                    cl.sendText(msg.to,"Done")

            elif "Spam:" in msg.text:
              if msg.from_ in admin + creator + peminjam:	
                strnum = msg.text.replace("Spam:","")
                num = int(strnum)
                for var in range(0,num):
                    cl.sendText(msg.to, wait["spam"])
				    
            elif "Spamg " in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:		
                   txt = msg.text.split(" ")
                   jmlh = int(txt[2])
                   teks = msg.text.replace("Spamg "+str(txt[1])+" "+str(jmlh)+ " ","")
                   tulisan = jmlh * (teks+"\n")
                   #Keke cantik <3
                   if txt[1] == "on":
                        if jmlh <= 999:
                             for x in range(jmlh):
                                   cl.sendText(msg.to, teks)
                        else:
                               cl.sendText(msg.to, "Out of range! ")
                   elif txt[1] == "off":
                         if jmlh <= 999:
                               cl.sendText(msg.to, tulisan)
                         else:
                               cl.sendText(msg.to, "Out of range! ")
			
            elif msg.text in ["Clear ban"]:
              if msg.from_ in admin + creator + peminjam:	
                wait["blacklist"] = {}
           	f=codecs.open('st2__b.json','w','utf-8')
              	json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)		
                cl.sendText(msg.to,"Sukses Membersihkan Daftar Penjahat")
		
            elif "Add penyewa @" in msg.text:
              if msg.from_ in creator:	
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Add penyewa @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                peminjam.append(target)
                                cl.sendText(msg.to,"Added to the penyewa list")
                            except:
                                pass
                    print "[Command]Staff add executed"
              else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Creator permission required.")
            elif "crashkontak @" in msg.text:
                if msg.from_ in creator + peminjam:
                    _name = msg.text.replace("crashkontak @","")
                    _nametarget = _name.rstrip(' ')
                    gs = cl.getGroup(msg.to)
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            xname = g.displayName + g.mid
                            xlen = str(len(xname)+1)
                            msg.contentType = 13
                            msg.text = 'mid'+xname+''
                            msg.contentMetadata = {'mid': "u1f41296217e740650e0448b96851a3e2',"}
                            cl.sendMessage(msg)
                            cl.sendText("crash kontak selesai")
                            print " ASWLO GENTOD!!!! crash !"
            elif "Expel penyewa @" in msg.text:
              if msg.from_ in creator:	
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Expel penyewa @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                peminjam.remove(target)
                                cl.sendText(msg.to,"Removed to the penyewa list")
                            except:
                                pass
                    print "[Command]Staff remove executed"
              else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Creator permission required.")		
            elif msg.text in ["List penyewa","list penyewa"]:
                if peminjam == []:
                    cl.sendText(msg.to,"The penyewa is empty")
                else:
                    cl.sendText(msg.to,"penyewa list: ")
                    mc = ""
                    for mi_d in peminjam:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    print "[Command]Stafflist executed"	
            elif msg.text in ["Creatlist","list creator"]:
                if creator == []:
                    cl.sendText(msg.to,"The creator is empty")
                else:
                    cl.sendText(msg.to,"creator list: ")
                    mc = ""
                    for mi_d in creator:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    print "[Command]Stafflist executed"			
            elif "Add staff @" in msg.text:
              if msg.from_ in admin + creator + peminjam:	
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Add staff @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.append(target)
                                cl.sendText(msg.to,"Added to the staff list")
                            except:
                                pass
                    print "[Command]Staff add executed"
              else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")

            elif "Expel staff @" in msg.text:
              if msg.from_ in admin + creator + peminjam:	
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Expel staff @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.remove(target)
                                cl.sendText(msg.to,"Removed to the staff list")
                            except:
                                pass
                    print "[Command]Staff remove executed"
              else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")

            elif msg.text in ["Stafflist","stafflist"]:
                if staff == []:
                    cl.sendText(msg.to,"The stafflist is empty")
                else:
                    cl.sendText(msg.to,"Staff list: ")
                    mc = ""
                    for mi_d in staff:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    print "[Command]Stafflist executed"			
				    
#==========================================
            elif "Youtube " in msg.text.lower():
                   query = msg.text.split(" ")
                   try:
                       if len(query) == 3:
                           isi = yt(query[2])
                           hasil = isi[int(query[1])-1]
                           cl.sendText(msg.to, hasil)
                       else:
                           isi = yt(query[1])
                           cl.sendText(msg.to, isi[0])
                   except Exception as e:
                       cl.sendText(msg.to, str(e))
            elif 'Vidio ' in msg.text:
                  if wait["media"] == True:
                     try:
                         textToSearch = (msg.text).replace('Vidio ', "").strip()
                         query = urllib.quote(textToSearch)
                  	 url = "https://www.youtube.com/results?search_query=" + query
                 	 response = urllib2.urlopen(url)
                  	 html = response.read()
                   	 soup = BeautifulSoup(html, "html.parser")
                    	 results = soup.find(attrs={'class':'yt-uix-tile-link'})
                  	 ght=('https://www.youtube.com' + results['href'])
			 l.sendVideoWithURL(msg.to,ght)
               	     except:
                   	    cl.sendText(msg.to,"Could not find it")
		  else:
		       cl.sendText(msg.to,"turn on media")
            elif "Grupid" in msg.text:
                if msg.from_ in creator + peminjam:
                    saya = msg.text.replace('Grupid','')
                    gid = cl.getGroup(msg.to)
                    cl.sendText(msg.to, "[ID Grup : ]\n" + gid.id)		
            elif ("Ban repeat " in msg.text):
              if msg.from_ in admin + creator + peminjam:	
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      wait["blacklist"][target] = True
                      f=codecs.open('st2__b.json','w','utf-8')
                      json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                      cl.sendText(msg.to,"Succes Banned ")
                   except:
                      pass
	    elif "Autokick on" in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:							      
		     wait["AutoKick"] = True
		     cl.sendText(msg.to,"Auto Kick Sudah Aktif")

	    elif "Autokick off" in msg.text:
              if msg.from_ in admin + staff + creator + peminjam:							      
		     wait["AutoKick"] = False
		     cl.sendText(msg.to,"Auto Kick Sudah Di Nonaktifkan")

#========================================
            elif "Update welcome:" in msg.text:
              if msg.from_ in admin + creator + peminjam:	
                wait["welmsg"] = msg.text.replace("Update welcome:","")
                cl.sendText(msg.to,"update welcome message succes"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Check welcome message"]:
              if msg.from_ in admin + creator:	
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"yor bot message\n\n" + wait["welmsg"])
                else:
                    cl.sendText(msg.to,"The automatic appending information is set as follows。\n\n" + wait["welmsg"])

    #-------------Fungsi Leave Group Start---------------#
            elif msg.text in ["Bye waifuku","Bye semua"]:
              if msg.from_ in creator + peminjam:	
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                        kk.leaveGroup(msg.to)
                        ks.leaveGroup(msg.to)
                        ka.leaveGroup(msg.to)
                        kc.leaveGroup(msg.to)	
                        kb.leaveGroup(msg.to)	
                        cl.leaveGroup(msg.to)			
                    except:
                        pas
            elif msg.text in ["Bye all","Bye sayang"]:
              if msg.from_ in creator + peminjam:	
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
			ki.sendText(msg.to,"see you yang")
                        ki.leaveGroup(msg.to)
			kk.sendText(msg.to,"makasih sayang")
                        kk.leaveGroup(msg.to)
			ks.sendText(msg.to,"dadah bebih")
                        ks.leaveGroup(msg.to)
			ka.sendText(msg.to,"mblaem")
                        ka.leaveGroup(msg.to)
			kc.sendText(msg.to,"mblaem-mblaem")
                        kc.leaveGroup(msg.to)	
			kb.sendText(msg.to,"Bye coeg")
                        kb.leaveGroup(msg.to)						
                    except:
                        pass
            elif msg.text in ["Bye _Second"]:
              if msg.from_ in creator + peminjam:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Bye _Third"]:
              if msg.from_ in creator + peminjam:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kk.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Bye _Fourth"]:
              if msg.from_ in creator + peminjam:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kc.leaveGroup(msg.to)
                    except:
                        pass
    #-------------Fungsi Leave Group Finish---------------#
            elif "Gift @" in msg.text:
                _name = msg.text.replace("Gift @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members: 
                    if _nametarget == g.displayName:
                        msg.contentType = 9
                        msg.contentMetadata={'PRDID': '89131c1a-e549-4bd5-9e60-e24de0d2e252',
                                    'PRDTYPE': 'THEME', 'MSGTPL': '10'}
                        msg.text = None
                        cl.dendMessage(msg,g)

#==================================================
            elif "All rename:" in msg.text:
              if msg.from_ in creator:
                string = msg.text.replace("All rename:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = kk.getProfile()
                    profile.displayName = string
                    kk.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ka.getProfile()
                    profile.displayName = string
                    ka.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ke.getProfile()
                    profile.displayName = string
                    ke.updateProfile(profile)
            elif msg.text.lower() == 'allbio:':
              if msg.from_ in creator:
                string = msg.text.lower().replace("allbio:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kk.getProfile()
                    profile.statusMessage = string
                    kk.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ke.getProfile()
                    profile.statusMessage = string
                    ke.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
                    kk.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ka.getProfile()
                    profile.statusMessage = string
                    ka.updateProfile(profile)
                    cl.sendText(msg.to,"successfully turn it into: " + string + "")
            elif "My name:" in msg.text:
              if msg.from_ in creator:
                string = msg.text.replace("My name:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"change name: "+string+"\nsucces")
            elif "Bot2 rename:" in msg.text:
              if msg.from_ in creator:
                string = msg.text.replace("Bot2 rename:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                    ki.sendText(msg.to,"change name: "+string+"\nsucces")
            elif "Bot3 rename:" in msg.text:
              if msg.from_ in creator:
                string = msg.text.replace("Bot3 rename:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = kk.getProfile()
                    profile.displayName = string
                    kk.updateProfile(profile)
                    kk.sendText(msg.to,"change name: "+string+"\nsucces")
            elif "Bot4 rename:" in msg.text:
              if msg.from_ in creator:
                string = msg.text.replace("Bot4 rename:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ke.getProfile()
                    profile.displayName = string
                    ke.updateProfile(profile)
                    ke.sendText(msg.to,"change name: "+string+"\nsucces")
            elif "Bot5 rename:" in msg.text:
              if msg.from_ in creator:
                string = msg.text.replace("Bot5 rename:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ka.getProfile()
                    profile.displayName = string
                    ka.updateProfile(profile)
                    ka.sendText(msg.to,"change name: "+string+"\nsucces")											
            elif "Bot6 rename:" in msg.text:
              if msg.from_ in creator:
                string = msg.text.replace("Bot6 rename:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = satpam.getProfile()
                    profile.displayName = string
                    satpam.updateProfile(profile)
                    satpam.sendText(msg.to,"change name: "+string+"\nsucces") 
            elif "Bot7 rename:" in msg.text:
              if msg.from_ in creator:
                    string = msg.text.replace("Bot5 rename:","")
                    if len(string.decode('utf-8')) <= 20:												
                     profile = km.getProfile()
                     profile.displayName = string		
                     G = random.choice(KAC).getGroup(op.param1)
                     G.preventJoinByTicket = False
	             cl.updateGroup(G)
                     Ticket = cl.reissueGroupTicket(op.param1)
                     km.acceptGroupInvitationByTicket(op.param1,Ticket)
	             G.preventJoinByTicket = True
                     km.updateGroup(G)												
                     km.updateProfile(profile)
                     km.sendText(msg.to,"change name: "+string+"\nsucces")
                     km.leaveGroup(msg.to)												  
    #-------------Fungsi Tag All Start---------------#
            elif msg.text in ["kiwkiw","Tagall","Kuchiyose no jutsu","Summon all member","Kuchiyose"]:
                  group = cl.getGroup(msg.to)
                  nama = [contact.mid for contact in group.members]

                  cb = ""
                  cb2 = ""
                  strt = int(0)
                  akh = int(0)
                  for md in nama:
                      akh = akh + int(6)

                      cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""

                      strt = strt + int(7)
                      akh = akh + 1
                      cb2 += "@nrik \n"

                  cb = (cb[:int(len(cb)-1)])
                  msg.contentType = 0
                  msg.text = cb2
                  msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}

                  try:
                      cl.sendMessage(msg)
                  except Exception as error:
                      print error
    #-------------Fungsi Tag All Finish---------------#

         #----------------Fungsi Banned Kick Target Start-----------------------#
            elif msg.text in ["Kill "]:
              if msg.from_ in admin + creator + peminjam:	
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        kk.sendText(msg.to,"Selamat tinggal")
                        kc.sendText(msg.to,"Jangan masuk lagi􀨁􀆷devil smile􏿿")
                        return
                    for jj in matched_list:
                        try:
                            klist=[ki,kk,kc]
                            kicker=random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
         #----------------Fungsi Banned Kick Target Finish----------------------#                

            elif "cleansemua" in msg.text:
              if msg.from_ in creator + peminjam:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("cleansemua","")
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    ki.sendText(msg.to,"maaf kalo gak sopan")
                    kk.sendText(msg.to,"dasar kalian jones..")
                    kc.sendText(msg.to,"wkwk grup jones")
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': mid}
                    ks.sendMessage(msg)
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                          if target not in Bots:
                            try:
                                klist=[ki,kk,cl,ke,ka,kc]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
				 pass

            elif "Cleanse" in msg.text:
	      if msg.from_ in creator + peminjam:
                if msg.toType == 2:
                    print "ok cleanse"
                    _name = msg.text.replace("Cleanse","")
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    cl.sendText(msg.to,"Just some casual cleansing ")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"you are not admin")
                    else:
                        for target in targets:
                          if not target in Bots:
                            if not target in admin:
                              if not target in owner:
                                if not target in creator:
                                    try:
                                     klist=[ki,kk,ka,cl,ke,kc]
                                     kicker=random.choice(klist)
                                     kicker.kickoutFromGroup(msg.to,[target])
                                     print (msg.to,[g.mid])
                                    except:
                                     cl.sendText(msg.to,"Group cleanse")
        #----------------Fungsi Kick User Target Start----------------------#
            elif "Nk " in msg.text:
              if msg.from_ in admin + creator + peminjam:	
                       nk0 = msg.text.replace("Nk ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    klist=[cl,ki,kk,kc]
                                    kicker=random.choice(klist)
                                    kicker.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ki.sendText(msg.to,"Kasian Di Kick....")
                                    kc.sendText(msg.to,"Hehehe")
        #----------------Fungsi Kick User Target Finish----------------------#      

            elif '/wiki ' in msg.text.lower():	
                  try:
                      wiki = msg.text.lower().replace("wiki ","")
                      wikipedia.set_lang("id")
                      pesan="Title ("
                      pesan+=wikipedia.page(wiki).title
                      pesan+=")\n\n"
                      pesan+=wikipedia.summary(wiki, sentences=1)
                      pesan+="\n"
                      pesan+=wikipedia.page(wiki).url
                      cl.sendText(msg.to, pesan)
                  except:
                          try:
                              pesan="Over Text Limit! Please Click link\n"
                              pesan+=wikipedia.page(wiki).url
                              cl.sendText(msg.to, pesan)
                          except Exception as e:
                              cl.sendText(msg.to, str(e))
            elif msg.text.lower() == 'bot restart':
              if msg.from_ in admin + creator + peminjam:	
                    print "[Command]Like executed"
                    try:
                        cl.sendText(msg.to,"Restarting...")
                        restart_program()
                    except:
                        cl.sendText(msg.to,"Please wait")
                        restart_program()
                        pass
            elif msg.text.lower() == 'ifconfig':
              if msg.from_ in admin + staff + creator + peminjam:		
                    botKernel = subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO NetStat===")
            elif msg.text.lower() == 'system':
              if msg.from_ in admin + staff + creator + peminjam:	
                    botKernel = subprocess.Popen(["df","-h"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO SYSTEM===")
            elif msg.text.lower() == 'kernel':
              if msg.from_ in admin + staff + creator + peminjam:	
                    botKernel = subprocess.Popen(["uname","-srvmpio"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO KERNEL===")
            elif msg.text.lower() == 'cpu':
              if msg.from_ in admin + staff + creator + peminjam:	
                    botKernel = subprocess.Popen(["cat","/proc/cpuinfo"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO CPU===")
            elif msg.text.lower() == 'runtime':
              if msg.from_ in admin + staff + creator + peminjam + peminjam:	
                eltime = time.time()
                van = "Bot has been running for "+waktu(eltime)
                cl.sendText(msg.to,van)
            elif msg.text in ["Simisimi on","Simisimi:on"]:
              if msg.from_ in admin + creator + peminjam:													  
                settings["simiSimi"][msg.to] = True
                cl.sendText(msg.to," Simisimi Di Aktifkan")
                
            elif msg.text in ["Simisimi off","Simisimi:off"]:
              if msg.from_ in admin + creator + peminjam:													  
                settings["simiSimi"][msg.to] = False
                cl.sendText(msg.to,"Simisimi Di Nonaktifkan")
		
            elif "Fancytext: " in msg.text:
                    txt = msg.text.replace("Fancytext: ", "")
                    cl.kedapkedip(msg.to,txt)
                    print "[Command] Kedapkedip"

#--------------------------------------------------------
            elif "Image " in msg.text:
              if wait["media"] == True:
                 search = msg.text.replace("Image ","")
                 url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                 raw_html = (download_page(url))
                 items = []
                 items = items + (_images_get_all_items(raw_html))
                 path = random.choice(items)
                 print path
                 try:
                     cl.sendImageWithURL(msg.to,path)
                 except:
                     pass
	      else:
                   cl.sendText(msg.to," Turn on media") 
#--------------------------------------------------------
            elif "Youtubesearch: " in msg.text:
                    query = msg.text.replace("Youtube ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'http://www.youtube.com/results'
                        params = {'search_query': query}
                        r = s.get(url, params=params)
                        soup = BeautifulSoup(r.content, 'html.parser')
                        hasil = ""
                        for a in soup.select('.yt-lockup-title > a[title]'):
                            if '&list=' not in a['href']:
                                hasil += ''.join((a['title'],'\nUrl : http://www.youtube.com' + a['href'],'\n\n'))
                        cl.sendText(msg.to,hasil)
                        print '[Command] Youtube Search'          

            elif "Id@en" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'en'
                kata = msg.text.replace("Id@en ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"════FROM ID════\n" + "" + kata + "\n════TO ENGLISH════\n" + "" + result + "\n══════SUKSES═════")

            elif 'clean invites' in msg.text.lower():
              if msg.from_ in admin:
               if msg.from_ in creator + peminjam:	
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        random.choice(KAC).cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No one is inviting。")
                        else:
                            cl.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            #----------------Fungsi Banned User Target Start-----------------------#
            elif "Banned @" in msg.text:
              if msg.from_ in admin + creator + peminjam:	
                if msg.toType == 2:
                    print "[Banned] Sukses"
                    _name = msg.text.replace("Banned @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Dilarang Banned Bot")
                        ki.sendText(msg.to,"Dilarang Banned Bot")
                        kc.sendText(msg.to,"Dilarang Banned Bot")
                        ko.sendText(msg.to,"Dilarang Banned Bot")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Akun begini mah banned aja")
                            except:
                                ki.sendText(msg.to,"Error")
            #----------------Fungsi Banned User Target Finish-----------------------# 
            
            #----------------Fungsi Unbanned User Target Start-----------------------#
            elif "Unban @" in msg.text:
              if msg.from_ in admin + creator + peminjam:	
                if msg.toType == 2:
                    print "[Unban] Sukses"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Tidak Ditemukan.....")
                        ki.sendText(msg.to,"Tidak Ditemukan.....")
                        kk.sendText(msg.to,"Tidak Ditemukan.....")
                        kc.sendText(msg.to,"Tidak Ditemukan.....")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Akun Bersih Kembali")
                            except:
                                ki.sendText(msg.to,"Error")
				
           #----------------Fungsi Unbanned User Target Finish-----------------------#
           
        #-------------Fungsi Spam Start---------------------#
            elif msg.text in ["Upchat","upchat"]:
                cl.sendText(msg.to,"Jones 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"Jones 􀔃􀆶squared up!􏿿")
                ko.sendText(msg.to,"Jones 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"Jones 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"Jones 􀔃􀆶squared up!􏿿")
                ko.sendText(msg.to,"Jones 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"Jones 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"Jones 􀔃􀆶squared up!􏿿")
                ko.sendText(msg.to,"Jones 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"Jones 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"Jones 􀔃􀆶squared up!􏿿")
                ko.sendText(msg.to,"Jones 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"Jones 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"Jones 􀔃􀆶squared up!􏿿")
                ko.sendText(msg.to,"Jones 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"Jones 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"Jones 􀔃􀆶squared up!􏿿")
                ko.sendText(msg.to,"Jones 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"Jones 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"Jones 􀔃􀆶squared up!􏿿")
                ko.sendText(msg.to,"Jones 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"Jones 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"Jones 􀔃􀆶squared up!􏿿")
                ko.sendText(msg.to,"Jones 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"Jones 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"Jones 􀔃􀆶squared up!􏿿")
                ko.sendText(msg.to,"Jones 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"Jones 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"Jones 􀔃􀆶squared up!􏿿")
                ko.sendText(msg.to,"Jones 􀔃􀆶squared up!􏿿")
        #-------------Fungsi Spam Finish---------------------#

        #-------------Fungsi Broadcast Start------------#
            elif "Bc " in msg.text:
				bctxt = msg.text.replace("Bc ","")
				ki.sendText(msg.to,(bctxt))
				kk.sendText(msg.to,(bctxt))
				kc.sendText(msg.to,(bctxt))
       #--------------Fungsi Broadcast Finish-----------#

            elif msg.text in ["Cv say hi"]:
                ki.sendText(msg.to,"Hi buddy 􀜁􀅔Har Har􏿿")
                kk.sendText(msg.to,"Hi buddy 􀜁􀅔Har Har􏿿")
                kc.sendText(msg.to,"Hi buddy 􀜁􀅔Har Har􏿿")

#-----------------------------------------------

            elif msg.text in ["Salam jones"]:
                ki.sendText(msg.to,"salam jones juga 􀜁􀅔Har Har􏿿")
                kc.sendText(msg.to,"salam jones juga 􀜁􀅔Har Har􏿿")
                ko.sendText(msg.to,"salam jones juga 􀜁􀅔Har Har􏿿")
            elif msg.text in ["Sayang dmn"]:
                ki.sendText(msg.to,"disinii beb")
                kc.sendText(msg.to,"disni jugaa yang")
                ko.sendText(msg.to,"kenapa beb?")
            elif msg.text in ["Bobo ah","Bobo dulu ah"]:
                ki.sendText(msg.to,"Selamat malam yang")
                kk.sendText(msg.to,"Have a nice dream beb 􀜁􀅔Har Har􏿿")
                kc.sendText(msg.to,"dadah beb")
            elif msg.text in ["Cv say chomel pekok"]:
                ki.sendText(msg.to,"Chomel pekok 􀜁􀅔Har Har􏿿")
                kk.sendText(msg.to,"Chomel pekok 􀜁􀅔Har Har􏿿")
                kc.sendText(msg.to,"Chomel pekok 􀜁􀅔Har Har􏿿")
            elif msg.text in ["#welcome"]:
                ki.sendText(msg.to,"Selamat datang di jones Family Room")
                kk.sendText(msg.to,"Jangan nakal ok!")
#-----------------------------------------------
            elif msg.text in ["PING","Ping","ping"]:
                ki.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                kk.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                kc.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
#-----------------------------------------------
#-------------------------------- WELCOME -----------------------------------
            if msg.text.lower() in ["wc","welcome"]:
                ginfo = cl.getGroup(msg.to)
                cl.sendText(msg.to,"Selamat Datang Di " + str(ginfo.name))
#-----------------------------------------------
            elif msg.text in ["Owner"]:
					msg.contentType = 13
					msg.contentMetadata = {'mid': "uab1ca173166a362c69ef62d420f9f784"}
					cl.sendMessage(msg)
		                        kk.sendText(msg.to,"Itu owner kami!")			
#-----------------------------------------------
					
       #-------------Fungsi Respon Start---------------------#
            elif msg.text in ["Respon","respon","Respon Dong","respon dong"]:
                cl.sendText(msg.to,"...")
                ki.sendText(msg.to,"......")
                kk.sendText(msg.to,"..........")
                kc.sendText(msg.to,"..............")
                ks.sendText(msg.to,"...................")
                ka.sendText(msg.to,"......................")
                kb.sendText(msg.to,"...........................")
                ko.sendText(msg.to,"...............................")
                ke.sendText(msg.to,"Complete 100%")
      #-------------Fungsi Respon Finish---------------------#
#------------------------------- Kerang Ajaib -------------------------------#
            elif "/apakah " in msg.text.lower():
                apk = msg.text.replace("/apakah ","")
                rnd = ['Ya','Tidak']
                p = random.choice(rnd)
                cl.sendText(msg.to,p)
                print "[Command] Kerang Ajaib"
#----------------------------------------------------------------------------

#------------------------------- COVER BY TAG -------------------------------#
            elif "cover @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("cover @","")
                    _nametarget = cover.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = cl.channel.getHome(target)
                                objId = h["result"]["homeInfo"]["objectId"]
                                cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/myhome/c/download.nhn?userid=" + target + "&oid=" + objId)
                            except Exception as error:
                                print error
                                cl.sendText(msg.to,"Upload image failed.")

            elif "Cover @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("Cover @","")
                    _nametarget = cover.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = cl.channel.getHome(target)
                                objId = h["result"]["homeInfo"]["objectId"]
                                cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/myhome/c/download.nhn?userid=" + target + "&oid=" + objId)
                            except Exception as error:
                                print error
                                cl.sendText(msg.to,"Upload image failed.")
#----------------------------------------------------------------------------
#-------------------------------- PP BY TAG ---------------------------------
            elif "pp @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("pp @","")
                    _nametarget = cover.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = cl.getContact(target)
                                cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                            except Exception as error:
                                print error
                                cl.sendText(msg.to,"Upload image failed.")

            elif "Pp @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("Pp @","")
                    _nametarget = cover.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = cl.getContact(target)
                                cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                            except Exception as error:
                                print error
                                cl.sendText(msg.to,"Upload image failed.")
#----------------------------------------------------------------------------
            elif 'lyric ' in msg.text.lower():
                try:
                    songname = msg.text.lower().replace('lyric ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'Lyric Lagu ('
                        hasil += song[0]
                        hasil += ')\n\n'
                        hasil += song[5]
                        cl.sendText(msg.to, hasil)
                except Exception as wak:
                        cl.sendText(msg.to, str(wak))
            elif 'wiki ' in msg.text.lower():
                  try:
                      wiki = msg.text.lower().replace("wiki ","")
                      wikipedia.set_lang("id")
                      pesan="Title ("
                      pesan+=wikipedia.page(wiki).title
                      pesan+=")\n\n"
                      pesan+=wikipedia.summary(wiki, sentences=1)
                      pesan+="\n"
                      pesan+=wikipedia.page(wiki).url
                      cl.sendText(msg.to, pesan)
                  except:
                          try:
                              pesan="Over Text Limit! Please Click link\n"
                              pesan+=wikipedia.page(wiki).url
                              cl.sendText(msg.to, pesan)
                          except Exception as e:
                              cl.sendText(msg.to, str(e))
            elif 'instagram ' in msg.text.lower():
                try:
                    instagram = msg.text.lower().replace("instagram ","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                    soup = BeautifulSoup(html.text, 'html5lib')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    user = "Name: " + text[-2] + "\n"
                    user1 = "Username: " + text[-1] + "\n"
                    followers = "Followers: " + text[0] + "\n"
                    following = "Following: " + text[2] + "\n"
                    post = "Post: " + text[4] + "\n"
                    link = "Link: " + "https://www.instagram.com/" + instagram
                    detail = "======INSTAGRAM INFO USER======\n"
                    details = "\n======INSTAGRAM INFO USER======"
                    cl.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                    cl.sendImageWithURL(msg.to, text1[0])
                except Exception as njer:
                	cl.sendText(msg.to, str(njer))
            elif 'music ' in msg.text.lower():
              if wait["media"] == True:
               	 try:
                     songname = msg.text.lower().replace('music ','')
                     params = {'songname': songname}
                     r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                     data = r.text
                     data = json.loads(data)
                     for song in data:
                         hasil = 'This is Your Music\n'
                         hasil += 'Judul : ' + song[0]
                         hasil += '\nDurasi : ' + song[1]
                         hasil += '\nLink Download : ' + song[4]
                         cl.sendText(msg.to, hasil)
                         cl.sendText(msg.to, "Please Wait for audio...")
                         cl.sendAudioWithURL(msg.to, song[3])
		 except Exception as njer:
		         cl.sendText(msg.to, str(njer))
	      else:
		   cl.sendText(msg.to, "Turn on Media")
		   
#-----------------------------------------------
            elif 'apakah' in msg.text.lower():
                tanya = msg.text.lower().replace("apakah","")
                jawab = ("Ya","Tidak","Mungkin","Bisa jadi")
                p = random.choice(jawab)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
		
            elif "/berapakah " in msg.text:
                apk = msg.text.replace("/berapakah ","")
                rnd = ['10%','20%','30%','40%','50%','60%','70%','80%','90%','100%','0%']
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")

            elif "/kapan " in msg.text:
                apk = msg.text.replace("/kapan ","")
                rnd = ["kapan kapan","besok","satu abad lagi","Hari ini","Tahun depan","Minggu depan","Bulan depan","Sebentar lagi","Tidak Akan Pernah"]
                p = random.choice(rnd)
                cl.sendText(msg.to,p)
		
            elif "Kapan " in msg.text:
                apk = msg.text.replace("Kapan ","")
                rnd = ["kapan kapan","besok","satu abad lagi","Hari ini","Tahun depan","Minggu depan","Bulan depan","Sebentar lagi","Tidak Akan Pernah"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
#---------------------------------- SONG ---------------------------------------------------------------------- SONG ------------------------------------
	    elif "/musik " in msg.text:
              if wait["media"] == True:
					songname = msg.text.replace("/musik ","")
					params = {"songname": songname}
					r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
					data = r.text
					data = json.loads(data)
					for song in data:
						abc = song[3].replace('https://','http://')
						cl.sendText(msg.to, "Title : " + song[0] + "\nLength : " + song[1] + "\nLink download : " + song[4])
						cl.sendText(msg.to, "Lagu " + song[0] + "\nSedang Di Prosses... Tunggu Sebentar ^_^ ")
						cl.sendAudioWithURL(msg.to,abc)
						cl.sendText(msg.to, "Selamat Mendengarkan Lagu " + song[0])
	      else:
		   cl.sendText(msg.to, "Turn on Media")	
            elif '/lirik ' in msg.text.lower():
                try:
                    songname = msg.text.lower().replace('/lirik ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'Lyric Lagu ('
                        hasil += song[0]
                        hasil += ')\n\n'
                        hasil += song[5]
                        cl.sendText(msg.to, hasil)
                except Exception as wak:
                        cl.sendText(msg.to, str(wak))
                        
	    elif "/musrik " in msg.text:
              if wait["media"] == True:
					songname = msg.text.replace("/musrik ","")
					params = {"songname": songname}
					r = requests.get('https://www.youtube.com/watch?v=%s' + urllib.urlencode(params))
					data = r.text
					data = json.loads(data)
					for song in data:
						abc = song[3].replace('https://','http://')
						hasil = 'Lyric Lagu ('
						hasil += song[0]
						hasil += ')\n\n'
						hasil += song[5]
						cl.sendText(msg.to, "Lagu " + song[0] + "\nSedang Di Prosses... Tunggu Sebentar ^_^ ")
						cl.sendAudioWithURL(msg.to,abc)
						cl.sendText(msg.to, "Title : " + song[0] + "\nLength : " + song[1] + "\nLink download : " + song[4] +"\n\n" + hasil)
						cl.sendText(msg.to, "Selamat Mendengarkan Lagu " + song[0])
	      else:
		   cl.sendText(msg.to, "Turn on Media")	
#----------------------------------------------------------------------------
            elif msg.text in ["Bot Like", "Bot like"]: #Semua Bot Ngelike Status Akun Utama
              if msg.from_ in creator or admin:
                print "[Command]Like executed"
                cl.sendText(msg.to,"Kami Siap Like Status Owner\nKami Delay untuk beberapa Detik\nJangan perintah kami dulu sampai kami Selesai Ngelike")
                try:
                  likePost()
                except:
                  pass
                
            elif msg.text in ["Like kamu", "Bot like temen"]: #Semua Bot Ngelike Status Teman
              if msg.from_ in creator or admin:
                print "[Command]Like executed"
                cl.sendText(msg.to,"Kami Siap Like Status Teman Boss")
                cl.sendText(msg.to,"Kami Siap Like Status Owner\nKami Delay untuk beberapa Detik\nJangan perintah kami dulu sampai kami Selesai Ngelike")
                try:
                  autolike()
                except:
                  pass
#--------------------------------- INSTAGRAM --------------------------------
            elif '/ig ' in msg.text.lower():
                try:
                    instagram = msg.text.lower().replace("/ig ","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                    soup = BeautifulSoup(html.text, 'html.parser')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    user = "Name: " + text[-2] + "\n"
                    user1 = "Username: " + text[-1] + "\n"
                    followers = "Followers: " + text[0] + "\n"
                    following = "Following: " + text[2] + "\n"
                    post = "Post: " + text[4] + "\n"
                    link = "Link: " + "https://www.instagram.com/" + instagram
                    detail = "========INSTAGRAM INFO ========\n"
                    details = "\n========INSTAGRAM INFO ========"
                    cl.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                    cl.sendImageWithURL(msg.to, text1[0])
                except Exception as njer:
                	cl.sendText(msg.to, str(njer))

#--------------------------[Youtube]---------------------
            elif 'Youtubevideo: ' in msg.text:
                try:
                    textToSearch = (msg.text).replace('Youtube ', "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                    cl.sendText(msg.to,'https://www.youtube.com' + results['href'])
                except:
                    cl.sendText(msg.to,"Could not find it")
#----------------------------------------------------------------------------
#--------------------------------- YOUTUBE ----------------------------------
            elif "/youtube " in msg.text:
                query = msg.text.replace("/youtube ","")
                with requests.session() as s:
                    s.headers['user-agent'] = 'Mozilla/5.0'
                    url = 'http://www.youtube.com/results'
                    params = {'search_query': query}
                    r = s.get(url, params=params)
                    soup = BeautifulSoup(r.content, 'html5lib')
                    hasil = ""
                    for a in soup.select('.yt-lockup-title > a[title]'):
                        if '&list=' not in a['href']:
                            hasil += ''.join((a['title'],'\nhttp://www.youtube.com' + a['href'],'\n\n'))
                    cl.sendText(msg.to,hasil)
                    print '[Command] Youtube Search'
#----------------------------------------------------------------------------
#--------------------------------- TRANSLATE --------------------------------
            elif "/translate-en " in msg.text:
                txt = msg.text.replace("/translate-en ","")
                try:
                    gs = goslate.Goslate()
                    trs = gs.translate(txt,'en')
                    cl.sendText(msg.to,trs)
                    print '[Command] Translate EN'
                except:
                    cl.sendText(msg.to,'Error.')

            elif "/translate-id " in msg.text:
                txt = msg.text.replace("/translate-en ","")
                try:
                    gs = goslate.Goslate()
                    trs = gs.translate(txt,'id')
                    cl.sendText(msg.to,trs)
                    print '[Command] Translate ID'
                except:
                    cl.sendText(msg.to,'Error.')
#----------------------------------------------------------------------------
      #-------------Fungsi Balesan Respon Start---------------------#
            elif msg.text in ["Ini Apa","ini apa","Apaan Ini","apaan ini"]:
                ki.sendText(msg.to,"Ya gitu deh intinya mah 􀨁􀅴questioning􏿿")

      #-------------Fungsi Balesan Respon Finish---------------------#

       #-------------Fungsi Speedbot Start---------------------#
            elif msg.text in ["Speedbot","speedbot","Sp","sp"]:
                start = time.time()
                cl.sendText(msg.to, "Waiting...")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sseconds" % (elapsed_time))
      #-------------Fungsi Speedbot Finish---------------------#

      #-------------Fungsi Banned Send Contact Start------------------#
            elif msg.text in ["Ban"]:
              if msg.from_ in admin + creator:		
                wait["wblacklist"] = True	
                cl.sendText(msg.to,"send contact")
                ki.sendText(msg.to,"send contact")
                kk.sendText(msg.to,"send contact")
                kc.sendText(msg.to,"send contact")
            elif msg.text in ["Unban"]:
              if msg.from_ in admin + creator:			
                wait["dblacklist"] = True
                cl.sendText(msg.to,"send contact")
                ki.sendText(msg.to,"send contact")
                kk.sendText(msg.to,"send contact")
                kc.sendText(msg.to,"send contact")
      #-------------Fungsi Banned Send Contact Finish------------------#

#-----------------------------------------------
            elif ".Youtube " in msg.text:
                 query = msg.text.replace(".Youtube ","")
                 with requests.session() as s:
                     s.headers['user-agent'] = 'Mozilla/5.0'
                     url    = 'http://www.youtube.com/results'
                     params = {'search_query': query}
                     r    = s.get(url, params=params)
                     soup = BeautifulSoup(r.content, 'html5lib')
                     for a in soup.select('.yt-lockup-title > a[title]'):
                         if '&List' not in a['href']:
                               cl.sendText(msg.to,'http://www.youtube.com' + a['href'] + a['title'])
#-----------------------------------------------

#-----------------------------------------------
            elif "Admin add @" in msg.text:
                if msg.from_ in creator + peminjam:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Admin add @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                admin.append(target)
                                cl.sendText(msg.to,"Admin Ditambahkan")
                            except:
                                pass
                    print "[Command]Staff add executed"
                else:
                    cl.sendText(msg.to,"Command DiTolak")
                    cl.sendText(msg.to,"Admin Tidak Bisa Menggunakan")

            elif "Admin remove @" in msg.text:
                if msg.from_ in creator + peminjam:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Admin remove @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                admin.remove(target)
                                cl.sendText(msg.to,"Admin Dihapus")
                            except:
                                pass
                    print "[Command]Staff remove executed"
                else:
                    cl.sendText(msg.to,"Command DiTolak")
                    cl.sendText(msg.to,"Admin Tidak Bisa Menggunakan")

            elif msg.text in ["Adminlist","adminlist"]:
              if msg.from_ in admin + creator + peminjam:	
                if admin == []:
                    cl.sendText(msg.to,"The adminlist is empty")
                else:
                    cl.sendText(msg.to,"Tunggu...")
                    mc = ""
                    for mi_d in admin:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    print "[Command]Stafflist executed" 
#-----------------------------------------------
            elif "Checkdate " in msg.text:
                tanggal = msg.text.replace("Checkdate ","")
                r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                data=r.text
                data=json.loads(data)
                lahir = data["data"]["lahir"]
                usia = data["data"]["usia"]
                ultah = data["data"]["ultah"]
                zodiak = data["data"]["zodiak"]
                cl.sendText(msg.to,"============ I N F O R M A S I ============\n"+"Date Of Birth : "+lahir+"\nAge : "+usia+"\nUltah : "+ultah+"\nZodiak : "+zodiak+"\n============ I N F O R M A S I ============")

            elif msg.text in ["Like:me","Like me"]: #Semua Bot Ngelike Status Akun Utama
                print "[Command]Like executed"
                cl.sendText(msg.to,"Like Status Owner")
                try:
                  likeme()
                except:
                  pass
                
            elif msg.text in ["Like:friend","Like friend"]: #Semua Bot Ngelike Status Teman
                print "[Command]Like executed"
                cl.sendText(msg.to,"Like Status Teman")
                try:
                  likefriend()
                except:
                  pass		
		
            elif msg.text in ["Memlist"]:   
                kontak = cl.getGroup(msg.to)
                group = kontak.members
                num=1
                msgs="═════════List Member═════════-"
                for ids in group:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═════════List Member═════════\n\nTotal Members : %i" % len(group)
                cl.sendText(msg.to, msgs)
                
            elif "Grupmember: " in msg.text:
                saya = msg.text.replace('Grupmember: ','')
                gid = cl.getGroupIdsJoined()
                num=1
                msgs="═════════List Member═════════-"
                for i in gid:
                    h = cl.getGroup(i).name
                    gna = cl.getGroup(i)
                    me = gna.members(i)
                    msgs+="\n[%i] %s" % (num, me.displayName)
                    num=(num+1)
                    msgs+="\n═════════List Member═════════\n\nTotal Members : %i" % len(me)
                    if h == saya:
                        cl.sendText(msg.to, msgs)		
#-----------------------------------------------
	    elif msg.text in ["Self Like"]:
		try:
		    print "activity"
		    url = cl.activity(limit=1)
		    print url
		    cl.like(url['result']['posts'][0]['userInfo']['mid'], url['result']['posts'][0]['postInfo']['postId'], likeType=1001)
		    cl.comment(url['result']['posts'][0]['userInfo']['mid'], url['result']['posts'][0]['postInfo']['postId'], "Mau Bot Protect?\nFollow ig : @rid1bdbx\nLalu dm ke dia")
		    cl.sendText(msg.to, "Success~")
		except Exception as E:
		    try:
			cl.sendText(msg.to,str(E))
		    except:
			pass

            elif "Steal " in msg.text:
              if msg.from_ in admin + staff + creator:	
                    salsa = msg.text.replace("Steal ","")
                    Manis = cl.getContact(salsa)
                    Imoet = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                    try:
                        cover = cl.channel.getCover(Manis)
                    except:
                        cover = ""
                    cl.sendText(msg.to,"Gambar Foto Profilenya")
                    cl.sendImageWithURL(msg.to,Imoet)
                    if cover == "":
                        cl.sendText(msg.to,"User tidak memiliki cover atau sejenisnya")
                    else:
                        cl.sendText(msg.to,"Gambar Covernya")
                        cl.sendImageWithURL(msg.to,cover)
			
                #----------------------
            elif "Pap cecan" in msg.text:
                tanya = msg.text.replace("Pap cecan","")
                jawab = ("https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQAa0KQ8XfoVfKRh82Ys63AX3VcuPml1JJFLk7iTEtMpmd7OzbN-yk_MGK6","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRPMwr1Igswf8wgrTURHbGAt9jn54SvimA6Ps6W6lCtItkrh4I-kA","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRg5SRVDjILsjUyBeLkBnbV96kX22_1mplLyjfCKws6nv8E_VtMDyV07e56bw","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTOXZ4yFF8R8vPVmEl21Txhvzh4YpUJkJ2uuO3KQLUzYIEVsuT9")
                jawaban = random.choice(jawab)
                cl.sendImageWithURL(msg.to,jawaban)
#-----------------------------------------------
#----------------------
            elif "Pap toket" in msg.text:
              if msg.from_ in adminsa + peminjam:
                tanya = msg.text.replace("Pap toket","")
                jawab = ("https://pbs.twimg.com/media/DQaSnbmUMAA67sE.jpg:large","https://4.bp.blogspot.com/-LUnpRcmusnk/WBtVDeVzYnI/AAAAAAAAAtA/PNMbmruQzYMBzOTFrRRhv2UVTGgnD6DmQCLcB/s400/IMG_20161102_212057.jpg","https://pbs.twimg.com/media/CzFralwUcAAuOuy.jpg","https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcTilO50kExe4q_t-l8Kfn98sxyrHcbWPWCu2GP2SNgg8XWGMaZc8h5zaxAeVA","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQKgSYYgB33GP3LAvVSYxKjDlbPokmtzSWjbWJogz8lbZMNSyvqJTE3qWpwBg","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTgwKO_CAdZpSlXVVfA29qglGQR00WHkeqq4JakyYDuzIW2tKhvGg","https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcSC3ZMq4PnCX5dj7Fc_N6HOG6R_XrmOM7r6uBtpEcBfbO4hMEXQirK_lU_ePw","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRgynJUxS4uYgaIiV_R6e4FY62QfhYRUEgYZg6psfJzWH_ci4dFng","https://2.bp.blogspot.com/-BBxz0kDierM/UX_0YauEVNI/AAAAAAAAFuc/vkUcWpqQOHU/s1600/ABG+Mansturbasi.jpg","https://pbs.twimg.com/media/BTRJOchCUAAlTqZ.jpg")
		jawaban = random.choice(jawab)
                cl.sendImageWithURL(msg.to,jawaban)
#-----------------------------------------------#----------------------
            elif "Pap anu" in msg.text:
              if msg.from_ in adminsa + peminjam:
                tanya = msg.text.replace("Pap anu","")
                jawab = ("https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQFFKdXErF56KzAa4oWnWQT34jmGKJ66lj1g0hnN4zwYh9GgW0dHWZfRnuM","https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQTn4_JMD1ZAg-XIk6JZ1Crhz9gtXEIS8AcjTA3SYmazAutt7ekHw","https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcTIVuITo7KicaU6UwPhol1Rvkq4aQwznly8Xl2SiTlAa_1FrSHuwhwV5XoElA")
                jawaban = random.choice(jawab)
                cl.sendImageWithURL(msg.to,jawaban)
#-----------------------------------------------
            elif "Steal @" in msg.text:
              if msg.from_ in admin + staff + creator:	
                    if msg.toType == 2:
                        steal = msg.text.replace("Steal @","")
                        stealname = steal.rstrip(" ")
                        group = cl.getGroup(msg.to)
                        targets = []
                        if steal == "":
                            cl.sendText(msg.to,"Invalid user")
                        else:
                            for i in group.members:
                                if stealname == i.displayName:
                                    targets.append(i.mid)
                            if targets == []:
                                cl.sendText(msg.to,"User tidak ditemukan")
                            else:
                                for target in targets:
                                    try:
                                        contact = cl.getContact(target)
                                        image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                        try:
                                            cover = cl.channel.getCover(contact)
                                        except:
                                            cover = ""
                                        try:
                                            cl.sendText(msg.to,"Gambar Foto Profilenya")
                                            cl.sendImageWithURL(msg.to,image)
                                            if cover == "":
                                                cl.sendText(msg.to,"User tidak memiliki cover atau sejenisnya")
                                            else:
                                                cl.sendText(msg.to,"Gambar Covernya")
                                                cl.sendImageWithURL(msg.to,cover)
                                        except Exception as error:
                                            cl.sendText(msg.to,(error))
                                            break
                                    except:
                                        cl.sendText(msg.to,"Error!")
                                        break
                    else:
                        cl.sendText(msg.to,"Tidak bisa dilakukan di luar wilayah")
#-----------------------------------------------
      #-------------Fungsi Bannlist Start------------------#          
            elif msg.text in ["Banlist"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"Tidak Ada Akun Terbanned")
                else:
                    ki.sendText(msg.to,"Blacklist user")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
      #-------------Fungsi Bannlist Finish------------------#  
      
            elif msg.text in ["Cek banned"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += mm + "\n"
                    cl.sendText(msg.to,cocoa + "")
            elif msg.text in ["Kill ban"]:
              if msg.from_ in admin + creator + peminjam:	
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"There was no blacklist user")
                        ki.sendText(msg.to,"There was no blacklist user")
                        kk.sendText(msg.to,"There was no blacklist user")
                        kc.sendText(msg.to,"There was no blacklist user")
                        return
                    for jj in matched_list:
                        cl.kickoutFromGroup(msg.to,[jj])
                        ki.kickoutFromGroup(msg.to,[jj])
                        kk.kickoutFromGroup(msg.to,[jj])
                        kc.kickoutFromGroup(msg.to,[jj])
                    cl.sendText(msg.to,"Blacklist gw kik aja")
                    ko.sendText(msg.to,"kok?")
                    ku.sendText(msg.to,"knp?")
                    kc.sendText(msg.to,"parah")
            elif msg.text in ["Clear"]:
              if msg.from_ in admin + staff + creator + peminjam:				
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"I pretended to cancel and canceled.")
            elif "random: " in msg.text:
              if msg.from_ in admin + creator + peminjam:	
                if msg.toType == 2:
                    strnum = msg.text.replace("random: ","")
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    try:
                        num = int(strnum)
                        group = cl.getGroup(msg.to)
                        for var in range(0,num):
                            name = "".join([random.choice(source_str) for x in xrange(10)])
                            time.sleep(0.01)
                            group.name = name
                            cl.updateGroup(group)
                    except:
                        cl.sendText(msg.to,"Error")
            elif msg.text in ["Kalender","Time","Waktu"]:
                timeNow = datetime.now()
                timeHours = datetime.strftime(timeNow,"(%H:%M)")
                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                inihari = datetime.today()
                hr = inihari.strftime('%A')
                bln = inihari.strftime('%m')
                for i in range(len(day)):
                    if hr == day[i]: hasil = hari[i]
                for k in range(0, len(bulan)):
                    if bln == str(k): blan = bulan[k-1]
                rst = hasil + ", " + inihari.strftime('%d') + " - " + blan + " - " + inihari.strftime('%Y') + "\nJam : [ " + inihari.strftime('%H:%M:%S') + " ]"
                cl.sendText(msg.to, rst)												  
            elif "albumat'" in msg.text:
                try:
                    albumtags = msg.text.replace("albumat'","")
                    gid = albumtags[:6]
                    name = albumtags.replace(albumtags[:34],"")
                    cl.createAlbum(gid,name)
                    cl.sendText(msg.to,name + "created an album")
                except:
                    cl.sendText(msg.to,"Error")
            elif "fakecat'" in msg.text:
                try:
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    name = "".join([random.choice(source_str) for x in xrange(10)])
                    anu = msg.text.replace("fakecat'","")
                    cl.sendText(msg.to,str(cl.channel.createAlbum(msg.to,name,anu)))
                except Exception as e:
                    try:
                        cl.sendText(msg.to,str(e))
                    except:
                        pass
        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True

def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"]
                cl.updateProfile(profile)

                profile2 = ki.getProfile()
                profile2.displayName = wait["cName2"]
                ki.updateProfile(profile2)

                profile3 = kk.getProfile()
                profile3.displayName = wait["cName3"]
                kk.updateProfile(profile3)

                profile4 = kc.getProfile()
                profile4.displayName = wait["cName4"]
                kc.updateProfile(profile4)

                profile5 = ks.getProfile()
                profile5.displayName = wait["cName5"]
                ks.updateProfile(profile5a)

                profile6 = ka.getProfile()
                profile6.displayName = wait["cName6"]
                ka.updateProfile(profile6)

                profile7 = kb.getProfile()
                profile7.displayName = wait["cName7"]
                kb.updateProfile(profile7)

                profile8 = ko.getProfile()
                profile8.displayName = wait["cName8"]
                ko.updateProfile(profile8)
                
                profile9 = ke.getProfile()
                profile9.displayName = wait["cName9"]
                ke.updateProfile(profile9)
                
                profile10 = ku.getProfile()
                profile10.displayName = wait["cName10"]
                ku.updateProfile(profile10)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()



while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
