#!/usr/bin/python3

"""
Author: William Albert Symes
Email: symeswilliam7@gmail.com
Program: Backup log
Version: 1.1
Copyright: All rights Reserved. William Albert Symes
"""
import sys
import os
import pathlib
import shutil
import smtplib
from datetime import datetime
from backupcfg import jobs, destPath, logPath, smtp

def Logging(message, dateTimeStamp):# creates log message with date time stamp
    try:
        file = open(logPath, "a")
        file.write(f"{message} {dateTimeStamp}\n")
        file.close()
    except FileNotFoundError:
        print("ERROR: File does not exist")
    except IOError:
        print("ERROR: File is not accesible")
        
def sendEmail(message, dateTimeStamp): 
    
    # create email message 
    email = 'To: ' + smtp["recipient"] + '\n' + 'From: ' + smtp["sender"] +'\n' + 'Subject: Backup Error\n\n' + message + '\n' 
    # connect to email server and send email
    try:
        smtp_server = smtplib.SMTP(smtp["server"], smtp["port"])# looking for server and port
        smtp_server.ehlo()
        smtp_server.starttls()
        smtp_server.ehlo()
        smtp_server.login(smtp["user"], smtp["password"])# signing in with the user and password
        smtp_server.sendmail(smtp["sender"], smtp["recipient"], email)# distingushing between the sender and recipient email
        smtp_server.close()
    except Exception as e:
        print("ERROR: Send email failed: " + str(e), file=sys.stderr)# displays ERROR on screen in sending email.
        
def error(errorMessage, dateTimeStamp):
    print(errorMessage)
    Logging(f"FAILURE {errorMessage} ", dateTimeStamp)#write failure to log file
    sendEmail(errorMessage , dateTimeStamp)#email message to admin
    


def main():

    dateTimeStamp = datetime.now().strftime("%Y%m%d-%H%M%S")# Makes a date time stamp
    argCount = len(sys.argv)
    if argCount != 2:# If not equal to 2 and testing job name is specified
        error("ERROR: Job name is missing from command line", dateTimeStamp)
    else:
        jobname = sys.argv[1]
        if jobname not in jobs:# testing if job name is vailed
            error("ERROR: jobname is not in jobs", dateTimeStamp)
        else:
            for srcPath in jobs[jobname]:
                if not os.path.exists(srcPath):# testing the path to source
                    error("ERROR: Source path file does not exist.", dateTimeStamp)
                else:
                    if not os.path.exists(destPath):# testing pasth to destination
                        error("ERROR: Destination path {destPath} does not exists", dateTimeStamp)
                    else:
                        
                        srcDetails = pathlib.PurePath(srcPath)
                        
                        dstLoc = destPath + "/" + srcDetails.name + "-" + dateTimeStamp
                        
                        if pathlib.Path(srcPath).is_dir():#copying directory
                            shutil.copytree(srcPath, dstLoc)
                        else:
                            shutil.copy2(srcPath, dstLoc)#copies the file
                        Logging(f"SUCCESS copied {srcPath} to {dstLoc}", dateTimeStamp)# path success message displayed in backups.log

    

if __name__ == '__main__':
    main()
