from mutagen.mp3 import MP3
from mutagen.id3 import ID3NoHeaderError
from mutagen.id3 import ID3, TIT2, TALB, TPE1, TPE2, COMM, USLT, TCOM, TCON, TDRC, TRCK, APIC

filename = r"C:\Users\cannistrarod\Music\BandcampDL\Awakening _ep_\Open your Eyes.mp3"
cover = r"C:\Users\cannistrarod\Music\BandcampDL\Awakening _ep_\Dank.jpg"
idata = open(cover, 'rb').read()
# create ID3 tag if not present
try:
    tags = ID3(filename)
except ID3NoHeaderError:
    print "Adding ID3 header;",
    tags = ID3()

tags["TIT2"] = TIT2(encoding=3, text=u'Dank')
tags["TALB"] = TALB(encoding=3, text=u'mutagen Album Name')
tags["TPE2"] = TPE2(encoding=3, text=u'mutagen Band')
tags["COMM"] = COMM(encoding=3, lang=u'eng', desc='desc', text=u'mutagen comment')
tags["TPE1"] = TPE1(encoding=3, text=u'mutagen Artist')
tags["TCOM"] = TCOM(encoding=3, text=u'mutagen Composer')
tags["TCON"] = TCON(encoding=3, text=u'mutagen Genre')
tags["TDRC"] = TDRC(encoding=3, text=u'2010')
tags["TRCK"] = TRCK(encoding=3, text=u'1')
tags["APIC"] = APIC(encoding=3, mime=u'image/jpeg', type=3, desc=u'cover', data=idata)

tags.save(filename)
