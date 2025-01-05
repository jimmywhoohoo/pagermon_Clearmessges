import sqlite3

# Path to your SQLite database
DB_PATH = "./messages.db"

# Connect to the database
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Clear the messages table
cursor.execute("DELETE FROM messages;")

# Optional: Run VACUUM to free up space
cursor.execute("VACUUM;")

# Commit and close the connection
conn.commit()
conn.close()

print("Messages cleared successfully.")
