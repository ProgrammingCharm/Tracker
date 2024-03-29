# app.py

from first_try_dml import add_meeting, add_action_item, get_all_meetings, get_all_users

from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__, template_folder="templates")

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		# Check if the form is for adding a meeting
		if 'name' in request.form and 'date' in request.form:
			name = request.form['name']
			date = request.form['date']
			add_meeting(name, date)
		# Check if the form is for adding an action item
		elif 'meeting_id' in request.form and 'item' in request.form and 'completion' in request.form and 'owner' in request.form:
			meeting_id = request.form['meeting_id']
			item = request.form['item']
			completion = request.form['notes']
			notes = request.form['notes']
			owner = request.form['owner']
			add_action_item(meeting_id, item, completion, notes, owner)

	meetings = get_all_meetings()
	users = get_all_users()
	return render_template('index.html', meetings=meetings, users=users)

if __name__ == '__main__':
	app.run(debug=True)


