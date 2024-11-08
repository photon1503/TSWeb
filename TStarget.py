class TSTarget:
    def __init__(self, Id, name, active, ra, dec, epochcode, rotation, roi, projectid, overrideExposureOrder):
        self.Id = Id
        self.name = name
        self.active = active
        self.ra = ra
        self.dec = dec
        self.epochcode = epochcode
        self.rotation = rotation
        self.coordinates = self.coordinates()
        self.roi = roi
        self.projectid = projectid
        self.overrideExposureOrder = overrideExposureOrder


    def coordinates(self):
        ra = self.ra
        dec = self.dec
        ra_h = int(ra / 15)
        ra_m = int((ra - ra_h * 15) * 4)
        ra_s = int((ra - ra_h * 15 - ra_m / 4) * 240)
        dec_d = int(dec)
        dec_m = int((dec - dec_d) * 60)
        dec_s = int((dec - dec_d - dec_m / 60) * 3600)
        return f'{ra_h:02d}h {ra_m:02d}m {ra_s:02d}s, {dec_d:02d}° {dec_m:02d}\' {dec_s:02d}" J2000'
    
    def __str__(self):
        return f'Target(Id={self.Id}, name={self.name}, active={self.active}, ra={self.ra}, dec={self.dec}, epochcode={self.epochcode}, rotation={self.rotation}, roi={self.roi}, projectid={self.projectid}, overrideExposureOrder={self.overrideExposureOrder})'
