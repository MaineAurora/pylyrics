#! /usr/bin/python3

import string
import urllib.request
import subprocess

def to(x, y):
    return x.find(y)
chars = list(i for i in string.ascii_lowercase) + ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

a = list((str(subprocess.getoutput("mocp -i|grep -w SongTitle:|sed 's/SongTitle://g'"))[1:]).lower())
b = list((str(subprocess.getoutput("mocp -i|grep -w Artist:|sed 's/Artist://g'"))[1:]).lower())


for i in a:
    if i not in chars:
        a.remove(i)

for i in b:
    if i not in chars:
        b.remove(i)


f = urllib.request.FancyURLopener({}).open("http://www.azlyrics.com/lyrics/{}/{}.html".format(b, a))

lyrics = str(f.read())[500:]
lyrics = lyrics[to(lyrics, "that. -->")+13:to(lyrics, "<!-- MxM banner")-32]
lyrics = "".join(lyrics.split("<br>"))
lyrics = lyrics.replace("\\n", "\n")
lyrics = "".join(lyrics.split('\\'))
lyrics = "".join(lyrics.split("<i>"))
lyrics = "".join(lyrics.split("</i>"))


lyrics = lyrics.replace("xe2x80x99", "'")
lyrics = lyrics.replace("&quot;" , '"')
lyrics = lyrics.replace("&amp;" , '&')
print("{}: {}\n\n".format(str(subprocess.getoutput("mocp -i|grep -w Artist:|sed 's/Artist://g'"))[1:], str(subprocess.getoutput("mocp -i|grep -w SongTitle:|sed 's/SongTitle://g'"))[1:]))
print(str(lyrics))
