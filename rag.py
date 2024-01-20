from langchain.llms import OpenAI
from langchain.chains import RetrievalAugmentedGeneration
from langchain.retrievers import ChromaDB
from langchain.tokenizers import DefaultTokenizer

# Initialize the OpenAI LLM with your API key
llm = OpenAI(api_key="XX_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

# Initialize the tokenizer
tokenizer = DefaultTokenizer()

# Initialize ChromaDB as the vector store for the retriever
vector_store = ChromaDB(api_key="zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz")

# Set up the retriever with ChromaDB
retriever = ChromaDB(vector_store=vector_store, tokenizer=tokenizer)

# Initialize RAG with the LLM and the retriever
rag = RetrievalAugmentedGeneration(llm=llm, retriever=retriever)

# Function to process user questions, search from ChromaDB embeddings, and generate responses
async def answer_question(question):
    # Use RAG to generate an answer to the question
    answer = await rag.generate(question)

    return answer

# Example usage
question = "Какую зарядку лучше использовать для Li L9?"
answer = await answer_question(question)
print(answer)
