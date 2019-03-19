import argparse
import csv
import numpy as np
import math

PREFIX = 'ITEM:'
TIMESTEP = 'TIMESTEP'
ATOMS = 'ATOMS'
SIZE = 'NUMBER'
BOX_BOUNDS = 'BOX'

# parse command line
parser = argparse.ArgumentParser()
parser.add_argument("input1", help="the name of input file 1")
parser.add_argument("input2", help="the name of input file 2")
parser.add_argument("-o", "--output", default="msd.txt", help="the name of output file")
args = parser.parse_args()

# open file
file1 = open(args.input1)  # "./4-db-msd-cu.lammpstrj"
file2 = open(args.input2)  # "./4-db-msd-db.lammpstrj")
result = open(args.output, "w")
result.write("timestep distance_A_B\n")
file1 = csv.reader(file1, delimiter=' ', skipinitialspace=True)
file2 = csv.reader(file2, delimiter=' ', skipinitialspace=True)

# read file to list
read1 = []
read2 = []
for line in file1:
    read1.append(line)
for line in file2:
    read2.append(line)

file1 = read1
file2 = read2

index1 = 0
index2 = 0
timestep = 1

# calculate the centers of the atoms of file1 and file2 in one time step
# and then calculate their distance
while index1 < len(file1) and index2 < len(file2):

    # find the begin index of the atoms of file1 in one time step
    while len(file1[index1]) < 2 or file1[index1][1] != ATOMS:
        index1 += 1

    # find the boundary of these atoms
    index1 += 1
    max_coordinate = np.array([float('-inf'), float('-inf'), float('-inf')])
    min_coordinate = np.array([float('inf'), float('inf'), float('inf')])
    while index1 < len(file1) and file1[index1][0] != PREFIX:
        for i in range(3):
            max_coordinate[i] = max(max_coordinate[i], float(file1[index1][i + 2]))
            min_coordinate[i] = min(min_coordinate[i], float(file1[index1][i + 2]))
        index1 += 1

    # get center1
    center1 = (max_coordinate + min_coordinate) / 2

    # find the begin index of the atoms of file2
    while len(file2[index2]) < 2 or file2[index2][1] != ATOMS:
        index2 += 1

    # find the boundary of these atoms
    index2 += 1
    max_coordinate = np.array([float('-inf'), float('-inf'), float('-inf')])
    min_coordinate = np.array([float('inf'), float('inf'), float('inf')])
    while index2 < len(file2) and file2[index2][0] != PREFIX:
        for i in range(3):
            max_coordinate[i] = max(max_coordinate[i], float(file2[index2][i + 2]))
            min_coordinate[i] = min(min_coordinate[i], float(file2[index2][i + 2]))
        index2 += 1

    # get center2
    center2 = (max_coordinate + min_coordinate) / 2

    # calculate distance
    dis = (center1 - center2) * (center1 - center2)
    dis = math.sqrt(sum(dis))
    result.write("{} {}\n".format(timestep, dis))
    timestep += 1

print("result has been successfully written to {}".format(args.output))
result.close()
