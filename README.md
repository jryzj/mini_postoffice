# mini_postoffice
ptyhon module,  easy way to send email.

## 

## example
```
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
    <img src = 'cid:{mmail_0}'>
    <img src = 'cid:{mmail_1}'>
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

