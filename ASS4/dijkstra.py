import csv
import math

class Point:
    name = ""
    distance = math.inf
    prev = -1
    visited = False

path = []
d = []
v = []
v_amount = 0
start = -1
end = -1

def printBack(i):
    if i == -1:
        return
    printBack(v[i].prev)

    if i != end:
        print(v[i].name, end=' -> ')
    else:
        print(v[i].name)
    return

# load csv into 2d array
print('Loading CSV..')
with open('/Users/EARTHPYY/Documents/CEProjects/ToC/toc-assignment/ASS4/edgedata.csv', newline='') as f:
    reader = csv.reader(f)
    heading = next(reader)
    v_amount = len(heading)

    if v_amount < 3:
        print('Vertex amount is less than 3!')
        quit()

    d = [[int(row[i]) for i in range(v_amount)] for row in reader]
    v = [Point() for i in range(v_amount)]
    for i in range(v_amount):
        # d.append(next(reader))
        v[i].name = heading[i]
print('CSV loaded!\nFound', v_amount, 'vertices: ', end='')
for i in range(v_amount):
    if i < v_amount - 1:
        print(v[i].name, end=', ')
    else:
        print(v[i].name)

start_name = input('Start vertex: ')
end_name = input('End vertex: ')

for i in range(v_amount):
    if v[i].name == start_name:
        start = i
    elif v[i].name == end_name:
        end = i

if start + end < 0 or start == end:
    print('Start and/or End vertex is incorrect!')
    quit()
print('\nFind shortest path using Dijkstra\'s Algorithm from', v[start].name, 'to', v[end].name, ':')

active = start
v[start].distance = 0
while True:
    print('Visiting ', v[active].name, '...', sep='')
    for i in range(v_amount):
        if i != active and d[active][i] != 0 and not v[i].visited:
            sum = v[active].distance + d[active][i]
            print('  Distance from', v[start].name, 'to', v[i].name, 'is', sum, end='')
            if sum < v[i].distance:
                print(', less than known distance (', v[i].distance, ') so update it to ', sum, '.', sep='')
                v[i].distance = sum
                v[i].prev = active
            else:
                print(', more than known distance (', v[i].distance, ') so keep it.', sep='')
    v[active].visited = True

    min_i = -1
    for i in range(v_amount):
        if not v[i].visited and v[i].distance != math.inf and (v[i].distance < v[min_i].distance or min_i == -1):
            min_i = i
    
    if min_i != -1:
        active = min_i
    else:
        print('  No vertex to visit anymore.')
        break

if not v[end].visited:
    print('End vertex is unreachable!')
    quit()

print('\nShortest path from', v[start].name, 'to', v[end].name, 'is\n  ', end='')
printBack(end)
print('with distance from', v[start].name, '=', v[end].distance)