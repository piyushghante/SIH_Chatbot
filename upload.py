# # # import os
# # # import mysql.connector
# # # import zipfile

# # # def extract_and_upload_pdfs(zip_file_path, db_connection, cursor):
# # #     try:
# # #         # Check if the ZIP file exists
# # #         if not os.path.isfile(zip_file_path):
# # #             return 'ZIP file not found.'

# # #         # Extract the PDFs from the ZIP archive
# # #         with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
# # #             pdf_files = [name for name in zip_file.namelist() if name.lower().endswith('.pdf')]

# # #             if not pdf_files:
# # #                 return 'No PDF files found in the ZIP archive.'

# # #             for pdf_file_name in pdf_files:
# # #                 # Check if a PDF with the same "id" already exists in the database
# # #                 cursor.execute("SELECT COUNT(*) FROM pdf_files WHERE file_name = %s", (pdf_file_name,))
# # #                 result = cursor.fetchone()

# # #                 if result and result[0] > 0:
# # #                     # A PDF with the same "id" already exists, delete it
# # #                     cursor.execute("DELETE FROM pdf_files WHERE file_name = %s", (pdf_file_name,))
# # #                     db_connection.commit()

# # #                 pdf_data = zip_file.read(pdf_file_name)
# # #                 # Insert the PDF data into the MySQL table
# # #                 cursor.execute("INSERT INTO pdf_files (file_name, pdf_data) VALUES (%s, %s)", (pdf_file_name, pdf_data))
# # #                 db_connection.commit()

# # #         return 'PDFs uploaded and inserted into the database successfully!'
# # #     except Exception as e:
# # #         return f'An error occurred: {str(e)}'

# # # # Example usage:
# # # if __name__ == '__main__':
# # #     db_connection = mysql.connector.connect(
# # #         host="sql12.freemysqlhosting.net",
# # #         user="sql12647419",
# # #         password="vKb8GgZwFe",
# # #         database="sql12647419"
# # #     )

# # #     cursor = db_connection.cursor()

# # #     zip_file_path = 'PDF.zip'  # Replace with the actual ZIP file path

# # #     result_message = extract_and_upload_pdfs(zip_file_path, db_connection, cursor)
# # #     print(result_message)

# # #     cursor.close()
# # #     db_connection.close()

# # import os
# # import mysql.connector
# # import zipfile
# # import streamlit as st

# # # Function to extract and upload PDFs
# # def extract_and_upload_pdfs(zip_file, db_connection, cursor):
# #     try:
# #         # Check if the ZIP file exists
# #         if not zip_file:
# #             return 'ZIP file not found.'

# #         # Extract the PDFs from the ZIP archive
# #         with zipfile.ZipFile(zip_file, 'r') as zip_file:
# #             pdf_files = [name for name in zip_file.namelist() if name.lower().endswith('.pdf')]

# #             if not pdf_files:
# #                 return 'No PDF files found in the ZIP archive.'

# #             for pdf_file_name in pdf_files:
# #                 # Check if a PDF with the same "id" already exists in the database
# #                 cursor.execute("SELECT COUNT(*) FROM pdf_files WHERE file_name = %s", (pdf_file_name,))
# #                 result = cursor.fetchone()

# #                 if result and result[0] > 0:
# #                     # A PDF with the same "id" already exists, delete it
# #                     cursor.execute("DELETE FROM pdf_files WHERE file_name = %s", (pdf_file_name,))
# #                     db_connection.commit()

# #                 pdf_data = zip_file.read(pdf_file_name)
# #                 # Insert the PDF data into the MySQL table
# #                 cursor.execute("INSERT INTO pdf_files (file_name, pdf_data) VALUES (%s, %s)", (pdf_file_name, pdf_data))
# #                 db_connection.commit()

# #         return 'PDFs uploaded and inserted into the database successfully!'
# #     except Exception as e:
# #         return f'An error occurred: {str(e)}'

# # # Streamlit UI
# # def main():
# #     st.title("PDF Upload to MySQL Database")

# #     # File upload widget
# #     uploaded_file = st.file_uploader("Choose a ZIP file", type=["zip"])

# #     if uploaded_file:
# #         st.write("Uploaded file:", uploaded_file.name)

# #         if st.button("Upload PDFs"):
# #             try:
# #                 db_connection = mysql.connector.connect(
# #                     host="sql12.freemysqlhosting.net",
# #                     user="sql12647419",
# #                     password="vKb8GgZwFe",
# #                     database="sql12647419"
# #                 )

# #                 cursor = db_connection.cursor()

# #                 result_message = extract_and_upload_pdfs(uploaded_file, db_connection, cursor)
# #                 st.success(result_message)

# #                 cursor.close()
# #                 db_connection.close()
# #             except Exception as e:
# #                 st.error(f"An error occurred: {str(e)}")

# # if __name__ == "__main__":
# #     main()

# import os
# import mysql.connector
# import zipfile
# import streamlit as st

# # Database credentials
# db_host = "sql12.freemysqlhosting.net"
# db_user = "sql12647419"
# db_password = "vKb8GgZwFe"
# db_database = "sql12647419"

# # Function to extract and upload PDFs (unchanged from previous code)
# def extract_and_upload_pdfs(zip_file, db_connection, cursor):
#     try:
#         # Check if the ZIP file exists
#         if not zip_file:
#             return 'ZIP file not found.'

#         # Extract the PDFs from the ZIP archive
#         with zipfile.ZipFile(zip_file, 'r') as zip_file:
#             pdf_files = [name for name in zip_file.namelist() if name.lower().endswith('.pdf')]

#             if not pdf_files:
#                 return 'No PDF files found in the ZIP archive.'

#             for pdf_file_name in pdf_files:
#                 # Check if a PDF with the same "id" already exists in the database
#                 cursor.execute("SELECT COUNT(*) FROM pdf_files WHERE file_name = %s", (pdf_file_name,))
#                 result = cursor.fetchone()

#                 if result and result[0] > 0:
#                     # A PDF with the same "id" already exists, delete it
#                     cursor.execute("DELETE FROM pdf_files WHERE file_name = %s", (pdf_file_name,))
#                     db_connection.commit()

#                 pdf_data = zip_file.read(pdf_file_name)
#                 # Insert the PDF data into the MySQL table
#                 cursor.execute("INSERT INTO pdf_files (file_name, pdf_data) VALUES (%s, %s)", (pdf_file_name, pdf_data))
#                 db_connection.commit()

#         return 'PDFs uploaded and inserted into the database successfully!'
#     except Exception as e:
#         return f'An error occurred: {str(e)}'

# # Streamlit UI
# def main():
#     st.title("PDF Upload to Mines ChatBot Database")

#     # Create a session variable to track login status
#     is_logged_in = st.session_state.get("is_logged_in", False)

#     if not is_logged_in:
#         # Display the login form
#         st.sidebar.header("Login")
#         username = st.sidebar.text_input("Username")
#         password = st.sidebar.text_input("Password", type="password")

#         if st.sidebar.button("Login"):
#             # Implement your authentication logic here
#             if username == "admin" and password == "admin":
#                 is_logged_in = True
#                 st.session_state["is_logged_in"] = True
#                 st.sidebar.success("Login successful!")
#             else:
#                 st.sidebar.error("Login failed. Please check your credentials.")

#     if is_logged_in:
#         # Display the upload page if logged in
#         uploaded_file = st.file_uploader("Choose a ZIP file", type=["zip"])

#         if uploaded_file:
#             st.write("Uploaded file:", uploaded_file.name)

#             if st.button("Upload PDFs"):
#                 try:
#                     db_connection = mysql.connector.connect(
#                         host=db_host,
#                         user=db_user,
#                         password=db_password,
#                         database=db_database
#                     )

#                     cursor = db_connection.cursor()

#                     result_message = extract_and_upload_pdfs(uploaded_file, db_connection, cursor)
#                     st.success(result_message)

#                     cursor.close()
#                     db_connection.close()
#                 except Exception as e:
#                     st.error(f"An error occurred: {str(e)}")

# if __name__ == "__main__":
#     main()

import os
import mysql.connector
import zipfile
import streamlit as st

# Database credentials
db_host = "sql12.freemysqlhosting.net"
db_user = "sql12647419"
db_password = "vKb8GgZwFe"
db_database = "sql12647419"

# Function to extract and upload PDFs (unchanged from previous code)
def extract_and_upload_pdfs(zip_file, db_connection, cursor):
    try:
        # Check if the ZIP file exists
        if not zip_file:
            return 'ZIP file not found.'

        # Extract the PDFs from the ZIP archive
        with zipfile.ZipFile(zip_file, 'r') as zip_file:
            pdf_files = [name for name in zip_file.namelist() if name.lower().endswith('.pdf')]

            if not pdf_files:
                return 'No PDF files found in the ZIP archive.'

            for pdf_file_name in pdf_files:
                # Check if a PDF with the same "id" already exists in the database
                cursor.execute("SELECT COUNT(*) FROM pdf_files WHERE file_name = %s", (pdf_file_name,))
                result = cursor.fetchone()

                if result and result[0] > 0:
                    # A PDF with the same "id" already exists, delete it
                    cursor.execute("DELETE FROM pdf_files WHERE file_name = %s", (pdf_file_name,))
                    db_connection.commit()

                pdf_data = zip_file.read(pdf_file_name)
                # Insert the PDF data into the MySQL table
                cursor.execute("INSERT INTO pdf_files (file_name, pdf_data) VALUES (%s, %s)", (pdf_file_name, pdf_data))
                db_connection.commit()

        return 'PDFs uploaded and inserted into the database successfully!'
    except Exception as e:
        return f'An error occurred: {str(e)}'

# Streamlit UI
def main():
    st.title("PDF Upload to Mines ChatBot Database")

    # Create a session variable to track login status
    is_logged_in = st.session_state.get("is_logged_in", False)

    if not is_logged_in:
        # Display the login form
        st.sidebar.header("Login")
        username = st.sidebar.text_input("Username")
        password = st.sidebar.text_input("Password", type="password")

        if st.sidebar.button("Login"):
            # Implement your authentication logic here
            if username == "admin" and password == "admin":
                is_logged_in = True
                st.session_state["is_logged_in"] = True
                st.sidebar.success("Login successful!")
            else:
                st.sidebar.error("Login failed. Please check your credentials.")

    if is_logged_in:
        # Display the logout button
        if st.sidebar.button("Logout"):
            is_logged_in = False
            st.session_state["is_logged_in"] = False
            st.sidebar.success("Logout successful!")

        # Display the upload page if logged in
        uploaded_file = st.file_uploader("Choose a ZIP file", type=["zip"])

        if uploaded_file:
            st.write("Uploaded file:", uploaded_file.name)

            if st.button("Upload PDFs"):
                try:
                    db_connection = mysql.connector.connect(
                        host=db_host,
                        user=db_user,
                        password=db_password,
                        database=db_database
                    )

                    cursor = db_connection.cursor()

                    result_message = extract_and_upload_pdfs(uploaded_file, db_connection, cursor)
                    st.success(result_message)

                    cursor.close()
                    db_connection.close()
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()

