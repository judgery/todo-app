import oracledb

# Configuration
pwd = "Casemiro18"
user = "sean_admin"
host = "Judge-PC"
port = 1521
service_name = "FREE"
conn = oracledb.connect(user=user, password=pwd, host=host, port=port, service_name=service_name)

BOOK_ID = "1"
TEXT_FILE_PATH = "WarAndPeace.txt"

# Connect to Oracle DB
connection = conn
cursor = connection.cursor()

# Create the insert SQL statement
insert_sql = """
    INSERT INTO WARANDPEACEV3 (book_id, page_no, page_text)
    VALUES (:book_id, :page_no, :page_text)
"""

# Read file and split into pages
with open(TEXT_FILE_PATH, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Group lines into pages (40 lines per page)
page_size = 40
pages = [lines[i:i + page_size] for i in range(0, len(lines), page_size)]

# Insert each page into the database
for page_no, page_lines in enumerate(pages, start=1):
    page_text = ''.join(page_lines)  # Join lines into a single string
    cursor.execute(insert_sql, {
        'book_id': 1,
        'page_no': page_no,
        'page_text': page_text
    })

# Commit changes and close connection
connection.commit()
cursor.close()
connection.close()

print("Data inserted successfully!")

