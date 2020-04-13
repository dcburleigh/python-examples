
"""Send email via standard module smtplib

https://docs.python.org/3.5/library/smtplib.html

usage:

from common import mailer

f = 'email.ini'
mailer.init_config(f)

mailer.send_simple("This is a test.",  address='test@example.com' )


"""
from configparser import ConfigParser
#from email.message import EmailMessage

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


config = None
config_file = 'email.ini'
smtp_port = 0

def init_config(f_in=None):
    global config_file, config, smtp_port

    if f_in:
        config_file = f_in

    config = ConfigParser()
    config.read(config_file)
    if 'port' in config['email']:
        smtp_port = config['email']['port']
    print('host: {}'.format( config['email']['smtp_host'] ))


def send0(text, subject="Testing", address=None):
    """Send email, choose best method"""

    if 'use_ssl' in config['email'] and config['email']['use_ssl']:
        send_ssl(text, subject, address)
    elif 'username' in config['email']:
        send_tls(text, subject, address)
    else:
        send_simple(text, subject, address)


def send1(text, subject="Testing", address=None):
    """Send email, trap all known exceptions """

    msg = get_message(text, subject, address)

    print("send from {} to {}".format(msg['From'], msg['To']))
    try:
        with smtplib.SMTP(  config['email']['smtp_host'], smtp_port ) as s:
            s.send_message(msg)
        return True
    except smtplib.SMTPRecipientsRefused:
        #logger.critical('[EMAIL] Email delivery rejected.')
        return False
    except smtplib.SMTPAuthenticationError:
        #logger.critical('[EMAIL] SMTP authentication error.')
        return False
    except smtplib.SMTPSenderRefused:
        #logger.critical('[EMAIL] SMTP sender refused.')
        return False
    except smtplib.SMTPException as error:
        #logger.critical(error)
        return False

    return True

def send_tls(text, subject="Testing", address=None):
    """ Send encrypted via TLS

SMTPHeloError
    The server didn’t reply properly to the HELO greeting.
SMTPNotSupportedError
    The server does not support the STARTTLS extension.
RuntimeError
    SSL/TLS support is not available to your Python interpreter.
    """

    msg = get_message( text, subject, address)

    with smtplib.SMTP(  config['email']['smtp_host'], smtp_port ) as s:
        try:
            s.set_debuglevel(2)
            # keyfile, certfile, context
            s.starttls()
            s.ehlo()
            if 'username' in config['email']:
                print("login '{}' '{}' ".format( config['email']['username'], config['email']['password']) )
                s.login(user=config['email']['username'], password=config['email']['password'])

            s.send_message(msg)
        except SMTPRecipientsRefused as err:
            print("ERROR: send failed {}".format(err))

def send_simple(text, subject="Testing", address=None):
    msg = get_message( text, subject, address)

    with smtplib.SMTP(  config['email']['smtp_host'], smtp_port ) as s:
        try:
            s.set_debuglevel(2)
            if 'username' in config['email']:
                # probably won't work, requires TLS?
                print("login {}".format( config['email']['username']) )
                s.login(user=config['email']['username'], password=config['email']['password'])

            s.send_message(msg)
        except SMTPRecipientsRefused as err:
            print("ERROR: send failed {}".format(err))


def send_ssl(text, subject="Testing", address=None):
    msg = get_message(text, subject, address)

    print("message={}".format(msg) )
    try:
        server = smtplib.SMTP_SSL(host=config['email']['smtp_host'])
        server.set_debuglevel(True)
        server.ehlo()
        server.login(user=config['email']['username'], password=config['email']['password'])
        server.send_message(msg)
        return True
    except smtplib.SMTPRecipientsRefused:
        #logger.critical('[EMAIL] Email delivery rejected.')
        return False
    except smtplib.SMTPAuthenticationError:
        #logger.critical('[EMAIL] SMTP authentication error.')
        return False
    except smtplib.SMTPSenderRefused:
        #logger.critical('[EMAIL] SMTP sender refused.')
        return False
    except smtplib.SMTPException as error:
        #logger.critical(error)
        return False

def get_message(text, subject="Testing", address=None):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] =  config['email']['return_email']
    #msg['To'] = config['email']['admin_email']
    if address:
        msg['To'] = address
    elif 'test_email' in config['email']:
        msg['To'] = config['email']['test_email']
    else:
        msg['To'] = config['email']['admin_email']

    if 'signature' in config['email']:
        text += "\n" + config['email']['signature']

    part = MIMEText(text, 'plain')

    msg.attach(part)
    print("len={} send from {} to {} via {}".format(len(text), msg['From'], msg['To'],  config['email']['smtp_host'] ))
    return msg
