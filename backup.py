#!/usr/bin/python3

"""
Author: William Albert Symes
Email: wasymes@hotmail.com 
Program: Backup log
Version: 1.1
"""
import sys
import os
import pathlib
import shutil
from datetime import datetime
from backupcfg import jobs, destPath

def main():
    dateTimeStamp = datetime.now().strftime("%Y%m%d-%H%M%S")# Makes a date time stamp
    argCount = len(sys.argv)
    if argCount != 2:# If not equal to 2
        print("ERROR: Job name is missing from command line")
    else:
        jobname = sys.argv[1]
        if jobname not in jobs:
            print("ERROR: jobname is not in jobs")
        else:
            srcPath = jobs[jobname]
            if not os.path.exists(srcPath):
                print("Error: Source path file does not exist.")
            else:
                if not os.path.exists(destPath):
                    print('Error destination path {destPath} does not exists')
                else:
                    
                    srcDetails = pathlib.PurePath(srcPath)
                    
                    dstLoc = destPath + "/" + srcDetails.name + "-" + dateTimeStamp
                    
                    if pathlib.Path(srcPath).is_dir():
                        shutil.copytree(srcPath, dstLoc)
                    else:
                        shutil.copy2(srcPath, dstLoc)
            pass
    

if __name__ == '__main__':
    main()
