def init(link):
    length=len(link)
    if link.count("flipkart",0,length):
        return "flipkart"
    elif link.count("voxpop",0,length):
        return "voxpop"
    else:
        return "-1"
