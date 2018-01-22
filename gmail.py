import time
import imaplib
import smtplib
import email
import secrets

class Gmail:

    smtp_server = "smtp.gmail.com" #ssl port 465
    imap_server = "imap.gmail.com" #port 993
    smtp_active = False

    def __init__(self, user, pwd):
        self.address = user
        self.server = None
        self.__login(pwd)

    def __del__(self):
        self.__logout()

    def __login(self, pwd):
        try:
            self.server = smtplib.SMTP_SSL(self.smtp_server, 465)
            self.server.login(self.address, pwd)
            self.smtp_active = True
        except Exception as e:
            print "Couldn't login!"
            print e.message

    def __logout(self):
        self.server.close()
        self.smtp_active = False

    def send_email(self, to, subject, body):
        to = to if type(to) is list else [to] #send to list or single person
        message = """From: %s\nTo: %s\nSubject: %s\n\n%s""" % (self.address, ", ".join(to), subject, body)
        try:
            self.server.sendmail(self.address, to, message)
        except Exception as e:
            print "Couldn't send mail"
            print e.message

    def read_email_from_gmail(self, pwd):
        try:
            mail = imaplib.IMAP4_SSL(self.imap_server)  # port 993
            mail.login(self.address, pwd)
            mail.select('Bandcamp')
            # mail.create('godlike')
            print mail.list()
            typ, data = mail.search(None, '(SUBJECT "new alhambra")')
            mail_ids = data[0].split()
            print mail_ids

            # id_list = mail_ids.split()
            # first_email_id = int(id_list[0])
            # latest_email_id = int(id_list[-1])

            for i in xrange(3, 0, -1):
                typ, data = mail.fetch(i, '(RFC822)')
                print typ

                for response_part in data:
                    if isinstance(response_part, tuple):
                        msg = email.message_from_string(response_part[1])
                        email_subject = msg['subject']
                        email_from = msg['from']
                        print 'From : ' + email_from + '\n'
                        print 'Subject : ' + email_subject + '\n'
                        if msg.is_multipart():
                            for payload in msg.walk():
                                # if payload.is_multipart(): ...
                                print payload.get_content_type()
                                if payload.get_content_type() == 'text/plain':
                                    print payload.get_payload(decode=True)
                        else:
                            print msg.get_payload(decode=True)
                    else:
                        print 'wow'

        except Exception, e:
            print str(e)


if __name__ == '__main__':
    m = Gmail(secrets.gmail_user, secrets.gmail_pass)
    m.send_email("djdcann@gmail.com", "What's good guy", "I love you son")