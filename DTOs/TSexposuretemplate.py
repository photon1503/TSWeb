class TSExposureTemplate:
    def __init__(self, Id, profileId, name, filtername, gain, offset, bin, readoutmode, twilightlevel, moonavoidanceenabled, moonavoidanceseparation, moonavoidancewidth, maximumhumidity, defaultexposure, moonrelaxscale, moonrelaxmaxaltitude, moonrelaxminaltitude, moondownenabled):
        self.Id = Id
        self.profileId = profileId
        self.name = name
        self.filtername = filtername
        self.gain = gain
        self.offset = offset
        self.bin = bin
        self.readoutmode = readoutmode
        self.twilightlevel = twilightlevel
        self.moonavoidanceenabled = moonavoidanceenabled
        self.moonavoidanceseparation = moonavoidanceseparation
        self.moonavoidancewidth = moonavoidancewidth
        self.maximumhumidity = maximumhumidity
        self.defaultexposure = defaultexposure
        self.moonrelaxscale = moonrelaxscale
        self.moonrelaxmaxaltitude = moonrelaxmaxaltitude
        self.moonrelaxminaltitude = moonrelaxminaltitude
        self.moondownenabled = moondownenabled

    def __str__(self):
        return f'FilterProfile(Id={self.Id}, profileId={self.profileId}, name={self.name}, filtername={self.filtername}, gain={self.gain}, offset={self.offset}, bin={self.bin}, readoutmode={self.readoutmode}, twilightlevel={self.twilightlevel}, moonavoidanceenabled={self.moonavoidanceenabled}, moonavoidanceseparation={self.moonavoidanceseparation}, moonavoidancewidth={self.moonavoidancewidth}, maximumhumidity={self.maximumhumidity}, defaultexposure={self.defaultexposure}, moonrelaxscale={self.moonrelaxscale}, moonrelaxmaxaltitude={self.moonrelaxmaxaltitude}, moonrelaxminaltitude={self.moonrelaxminaltitude}, moondownenabled={self.moondownenabled})'
