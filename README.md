# Tracker
Tracker is a productivity tool for keeping track of action items and meetings. This is a simple web application that uses a development server on your local machine where you can insert entries (action items and meetings data). 

# Steps for Running on Local Machine
1. Download the files from the main branch (ddl.py, dml.py, app.py) in a folder on your local machine. Then download the file from the branch called "templates" index.html onto your local machine. Create another folder in that folder called templates and place the index.html within. 

Your file tree should like this:
tracker (main folder) -> ddl.py -> dml.py -> app.py -> templates (folder inside folder) -> index.html

2. Open a terminal window and move to this directory: 
cd /Desktop/projects/tracker/ 

3. Check to see all files were added correctly by running the command to list the files/folder within current directory: ls

4. You now need to set up the database, this is done by first running the file ddl.py through the python interpreter. But first, we need to ensure that python is in fact on your local machine. To download python on your local machine, you can go to the main python website and download the latest version:
https://www.python.org/downloads/release/python-3122/

5. Once that is done: You now need to set up the database.

6. Run python3 (or python) within the terminal session to set up the existing database: 

python3 ddl.py 

This should effectively setup a database on-disk, meaning it will be stored on your local machine either on your SSD or HDD. Within the ddl.py file that you just ran, there is a connection object that creates a new database on-disk called "tracker.db", you should see this be added to your current folder as "tracker.db". 

You can check to make sure this was created by entering the sqlite command line interface. Sqlite is the technology that is used to set up a database on-disk so you can use tracker productivity tool on your local machine. Run the following into the terminal:

sqlite3 tracker.db 

sqlite3 opens the sqlite command line interface and tracker.db is the name of the database that was created on-disk. Once within, you can view the schema setup to see what tables were created and the different files within: 

.schema 
.table 
.quit 

And you can exit with .quit which smoothly exits out of this command line interface. This shows you a little of what is going on behind-the-scenes. You can come back to this command-line interface to view the actual entries you make once you have set up the development server (and thus, the user interface of the application).

7. Once you have confirmed the database is actually setup by visting the command line interface of sqlite, you are ready to run the app.py file in your local machine: 

Download the Flask application package in your terminal session: 

pip install Flask 

Then go ahead and run the python3 command on the app.py file: 
python3 app.py 

This should spit out a lot of lines of information confirming that a flask application is being setup with it resulting in a message saying that the web application is live at http://127.0.0.1:5000/ where you can copy into a search engine's browser.

At this point, you can visit the url provided by the terminal and see the Tracker productivity tool! Currently, this tool allows you to add a meeting, and then add an action item associated with that meeting. Later on, it will have the ability to view action items by meeting and user. For now, to view your actual entries. You can go back to the command-line interface of sqlite3 and read from the database using the following commands:

SELECT * FROM meetings;

This will present all entries and all associated data with the entries added.

SELECT * FROM action_items;

This will present all entries and all associated data with the entries for action items added. 

        
