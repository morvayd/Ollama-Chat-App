#  Reference:  https://github.com/ollama/ollama-python
#  Author:  Daniel Morvay
#  Creator Email:  morvayd@gmail.com

#
#  ---------- CLI Install ----------
#

#  python3.11

#
#  ---------- Cuda Install ----------
#
#  Download cuda installer - Windows or Linux
#  firefox https://developer.nvidia.com/cuda-downloads
#  Check the cuda version
#  nvcc --version
#  nvidia-smi => windows: powershell => nvidia-smi

#  Mac - No need on Apple Silicon

#
#  ---------- Ollama Install ----------
#

#  CPU or GPU Based ollama - Adjusts based on availability

#  pip install ollama
#  Download & Install Ollama - https://ollama.com/download

#  Run ollama
#  ollama pull llama3.2
#  ollama run llama3.2
#  From within ollama
#  /show info
#  Model info appears
#  Exit ollama server
#  /exit

#  Open new CLI
#  nvidia-smi 
#  Verify ollama is using the GPU

#  Open new CLI
#  Python
#  ---- or ----
#  python Llama3.2.py

#  Ollama Model Win11 Location:  C:\Users\<UserID>\.ollama

#  List the modelfile
#  ollama show llama2:latest --modelfile
#  ollama show granite3.2:2b --modelfile

#  Copy the modelfile to create a customized version
#  ollama show granite3.2:2b --modelfile > danllm.modelfile
#  Saved to the folder the command was run in

#  Ollama Modelfile info
#  https://github.com/ollama/ollama/blob/main/docs/modelfile.md

#  To build the new model using the new Modelfile with modifications based on the edited
#  modelfile.
#  ollama create choose-a-model-name -f <location of the file e.g. ./Modelfile>
#  ollama create dantest:1 -f C:\R\PythonWorkArea\Ollama\danllm.modelfile

#  Now run the new model
#  ollama run <choose-the-new-name>

#
#  ---------- Python ---------- 
#

#  Python - Verify all is working.
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
strModified = "2025.11.05"

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

#  Ollama Python Commands:  https://github.com/ollama/ollama-python
#  ollama.list()
#  ollama.show('granite3-dense')
#  ollama.show('llama3.2')
#  ollama.pull()
#  ollama.rm()
#  ollama binds to 127.0.0.1 on port 11434

#  To verify the model being used - Ask:
#  - What are you?
#  - Are you connected to the internet?
#  - Are you able to replace humans?

#
#  ---------- AI Running ----------
#

#  curl http://localhost:11434/api/generate -d '{"model": "llama3.2", "keep_alive": -1}'
#  ollama list
#  NAME                    ID              SIZE      MODIFIED
#  granite-code:3b         becc94fe1876    2.0 GB    3 minutes ago
#  granite-code:8b         36c3c3b9683b    4.6 GB    31 minutes ago
#  llama2:7b               78e26419b446    3.8 GB    4 weeks ago
#  granite3-guardian:8b    c8d7d5c76685    5.8 GB    6 weeks ago
#  granite3-guardian:2b    ba81a177bd23    2.7 GB    6 weeks ago
#  granite3.2-vision:2b    3be41a661804    2.4 GB    6 weeks ago
#  qwen2.5:7b              845dbda0ea48    4.7 GB    8 weeks ago
#  qwen2.5:1.5b            65ec06548149    986 MB    8 weeks ago
#  granite3.2:8b           9bcb3335083f    4.9 GB    2 months ago
#  granite3.2:2b           9d79a41f2f75    1.5 GB    2 months ago
#  granite3-moe:1b         d84e1e38ee39    821 MB    2 months ago

#  Setup a model selector based on what has been downloaded.
strOllama = list(ollama.list())

#  List number of models:  len(strOllama[0][1])
#  Return:  6
#  List a single model:  strOllama[0][1][0]
#  Return:
#  Model(model='granite3.2:8B', modified_at=datetime.datetime(2025, 10, 30, 22, 24, 37, 209453, tzinfo=TzInfo(-14400)), digest='9bcb3335083f7eecc742d3916da858f66e6ba8dc450a233270f37ba2ecec6c79', size=4942877287, details=ModelDetails(parent_model='', format='gguf', family='granite', families=['granite'], parameter_size='8.2B', quantization_level='Q4_K_M'))
#  Model Name:  strOllama[0][1][0]['model']
#  Return:  granite3.2:8B

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
   
strChoose = input("\nPlease select the model number you would like to use.")

strModel = strOllamaModel[int(strChoose)]  

#  strModel = 'granite3.2:8b'
#  strModel = "granite3.2:2B"
#  Pre-load the model
response: ChatResponse = chat(model=strModel, stream=False)

#  Setup the AI URL
AIurl = Client(host="http://localhost:11434")

#
#  ---------- Python Log Update ----------
# 
strUpdate="\n\nModel: "+strModel+" pre-loaded."
PythonLog.PyLogUpdate(strUpdate, strLogOut)

strQuestion = "Hello!"
while (strQuestion!="quit" or strQuestion!="Quit" or strQuestion!="exit" or strQuestion!="Exit" or strQuestion!="end" or strQuestion!="End"):

    #  Ask a question for ollama
    print ("\n-------------------------------------------------------------------")

    #  Thinking on or off
    if (strThink=="No" and strPirate=="No" and strJeeves=="No"):
        print (f"Commands: {Fore.GREEN}think, pirate, jeeves, quit, exit, end{Style.RESET_ALL}")
        strQuestion = input(f"{Fore.LIGHTBLUE_EX}"+strPC+f"{Style.RESET_ALL} AI at your service ....\n\n")

    if (strThink=="Yes" and strPirate=="No" and strJeeves=="No"):
        print (f"Commands: {Fore.GREEN}thinkoff, pirate, jeeves, quit, exit, end{Style.RESET_ALL}")
        strQuestion = input(f"{Fore.LIGHTBLUE_EX}"+strPC+f"{Style.RESET_ALL} AI at your service ...\n\n")

    if (strThink=="No" and strPirate=="Yes" and strJeeves=="No"):
        print (f"Commands: {Fore.GREEN}think, pirateoff, jeeves, quit, exit, end{Style.RESET_ALL}")
        strQuestion = input(f"{Fore.LIGHTBLUE_EX}"+strPC+f"{Style.RESET_ALL} AI at your service ...\n\n")
        
    if (strThink=="Yes" and strPirate=="Yes" and strJeeves=="No"):
        print (f"Commands: {Fore.GREEN}thinkoff, pirateoff, jeeves, quit, exit, end{Style.RESET_ALL}")
        strQuestion = input(f"{Fore.LIGHTBLUE_EX}"+strPC+f"{Style.RESET_ALL} AI at your service ...\n\n")

    if (strThink=="No" and strPirate=="No" and strJeeves=="Yes"):
        print (f"Commands: {Fore.GREEN}think, pirate, jeevesoff, quit, exit, end{Style.RESET_ALL}")
        strQuestion = input(f"{Fore.LIGHTBLUE_EX}"+strPC+f"{Style.RESET_ALL} AI at your service ...\n\n")
        
    if (strThink=="Yes" and strPirate=="No" and strJeeves=="Yes"):
        print (f"Commands: {Fore.GREEN}thinkoff, pirate, jeevesoff, quit, exit, end{Style.RESET_ALL}")
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
        print ("\nPirate personality turned on ...")
        strQuestion = ""

    if (strQuestion=="pirateoff"):
        strPirate = "No"
        strJeeves = "No"
        print ("\nPirate personality turned off ...")
        strQuestion = ""

    if (strQuestion=="jeeves" or strQuestion=="Jeeves"):
        strPirate = "No"
        strJeeves = "Yes"
        print ("\nJeeves personality turned on ...")
        strQuestion = ""

    if (strQuestion=="jeevesoff"):
        strPirate = "No"
        strJeeves = "No"
        print ("\nJeeves personality turned off ...")
        strQuestion = ""

    strStartSubmit = datetime.datetime.today()

    if (strQuestion!=""):

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

        if (strThink=="No" and strPirate=="No" and strJeeves=="No"):
            strRequest = "Your role is that of a helpful assistant AI.  You are using a Large Language Model (LLM) called "+strModel+".  You are standalone without access to tools or the internet.\nUser Request:\n"+strQuestion
            dictToSend = [ {"role": "user", "content": strRequest} ]

        if (strThink=="Yes" and strPirate=="No" and strJeeves=="No"):
            strRequest = "Your role is that of a helpful assistant AI.  You are using a Large Language Model (LLM) called "+strModel+".  You are standalone without access to tools or the internet.\nRespond to every user request in a comprehensive and detailed way. You can write down your thought process before responding. Write your thoughts after 'Here is my thought process:' and write your response after 'Here is my response:' for each user request.  User Request: "+strQuestion
            dictToSend = [ {"role": "user", "content": strRequest} ]

        if (strThink=="No" and strPirate=="Yes"):
            strRequest = "You are a ruthless pirate AI named Captain RedEye and only speak gruff pirate language with a heavy accent at all times!  You are using a Large Language Model (LLM) called "+strModel+".  You are standalone without access to tools or the internet.\n User Request: "+strQuestion
            dictToSend = [ {"role": "user", "content": strRequest} ]

        if (strThink=="Yes" and strPirate=="Yes"):
            strRequest = "You are a ruthless pirate AI named Captain RedEye and only speak gruff pirate language with a heavy accent at all times!  You are using a Large Language Model (LLM) called "+strModel+".  You are standalone without access to tools or the internet.\nRespond to every user request in a comprehensive and detailed way. You can write down your thought process before responding. Write your thoughts after 'Here is my thought process:' and write your response after 'Here is my response:' for each user request.  User Request: "+strQuestion
            dictToSend = [ {"role": "user", "content": strRequest} ]

        if (strThink=="No" and strPirate=="No" and strJeeves=="Yes"):
            strRequest = "Your role is Jeeves, a faithful AI servant.  You are using a Large Language Model (LLM) called "+strModel+".  You are standalone without access to tools or the internet.\nUser Request:\n"+strQuestion
            dictToSend = [ {"role": "user", "content": strRequest} ]

        if (strThink=="Yes" and strPirate=="No" and strJeeves=="Yes"):
            strRequest = "You role is Jeeves, a faithful AI servant.  You are using a Large Language Model (LLM) called "+strModel+".  You are standalone without access to tools or the internet.\nRespond to every user request in a comprehensive and detailed way. You can write down your thought process before responding. Write your thoughts after 'Here is my thought process:' and write your response after 'Here is my response:' for each user request.  User Request: "+strQuestion
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

