from email.message import EmailMessage
import mimetypes
from email.utils import getaddresses
from email.utils import make_msgid
import chardet


class MiniMail():
    def __init__(self, from_ = '', to = '', subject ='', gid = 'aipython', prefix = 'mmail'):
        self._mail = EmailMessage()
        self._from = from_
        self._to = to
        self._subject = subject
        self._gid = gid
        self._prefix = prefix + '_'
    
    def add_text(self, content):
        self._mail.set_content(content)
        
    def add_html(self, html, cid_list = []):
        self._mail.add_alternative(html, subtype = 'html')
        if cid_list:
            body = self._mail.get_payload()
            for l in cid_list:
                print(__name__, '==', l['maintype']) 
                if l['maintype'] in ['audio', 'video', 'image']:
                    body[-1].add_related(l['attachment'], l['maintype'], l['subtype'], cid = l['cid'])
                elif l['maintype'] == 'text':
                    body[-1].add_attachment(l['attachment'], subtype = l['subtype'], charset = l['encoding'], \
                                            cid = l['cid'], filename = l['filename'] )
                else:
                    body[-1].add_attachment(l['attachment'], maintype = l['maintype'], subtype = l['subtype'], \
                                            filename = l['filename'])
    
    def add_html_auto(self, html, src_list):
        cid_list = self.make_cid_list(src_list)
        fmt = dict()
        for l in range(len(cid_list)):
            fmt[self._prefix + str(l)] = cid_list[l]['cid']
        html = html.format(**fmt)
        self.add_html(html, cid_list)        
        
    def get_encoding(self, b):
        encoding = chardet.detect(b)
        if float(encoding['confidence']) > 0.9:
            return encoding['encoding']
        else:
            return 'binary'

    def get_MEMF(self, file):
        mtype = mimetypes.guess_type(file, strict = False)[0].split('/')
        print(mtype)
        encoding = self.get_file_encoding(file)
        mode = 'r' + ('b' if encoding == 'binary' else '')
        encoding = encoding if encoding != 'binary' else None
        filename = file.split('/')[-1]
        return mtype, encoding, mode, filename

    def get_file_encoding(self, file):
        with open(file, 'rb') as f:
            encoding = self.get_encoding(f.read())
        return encoding
    
    def add_attachment(self, files):
        cid_list = self.make_cid_list(files)
        for l in cid_list:
            self._mail.add_attachment(l['attachment'], maintype = l['maintype'], subtype = l['subtype'], \
                                            filename = l['filename']) 
    def add_email(self, mail):
        self._mail.add_attachment(mail)
    
    
    def make_cid_list(self, files):
        cid_list = []
        for file in files:
            mtype, encoding, mode, filename = self.get_MEMF(file)
            with open(file, mode, encoding = encoding) as f:
                fdata = f.read()
            cid_list.append({'attachment': fdata, 'maintype' : mtype[0], 'subtype' : mtype[1], \
                             'cid': make_msgid(domain = self._gid)[1:-1], 'filename' : filename, 'encoding' : encoding})
        return cid_list
    
    
    def set_property(self, property_, value):
        property_ = '_' + property_
        self.__dict__[property_] = value
        
    def get_property(self, property_):
        return self.__dict__['_' + property_]
    
    def get_addresses(self):
        tos = self._mail.get_all('to', [])
        ccs = self._mail.get_all('cc', [])
        resent_tos = self._mail.get_all('resent-to', [])
        resent_ccs = self._mail.get_all('resent-cc', [])
        addresses = []
        for t in getaddresses(tos + ccs + resent_tos + resent_ccs):
            addresses.append(t[1])
        return addresses        
    
    def get_mail(self):
        self._mail['From'] = self._from
        self._mail['To'] = self._to
        self._mail['Subject'] = self._subject
        return self._mail
    

    
######################################################
import smtplib
import re

class MiniPostMan:
## plain/html, smtp/ssl, text/multipart, one/list
    def __init__(self, host='', useremail='', pwd=''):
        self._host = host
        self._user = useremail
        self._pwd = pwd
    
    def email_valid(self, addresses):
        patten = pattern = r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$'
        if isinstance(addresses,list):
            for addr in addresses:
                if not re.search(patten, addr):
                    print('email error')
                    return False
        else:
            if not re.search(patten, addresses):
                print('email error')
                return False
        return True
    
    def quick_send(self, receiver, subject='hello', content=''):
        if self.email_valid(receiver):
            msg = EmailMessage()
            msg['Subject'] = subject
            msg['From'] = f'{self._user}<{self._user}>'
            msg['To'] = receiver
            
            try:
                smtpObj = smtplib.SMTP(self._host)
                smtpObj.set_debuglevel(1)
                smtpObj.login(self._user, self._pwd)
                smtpObj.sendmail(self._user, receiver, msg.as_string())                
                print('sent email')
                smtpObj.quit()
            except smtplib.SMTPException as err:
                print('failed:', err)       
    
    def get_addresses(self, mail):
        tos = mail.get_all('to', [])
        ccs = mail.get_all('cc', [])
        resent_tos = mail.get_all('resent-to', [])
        resent_ccs = mail.get_all('resent-cc', [])
        addresses = []
        for t in getaddresses(tos + ccs + resent_tos + resent_ccs):
            addresses.append(t[1])
        return addresses   
    
    def send_mail(self, mail, method = 'smtp'):
        if self.email_valid(self.get_addresses(mail)):
            if method == 'smtp':
                try:
                    smtpObj = smtplib.SMTP(self._host)
                    smtpObj.set_debuglevel(1)
                    smtpObj.login(self._user, self._pwd)
                    smtpObj.send_message(mail)
                    smtpObj.quit()                    
                except smtplib.SMTPException as err:
                    print('failed', err)
        
    
    def set_property(self, property,value):
        property = '_' + property
        print(property)
        self.__dict__[property] = value