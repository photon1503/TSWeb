class TSProject:
    def __init__(self, Id, profileId, name, description, state, priority, createdate, activedate, inactivedate, minimumtime, minimumaltitude, usecustomhorizon, horizonoffset, meridianwindow, filterswitchfrequency, ditherevery, enablegrader, isMosaic, flatsHandling):
        self.Id = Id
        self.profileId = profileId
        self.name = name
        self.description = description
        self.state = state
        self.priority = priority
        self.createdate = createdate
        self.activedate = activedate
        self.inactivedate = inactivedate
        self.minimumtime = minimumtime
        self.minimumaltitude = minimumaltitude
        self.usecustomhorizon = usecustomhorizon
        self.horizonoffset = horizonoffset
        self.meridianwindow = meridianwindow
        self.filterswitchfrequency = filterswitchfrequency
        self.ditherevery = ditherevery
        self.enablegrader = enablegrader
        self.isMosaic = isMosaic
        self.flatsHandling = flatsHandling

    def __str__(self):
        return f'Project(Id={self.Id}, profileId={self.profileId}, name={self.name}, description={self.description}, state={self.state}, priority={self.priority}, createdate={self.createdate}, activedate={self.activedate}, inactivedate={self.inactivedate}, minimumtime={self.minimumtime}, minimumaltitude={self.minimumaltitude}, usecustomhorizon={self.usecustomhorizon}, horizonoffset={self.horizonoffset}, meridianwindow={self.meridianwindow}, filterswitchfrequency={self.filterswitchfrequency}, ditherevery={self.ditherevery}, enablegrader={self.enablegrader}, isMosaic={self.isMosaic}, flatsHandling={self.flatsHandling})'
