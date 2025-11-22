#  Author:  Daniel Morvay
#  Creator Email:  morvayd@gmail.com

#
#  ---------- CLI Install ----------
#

#  From the system Command Line Interface (CLI)
pip install colorama
pip install ollama
pip install pandas
pip install sqlite3

#
#  ---------- Cuda Install ----------
#
#  Download and install cuda installer - Windows or Linux
firefox https://developer.nvidia.com/cuda-downloads

#  Check the cuda version from the CLI
nvcc --version
#  nvidia-smi => windows: powershell => nvidia-smi
nvidia-smi
#  Reports back info regarding the NVIDIA GPU

#  ----- Mac - No need on Apple Silicon -----

#
#  ---------- Ollama Install ----------
#

#  CPU or GPU Based ollama - Adjusts based on availability

#  Download & Install Ollama
firefox  https://ollama.com/download

#  ----- Run ollama -----
ollama pull llama3.2:2b
ollama run llama3.2:2b
#  From within ollama
/show info
#  Model info appears
#  Exit ollama server
/exit

#  Linux & Windows - Verify - Open new CLI
nvidia-smi 
#  Verify ollama is using the GPU

#  Ollama Model Win11 Location:  C:\Users\<UserID>\.ollama

#  List the modelfile
ollama show llama2:latest --modelfile
ollama show granite3.2:2b --modelfile

#  Copy the modelfile to create a customized version
ollama show granite3.2:2b --modelfile > danllm.modelfile
#  Saved to the folder the command was run in

#  Ollama Modelfile info
#  Reference:  
firefox https://github.com/ollama/ollama/blob/main/docs/modelfile.md

#  To build the new model using the new Modelfile with modifications based on the edited
#  modelfile.
#  ollama create <choose-a-model-name> -f <location of the file e.g. ./Modelfile>
ollama create dantest:1 -f C:\R\PythonWorkArea\Ollama\danllm.modelfile

#  Now run the new model
#  ollama run <choose-the-new-name>
ollama run dantest:1

#
#  ---------- Ollama with Python ----------
#

#  Note:  
#  PythonLog.py - keep in the same folder as Python-Library-Locate.py
#  This will create a PythonLogs folder and save app logs there.  

#  Run the app
python3 GPU-ollama-chat.py
