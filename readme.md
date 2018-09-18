### Script to convert output of OpenFOAM sample patch/plane function-objects to file format needed by the timeVaryingFixedMapped boundary condition.

### A typical source directory name is *boundaryDataPre* and target directory is *boundaryData*. Requires bash shell and python3  for script execution

### Script inputs are as follows:

* ### file-name *inputFile*
* #### scriptLoc="location of this bash & python scripts"
* #### fLoc="surface sample location"
* #### boundaryNameOld="source sample plane/patch name"
* #### boundaryNameNew="target patch name"


> xmin=-1.0
> 
> xmax=1.0
> 
> ymin=0.0
> 
> ymax=1.0
> 
> zmin=0.0
> 
> zmax=1.0

### provide plane offset vector from source-plane to target-plane
> xOff=0
> 
> yOff=0
>
>zOff=0
