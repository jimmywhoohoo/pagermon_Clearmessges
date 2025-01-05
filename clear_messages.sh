#!/bin/bash
# Path to your SQLite database
DB_PATH="./messages.db"

# Clear the messages table
sqlite3 "$DB_PATH" "DELETE FROM messages;"

# Optional: Run VACUUM to free up space
sqlite3 "$DB_PATH" "VACUUM;"

echo "Messages cleared successfully."
