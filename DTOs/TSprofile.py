class TSProfile:
    def __init__(self, Id, profileId, enableGradeRMS, enableGradeStars, enableGradeHFR, maxGradingSampleSize, rmsPixelThreshold, detectedStarsSigmaFactor, hfrSigmaFactor, acceptimprovement, exposurethrottle, parkonwait, enableSmartPlanWindow, enableSynchronization, syncWaitTimeout, syncActionTimeout, syncSolveRotateTimeout, enableMoveRejected, enableGradeFWHM, enableGradeEccentricity, fwhmSigmaFactor, eccentricitySigmaFactor, enableDeleteAcquiredImagesWithTarget, syncEventContainerTimeout):
        self.Id = Id
        self.profileId = profileId
        self.enableGradeRMS = enableGradeRMS
        self.enableGradeStars = enableGradeStars
        self.enableGradeHFR = enableGradeHFR
        self.maxGradingSampleSize = maxGradingSampleSize
        self.rmsPixelThreshold = rmsPixelThreshold
        self.detectedStarsSigmaFactor = detectedStarsSigmaFactor
        self.hfrSigmaFactor = hfrSigmaFactor
        self.acceptimprovement = acceptimprovement
        self.exposurethrottle = exposurethrottle
        self.parkonwait = parkonwait
        self.enableSmartPlanWindow = enableSmartPlanWindow
        self.enableSynchronization = enableSynchronization
        self.syncWaitTimeout = syncWaitTimeout
        self.syncActionTimeout = syncActionTimeout
        self.syncSolveRotateTimeout = syncSolveRotateTimeout
        self.enableMoveRejected = enableMoveRejected
        self.enableGradeFWHM = enableGradeFWHM
        self.enableGradeEccentricity = enableGradeEccentricity
        self.fwhmSigmaFactor = fwhmSigmaFactor
        self.eccentricitySigmaFactor = eccentricitySigmaFactor
        self.enableDeleteAcquiredImagesWithTarget = enableDeleteAcquiredImagesWithTarget
        self.syncEventContainerTimeout = syncEventContainerTimeout
