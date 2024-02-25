# Allows for database operations to occur: adding a meeting entry into the database, adding an action item. 

import sqlite3

def add_meeting(name, date):
	conn = sqlite3.connect("tracker.db")
	cursor = conn.cursor()
	cursor.execute(
		"""
		INSERT INTO meetings (name, date) VALUES (?, ?)
		""",
		(name, date)
	)
	conn.commit()
	conn.close()


def add_action_item(meeting_id, item, completion, notes, owner):
	conn = sqlite3.connect("tracker.db")
	cursor = conn.cursor()
	cursor.execute(
		"""
		INSERT INTO action_items (meeting_id, item, completion, notes, owner) VALUES (?, ?, ?, ?, ?)
		""",
		(meeting_id, item, completion, notes, owner)
	)
	conn.commit()
	conn.close()

def get_action_items_by_meeting(meeting_name):
	conn = sqlite3.connect("tracker.db")
	cursor = conn.cursor()
	cursor.execute(
		"""
		SELECT action_items.item, action_items.completion, action_items.notes FROM action_items
		INNER JOIN meetings ON meetings.id = action_items.meeting_id 
		WHERE meetings.name = ?
		ORDER BY action_items.completion, meetings.date, action_items.owner, action_items.notes
		""",
		(meeting_name,)
		)
	action_items = cursor.fetchall()
	conn.close()
	return action_items

def get_action_items_by_user(user):
	conn = sqlite3.connect("tracker.db")
	cursor = conn.cursor()
	cursor.execute(
		"""
		SELECT action_items.item, action_items.completion, meetings.date, action_items.notes FROM action_items
		INNER JOIN meetings ON meetings.id = action_items.meeting_id 
		WHERE action_items.owner = ?
		ORDER BY action_items.completion, meetings.date, action_items.notes
		""",
		(user,)
		)
	action_items = cursor.fetchall()
	conn.close()
	return action_items

def get_all_meetings():
	conn = sqlite3.connect("tracker.db")
	cursor = conn.cursor()
	cursor.execute("SELECT name FROM meetings")
	meetings = cursor.fetchall()
	conn.close()
	return meetings

def get_all_users():
	conn = sqlite3.connect("tracker.db")
	cursor = conn.cursor()
	cursor.execute("SELECT DISTINCT owner FROM action_items")
	users = cursor.fetchall()
	conn.close()
	return users
