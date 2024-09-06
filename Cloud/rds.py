import mysql.connector

# Connect to MySQL server
conn = mysql.connector.connect(
    host="database-2.cha4i628il1e.us-west-2.rds.amazonaws.com",  # public-endpoint
    user="admin",
    password="shreesha41223"
)

# Create a cursor object
cursor = conn.cursor()

# Create a new database
cursor.execute("CREATE DATABASE my_new_database")
conn.commit()

# Confirm the database creation
cursor.execute("SHOW DATABASES")
for db in cursor:
    print(db)

# Create a new table
create_table_query = """
CREATE TABLE my_new_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    email VARCHAR(100)
)
"""

cursor.execute("USE my_new_database")
cursor.execute(create_table_query)

cursor.execute("SHOW TABLES")
for table in cursor:
    print(table)

insert_query = """
INSERT INTO my_new_table (name, age, email)
VALUES (%s, %s, %s)
"""
data = ("John Doe", 30, "john.doe@example.com")

# Execute the insert query
cursor.execute(insert_query, data)

# Confirm the insertion
cursor.execute("SELECT * FROM my_new_table")
for row in cursor:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()