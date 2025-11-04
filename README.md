# Ollama-Chat-App
This python app was developed utilizing Python 3.13.7
  - Testing occurred on Windows 11, MacOS 15.3.1 and Linux Mint 22.04.
It utilizes a local Ollama server, chats locally with any downloaded Ollama LLM &amp; SLM, giving a choice of model to use at startup.  Very easy local AI usage without uploads.  Additionally personalities with thinking were incorporated.  These include the usual helpful assistant, the always ready butler Jeeves and Pirate captain RedEye!  Thinking can be turned on or off where the AI will report thought processes before answering.  

#  Install Procedure 

0) On Windows or Linux - Install the NVIDIA CUDA drivers for your OS & hardware
   - https://developer.nvidia.com/downloads

2) Install Ollama server
   - https://ollama.com/ => Download
   - Verify operation - Find ollama app in the toolbar of your OS.
   - Note:  For local operation only, within the Ollama app, click Settings, then Airplane Mode slider = On
  
3) Open a cli to install local Ollama models
   - ollama list
   - May not return anything until models have been downloaded and installed.
   - Models are listed under the Ollama website / Search
   - Example:  ollama pull <modelname>
   - ollama pull granite3.2:2b

4) Install Python libraries
   - pip install ollama
   - pip install platform
   - pip install getpass
   - pip install datetime
   - pip install sqlite3
   - pip install pandas
   - pip install colorama
  
4) Download both "GPU-ollama-chat.py" and "PythonLog.py" to a folder

5) Within the CLI, navigate to the folder where your downloads exist.

#  Run the app within Python
6) python3 "GPU-ollama-chat.py"
  - The app will initialize, prompt you to choose a model that you've downloaded using Ollama.
  - Within this folder, the PythonLogs folder and the PythonLogAI folder will be created.
  - PythonLogs folder - will contain a basic log of this apps' operation.
  - PythonLogAI folder - will contain a SQLite3 database file tracking the AI interactions.  The initial prompt, the reply, how long it took, and number of tokens utilized on the input and output side.
  - Token tracking allows a way to track money saved since the inference was local.  Compare against pricing on your favorite AI service.

7) Issues, trouble, enhancements, please post within the repository issues.

Thank you!

D. Morvay
