<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Automated Monthly Message Clearing for SQLite Database</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
        }
        h1, h2, h3 {
            color: #333;
        }
        code {
            background-color: #f4f4f4;
            padding: 2px 5px;
            border-radius: 3px;
            font-family: monospace;
        }
        pre {
            background-color: #f4f4f4;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
        a {
            color: #0366d6;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <h1>Automated Monthly Message Clearing for SQLite Database</h1>
    <p>This repository provides a script to automatically clear messages from an SQLite database once a month. It is designed to work with a database file (<code>messages.db</code>) and can be scheduled using <code>cron</code> (Linux/macOS) or Task Scheduler (Windows).</p>

    <h2>Features</h2>
    <ul>
        <li><strong>Clear Messages</strong>: Deletes all rows from the <code>messages</code> table in your SQLite database.</li>
        <li><strong>Optional Archiving</strong>: Supports archiving messages to a separate table or CSV file before clearing.</li>
        <li><strong>Scheduling</strong>: Can be scheduled to run automatically on the first day of every month.</li>
        <li><strong>Lightweight</strong>: Uses simple shell or Python scripts for easy customization.</li>
    </ul>

    <h2>Prerequisites</h2>
    <ul>
        <li><strong>SQLite3</strong>: Ensure <code>sqlite3</code> is installed on your system.
            <ul>
                <li>On Linux/macOS: Pre-installed or install via <code>sudo apt install sqlite3</code> (Linux) or <code>brew install sqlite</code> (macOS).</li>
                <li>On Windows: Download from the <a href="https://www.sqlite.org/download.html" target="_blank">SQLite website</a>.</li>
            </ul>
        </li>
        <li><strong>Python (Optional)</strong>: If using the Python script, ensure Python 3.x is installed.</li>
    </ul>

    <h2>Setup</h2>

    <h3>1. Clone the Repository</h3>
    <p>Clone this repository to your local machine:</p>
    <pre><code>git clone https://github.com/jimmywhoohoo/pagermon_Clearmessges.git
cd pagermon_Clearmessges</code></pre>

    <h3>2. Configure the Script</h3>
    <p>Edit the script (<code>clear_messages.sh</code> or <code>clear_messages.py</code>) to specify the path to your SQLite database file (<code>messages.db</code>).</p>
    <p>For example, in <code>clear_messages.sh</code>:</p>
    <pre><code>DB_PATH="./messages.db"</code></pre>

    <h3>3. Make the Script Executable (Linux/macOS)</h3>
    <p>If using the shell script, make it executable:</p>
    <pre><code>chmod +x clear_messages.sh</code></pre>

    <h2>Usage</h2>

    <h3>Run the Script Manually</h3>
    <p>To clear messages manually, run the script:</p>
    <pre><code>./clear_messages.sh</code></pre>
    <p>or</p>
    <pre><code>python clear_messages.py</code></pre>

    <h3>Schedule the Script</h3>
    <h4>On Linux/macOS (using <code>cron</code>):</h4>
    <ol>
        <li>Open the crontab editor:
            <pre><code>crontab -e</code></pre>
        </li>
        <li>Add the following line to schedule the script to run on the first day of every month at midnight:
            <pre><code>0 0 1 * * /path/to/pagermon_Clearmessges/clear_messages.sh >> /path/to/pagermon_Clearmessges/clear_messages.log 2>&1</code></pre>
        </li>
        <li>Save and exit the editor.</li>
    </ol>

    <h4>On Windows (using Task Scheduler):</h4>
    <ol>
        <li>Open Task Scheduler.</li>
        <li>Create a new task:
            <ul>
                <li>Set the trigger to "Monthly" and choose the day (e.g., the 1st of the month).</li>
                <li>Set the action to run your script (e.g., <code>clear_messages.bat</code> or <code>python clear_messages.py</code>).</li>
            </ul>
        </li>
        <li>Save the task.</li>
    </ol>

    <h2>Optional: Archive Messages</h2>
    <p>If you want to archive messages before clearing them, modify the script to export the data to a CSV file or a separate table.</p>

    <h3>Example: Archive to CSV</h3>
    <p>Add the following lines to your script:</p>
    <pre><code>sqlite3 ./messages.db ".mode csv" ".headers on" ".output messages_archive.csv" "SELECT * FROM messages;"</code></pre>

    <h3>Example: Archive to a New Table</h3>
    <p>Add the following SQL commands to your script:</p>
    <pre><code>CREATE TABLE IF NOT EXISTS messages_archive AS SELECT * FROM messages;</code></pre>

    <h2>Logs</h2>
    <p>If you scheduled the script using <code>cron</code>, logs will be saved to <code>clear_messages.log</code> in the repository directory. Check this file for debugging purposes.</p>

    <h2>Contributing</h2>
    <p>If you'd like to contribute to this project, please fork the repository and submit a pull request. For major changes, open an issue first to discuss your ideas.</p>

    <h2>License</h2>
    <p>This project is licensed under the MIT License. See the <a href="LICENSE">LICENSE</a> file for details.</p>

    <h2>Support</h2>
    <p>If you encounter any issues or have questions, feel free to open an issue on the <a href="https://github.com/jimmywhoohoo/pagermon_Clearmessges/issues" target="_blank">GitHub repository</a>.</p>
</body>
</html>
