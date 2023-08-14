1. Introduction
This documentation provides instructions for generating an XML product feed from a given SQLite database of products, adhering to the Google Merchant product data specifications. The implementation uses Python and the SQLite database.

3. Setup
Prerequisites 
Python (recommended version 3.6+)
SQLite database file (download link provided in the task)

Downloading the Database
Click on the following link to download the SQLite database: data.sqlite
Save the downloaded file as data.sqlite in the same directory as the script.

3. Running the code
Clone or download the project repository from GitHub: https://github.com/hedizita/SIBPTC/tree/main 

4. Github repository
You can see several Python files besides the downloaded sqlite file, README.md and .gitignore. I also created SQL files throughout the process: data.sqbpro, db.mssql.

The files nn.py and nn2.py are previous test files for creating the base, you do not need to run these since there will be several errors.

The base.py file is the one that creates the feed.xml given in the task.

