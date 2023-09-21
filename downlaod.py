import mysql.connector
import os
import re

def clean_filename(filename):
    # Remove invalid characters and replace them with underscores
    cleaned_filename = re.sub(r'[\/:*?"<>|]', '_', filename)
    return cleaned_filename

def download_pdfs_from_db(db_connection, cursor, output_folder):
    try:
        # Create the output folder if it doesn't exist
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Retrieve all PDFs from the database
        cursor.execute("SELECT file_name, pdf_data FROM pdf_files")
        pdf_records = cursor.fetchall()

        if not pdf_records:
            return 'No PDFs found in the database.'

        for pdf_record in pdf_records:
            file_name, pdf_data = pdf_record
            cleaned_file_name = clean_filename(file_name)
            file_path = os.path.join(output_folder, cleaned_file_name)

            # Save the PDF data to a file
            with open(file_path, 'wb') as pdf_file:
                pdf_file.write(pdf_data)

        return 'PDFs downloaded successfully!'
    except Exception as e:
        return f'An error occurred: {str(e)}'

# Example usage:
if __name__ == '__main__':
    db_connection = mysql.connector.connect(
        host="sql12.freemysqlhosting.net",
        user="sql12647419",
        password="vKb8GgZwFe",
        database="sql12647419"
    )

    cursor = db_connection.cursor()

    output_folder = 'downloaded_pdfs'  # Replace with the desired output folder path

    result_message = download_pdfs_from_db(db_connection, cursor, output_folder)
    print(result_message)

    cursor.close()
    db_connection.close()
