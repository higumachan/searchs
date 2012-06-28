#coding: utf-8

import urllib
import urllib2
import BeautifulSoup

URL = "http://b.hatena.ne.jp/search/text";

def search(query, user_count=None):
    q = {
        "q": query.encode("utf-8"),
    };
    if user_count:
        q["users"] = user_count;
    url_query = urllib.urlencode(q);
    html = urllib2.urlopen(URL + "?" + url_query).read();
    soup = BeautifulSoup.BeautifulSoup(html);

    search_results = soup.findAll(attrs={"class": "search-result"});
    results = [];
    for search_result in search_results:
        for a in search_result.findAll("a"):
            if (a["href"].find("http") != -1):
                results.append(a["href"]);

    print results
            

if __name__ == "__main__":
    search(u"オスプレイ");
