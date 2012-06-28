# coding: utf-8

import urllib2
import urllib
import json

BASE_URLS = {
    'web': 'http://ajax.googleapis.com/ajax/services/search/web',
    'local': 'http://ajax.googleapis.com/ajax/services/search/local',
    'video': 'http://ajax.googleapis.com/ajax/services/search/video',
    'blog': 'http://ajax.googleapis.com/ajax/services/search/blogs',
    'news': 'http://ajax.googleapis.com/ajax/services/search/news',
    'book': 'http://ajax.googleapis.com/ajax/services/search/books',
    'image': 'http://ajax.googleapis.com/ajax/services/search/images',
}


def search(query, genre):
    q = urllib.urlencode({
        "q": query.encode("utf-8"),
        "v": 1.0,
        "hl": "jp",
    });

    data = json.loads(urllib2.urlopen(BASE_URLS[genre] + "?"  + q).read());

    return (data);

if __name__ == "__main__":
    query = u"オスプレイ";

    print search(query, "web");

