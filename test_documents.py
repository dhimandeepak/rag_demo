# Import necessary libraries
from dotenv import load_dotenv
from llama_index.core import SimpleDirectoryReader

# Load environment variables
load_dotenv()

# Load documents from a directory (you can change this path as needed)
documents = SimpleDirectoryReader("data").load_data()

# Add this section to explore the documents
print(f"Number of documents loaded: {len(documents)}")
for i, doc in enumerate(documents):
    print(f"\nDocument {i+1}:")
    #print(f"Text preview: {doc.text[:200]}...")  # Print first 200 characters
    print(f"Metadata: {doc.metadata}")

print(documents[0].text)