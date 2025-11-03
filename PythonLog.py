print ("\nCustom Library Loaded - PythonLog")

#  strPythonScript = "PythonLog.py"
#  strModified = "2025.11.03"
#  Author:  Daniel Morvay
#  Email:   mwwdata@outlook.com

#  Description:  
#  Logging Function - Require the main script to push all variables needed.
#  Adjusted variables to prevent confusion with existing variable in the calling
#  code.  

#  Comments:  
#  Commented strModified - don't want it confused with the calling .py files.

#  Called through the following methods:
'''
import PythonLog 

#
#  ---------- Python Log Start ----------
#
#  Note:  strLogPath, strLogOut are created & returned at the start of Logging
strReturn = PythonLog.PyLogStart(strPythonScript, strModified, strPyVer, strOS, strOSVer, strPC, strUser, strStartTime, strDateNow)

#
#  ---------- Python Log Update ----------
#
strUpdate = "==> Loaded text"
strUpdate = strUpdate+"\nUpdate Line 1: "
strUpdate = strUpdate+"\nUpdate Line 2: "
PythonLog.PyLogUpdate(strUpdate, strLogOut)

'''

#
#  ---------- Libraries to Load ----------
#

#  Note:  All libraries called within these functions must be loaded here.
import os

#
#  ---------- Function Definition ----------
#

def PyLogStart(strPythonScript, strModified, strPyVer, strOS, strOSVer, strPC, strUser, strStartTime, strDateNow):

    #
    #  ---------- Python Log Start ----------
    #
    strLogPath = "PythonLogs"

    strLogOut = strLogPath+"/"+strDateNow+"-"+strPC+"-PythonLog.txt"

    #  Create the initial folder if it doesn't exist.
    if os.path.isdir(strLogPath)==False:
        os.mkdir(strLogPath)

    #  Create an initial log file if it doesn't exist.
    if os.path.isfile(strLogOut)==False:
        fileOutLog = open(strLogOut, "w");
        fileOutLog.close()

    #
    #  ---------- Python Log Update ----------
    #
    strUpdate="\n***********************************************************"
    strUpdate=strUpdate+"\n-----------------------------------------------------------"
    sstrUpdate=strUpdate+"\nPython Script Name:          "+strPythonScript
    strUpdate=strUpdate+"\nPython Script Last Modified: "+strModified
    strUpdate=strUpdate+"\nPython Version:              Python "+strPyVer
    strUpdate=strUpdate+"\nOS Version:                  "+strOSVer
    strUpdate=strUpdate+"\nPython Script Start:         "+str(strStartTime)
    strUpdate=strUpdate+"\nPC Name:                     "+strPC
    strUpdate=strUpdate+"\nUser Name:                   "+strUser
    strUpdate=strUpdate+"\n-----------------------------------------------------------"
    strUpdate=strUpdate+"\n\n---------- "+strPythonScript+" Started ----------"

    print(strUpdate)
    fileOutLog = open(strLogOut, "a");
    strTemp = fileOutLog.write(strUpdate)
    strTemp = fileOutLog.close()

    return strLogPath, strLogOut

def PyLogUpdate(strUpdate, strLogOut):

    #
    #  ---------- Python Log Update ----------
    #

    print(strUpdate)
    fileOutLog = open(strLogOut, "a");
    strTemp = fileOutLog.write(strUpdate)
    strTemp = fileOutLog.close()

def PyLogEnd(strUpdate, strLogOut):
    
    #
    #  ---------- Python Log Update ----------
    #

    print(strUpdate)
    fileOutLog = open(strLogOut, "a");
    strTemp = fileOutLog.write(strUpdate)
    strTemp = fileOutLog.close()
