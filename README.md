## mini_postoffice

python module,  easy way to send email.  



### Class.MiniMail

MiniMail is class to create a mail body, is an inherit class from email.message.EmailMessage, which can be sent by smtplib of python, or the class MiniPostMan afterward.  
chardet is the only extend module, which is to recognize the encoding of file.    



#### Method

***class MiniMail(self, from_ = '', to = '', subject ='', gid = 'aipython', prefix = 'mmail')***  
Initialize instance  
***from, to, subject*** :   refer to [RFC822](https://tools.ietf.org/html/rfc822.html#section-4.5 "RFC822"), which are mini requirement for email fields  
***gid*** : as part identification for content-id in email  
***mmail*** : used in html template, as format id  



***MiniMail.add_text(self, content, encoding = 'utf-8')***  
Add plain text content in email  
***content*** : string, plain text content  
***encoding*** : string, charset of content   



***MiniMail.add_html(self, html, cids, body = None)***  
Add html to email or an instance of EmailMessage   
***html*** : string, the html content  
***cids*** : list or dictionary, resources for html, which made by make_cid_list() or make_cid_dict(), in which are objects with the keys of attachment, maintype, subtype, cid, filename, encoding.  
***body*** : can be EmailMessage, or payload of email  



***MiniMail.add_html_auto(self, html, sources, body = None)***  
Easy way to call MiniMail.add_html()  
***html*** : string, the html template, in which the refer will like mmail_0, mmail is self._prefix, 0 is the index of 			fmt list, e.g. fmt = {'mmail_0' : 'abc', 'mmail_1' : 'def'}, then after html formating, mmail_0 will be 			replaced by abc, mmail_1 will be replaced by def.  
***sources*** : list or dictionary,  path of resource files which will be referenced in html.  
***body*** : email.message, can be an instance of EmailMessage, or payload of email  



***MiniMail.get_encoding(self, b)***  
Get the content encoding, using module chardet to detect  
***b*** : byte, the content of file  
***return*** : string, name of encoding



***MiniMail.get_MEMF(self, file)***  
Get mimetype, encoding, opening mode, filename of file path  
 ***file*** : string, file path  
***return*** : tuple of string, with minetype, encoding, mode, filename



***MiniMail.get_file_encoding(self, file)***  
Get encoding of file  
 ***file*** : string, file path  
***return*** : string, name of encoding



***MiniMail.add_attachment(self, files, body = None)***  
Add files as attachment into email or an instance of EmailMessage  
***files*** : list, files to attach  
***body*** : email.message, can be an instance of EmailMessage, or payload of email  



***MiniMail.add_email(self, mail, body = None)***  
Add mail as attachment into email or an instance of EmailMessage  
***mail*** : email.message or .eml, email to attach  



***MiniMail.make_cid_list(self, files)***  
Prepare files data for other methods, data have bytes of file, maintype, subtype, cid, filename, encoding  
***files*** : list,  list of file path  
***return*** : list, of cid objects



***MiniMail.make_cid_dict(self, files)***  
Prepare files data for other methods, data have bytes of file, maintype, subtype, cid, filename, encoding  
***files*** : list,  list of file path  
***return*** : dictionary, of cid objects



***MiniMail.sorting_cids(self, cids)***  
Soring cids, to make self._embedded type at first in cids, after that other type.  
***cids*** : list,  or dictionary, data set from cid_list() or cid_dict()
***return*** : list



***MiniMail.set_property(self, property_, value)***  
General method to assign value to inner properties  
***property\_*** : string, name of property  
***value***: all kind of types  



***MiniMail.get_property(self, property_)***  
General method to get value of inner properties  
***property\_*** : string, name of property  
***return*** : value of property



***MiniMail.get_addresses(self)***  
Get all email addresses in email  
***return*** : list, of all addresses



***MiniMail.get_mail(self)***  
Get total email body  
***return*** : EmailMessage, email body



---

#### Class.MiniPostMan

MiniPostMan fulfills lite function to send email, of which inner core is stmplib, standard module of python.  


#### Method

***class MiniPostMan(self, host='', useremail='', pwd=''，debuglevel = 0)***  
Initialization of class, setting required properties  
***host*** : string, the smtp server url  
***usermail*** : string, account to login host, email address of sender is ok  
***pwd*** ： password of login  
***debuglevel*** ：set the debug output level



***MiniPostMan.email_valid(self, addresses)***  
Validate email address  
***addresses*** : list, with email addresses   
***return*** : boolean



***MiniPostMan.quick_send(self, receiver, subject='hello', content='')***  
Lite method to send a text email  
***receiver*** : string, email address of receiver  
***subject*** : string, subject of email  
***content*** : string, message  



***MiniPostMan.get_addresses(self, mail)***  
Get all addresses in mail  
***mail*** : email.message, an instance of email.messages  
***return*** : list, of all addresses



***MiniPostMan.send_mail(self, mail, method = 'smtp')***  
Send email  
***mail*** : email.message, an instance of email.messages  
***method*** : string, send method, smtp or ssl  



***MiniPostMan.set_property(self, property_, value)***  
General method to assign value to inner properties  
***property\_*** : string, name of property  
***value*** : all kind of types  



---

### Usage

1. Creating instance of email, calls MiniMail.
2. Setting fields necessarily, such as 'From', ‘To', calls MiniMail.set_property.
3. Adding contents into the email instance, calls MiniMail.add_text, MiniMail.add_html_auto, MiniMail.add_attachment, MiniMail.add_email, according to perposes.
4. Creating instance of MiniPostman.
5. Setting URL and credential of email server, calls MiniPostman.set_property.
6.  Sending mail,  calls MiniPostman.send_mail with the email content getting by calling MiniMail.get_mail.



------



### Example

```python
from mini_postoffice import MiniPostMan
from mini_postoffice import MiniMail

#create an instance of MiniPostMan
amail = MiniPostMan()
amail.set_property('host', 'smtp.gmailx.com') #smtp server
amail.set_property('user', 'aipython@gmailx.com') #account of sender for smtp server
amail.set_property('pwd', 'IqkPjWHFpz3') #password of sender for smp server

#create an instance of MiniMail
tmail = MiniMail()
tmail.set_property('from','aipython@gmailx.com')  #
# tmail.set_property('to', 'datadriver<23817@gmailx.com>,jry<jry@gmailx.com>') #if want to send to many receivers
tmail.set_property('to', 'datadriver<23817@gmailx.com>') #email of recevier
tmail.set_property('subject', 'mini postoffice') #subject of email, optional

#html template
h = '''
<html>
  <head></head>
  <body>
    <h3>mini_postoffice</h3>
    <p>a email module, coded in python.</p>
    <img src = 'cid:{mmail_1}'>
    <img src = 'cid:{mmail_0}'>
  </body>
</html>
'''

#format html template
cid_list = tmail.make_cid_list(['image.jpg', 'image1.png'])
src = []
for c in cid_list:
    src.append(c['cid'])    
h = h.format(img1 = src[0], img2 = src[1])

tmail.add_html_auto(h,[])  #add html to email
tmail.add_attachment(['image.jpg', 'excel.xlsx']) #add other attachment, optional

amail.send_mail(tmail.get_mail()) #send mail
```

Be aware for the mapping when call ***add_html_auto***.  *{mmail_**1**}* will be replaced by '*image1.png*', beacuse the index of '*image1.png*' in cid_list is **1**, *{mmail_**0**}* will be replaced by '*image.jpg*',  because the index is **0** in cid_list.



---

### Illustration of email

![illustration of Email structure](https://github.com/jryzj/mini_postoffice/blob/master/illustration%20of%20email%20structure.png?raw=true)



------

### Reference

[email](https://docs.python.org/3.6/library/email.html#module-email) — An email and MIME handling package of Python

[smtplib](https://docs.python.org/3.6/library/smtplib.html#module-smtplib) — SMTP protocol client of Python

[chardet](https://pypi.org/project/chardet/)  — chardet 3.0.4

[MIME](https://en.wikipedia.org/wiki/MIME) — from wikipedia

[RFC1521](https://tools.ietf.org/html/rfc1521) — multipart/alternative, multipart/mixed

[RFC2112](https://tools.ietf.org/html/rfc2112) — multipart/related

[RFC4021](https://tools.ietf.org/html/rfc4021#section-2.1.2) — Registration of Mail and MIME Header Fields

[RFC2045](https://tools.ietf.org/html/rfc2045), [RFC2046](https://tools.ietf.org/html/rfc2046), [RFC2047](https://tools.ietf.org/html/rfc2047), [RFC2048](https://tools.ietf.org/html/rfc2048) — Multipurpose Internet Mail Extensions, Part one to Part four

[RFC5321](https://tools.ietf.org/html/rfc5321) — Simple Mail Transfer Protocol

[RFC5322](https://tools.ietf.org/html/rfc5322.html) — Internet Message Format

[RFC2821](https://tools.ietf.org/html/rfc2821.html), [RFC6532](https://tools.ietf.org/html/rfc6532.html), [RFC6657](https://tools.ietf.org/html/rfc6657), [RFC5233](https://tools.ietf.org/html/rfc5233.html)

