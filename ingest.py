# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain.document_loaders import PyPDFLoader, DirectoryLoader
# from langchain.embeddings import HuggingFaceEmbeddings
# from langchain.vectorstores import FAISS


# DATA_PATH ="data/"
# DB_FAISS_PATH = "vectorstores/db_faiss"

# def create_vector_db():
#     loader=DirectoryLoader(DATA_PATH,glob='*.pdf', loader_cls=PyPDFLoader)
#     documents=loader.load()
#     text_spliter=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=50)
#     texts=text_spliter.split_documents(documents)
    
#     embeddings=HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2',model_kwargs={'device':'cpu'})
    
#     db=FAISS.from_documents(texts,embeddings)
#     db.save_local(DB_FAISS_PATH)

# if __name__ == '__main__':
#     create_vector_db()


import mysql.connector
import os
import re
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

def clean_filename(filename):
    # Remove invalid characters and replace them with underscores
    cleaned_filename = re.sub(r'[\/:*?"<>|]', '_', filename)
    return cleaned_filename
def download_pdfs_from_db_and_process(db_connection, cursor, output_folder):
    try:
        # Create the output folder if it doesn't exist
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Retrieve all PDFs from the database
        cursor.execute("SELECT file_name, pdf_data FROM pdf_files")
        pdf_records = cursor.fetchall()

        if not pdf_records:
            return 'No PDFs found in the database.'

        downloaded_pdfs = []

        for pdf_record in pdf_records:
            file_name, pdf_data = pdf_record
            cleaned_file_name = clean_filename(file_name)
            file_path = os.path.join(output_folder, cleaned_file_name)

            # Save the PDF data to a file
            with open(file_path, 'wb') as pdf_file:
                pdf_file.write(pdf_data)

            downloaded_pdfs.append(file_path)

        # Process the downloaded PDFs
        process_downloaded_pdfs(output_folder)  # Pass the folder path instead of a list

        return 'PDFs downloaded and processed successfully!'
    except Exception as e:
        return f'An error occurred: {str(e)}'

def process_downloaded_pdfs(pdf_folder):  # Accept a folder path as an argument
    DB_FAISS_PATH = "vectorstores/db_faiss"

    loader = DirectoryLoader(pdf_folder, loader_cls=PyPDFLoader)  # Load PDFs from the folder
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    texts = text_splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2', model_kwargs={'device': 'cpu'})

    db = FAISS.from_documents(texts, embeddings)
    db.save_local(DB_FAISS_PATH)


if __name__ == '__main__':
    db_connection = mysql.connector.connect(
        host="sql12.freemysqlhosting.net",
        user="sql12647419",
        password="vKb8GgZwFe",
        database="sql12647419"
    )

    cursor = db_connection.cursor()

    output_folder = 'downloaded_pdfs'  # Replace with the desired output folder path

    result_message = download_pdfs_from_db_and_process(db_connection, cursor, output_folder)
    print(result_message)

    cursor.close()
    db_connection.close()
