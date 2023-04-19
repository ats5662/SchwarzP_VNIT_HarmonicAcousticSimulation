# trace generated using paraview version 5.11.0-465-g6568ba93f5
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 11

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'openCFS HDF5 reader'
inputDeckcfs = openCFSHDF5reader(registrationName='InputDeck.cfs', FileName=r"C:\Users\19139\Desktop\InputDeck.cfs")
inputDeckcfs.Regions = ['element set 1', 'node set 1', 'node set 2']

# get animation scene
animationScene1 = GetAnimationScene()

# get the time-keeper
timeKeeper1 = GetTimeKeeper()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# Properties modified on inputDeckcfs
inputDeckcfs.Regions = ['element set 1']

UpdatePipeline(time=377.0, proxy=inputDeckcfs)

# create a new 'Plot Over Line'
plotOverLine1 = PlotOverLine(registrationName='PlotOverLine1', Input=inputDeckcfs)
plotOverLine1.Point1 = [0.0, 0.0, 0.0023756627924740314]
plotOverLine1.Point2 = [0.02540000155568123, 0.02540004812180996, 0.3665125072002411]

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=plotOverLine1)

# Properties modified on plotOverLine1
plotOverLine1.Resolution = 10000
plotOverLine1.Point1 = [0.0, 0.0, 0.366513]
plotOverLine1.Point2 = [0.0, 0.0, 0.0365125]

UpdatePipeline(time=377.0, proxy=plotOverLine1)

# set active source
SetActiveSource(plotOverLine1)

UpdatePipeline(time=377.0, proxy=plotOverLine1)

# Properties modified on plotOverLine1
plotOverLine1.Point1 = [1e-05, 1e-05, 0.366513]
plotOverLine1.Point2 = [1e-05, 1e-05, 0.0365125]

# Properties modified on plotOverLine1
plotOverLine1.Point1 = [0.001, 0.001, 0.366513]
plotOverLine1.Point2 = [0.001, 0.001, 0.0365125]

UpdatePipeline(time=377.0, proxy=plotOverLine1)

# create extractor
cSV1 = CreateExtractor('CSV', plotOverLine1, registrationName='CSV1')
# trace defaults for the extractor.
cSV1.Trigger = 'TimeValue'

# Properties modified on cSV1.Writer
cSV1.Writer.Precision = 7
cSV1.Writer.AddTimeStep = 1
cSV1.Writer.AddTime = 1

# save extracts
SaveExtracts(ExtractsOutputDirectory='//wsl.localhost/Ubuntu-22.04/home/ats5662/SchwarzP_VNIT_HarmonicAcousticSimulation/coupledPressureThermoviscousAcoustics/results_hdf5/centerlineSample',
    GenerateCinemaSpecification=0,
    AnimationScene=animationScene1,
    FrameRate=1,
    FrameStride=1,
    FrameWindow=[0, 149])