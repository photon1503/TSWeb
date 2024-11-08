import os
import sqlite3
from flask import Flask, jsonify, render_template, request, redirect, url_for

from TSprofile import *
from TSproject import *
from TStarget import *
from TSexposureplan import *

app = Flask(__name__)

def db():
    return sqlite3.connect('schedulerdb.sqlite')

@app.route('/', methods=['GET', 'POST'])
def index():
    # Connect to the SQLite database
    conn = db()
    c = conn.cursor()

    # Fetch data from the database
    c.execute("SELECT * FROM profilepreference");
    profiles = [TSProfile(*row) for row in c.fetchall()]

    c.execute("SELECT * FROM project ")
    projects = [TSProject(*row) for row in c.fetchall()]

    c.execute("SELECT * from target")
    targets = [TSTarget(*row) for row in c.fetchall()]
  
    conn.close()

    return render_template('index.html', projects=projects, profiles=profiles, targets=targets)

@app.route('/target/<int:target_id>', methods=['GET'])
def get_target_details(target_id):
    conn = db()
    c = conn.cursor()

    # Fetch target details
    c.execute("SELECT * FROM target WHERE id = ?", (target_id,))
    target_row = c.fetchone()
    target = TSTarget(*target_row) if target_row else None

    # Fetch exposure plans
    c.execute("SELECT * FROM exposureplan WHERE targetid = ?", (target.Id,))
    exposure_plan_rows = c.fetchall()
    exposure_plans = [TSExposurePlan(*row) for row in exposure_plan_rows]


    conn.close()

    return {
        'target': target.__dict__,
        'exposurePlans': [plan.__dict__ for plan in exposure_plans]
    }

@app.route('/project/<int:project_id>', methods=['GET'])
def get_project_details(project_id):
    conn = db()
    c = conn.cursor()

    # Fetch project details
    c.execute("SELECT * FROM project WHERE id = ?", (project_id,))
    project_row = c.fetchone()
    project = TSProject(*project_row) if project_row else None

    conn.close()

    return {
        'project': project.__dict__
    }

@app.route('/toggle-target-enabled/<int:target_id>', methods=['POST'])
def toggle_target_enabled(target_id):
    data = request.get_json()
    new_status = data['enabled']

    conn = db()
    c = conn.cursor()
    c.execute("UPDATE target SET active = ? WHERE Id = ?", (new_status, target_id))
    conn.commit()
    conn.close()

    return jsonify(success=True)

if __name__ == '__main__':
    app.run(debug=True)