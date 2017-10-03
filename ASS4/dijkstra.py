import csv
from collections import namedtuple

Point = namedtuple('Point', ['name', 'distance', 'prev'])
tab = []
vertex = []

# load csv into 2d array
print('Loading CSV..')
with open('/Users/EARTHPYY/Documents/CEProjects/ToC/toc-assignment/ASS4/edgedata.csv', newline='') as f:
    reader = csv.reader(f)
    heading = next(reader)
    for i in range(len(heading)):
        tab.append(next(reader))
        vertex.append(Point(heading[i], -1, -1))
print('CSV loaded!')
print('Found', len(heading), 'vertices:', heading)
# start = 