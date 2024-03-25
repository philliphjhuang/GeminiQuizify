import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
import PyPDF2
import os
import tempfile
import uuid

class DocumentProcessor:
    """
    This class encapsulates the functionality for processing uploaded PDF documents using Streamlit
    and Langchain's PyPDFLoader. It provides a method to render a file uploader widget, process the
    uploaded PDF files, extract their pages, and display the total number of pages extracted. 
    """
    def __init__(self):
        self.pages = [] # List to keep track of pages from all documents

    def ingest_documents(self):
        # Step 1: Render a file uploader widget.
        uploaded_files = st.file_uploader("Upload PDF files", type=["pdf"], accept_multiple_files=True)

        if uploaded_files:
            for uploaded_file in uploaded_files:
                # Generate a unique identifier to append to the file's original name
                unique_id = uuid.uuid4().hex
                original_name, file_extension = os.path.splitext(uploaded_file.name)
                temp_file_name = f"{original_name}_{unique_id}{file_extension}"
                temp_file_path = os.path.join(tempfile.gettempdir(), temp_file_name)

                # Write the uploaded PDF to a temporary file
                with open(temp_file_path, 'wb') as f:
                    f.write(uploaded_file.getvalue())
                
                # Step 2: Process the file (Use PyPDFLoader2 to load the PDF and extract pages)
                if uploaded_file is not None:
                    pdf_reader = PyPDF2.PdfReader(uploaded_file)
                    num_pages = len(pdf_reader.pages)
                    st.write(f"{original_name}.pdf contains {num_pages} pages.")

                # Step 3: Add the extracted pages to the 'pages' lsit
                if uploaded_file is not None:
                    for page_number in range(len(pdf_reader.pages)):
                        page = pdf_reader.pages[page_number]
                        self.pages.append(page.extract_text())
                
                # Clean up by deleting the temporary file
                os.unlink(temp_file_path)

            st.write(f"Total pages processed: {len(self.pages)}")

if __name__ == "__main__":
    processor = DocumentProcessor()
    processor.ingest_documents()