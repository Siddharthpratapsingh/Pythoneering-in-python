
import imaplib

imap_host = 'imap.gmail.com'
imap_user = 'siddharth1998.ra@gmail.com'
imap_pass = 'papama#1'

## connect to host using SSL
imap = imaplib.IMAP4_SSL(imap_host)

## login to server
imap.login(imap_user, imap_pass)

## get status for the mailbox (folder) INBOX
status, response = imap.status('INBOX', "(UNSEEN)")

print status

unreadcount = int(response[0].split()[2].strip(').,]'))
print unreadcount
