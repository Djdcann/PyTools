import json
import re
import os
import urllib

# download_path = r"D:\Music\BandcampDL"
download_path = r"C:\Users\cannistrarod\Music\BandcampDL"

# download music from bandcamp URL
def bandcamp_download(url):
    site = urllib.urlopen(url)
    url_data = url.split('/')
    html = site.read()

    # determine if url is to album or track
    if len(url_data) < 5 or url_data[3] == 'album':
        m = re.search(r'(?<=album_title: )"(.+)"', html)
        album = m.group(1)
    else:
        album = url_data[4]

    # remove non-valid characters from path
    album = validate(album)

    print 'downloading album/track %s' % album

    m = re.search(r'(?<=trackinfo: )\[\{.+\}\]', html)

    if not os.path.exists(download_path + "\\" + album):
        os.makedirs(download_path + "\\" + album)

    # open file to write deets
    info = open(download_path + "\\" + album + "\\_id3_data.txt", "a+")
    info.write("URL: " + url + "\n")
    info.write("Album: " + album + "\n")

    data = json.loads(m.group(0))
    n = 0

    # foreach song in album
    for i in data:
        file = validate(i['title'])
        print 'downloading %s...' % file
        # print i['file']['mp3-128']
        path = '%s/%s.mp3' % (download_path + "\\" + album, file)
        mp3 = i['file']['mp3-128']

        n += 1
        line = "%s. %s\n" % (n, i['title'])
        info.write(line)

        # dl the file
        try:
            if "https:/" in mp3:
                urllib.urlretrieve(mp3, path)
            else:
                urllib.urlretrieve("https:" + mp3, path)
        except Exception as e:
            print e

    info.close()

    return album


# validate directory or file name
def validate(name):
    # return re.sub(r'[~"?+/#%&*{}:<>|\\]', '_', name)
    return re.sub(r'[^\w\-_\. ]', '_', name)


if __name__ == '__main__':
    # get_url = "https://elhuervo.bandcamp.com/album/le-temps"
    url = raw_input('Enter URL plz: ')

    # print get_url.split('/')
    bandcamp_download(url)
