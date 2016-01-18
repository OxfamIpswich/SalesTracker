import smtplib
from smtplib import SMTPException
from Config import read_config
from Log import Log




def SendMail(sender = None , to = None, cc = None, subject = None, body = '' ):
    """
    Sends Emails loads login and server information from config.ini.
    Args:
        sender:
        to:
        cc:
        subject:
        body:

    Returns:
    Exceptions:
    SMTPException

    """
    emailinfo = read_config(section='Email_Login')
    emailserver = read_config(section='Email_Server')

    try:
        Log.info(('EMAIL:', 'Attempting to connect to email server'))
        session = smtplib.SMTP(**emailserver)
        session.ehlo()
        session.starttls()
        session.login(**emailinfo)
        Log.info(('EMAIL:', 'Successfully connected to email server'))

        Log.info(('EMAIL:', 'Trying to send an email'))
        headers = "\r\n".join(["from: " + sender,
                       "subject: " + subject,
                       "to: " + to,
                       "mime-version: 1.0",
                       "content-type: text/html"])
        content = headers + "\r\n\r\n" + body
        session.sendmail(sender, to, content)
        Log.info(('EMAIL:', 'Successfully sent email'))
    except SMTPException as e:
        Log.error(('EMAIL:', e))
        Log.info('EMAIL:PARAMS:',sender, to, content)
        Log.info('EMAIL:', 'Failed to send email')












