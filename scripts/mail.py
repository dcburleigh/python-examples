
from utils import mailer
import sys

me = None

def test1():
    text = '''This is a test of the SMTP server.
This is another line.
End of message.'''
    mailer.send_simple(text, address=me)
    #mailer.send1(text, address=me)

def test2():
    text = '''This is a test of the SMTP server supporting TLS.
This is another line.
End of message.'''
    mailer.send_tls(text, address=me)

def test3():
    text = '''This is a test of the SMTP server.
This is another line.
End of message.'''
    mailer.send0(text, address=me)
    #mailer.send1(text, address=me)

def main():
    global me

    if len(sys.argv) > 1:
        me = sys.argv[1]

    mailer.init_config()
    #test1()
    #test2()
    test3()

if __name__ == "__main__":
    status = main()
    sys.exit(status)
