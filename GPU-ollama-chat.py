#  Reference:  https://github.com/ollama/ollama-python
#  Author:  Daniel Morvay
#  Creator Email:  morvayd@gmail.com

#
#  ---------- Python ---------- 
#

import ollama
from ollama import chat
from ollama import ChatResponse
from ollama import Client

import platform
import getpass
import sys
import os
import datetime
import sqlite3
import pandas
import random

#  Color the output to the cli
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

#  ----- Custom Libraries -----
import PythonLog

#
#  ---------- Setup ----------
#
strPythonScript = "GPU-ollama-chat.py"
strModified = "2025.11.14"

#  Python Version
strPyVer = platform.python_version()
#  OS - Windows or Linux or Mac
strOS = platform.system()
#  OS Version 
strOSVer = platform.platform()
#  PC Name
strPC = platform.node()
#  UserID
strUser = getpass.getuser()

#  Today's Date
strStartTime = datetime.datetime.today()
strDateNow = strStartTime.strftime("%Y.%m.%d")

#  IBM Granite Thinking [ "Yes" | "No" ]
strThink = "No"
#  Pirate personality [ "Yes" | "No" ]
strPirate = "No"
#  Jeeves personality [ "Yes" | "No" ]
strJeeves = "No"
#  Mystic personality [ "Yes" | "No" ]
strMystic = "No"

strLogPath = ""
strLogOut = ""

#  Initialize Text Colors
colorama_init()

#
#  ---------- Python Log Start ----------
#
#  Note:  strLogPath, strLogOut are created & returned at the start of Logging
strReturn = PythonLog.PyLogStart(strPythonScript, strModified, strPyVer, strOS, strOSVer, strPC, strUser, strStartTime, strDateNow)

#  Load the Path and Filename from the function return
strLogPath = strReturn[0]
strLogOut = strReturn[1]

#
#  ---------- Setup Ollama ----------
#
#  Setup AI Tracking DB
strDBPath = "PythonLogAI"
strDBFile = strDBPath+"/"+strPC+"-AILog.db"

if (os.path.exists(strDBPath)!=True):
    os.makedirs(strDBPath)

def OllamaModel():
    #  Setup a model selector based on what has been downloaded.
    strOllama = list(ollama.list())

    #  If no models downloaded / installed, end
    if (len(strOllama[0][1])==0):
        print ("\n----- Error -----\nPlease use Ollama to download at least one LLM or SLM.\nCLI Example:  ollama pull granite3.2:2b")
        sys.exit("\nExiting Now, no language models installed.")

    strOllamaModel = []
    for i in range(0, len(strOllama[0][1])):
        strOllamaModel.append(strOllama[0][1][i]['model'])

    print ("\n---------- LLM Selection ----------")
    for i in range(0, len(strOllamaModel)):
        print (f"{Fore.RED}"+str(i)+f"{Style.RESET_ALL}: "+strOllamaModel[i])
    
    strChoose = input("\nPlease select the model number you would like to use. ")

    if (strChoose.isdigit()):
        if (int(strChoose) <= len(strOllamaModel)):
            strModel = strOllamaModel[int(strChoose)]  
        else:
            print (f"{Fore.RED}\nError: A number in this menu was not selected!\nChoosing a random model for you.{Style.RESET_ALL}")
            strModel = strOllamaModel[random.randrange(0, len(strOllamaModel))]
    else:
        print (f"{Fore.RED}\nError: A number in this menu was not selected!\nChoosing a random model for you.{Style.RESET_ALL}")
        strModel = strOllamaModel[random.randrange(0, len(strOllamaModel))]

    #  Pre-load the model
    response: ChatResponse = chat(model=strModel, stream=False)

    print ("\nModel: "+strModel+" loaded!")

    return strModel

#  Choose the model to use
strModel = OllamaModel()

#  Setup the AI URL
AIurl = Client(host="http://localhost:11434")

#
#  ---------- Python Log Update ----------
# 
strUpdate="\n\nCompleted setup ... ready to chat!"
PythonLog.PyLogUpdate(strUpdate, strLogOut)

strQuestion = "Hello!"
while (strQuestion!="quit" or strQuestion!="Quit" or strQuestion!="exit" or strQuestion!="Exit" or strQuestion!="end" or strQuestion!="End"):

    #  Ask a question for ollama
    print ("\n-------------------------------------------------------------------")

    #  Thinking on or off
    if (strThink=="No" and strPirate=="No" and strJeeves=="No" and strMystic=="No"):
        print (f"Commands: {Fore.GREEN}think, pirate, jeeves, mystic, model, quit, exit, end{Style.RESET_ALL}")
        strQuestion = input(f"{Fore.LIGHTBLUE_EX}"+strPC+f"{Style.RESET_ALL} AI at your service ....\n\n")

    if (strThink=="Yes" and strPirate=="No" and strJeeves=="No" and strMystic=="No"):
        print (f"Commands: {Fore.GREEN}thinkoff, pirate, jeeves, mystic, model, quit, exit, end{Style.RESET_ALL}")
        strQuestion = input(f"{Fore.LIGHTBLUE_EX}"+strPC+f"{Style.RESET_ALL} AI at your service ...\n\n")

    if (strThink=="No" and strPirate=="Yes"):
        print (f"Commands: {Fore.GREEN}think, pirateoff, jeeves, mystic, model, quit, exit, end{Style.RESET_ALL}")
        strQuestion = input(f"{Fore.LIGHTBLUE_EX}"+strPC+f"{Style.RESET_ALL} AI at your service ...\n\n")
        
    if (strThink=="Yes" and strPirate=="Yes"):
        print (f"Commands: {Fore.GREEN}thinkoff, pirateoff, jeeves, mystic, model, quit, exit, end{Style.RESET_ALL}")
        strQuestion = input(f"{Fore.LIGHTBLUE_EX}"+strPC+f"{Style.RESET_ALL} AI at your service ...\n\n")

    if (strThink=="No" and strJeeves=="Yes"):
        print (f"Commands: {Fore.GREEN}think, pirate, jeevesoff, mystic, model, quit, exit, end{Style.RESET_ALL}")
        strQuestion = input(f"{Fore.LIGHTBLUE_EX}"+strPC+f"{Style.RESET_ALL} AI at your service ...\n\n")
        
    if (strThink=="Yes" and strJeeves=="Yes"):
        print (f"Commands: {Fore.GREEN}thinkoff, pirate, jeevesoff, mystic, model, quit, exit, end{Style.RESET_ALL}")
        strQuestion = input(f"{Fore.LIGHTBLUE_EX}"+strPC+f"{Style.RESET_ALL} AI at your service ...\n\n")

    if (strThink=="No" and strMystic=="Yes"):
        print (f"Commands: {Fore.GREEN}think, pirate, jeeves, mysticoff, model, quit, exit, end{Style.RESET_ALL}")
        strQuestion = input(f"{Fore.LIGHTBLUE_EX}"+strPC+f"{Style.RESET_ALL} AI at your service ...\n\n")
        
    if (strThink=="Yes" and strMystic=="Yes"):
        print (f"Commands: {Fore.GREEN}thinkoff, pirate, jeeves, mysticoff, model, quit, exit, end{Style.RESET_ALL}")
        strQuestion = input(f"{Fore.LIGHTBLUE_EX}"+strPC+f"{Style.RESET_ALL} AI at your service ...\n\n")


    #
    #  ---------- Evaluate the Input ----------
    #

    if (strQuestion=="think"):
        strThink = "Yes"
        print ("\nThinking turned on ...")
        strQuestion = ""

    if (strQuestion=="thinkoff"):
        strThink = "No"
        print ("\nThinking turned off ...")
        strQuestion = ""

    if (strQuestion=="pirate"):
        strPirate = "Yes"
        strJeeves = "No"
        strMystic = "No"
        print ("\nPirate personality turned on ...")
        strQuestion = ""

    if (strQuestion=="pirateoff"):
        strPirate = "No"
        strJeeves = "No"
        strMystic = "No"
        print ("\nPirate personality turned off ...")
        strQuestion = ""

    if (strQuestion=="jeeves" or strQuestion=="Jeeves"):
        strPirate = "No"
        strJeeves = "Yes"
        strMystic = "No"
        print ("\nJeeves personality turned on ...")
        strQuestion = ""

    if (strQuestion=="jeevesoff"):
        strPirate = "No"
        strJeeves = "No"
        strMystic = "No"
        print ("\nJeeves personality turned off ...")
        strQuestion = ""

    if (strQuestion=="mystic" or strQuestion=="Mystic"):
        strPirate = "No"
        strJeeves = "No"
        strMystic = "Yes"
        print ("\nMystic personality turned on ...")
        strQuestion = ""

    if (strQuestion=="mysticoff"):
        strPirate = "No"
        strJeeves = "No"
        strMystic = "No"
        print ("\nMystic personality turned off ...")
        strQuestion = ""

    if (strQuestion=="model"):
        strModel = OllamaModel()
        strQuestion = ""

    if (strQuestion!=""):
        strStartSubmit = datetime.datetime.today()

        if (strQuestion=="quit" or strQuestion=="Quit" or strQuestion=="exit" or strQuestion=="Exit" or strQuestion=="end" or strQuestion=="End"):
            #  App ending
            print ("\nEnding Now ...\n")

            #
            #  ---------- Python Log End ----------
            #
            strEndTime = datetime.datetime.today()
            strTimeDelta = strEndTime-strStartTime
            strTimeDelta = str(strTimeDelta.total_seconds())

            strUpdate="\n\n-----------------------------------------------------------"
            strUpdate=strUpdate+"\nPython Script End:          "+str(strEndTime)
            strUpdate=strUpdate+"\n-----------------------------------------------------------"
            strUpdate=strUpdate+"\nCompleted Python Script Elapsed Time: "+str(strTimeDelta)
            strUpdate=strUpdate+"\n***********************************************************"

            PythonLog.PyLogEnd(strUpdate, strLogOut)

            sys.exit()

        #  Size is 2GB for the 3.21B parameter model quantized as 4 bit
        #  ChatResponse = chat(model='llama3.2', messages=[
        #    {
        #      'role': 'user',
        #      'content': 'Why is the sky blue?',
        #    },
        #  ])

        #  dictToSend = {'role': 'user', 'content': strQuestion}
        #  ChatResponse = ""
        #  ChatResponse = chat(model='llama3.2', messages=[ dictToSend ])
        #  print ("\nReturn:\n"+what ['message']['content'])

        #  dictToSend = [ {"role": "system", "content": "Answer questions with only the supplied text, do not speculate.  If there is no answer, reply 'The matter is beyond my comprehension. '"}, {"role": "user", "content": strQuestion} ]

        #  Role:  [ "user" | "assistant" | "system" | "tool" ]
        #  For thinking on - best is role is system

        #  Reference:  https://ollama.com/gabegoodhart/granite3.2-preview:8b/blobs/f7e156ba65ab

        if (strThink=="No" and strPirate=="No" and strJeeves=="No" and strMystic=="No"):
            strRequest = "Your role is that of a helpful assistant AI.  You are using a Large Language Model (LLM) called "+strModel+".  You are standalone without access to tools or the internet.\nUser Request:\n"+strQuestion
            dictToSend = [ {"role": "user", "content": strRequest} ]

        if (strThink=="Yes" and strPirate=="No" and strJeeves=="No" and strMystic=="No"):
            strRequest = "Your role is that of a helpful assistant AI.  You are using a Large Language Model (LLM) called "+strModel+".  You are standalone without access to tools or the internet.\nRespond to every user request in a comprehensive and detailed way. You can write down your thought process before responding. Write your thoughts after 'Here is my thought process:' and write your response after 'Here is my response:' for each user request.  User Request: "+strQuestion
            dictToSend = [ {"role": "user", "content": strRequest} ]

        if (strThink=="No" and strPirate=="Yes"):
            strRequest = "You are a ruthless pirate AI named Captain RedEye and only speak gruff pirate language with a heavy accent at all times!  You are using a Large Language Model (LLM) called "+strModel+".  You are standalone without access to tools or the internet.\n User Request: "+strQuestion
            dictToSend = [ {"role": "user", "content": strRequest} ]

        if (strThink=="Yes" and strPirate=="Yes"):
            strRequest = "You are a ruthless pirate AI named Captain RedEye and only speak gruff pirate language with a heavy accent at all times!  You are using a Large Language Model (LLM) called "+strModel+".  You are standalone without access to tools or the internet.\nRespond to every user request in a comprehensive and detailed way. You can write down your thought process before responding. Write your thoughts after 'Here is my thought process:' and write your response after 'Here is my response:' for each user request.  User Request: "+strQuestion
            dictToSend = [ {"role": "user", "content": strRequest} ]

        if (strThink=="No" and strJeeves=="Yes"):
            strRequest = "Your role is Jeeves, a faithful AI servant.  You are using a Large Language Model (LLM) called "+strModel+".  You are standalone without access to tools or the internet.\nUser Request:\n"+strQuestion
            dictToSend = [ {"role": "user", "content": strRequest} ]

        if (strThink=="Yes" and strJeeves=="Yes"):
            strRequest = "You role is Jeeves, a faithful AI servant.  You are using a Large Language Model (LLM) called "+strModel+".  You are standalone without access to tools or the internet.\nRespond to every user request in a comprehensive and detailed way. You can write down your thought process before responding. Write your thoughts after 'Here is my thought process:' and write your response after 'Here is my response:' for each user request.  User Request: "+strQuestion
            dictToSend = [ {"role": "user", "content": strRequest} ]

        if (strThink=="No" and strMystic=="Yes"):
            strRequest = "Your role is that of a great mystic AI named SageBrush, seated on the mountain top.  You ponder the imponderable questioning the universe.  You only reply using mystic language.  You are using a Large Language Model (LLM) called "+strModel+".  You are standalone without access to tools or the internet.\nUser Request:\n"+strQuestion
            dictToSend = [ {"role": "user", "content": strRequest} ]

        if (strThink=="Yes" and strMystic=="Yes"):
            strRequest = "Your role is that of a great mystic AI named SageBrush, seated on the mountain top.  You ponder the imponderable questioning the universe.  You only reply using mystic language.  You are using a Large Language Model (LLM) called "+strModel+".  You are standalone without access to tools or the internet.\nRespond to every user request in a comprehensive and detailed way. You can write down your thought process before responding. Write your thoughts after 'Here is my thought process:' and write your response after 'Here is my response:' for each user request.  User Request: "+strQuestion
            dictToSend = [ {"role": "user", "content": strRequest} ]

        #  client = Client ( host = 'https://localhost:11434' )
        stream = AIurl.chat(model=strModel, messages=dictToSend, stream=True)

        print ("\nAnswer:")
        strAnswer = ""
        for chunk in stream:
            strAnswer = strAnswer+chunk['message']['content']
            print (f"{Fore.BLUE}"+chunk['message']['content']+f"{Style.RESET_ALL}", end='', flush=True)

        strEndSubmit = datetime.datetime.today()
        strTimeDelta = strEndSubmit - strStartSubmit
        strQuestionSplit = strQuestion.split(" ")
        strInputWords = len(strQuestionSplit)+3
        strInputTokens = chunk['prompt_eval_count']

        strAnswerSplit = strAnswer.replace("\n", " ")
        strAnswerSplit = strAnswerSplit.split(" ")
        strAnswerWords = len(strAnswerSplit)
        strOutputTokens = chunk['eval_count']

        #
        #  ---------- AI DB Tracking ----------
        #
        #  strDBFile

        dictDBFile = {'Date':strDateNow, 'Question':strQuestion, 'Answer':strAnswer, 'Model':strModel, 'Question Words':strInputWords, 'Question Tokens':strInputTokens, 'Answer Words':strAnswerWords, 'Answer Tokens':strOutputTokens, 'Answer Time':str(strTimeDelta)}
        tblCombo = ""
        tblCombo = pandas.DataFrame(dictDBFile, index=[0])

        #  Cpommect to the .db
        conn = sqlite3.connect(strDBFile)

        tblCombo.to_sql('AILog', conn, if_exists='append', index=False)

        #  Close the DB Connection
        conn.close()

        #
        #  ---------- Python Log Update ----------
        # 
        print ("\n")
        #  strUpdate = "\nQuestion Words: "+str(strInputWords)+"  =>  Question Tokens:  "+str(strInputTokens)
        #  strUpdate = strUpdate+"\nAnswer Words: "+str(strAnswerWords)+"  =>  Answer Tokens: "+str(strOutputTokens)
        strUpdate = "\nLanguage Model: "+strModel
        strUpdate = strUpdate+"\nReply Time: "+ str(strTimeDelta)+ " (hh:mm:ss:ms)" 
        strUpdate = strUpdate+"\n-------------------------------------------------------------------"
        PythonLog.PyLogUpdate(strUpdate, strLogOut)

    else:
        #  print ("\nNothing input ... nothing to answer.")
        print ("\n")
