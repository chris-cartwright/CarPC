
import xbmc
import xml.dom.minidom
import random

# Can't find a way to play the favourites list - manual approach it is
tree = xml.dom.minidom.parse("/storage/.kodi/userdata/favourites.xml")
nodes = tree.getElementsByTagName("favourite")
datas = [x.childNodes[0].data for x in nodes]

# Get just the file name
files = [x[11:-2] for x in datas]

# SystemRandom does appear to be random at each boot
rand = random.SystemRandom()
rand.shuffle(files)

songList = xbmc.PlayList(xbmc.PLAYLIST_MUSIC)
songList.clear()

for f in files:
    songList.add(f)

# This shuffle appears to use time()
# time will always be the same value because the RPi doesn't have an RTC
#songList.shuffle()

xbmc.executebuiltin("xbmc.playercontrol(RepeatAll)")

xbmc.Player().play(songList)
