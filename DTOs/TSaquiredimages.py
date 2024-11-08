class AquiredImage:
    def __init__(self, Id, projectId, targetId, acquireddate, filtername, accepted, metadata, rejectreason, profileId):
        self.Id = Id
        self.projectId = projectId
        self.targetId = targetId
        self.acquireddate = acquireddate
        self.filtername = filtername
        self.accepted = accepted
        self.metadata = metadata
        self.rejectreason = rejectreason
        self.profileId = profileId

    def __str__(self):
        return (f'Exposure(Id={self.Id}, projectId={self.projectId}, targetId={self.targetId}, '
                f'acquireddate={self.acquireddate}, filtername={self.filtername}, accepted={self.accepted}, '
                f'metadata={self.metadata}, rejectreason={self.rejectreason}, profileId={self.profileId})')
