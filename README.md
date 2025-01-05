Automated Monthly Message Clearing for SQLite Database
This repository provides a script to automatically clear messages from an SQLite database once a month. It is designed to work with a database file (messages.db) and can be scheduled using cron (Linux/macOS) or Task Scheduler (Windows).

Features
Clear Messages: Deletes all rows from the messages table in your SQLite database.

Optional Archiving: Supports archiving messages to a separate table or CSV file before clearing.

Scheduling: Can be scheduled to run automatically on the first day of every month.

Lightweight: Uses simple shell or Python scripts for easy customization.

Prerequisites
SQLite3: Ensure sqlite3 is installed on your system.

On Linux/macOS: Pre-installed or install via sudo apt install sqlite3 (Linux) or brew install sqlite (macOS).

On Windows: Download from the SQLite website.

Python (Optional): If using the Python script, ensure Python 3.x is installed.

Setup
1. Clone the Repository
Clone this repository to your local machine:

bash
Copy
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
2. Configure the Script
Edit the script (clear_messages.sh or clear_messages.py) to specify the path to your SQLite database file (messages.db).

For example, in clear_messages.sh:

bash
Copy
DB_PATH="./messages.db"
3. Make the Script Executable (Linux/macOS)
If using the shell script, make it executable:

bash
Copy
chmod +x clear_messages.sh
Usage
Run the Script Manually
To clear messages manually, run the script:

bash
Copy
./clear_messages.sh
or

bash
Copy
python clear_messages.py
Schedule the Script
On Linux/macOS (using cron):
Open the crontab editor:

bash
Copy
crontab -e
Add the following line to schedule the script to run on the first day of every month at midnight:

bash
Copy
0 0 1 * * /path/to/your-repo-name/clear_messages.sh >> /path/to/your-repo-name/clear_messages.log 2>&1
Save and exit the editor.

On Windows (using Task Scheduler):
Open Task Scheduler.

Create a new task:

Set the trigger to "Monthly" and choose the day (e.g., the 1st of the month).

Set the action to run your script (e.g., clear_messages.bat or python clear_messages.py).

Save the task.

Optional: Archive Messages
If you want to archive messages before clearing them, modify the script to export the data to a CSV file or a separate table.

Example: Archive to CSV
Add the following lines to your script:

bash
Copy
sqlite3 ./messages.db ".mode csv" ".headers on" ".output messages_archive.csv" "SELECT * FROM messages;"
Example: Archive to a New Table
Add the following SQL commands to your script:

sql
Copy
CREATE TABLE IF NOT EXISTS messages_archive AS SELECT * FROM messages;
Logs
If you scheduled the script using cron, logs will be saved to clear_messages.log in the repository directory. Check this file for debugging purposes.

Contributing
If you'd like to contribute to this project, please fork the repository and submit a pull request. For major changes, open an issue first to discuss your ideas.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Support
If you encounter any issues or have questions, feel free to open an issue on the GitHub repository.
