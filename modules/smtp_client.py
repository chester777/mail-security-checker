import threading
import smtplib

class SMTPClient(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
