import csv
import math

# class of vertex containing name, distance, previous vertex, visited status
class Vertex:
    name = ''
    distance = math.inf
    prev = -1
    visited = False

# initilize variables
path = []
d = []
v = []
v_amount = 0
start = -1
end = -1

# print function using recursion
def printBack(i):
    if i == -1:
        return

    # call previous vertex
    printBack(v[i].prev)

    # print current vertex's name
    if i != end:
        print(v[i].name, end=' -> ')
    else:
        print(v[i].name)
    return

# load data from csv
print('Loading CSV..')
with open('/Users/EARTHPYY/Documents/CEProjects/ToC/toc-assignment/ASS4/edgedata.csv', newline='') as f:
    reader = csv.reader(f)
    heading = next(reader)
    v_amount = len(heading)

    # check if vertex amount >= 3
    if v_amount < 3:
        print('Vertex amount is less than 3!')
        quit()
    # load weight into array
    d = [[int(row[i]) for i in range(v_amount)] for row in reader]
    v = [Vertex() for i in range(v_amount)]
    for i in range(v_amount):
        # d.append(next(reader))
        v[i].name = heading[i]

print('CSV loaded!\nFound', v_amount, 'vertices: ', end='')
for i in range(v_amount):
    if i < v_amount - 1:
        print(v[i].name, end=', ')
    else:
        print(v[i].name)

# input start/end vertex
start_name = input('Start vertex: ')
end_name = input('End vertex: ')
# mapping name to index
for i in range(v_amount):
    if v[i].name == start_name:
        start = i
    elif v[i].name == end_name:
        end = i

# check if start/end vertex is correct
if start + end < 0 or start == end:
    print('Start and/or End vertex is incorrect!')
    quit()
print('\nFind shortest path using Dijkstra\'s Algorithm from', v[start].name, 'to', v[end].name, ':')

# first visit is start vertex
active = start
# set first vertex's distance to 0
v[start].distance = 0
# loop until no vertex to visit
while True:
    print('Visiting ', v[active].name, '...', sep='')
    # find active's neighbor vertex
    for i in range(v_amount):
        # check weather it is visited or not & not itself & connected
        if i != active and d[active][i] != 0 and not v[i].visited:
            # sum = active's distance + weight from active to selected neighbor
            sum = v[active].distance + d[active][i]
            print('  Distance from', v[start].name, 'to', v[i].name, 'is', sum, end='')
            # check if new distance is less than known distance
            if sum < v[i].distance:
                print(', less than known distance (', v[i].distance, ') so update it to ', sum, '.', sep='')
                # update selected's distance
                v[i].distance = sum
                # update selected's previous vertex to active
                v[i].prev = active
            else:
                print(', more than known distance (', v[i].distance, ') so keep it.', sep='')
    # set active vertex to visited
    v[active].visited = True

    # find vertex that has minimum distance from start to next iteration
    min_i = -1
    for i in range(v_amount):
        # check weather it is visited or not and must be neighbor of one of visited vertex
        if not v[i].visited and v[i].distance != math.inf and (v[i].distance < v[min_i].distance or min_i == -1):
            min_i = i
    # if found then set it to be next vertex to visit
    if min_i != -1:
        active = min_i
    # if not found then stop visit
    else:
        print('  No vertex to visit anymore.')
        break

# check if end vertex is reachable by check visited status
if not v[end].visited:
    print('End vertex is unreachable!')
    quit()

# print answer
print('\nShortest path from', v[start].name, 'to', v[end].name, 'is\n  ', end='')
printBack(end)
print('with distance from start =', v[end].distance)