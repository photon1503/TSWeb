from astropy.coordinates import SkyCoord
from astropy import units as u

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
        coord = SkyCoord(ra=self.ra * u.hour, dec=self.dec * u.degree, frame='icrs')
        ra_hms = coord.ra.hms
        dec_dms = coord.dec.dms
        return f'{int(ra_hms.h):02d}h {int(ra_hms.m):02d}m {ra_hms.s:05.2f}s, {int(dec_dms.d):02d}° {abs(int(dec_dms.m)):02d}\' {abs(dec_dms.s):04.1f}" J2000'

    
    def __str__(self):
        return f'Target(Id={self.Id}, name={self.name}, active={self.active}, ra={self.ra}, dec={self.dec}, epochcode={self.epochcode}, rotation={self.rotation}, roi={self.roi}, projectid={self.projectid}, overrideExposureOrder={self.overrideExposureOrder})'
