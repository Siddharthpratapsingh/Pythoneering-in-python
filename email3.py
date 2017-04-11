import smtplib

server = smtplib.SMTP('smtp.gmail.com',587)
server.login("siddharthsingh.ra@gmail.com","papama#1")
msg = "Hello!"
server.sendmail("siddharthsingh.ra@gmail.com","siddharth.scorpio22@gmail.com",msg)
server.quit()
