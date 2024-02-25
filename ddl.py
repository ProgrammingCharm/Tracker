# File contains Data Definition Language for initial database setup

import sqlite3

conn = sqlite3.connect("tracker.db")
cursor = conn.cursor()

cursor.execute(
	"""
	CREATE TABLE IF NOT EXISTS meetings(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		name TEXT,
		date DATE
	)
	"""

)
cursor.execute(
	"""
	CREATE TABLE IF NOT EXISTS action_items(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		meeting_id INTEGER,
		item TEXT,
		completion TEXT,
		notes TEXT,
		owner TEXT,
		FOREIGN KEY (meeting_id) REFERENCES meeting(id)
	)
	"""
)

conn.commit()
conn.close()




