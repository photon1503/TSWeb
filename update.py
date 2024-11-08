    if request.method == 'POST':
        # Handle form submission to update project data
        id = request.form['id']
        profileId = request.form['profileId']
        name = request.form['name']
        description = request.form['description']
        state = request.form['state']
        priority = request.form['priority']
        createdate = request.form['createdate']
        activedate = request.form['activedate']
        inactivedate = request.form['inactivedate']
        minimumtime = request.form['minimumtime']
        minimumaltitude = request.form['minimumaltitude']
        usecustomhorizon = 'usecustomhorizon' in request.form
        horizonoffset = request.form['horizonoffset']
        meridianwindow = request.form['meridianwindow']
        filterswitchfrequency = request.form['filterswitchfrequency']
        ditherevery = request.form['ditherevery']
        enablegrader = 'enablegrader' in request.form
        isMosaic = 'isMosaic' in request.form
        flatsHandling = request.form['flatsHandling']

        c.execute("UPDATE project SET profileId = ?, name = ?, description = ?, state = ?, priority = ?, createdate = ?, activedate = ?, inactivedate = ?, minimumtime = ?, minimumaltitude = ?, usecustomhorizon = ?, horizonoffset = ?, meridianwindow = ?, filterswitchfrequency = ?, ditherevery = ?, enablegrader = ?, isMosaic = ?, flatsHandling = ? WHERE Id = ?",
                 (profileId, name, description, state, priority, createdate, activedate, inactivedate, minimumtime, minimumaltitude, usecustomhorizon, horizonoffset, meridianwindow, filterswitchfrequency, ditherevery, enablegrader, isMosaic, flatsHandling, id))
        conn.commit()
        return redirect(url_for('index'))