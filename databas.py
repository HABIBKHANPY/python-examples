import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('records.db')
cursor = conn.cursor()

# Create a table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS records (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    age INTEGER,
                    email TEXT
                )''')
conn.commit()

def add_record(name, age, email):
    cursor.execute('''INSERT INTO records (name, age, email) VALUES (?, ?, ?)''', (name, age, email))
    conn.commit()
    print("Record added successfully.")

def view_records():
    cursor.execute('''SELECT * FROM records''')
    records = cursor.fetchall()
    print("ID | Name | Age | Email")
    for record in records:
        print(record)

def remove_record(record_id):
    cursor.execute('''DELETE FROM records WHERE id = ?''', (record_id,))
    conn.commit()
    print("Record removed successfully.")

# Example usage
add_record("Asif Khan", 30, "asif@example.com")
add_record("Waseem zahid", 25, "waseem@example.com")
view_records()
remove_record(1)
view_records()

# Close the connection
conn.close()
