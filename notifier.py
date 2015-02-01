def init(ans):
    import smtplib
    msg =  ans

    username = '' #your email id here
    password = '' #your password here

    fromaddr = username
    toaddrs = password

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()
