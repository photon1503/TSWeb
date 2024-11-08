import os
import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # Connect to the SQLite database
    conn = sqlite3.connect('schedulerdb.sqlite')
    c = conn.cursor()

    # Fetch data from the database
    c.execute("SELECT * FROM profilepreference");
    profiles = c.fetchall()

    c.execute("SELECT * FROM project ")
    projects = c.fetchall()

    c.execute("SELECT * from target")
    targets = c.fetchall()  
    conn.close()

    return render_template('index.html', projects=projects, profiles=profiles, targets=targets)

if __name__ == '__main__':
    app.run(debug=True)