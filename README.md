# Telegram-RAG - Telegram Parser with RAG and ChromaDB
Integrating of Retrieval-augmented Generation (RAG) with ChromaDB and Langchain to enable users to ask questions from parsed Telegram data with the ChatGPT API.

![splash]([[https://github.com/[username]/[reponame]/blob/[branch]/image.jpg?raw=true](https://media.cloudbooklet.com/uploads/2023/10/30100253/Telegram-AI-Chatbots-1.jpg)](https://media.cloudbooklet.com/uploads/2023/10/30100253/Telegram-AI-Chatbots-1.jpg))


## About 

This project is designed to parse messages from a Telegram group and enable querying that data using a Retrieval-Augmented Generation (RAG) model, which leverages ChromaDB for efficient vector storage and retrieval, and Langchain to provide a seamless interface for language model interactions.

## Features

- **Telegram Message Parsing**: Extract messages from a Telegram group from its inception to create a searchable dataset.
- **Retrieval-Augmented Generation (RAG)**: Combine retrieved information with language model generation for informed responses.
- **ChromaDB Integration**: Use ChromaDB as a vector store to facilitate fast and scalable retrieval of message embeddings.
- **Langchain Interface**: Utilize Langchain to integrate the RAG model with ChromaDB and the OpenAI GPT (ChatGPT) API.

## Project Structure

- `tg_dumper.py`: Contains the code for parsing Telegram group messages.
- `rag.py`: Includes the RAG logic and integration with Langchain and ChromaDB.
- `utils.py`: Utility scripts and helpers for the project.
- `requirements.txt`: The Python dependencies required for the project.

## Installation

To set up this project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/telegram-parser-rag.git
   cd telegram-parser-rag
2. Install the required Python packages:
3. ```pip install -r requirements.txt```
4. Create a .env file with your API keys and other configuration settings.
5. Run the Telegram parser script to collect data (see Usage section).

## Usage
Telegram Parser
To parse messages from a Telegram group, run the script located in the telegram_parser/ directory. This requires setting up your Telegram API keys and group information.
```python telegram_parser/parser.py```

### RAG with ChromaDB and Langchain
Once you have your dataset from the Telegram parser, you can use the RAG component to answer questions based on this data.
```python rag/answer_question.py "Your question here"```

### Configuration
You will need to provide your own API keys for Telegram, ChromaDB, and OpenAI. These should be set in your .env file or your environment variables.

### Contributing
Contributions are welcome! Please feel free to submit a pull request or create an issue if you have suggestions or find a bug.

### License
This project is released under the MIT License. See the LICENSE file for details.

### Contact
If you have any questions or comments, please open an issue in this repository or reach out directly to the repository maintainers or write me on telegram @uberwow.
