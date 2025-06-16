import getpass
import oracledb

pwd = "Casemiro18"
user = "sean_admin"
host = "Judge-PC"
port = 1521
service_name = "FREE"
conn = oracledb.connect(user=user, password=pwd, host=host, port=port, service_name=service_name)

connection = conn
cursor = connection.cursor()

with connection.cursor() as cursor:
    #cursor.execute("insert into WARANDPEACEV3 (book_id int, page_no int, page_text clob)")
    for row in cursor.execute("select * from WARANDPEACEV3"):
        print(row)


# filepath = "WarAndPeace.txt"
# book_id = "1"
# pages = text_file(filepath)
# insert_pages(pages, book_id)

# with open("WarAndPeace.txt", 'r') as file:
#     content = file.read()
#
#     pages = [content[i:i + 4000] for i in range(0, len(content), 4000)]
#     return pages
#
# def insert_pages(pages, book_id):
#     connection = conn
#     cursor = connection.cursor()
#
#     for page_number, text in enumerate(pages, start=1):
#         cursor.execute("""
#         insert into WarAndPeace (book_id, page_no, page_text)
#         values (:book_id, :page_number, :text)
#         """, {
#             'book_id': book_id, 'page_no': page_number, 'page_text': text
#         })
#
#     connection.commit()
#
#     cursor.close()
#     connection.close()
#
#
