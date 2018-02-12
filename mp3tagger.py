from mutagen.id3 import ID3NoHeaderError
from mutagen.id3 import ID3, TIT2, TALB, TPE1, TPE2, COMM, USLT, TCOM, TCON, TDRC, TRCK, APIC
import datetime

y = datetime.datetime.now().year

def tagFile(file_path, title, artist, album, track, cover_path, year=y):
    idata = open(cover_path, 'rb').read()
    # create ID3 tag if not present
    try:
        tags = ID3(file_path)
        #id3 tags already exist
        return
    except ID3NoHeaderError:
        # print "Adding ID3 header;",
        tags = ID3()
        tags["TIT2"] = TIT2(encoding=3, text=title)
        tags["TALB"] = TALB(encoding=3, text=album)
        tags["TPE2"] = TPE2(encoding=3, text=artist)
        # tags["COMM"] = COMM(encoding=3, lang=u'eng', desc='desc', text=u'mutagen comment')
        tags["TPE1"] = TPE1(encoding=3, text=artist)
        # tags["TCOM"] = TCOM(encoding=3, text=u'mutagen Composer')
        # tags["TCON"] = TCON(encoding=3, text=u'mutagen Genre')
        tags["TDRC"] = TDRC(encoding=3, text=year)
        tags["TRCK"] = TRCK(encoding=3, text=track)
        tags["APIC"] = APIC(encoding=3, mime=u'image/jpeg', type=3, desc=u'cover', data=idata)

        tags.save(file_path)
