#!/bin/bash
#!/usr/bin/python

source inputFile.sh
# exit

#--------------------------------------------------------------------------------#
# Create the output boundary data file directory called "boundaryData".
mkdir -p $fLoc/boundaryData
cd $fLoc/boundaryData

# Within that directory, create a boundary condition specific directory.
mkdir -p $boundaryNameNew
cd $boundaryNameNew

# Make a list of times in which patches were sampled.
ls $fLoc/boundaryDataPre > timeList
lim=`wc -l timeList | awk '{print $1}'`;
lim=0 # first 1 seconds

echo 'Total samples' $lim
declare -i startindex
startindex=1;

# Loop over the various times and process the data.
for ((index = $startindex; index <$lim; index = index+1)); #$lim
do   # get the time for this index.
   time=`awk -v var=$index '{if (NR==var) {print}}' timeList`;
   echo "Time" $time"..."

 # process the points file.
   if [[ index -eq $startindex ]]
   then
       # for cell interpolation scheme (face centers)
       cp $fLoc/boundaryDataPre/$boundaryNameOld/faceCentres ./pointCoordinates

       #---- call the points file processing python script-----# pointCentroides = points
       python $scriptLoc/points.py pointCoordinates pointIndex points $xmin $xmax $ymin $ymax $zmin $zmax $xOff $yOff $zOff
       rm pointCoordinates
   fi

   # make the time directory and process the flow variable data. Note, that this
   # is set up to process U, p_rgh, T, nuLES, and kappaLES. Add more variables as desired.
   mkdir -p $time
   cd $time
   cp $fLoc/boundaryDataPre/$time/$boundaryNameOld/vectorField/U ./UPre

#    cp $fLoc/boundaryDataPre/$time/$boundaryNameOld/scalarField/p ./pPre
#    cp $fLoc/boundaryDataPre/$time/$boundaryNameOld/scalarField/flm ./flmPre
#    cp $fLoc/boundaryDataPre/$time/$boundaryNameOld/scalarField/fmm ./fmmPre

   #--call the data file processing python script-------------------------------------------#
   #-------------------------------------indexFile
   python $scriptLoc/data.py UPre    U   ../pointIndex

#    python $scriptLoc/data.py pPre    p   ../pointIndex
#    python $scriptLoc/data.py flmPre  flm   ../pointIndex
#    python $scriptLoc/data.py fmmPre  fmm   ../pointIndex

   rm *Pre

   cd ../
done
# rm timeList
# rm index
# rm
