class TSExposurePlan:
    def __init__(self, Id, profileId, exposure, desired, acquired, accepted, targetid, exposureTemplateId):
        self.Id = Id
        self.profileId = profileId
        self.exposure = exposure
        self.desired = desired
        self.acquired = acquired
        self.accepted = accepted
        self.targetid = targetid
        self.exposureTemplateId = exposureTemplateId

    def __str__(self):
        return f'ExposurePlan(Id={self.Id}, profileId={self.profileId}, exposure={self.exposure}, desired={self.desired}, acquired={self.acquired}, accepted={self.accepted}, targetid={self.targetid}, exposureTemplateId={self.exposureTemplateId})'
