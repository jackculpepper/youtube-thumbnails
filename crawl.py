
import json
import urllib

from urlparse import urlparse

start = 'ZehB5TVIUIM'
start = 'Nd5uptCfOmc'

url_template = 'https://gdata.youtube.com/feeds/api/videos/%s/related?v=2&alt=json&max-results=50'

queue = []
queue.append(start)

h = {}

def expand(id):
    children = []

    try:
        f = urllib.urlopen(url_template % id)
        str = f.read()
        f.close()

        response = json.loads(str)

        # print the first related video
        entries = response['feed']['entry']


        for e in entries:
            src = e['content']['src']

            p = urlparse(src)

            if p.scheme == 'https':
                # rip out the video id
                id = p.path.split('/')[-1]

                if not h.has_key(id):

                    with open('video_id.txt', 'a') as fh:
                        fh.write(id + '\n')

                    h[id] = 1
                    children.append(id)
            else:
                print "got scheme", p.scheme

#            if id == '0':
#                import IPython ; IPython.embed()

    except:
        pass

    return children

while len(queue):
    id = queue.pop()
    children = expand(id)
    queue = children + queue

    print "hash %d queue %d" % (len(h.keys()), len(queue))


