import poplib
import getpass
import pyttsx

mailServer = 'pop.googlemail.com'
emailID = 'siddharth1998.ra@gmail.com'
emailPass = 'papama#1'

#Open connection to mail server(Secured using SSL)
myEmailConnection = poplib.POP3_SSL(mailServer,'995')
#Print the response message from server
print myEmailConnection.getwelcome()
#Set email address
myEmailConnection.user(emailID)
#Set password
myEmailConnection.pass_(emailPass)
#Get information about the email address
EmailInformation = myEmailConnection.stat()
print "Number of new emails: %s (%s bytes)" % EmailInformation
#Reading an email
print "\n\n====\nRead Messages\n====\n\n"
#Reading all emails
numberofmails = EmailInformation[0]
for i in range(numberofmails):
    for email in myEmailConnection.retr(i+1)[1]:
        print email
