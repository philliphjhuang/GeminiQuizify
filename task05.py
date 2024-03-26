import sys
import os
import streamlit as st
sys.path.append(os.path.abspath('../../'))
from task03 import DocumentProcessor
from task04 import EmbeddingClient

from langchain_core.documents import Document
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma

class ChromaCollectionCreator:
    def __init__(self, processor, embed_model):
        self.processor = processor
        self.embed_model = embed_model
        self.db = None  # Initialize the Chroma collection database here

    def create_chroma_collection(self):
        # Step 1: Check for processed documents
        if len(self.processor.pages) == 0:
            st.error("No documents found.", icon="💀")
            return
        
        # Step 2: Split documents into text chunks
        splitter = CharacterTextSplitter(separator=". ", chunk_size=500, chunk_overlap=100)
        texts = []
        for page in self.processor.pages:
            page_text_chunks = splitter.split_text(page)  # Pass the text content to the split_text method
            texts.extend(page_text_chunks)
        if texts is not None:
            st.success(f"Successfully split pages into {len(texts)} documents.", icon="👌")
        else:
            st.error("Failed to split pages into text chunks.", icon="💀")
        
        # Step 3: Create the Chroma Collection
        chroma_collection = []
        for text in texts:
            chroma_collection.append(Document(page_content=text))
        self.db = Chroma.from_documents(chroma_collection, self.embed_model)
        if self.db:
            st.success("Successfully created Chroma Collection.", icon="👌")
        else:
            st.error("Failed to create Chroma Collection.", icon="💀")
    
    def query_chroma_collection(self, query) -> Document:
        if self.db:
            docs = self.db.similarity_search_with_relevance_scores(query)
            if docs:
                return docs[0]
            else:
                st.error("No matching documents found.", icon="💀")
        else:
            st.error("Chroma Collection has not been created.", icon="💀")

if __name__ == "__main__":
    processor = DocumentProcessor()
    processor.ingest_documents()

    embed_config = {
        "model_name" : "textembedding-gecko@003",
        "project"    : "your-project-name", # Enter your own project id,
        "location"   : "us-central1"
    }

    embed_client = EmbeddingClient(**embed_config)

    chroma_creator = ChromaCollectionCreator(processor, embed_client)

    with st.form("Load Data to Chroma"):
        st.write("Select PDFs for Ingestion, then click Submit.")

        submitted = st.form_submit_button("Submit")
        if submitted:
            chroma_creator.create_chroma_collection()
