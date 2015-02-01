def init(link):
    import bs4
    from bs4 import NavigableString
    import urllib2


    try:
        webpage = urllib2.urlopen(link)
        soup = bs4.BeautifulSoup(webpage.read().decode('utf8'))
    except:
        print "Error"

    div=soup.findAll('span',{'class':'selling-price'})[0]
    return str(div.string).replace("R","").replace("s.","").replace(",","").replace('\n',"").replace(' ',"")
