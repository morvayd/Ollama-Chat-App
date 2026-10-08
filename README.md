# GPU-Ollama-Chat

A powerful, terminal-based Python application that allows you to interact with local Large Language Models (LLMs) via [Ollama](https://ollama.com/). Experience the power of local AI with customizable personalities and detailed interaction logging.

## 🚀 Key Features

### 🏠 Fully Local AI
Powered by **Ollama**, this application ensures that your conversations stay on your machine. No data ever leaves your hardware, providing ultimate privacy and speed.

### 🎭 Immersive Personalities
Transform your AI interaction with four distinct personas. You can switch between them to change the tone and style of the response:

*   **Jeeves**: Your faithful and impeccable servant. Always ready to assist with utmost respect and precision.
*   **SageBrush**: The Mystic Sage of the mountain top. Ponders the imponderable, responding with cryptic and mystical language.
*   **Captain RedEye**: A ruthless and salty pirate. Expect aggressive, bold, and high-seas-inspired responses.
*   **The Dull Assistant**: The definition of boring. Provides the most basic, uninspired, and monotonous responses possible.

### 📊 Advanced AI Tracking
Never lose a thought. The application automatically logs every interaction to a local SQLite database (`PythonLogAI/`), tracking:
*   Question & Answer text
*   Model used
*   Tokens consumed (Input/Output)
*   Time taken for response
*   Word counts

## 🛠️ Prerequisites

Before running the application, ensure you have the following installed:

1.  **Ollama**: The core engine for running local LLMs. [Download here](https://ollama.com/).
2.  **Python 3.x**: Ensure Python is installed and added to your system's PATH.

## ⚙️ Installation

1.  **Clone the repository** (if applicable).
2.  **Install the required Python libraries** using pip:

    ```bash
    pip install colorama ollama pandas
    ```

3.  **Pull an LLM model** via Ollama (if you haven't already). For example, to use the Granite model:

    ```bash
    ollama pull granite3.2:2b
    ```

## 🚀 Usage

Once everything is set up, simply run the script:

```bash
python GPU-ollama-chat.py
```

**Follow the interactive menu to:**
1.  **Select your model**: Choose from any model currently installed in your Ollama library.
2.  **Choose a personality**: Select the persona that fits your mood.
3.  **Chat**: Start typing your questions!

## 🛠️ Technical Details

*   **Logging**: Uses a dedicated `PythonLog` module to track application performance and interaction metrics.
*   **Database**: Data is stored locally in a SQLite database for lightweight and efficient retrieval.
*   **Colors**: Uses `colorama` for a rich, readable terminal experience.

---
**Author:** Daniel Morvay
**License:** MIT
