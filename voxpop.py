def init(link):
    import bs4
    from bs4 import NavigableString
    import urllib2


    try:
        webpage = urllib2.urlopen(link)
        soup = bs4.BeautifulSoup(webpage.read().decode('utf8'))
    except:
        print "Error"

    div=soup.findAll('div',{'class':'price'})[0]

    for tag in div.descendants:
        if not isinstance(tag,NavigableString):
            if tag.name=="span":
                return str(tag.string).replace('\n','').replace("/-","")
