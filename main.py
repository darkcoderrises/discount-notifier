import getlink,finder,getprevvalue,update,notifier

import flipkart,voxpop

links=getlink.init()
ans = ""
updater = ""

for link in links:
    flag=0
    k = finder.init(link)
    if(k=="flipkart"):
        ans=flipkart.init(link)
    elif(k=="voxpop"):
        ans=voxpop.init(link)
    else:
        flag=1
        ans=ans+"could not find for "+ link + '\n'

    if flag == 0:
        updater=updater+link+" "+ans+"\n";
        if int(ans)<int(getprevvalue.init(link)):
            if int(getprevvalue.init(link)) != 10000000000000:
                notifier.init("Hurry Prices Dropped from "+ getprevvalue.init(link) +" to " + ans +"\n"+link)
update.init(updater)
