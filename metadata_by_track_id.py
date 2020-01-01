def metadata(t_id):
    import requests
    from lxml import html
    from lxml import etree
    import re

    url="https://open.spotify.com/track/"+str(t_id)

    r=requests.get(url).content
    tree=html.fromstring(r)

    t_name=tree.xpath('//*[@id="body"]/div[1]/header/div[3]/div[2]/div[1]/div[2]/h1/span/text()')
    t_artist=tree.xpath('//*[@id="body"]/div[1]/header/div[3]/div[2]/div[1]/div[2]/h2')
    t_cover_url=tree.xpath('//*[@id="body"]/div[1]/header/div[3]/div[2]/div[1]/div[1]/button/div[1]')

    #track artists
    a_artists=""
    for e in t_artist:
        a_artists+=str(etree.tostring(e, pretty_print=True))

    a_pat=">[a-zA-Z0-9\s!?§$%&#-_]+</a>"
    res_artists=re.findall(a_pat, a_artists)

    #pop ">By <"
    if res_artists[0] == ">By <":
        res_artists.pop(0)
    artists=[]
    for artist in range(len(res_artists)):
        artists.append(res_artists[artist][1:-4])

    #track cover
    for e in t_cover_url:
        cover_elem=str(etree.tostring(e, pretty_print=True))

    cover_pat="url\([\.a-zA-Z0-9\/-_]*\),"
    res_url=re.findall(cover_pat, cover_elem)
    cover_url=[res_url[0][6:-2]]

    return {
        "title": t_name,
        "artists": artists,
        "cover_url": cover_url
    }

if __name__ == "__main__":
    import sys
    arg=sys.argv
    arg.pop(0)
    if len(arg) != 1:
        print("This script needs exactly one argument (the track-ID)!")
    else:
        print(metadata(str(arg[0])))
