from langchain.llms import OpenAI
from langchain.chains import RetrievalAugmentedGeneration
from langchain.retrievers import ChromaDB
from langchain.tokenizers import DefaultTokenizer
import asyncio
from bs4 import BeautifulSoup
import openai

async def index_data_in_chromadb(data, vector_store):
    # Assuming 'data' is a list of texts for which you want to create embeddings
    for text in data:
        # Step 1: Create embeddings using OpenAI's API
        # In this hypothetical example, we're assuming OpenAI has an endpoint that allows us to create embeddings
        try:
            response = openai.Embedding.create(
                input=text,
                engine="text-embedding-ada-001",  # Just an example, use the appropriate embedding engine
                api_key="XX_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"  # Replace with your actual API key
            )
            embedding = response['data']  # Assuming the embedding data is returned under a 'data' key
        except openai.error.OpenAIError as e:
            print(f"An error occurred while creating embeddings: {e}")
            continue

        # Step 2: Store the embeddings in ChromaDB
        # Here 'chromadb_store_embedding' is a placeholder for the actual method you would use to save the embedding
        try:
            await vector_store.chromadb_store_embedding(text, embedding)
        except Exception as e:
            print(f"An error occurred while storing embeddings in ChromaDB: {e}")

# Function to parse HTML and extract text
async def parse_html_and_index(file_path, vector_store):
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Use BeautifulSoup or another HTML parser to extract the text
    soup = BeautifulSoup(html_content, 'html.parser')
    texts = soup.get_text(separator=' ', strip=True)

    # Here we assume that texts is a list of string,
    # each string should be a piece of text that you want to index.
    await index_data_in_chromadb(texts, vector_store)

# Function to initialize and index data to ChromaDB
async def initialize_and_index(file_path):
    # Initialize ChromaDB as the vector store for the retriever
    vector_store = ChromaDB(api_key="zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz")

    # Parse the HTML and index the data
    await parse_html_and_index(file_path, vector_store)

html_file_path = 'telegram_group_messages.html'
await initialize_and_index(html_file_path)

# Initialize the OpenAI LLM with your API key
llm = OpenAI(api_key="XX_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

# Initialize the tokenizer
tokenizer = DefaultTokenizer()


# Set up the retriever with ChromaDB
retriever = ChromaDB(vector_store=vector_store, tokenizer=tokenizer)

# Initialize RAG with the LLM and the retriever
rag = RetrievalAugmentedGeneration(llm=llm, retriever=retriever)

# Function to process user questions, search from ChromaDB embeddings, and generate responses
async def answer_question(question):
    # Use RAG to generate an answer to the question
    answer = await rag.generate(question)

    return answer

async def main():
    # Example usage
    question = "Какую зарядку лучше использовать для Li L9?"
    answer = await answer_question(question)
    print(answer)

# Run the main function in the event loop
asyncio.run(main())
