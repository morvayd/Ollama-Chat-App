#  Reference:  https://github.com/ollama/ollama-python
#  Author:  Daniel Morvay
#  Creator Email:  morvayd@gmail.com
#  strModified = "2025.11.22"

#
#  ---------- Python ---------- 
#

#  Ollama commands in python
#  ollama binds to 127.0.0.1 on port 11434

ollama.list()
ollama.show('granite3-dense')
ollama.show('llama3.2')
ollama.pull()
ollama.rm()

#  To verify the model being used - Ask:
#  - What are you?
#  - Are you connected to the internet?
#  - Are you able to replace humans?

#
#  ---------- AI Running ----------
#

curl http://localhost:11434/api/generate -d '{"model": "llama3.2", "keep_alive": -1}'
ollama list
#  Return:

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

strOllama = list(ollama.list())

#  List number of models:
len(strOllama[0][1])
#  Return:  6

#  List a single model:
strOllama[0][1][0]
#  Return:
#  Model(model='granite3.2:8B', modified_at=datetime.datetime(2025, 10, 30, 22, 24, 37, 209453, tzinfo=TzInfo(-14400)), digest='9bcb3335083f7eecc742d3916da858f66e6ba8dc450a233270f37ba2ecec6c79', size=4942877287, details=ModelDetails(parent_model='', format='gguf', family='granite', families=['granite'], parameter_size='8.2B', quantization_level='Q4_K_M'))

#  Model Name:
strOllama[0][1][0]['model']
#  Return:  granite3.2:8B

