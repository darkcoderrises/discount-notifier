def init(link):
    file = open('value','r')
    values = str(file.read())
    values = values.split('\n')
    for value in values:
        if value.count(link,0,len(value)):
                return value.split(" ")[1]
    return("10000000000000")
