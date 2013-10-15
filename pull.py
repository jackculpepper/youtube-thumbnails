
import urllib
import os

video_ids = [line.strip() for line in open('video_id.txt')]

thumburl_fmt = 'http://img.youtube.com/vi/%s/0.jpg'

for i, v_id in enumerate(video_ids):
    thumburl = thumburl_fmt % v_id

    dpath = 'thumbnail/%s' % v_id[:2]
    if not os.path.isdir(dpath): os.makedirs(dpath)

    fpath = '%s/%s.jpg' % (dpath, v_id)

    if not os.path.isfile(fpath):
        jpeg = urllib.urlopen(thumburl).read()


        with open('%s/%s.jpg' % (dpath, v_id), 'w') as fh:
            fh.write(jpeg)

    print '\r%d / %d' % (i, len(video_ids)),

print

