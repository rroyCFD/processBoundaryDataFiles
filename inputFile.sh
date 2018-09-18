# Input variables

# directories
scriptLoc="/media/rroy/Disk2/WIND-Project/BolundHill/BoundaryDataProcessingScripts/processBoundaryDataFiles"
fLoc="/home/rroy/OpenFOAM/rroy-2.1.x/run/periodicChannelFlow/3D-LES/Re-590/128x64x128/pisoChannelFoamMod/cyclic/postProcessing/"

# Name of the boundaries to process.
boundaryNameOld="inout_left"
boundaryNameNew="inout_left"

# source plane bound:
xmin=-1
xmax=1
ymin=0
ymax=2
zmin=0.0
zmax=3.15

# linear offset from source plane to target patch
xOff=-6.28
yOff=0
zOff=0
