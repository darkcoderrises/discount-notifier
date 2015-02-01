def init():
    file = open('link','r')
    a = str(file.read())
    return a.split('\n')
