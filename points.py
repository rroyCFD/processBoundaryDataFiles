#!/usr/bin/python
# -*- coding: utf-8 -*-

# This script reads in the points and faces files created by OpenFOAM's sample
# patch function object and creates a points file needed by the
# timeVaryingFixedMapped boundary condition
#
# Usage:  ./points.py [verticesFileName] [facesFileName] [newCentroidsFileName] [newIndicesFileName] [xMin xMax yMin yMax zMin zMax]
# User input
import sys, math
print( 'sys = ',sys.argv)

i = 1;
vertexFile = sys.argv[i]; i += 1;
indexFile = sys.argv[i]; i += 1;
centroidFile = sys.argv[i]; i += 1;

xMin = float(sys.argv[i]); i += 1;
xMax = float(sys.argv[i]); i += 1;
yMin = float(sys.argv[i]); i += 1;
yMax = float(sys.argv[i]); i += 1;
zMin = float(sys.argv[i]); i += 1;
zMax = float(sys.argv[i]); i += 1;

xOff = float(sys.argv[i]); i += 1;
yOff = float(sys.argv[i]); i += 1;
zOff = float(sys.argv[i]); i += 1;

# Open the boundary faces vertices file.
fid = open(vertexFile,'r')

# Find the number of vertices.
nVertices = '\n'
while nVertices == '\n':
    nVertices = fid.readline()

nVertices = int(nVertices)
print('nVertices',nVertices)

dataCentroid = []
# Read in vertices.
xVertex = []
yVertex = []
zVertex = []
fid.readline()
for i in range(nVertices):
    data = fid.readline()
    data = data.lstrip('(')
    data = data.rstrip(')\n')
    data = data.split()
    xVertex.append(float(data[0]))
    yVertex.append(float(data[1]))
    zVertex.append(float(data[2]))
    dataCentroid.append([xVertex[i],yVertex[i],zVertex[i],i])
# Close the vertices file.
fid.close()

# Now, get rid of locations outside of the range of interest.
j = 0
dataCentroidNew = []
for i in range(nVertices):
    if (dataCentroid[i][0] >= xMin and dataCentroid[i][0] <= xMax and
        dataCentroid[i][1] >= yMin and dataCentroid[i][1] <= yMax and
        dataCentroid[i][2] >= zMin and dataCentroid[i][2] <= zMax):
        dataCentroidNew.append(dataCentroid[i])
        j = j+1
nFaces = j
print('nFaces within the range: ',nFaces)
#--------------------------------------------------------------------------------------------------#

#-------------------------------------------------------------------------------------------#
print("Writing index list for use in ordering/reordering flow variable files")
fid = open(indexFile,'w')
fid.write(str(nFaces))
fid.write('\n')
fid.write('(\n')
for i in range(nFaces):
   fid.write('{0}\n'.format(str(dataCentroidNew[i][3])))

fid.write(')')
fid.close()

#--------------------------------------------------------------------------------------------------#
# Write new points data to file
f = int(0)
fid = open(centroidFile,'w')
fid.write('/*--------------------------------*- C++ -*----------------------------------*\\\n')
fid.write('| =========                 |                                                 |\n')
fid.write('| \\\\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |\n')
fid.write('|  \\\\    /   O peration     | Version:  2.1                                   |\n')
fid.write('|   \\\\  /    A nd           | Web:      http://www.OpenFOAM.org               |\n')
fid.write('|    \\\\/     M anipulation  |                                                 |\n')
fid.write('\*---------------------------------------------------------------------------*/\n')
fid.write('FoamFile\n')
fid.write('{\n')
fid.write('    version     2.0;\n')
fid.write('    format      ascii;\n')
fid.write('    class       vectorField;\n')
fid.write('    object      points;\n')
fid.write('}\n')
fid.write('// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //\n\n')
fid.write('\n\n\n\n')
# number of coraseMeash face centers + new log-extrapolated points for finemesh
fid.write(str(nFaces))
fid.write('\n')
fid.write('(\n')
for i in range(nFaces):
    fid.write('({0} {1} {2})\n'.format( str(dataCentroidNew[i][0] + xOff),
	                                      str(dataCentroidNew[i][1] + yOff),
				                                str(dataCentroidNew[i][2] + zOff))
                                      );
fid.write(')')
fid.close()

#-------------------------------------------------------------------------------------------#
#Print out information to the screen.
print( '\nNumber of vertices on source = ', nVertices)
print( 'Number of vertices for target = ', nFaces)
print( 'x_min = ',xMin)
print( 'x_max = ',xMax)
print( 'y_min = ',yMin)
print( 'y_max = ',yMax)
print( 'z_min = ',zMin)
print( 'z_max = ',zMax)