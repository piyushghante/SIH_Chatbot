# import mysql.connector

# def clear_table(db_connection, cursor, table_name):
#     try:
#         # Delete all records from the specified table
#         delete_query = f"DELETE FROM {table_name}"
#         cursor.execute(delete_query)
#         db_connection.commit()
#         return f'All records in the table {table_name} have been deleted.'
#     except Exception as e:
#         return f'An error occurred: {str(e)}'

# # Example usage:
# if __name__ == '__main__':
#     db_connection = mysql.connector.connect(
#         host="sql12.freemysqlhosting.net",
#         user="sql12647419",
#         password="vKb8GgZwFe",
#         database="sql12647419"
#     )

#     cursor = db_connection.cursor()

#     table_name = "pdf_files"  # Replace with the actual table name

#     result_message = clear_table(db_connection, cursor, table_name)
#     print(result_message)

#     cursor.close()
#     db_connection.close()
