# Hashcode 2021
# Team Depresso
# Problem  - Traffic Signaling

## Data Containers

class Street:

    def __init__(self, start, end, name, L):
        self.start = start
        self.end = end
        self.name = name
        self.time = L

    def show(self):
        print(self.start, self.end, self.name, self.time)


class Car:

    def __init__(self, P, path):
        self.P = P  # the number of streets that the car wants to travel
        self.path = path  # names of the streets
        # the car starts at the end of first street

    def show(self):
        print(self.P, self.path)


# Just getting data
with open('b.txt') as f:
    D, I, S, V, F = list(map(int, f.readline()[:-1].split(" ")))
    '''
    l1 = f.readline()[:-1].split(' ')
    D = int(l1[0]) # Duration of simulation 1 <D<10^4
    I = int(l1[1]) # The number of intersections 2 ≤ I ≤ 10^5
    S = int(l1[2]) # The number of streets 2 ≤ S ≤ 10 5
    V = int(l1[3]) # The number of cars 1 ≤ V ≤ 10 3
    F = int(l1[4]) # The bonus points for each car that reaches
              # its destination before time D1 ≤ F ≤ 10 3
    '''
    # B, E, streets_descriptions = [], [], []
    streets = [0] * S
    for i in range(S):
        line = f.readline()[:-1].split(' ')
        street = Street(int(line[0]), int(line[1]), line[2], int(line[3]))
        streets[i] = street
        #street.show()

    cars = [0] * V
    for i in range(V):
        line = f.readline()[:-1].split(' ')
        car = Car(int(line[0]), line[1:])

        cars[i] = car
        #car.show()

roads_used = set()
for car in cars:
  roads_used |= set(car.path)

streets_copy = []
for s in range(len(streets)):
  if streets[s].name in roads_used:
    streets_copy.append(streets[s])

#print(roads_used)
#print(len(streets_copy))
    # Get Junctions
with open("b-naive.txt", 'w+') as f:
    f.write('\n')
    numOfSchedules = 0
    for i in range(I):
        strIn = []
        for s in range(len(streets_copy)):
            if streets_copy[s].end == i:
                strIn.append(streets_copy[s])
        if len(strIn) != 0:
            numOfSchedules += 1
            f.write(str(i) + '\n')
            f.write(str(len(strIn)) + '\n')
            time = 2
            for street in strIn:
                f.write(street.name + ' ' + str(time) + '\n')
    print(numOfSchedules)


