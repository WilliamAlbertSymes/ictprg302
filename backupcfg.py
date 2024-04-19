jobs ={'job17': ['/home/ec2-user/environment/ictprg302/file1.dat'],
       'job18': ['/home/ec2-user/environment/ictprg302/dict.dat'],
       'job19': ['/home/ec2-user/environment/ictprg302/file1.dat','/home/ec2-user/environment/ictprg302/file2.dat','/home/ec2-user/environment/ictprg302/file3.dat']}
       
destPath = '/home/ec2-user/environment/ictprg302/backups'  

 # SMTP settings
smtp = {"sender": "symeswilliam7@gmail.com", # elasticemail.com verified sender
"recipient": "09135451@students.sunitafe.edu.au", # elasticemail.com verified recipient
"server": "smtp.elasticemail.com", # elasticemail.com SMTP server
"port": 2525, # elasticemail.com SMTP port
"user": "symeswilliam7@gmail.com", # elasticemail.com user
"password": ""} # elasticemail.com password

logPath = '/home/ec2-user/environment/ictprg302/backups.log'