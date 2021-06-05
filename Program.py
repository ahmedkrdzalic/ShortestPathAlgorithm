import csv


# Ths function runs through whole info_list to see if there is any not visited node
def are_visited():
    for node in info_list:
        if node[3] == False:
            return False


# Finds and selects vertex with shortest known path at the time that is not visited
def find_current_vertex():
    sml_val = float('inf')
    CURRENT = None
    for node in info_list:
        if (node[3] == False and (node[1] < sml_val or node[1] == 0)):
            sml_val = node[1]
            CURRENT = node[0]
    #---In case that node is not connected it will skip it---
    if CURRENT == None:
        for node in info_list:
            if (node[3] == False):
                CURRENT = node[0]
                break
    #--------------------------------------------------------
    return CURRENT


def dijkstra():
    CURRENT = find_current_vertex()
    for i, neighbor in enumerate(adjMTX[CURRENT-1]):
        if neighbor == 1:  # if neighbor = 1, it has an edge with that node
            possible_shortest_path = info_list[CURRENT-1][1] + 1  # taking current's node shortest path and adding one to form path length over current node
            if possible_shortest_path < info_list[i][1]:  # if possible_shortest_path is smaller than parth already there
                info_list[i][1] = possible_shortest_path  # assigning new shortest path to that neighbour
                info_list[i][2] = info_list[CURRENT-1][0]  # over which node we got this shortest path
    # set current node as visited (True)
    info_list[CURRENT-1][3] = True


# This function form/constructs adjacency matrix with all edges
def form_adjMTX(rows):
    adjMTX1 = [([0] * rows) for i in range(rows)]  # Construct matrix with default values
    with open('FromTo.csv', 'r', encoding='utf8') as file:
        csv_reader = csv.DictReader(file)
        current = 0
        for line in csv_reader:
            if current != int(line['from_ID']):
                current = int(line['from_ID'])
            valFrom = int(line['from_ID'])
            valTo = int(line['to_ID'])

            adjMTX1[valFrom - 1][valTo - 1] = 1
            adjMTX1[valTo - 1][valFrom - 1] = 1
    return adjMTX1

# Constructing path and returning readable string of the path for user
def construct_path(end_node, start_node):
    global cities_list
    previous_node = info_list[end_node-1][2]
    if previous_node == None:
        return "Cities are not connected!"

    path = [end_node]
    while previous_node != start_node:
        path.append(previous_node)
        previous_node = info_list[previous_node-1][2]
    path.append(start_node)


    path.reverse()  # reversing because path is constructed backwards
    for j in range(len(path)):
        path[j] = cities_list[path[j]-1][1]
    path_str = ' -> '.join(e for e in path)  # constructing string of the path
    return path_str


def load_cities(cityNames):
    global cities_list
    cities_list = []
    with open(cityNames, 'r', encoding='utf8') as file:
        csv_reader = csv.DictReader(file)
        dictOfCities = {}
        for city in csv_reader:
            dictOfCities[city['Name']] = city['City_ID']
            cities_list.append([int(city['City_ID']), city['Name']])
    return dictOfCities


# START of the program
if __name__ == "__main__":
    # load all cities in dictionary, where every city will have hash value so we can access it quickly
    cities_list = None
    cities = load_cities("cityName.csv")

    numOfRows = len(cities)

    source = input("Enter starting city: ")  # ask user to enter start and end cities
    end = input("Enter end city: ")

    source = int(cities[source])
    end = int(cities[end])

    adjMTX = form_adjMTX(numOfRows)

    # initialize list with default info
    # this list has columns: "name of the node", "shortest path", "last node", "visited"
    info_list = [[i, float('inf'), None, False] for i in range(1, numOfRows + 1)]

    info_list[source - 1][1] = 0  # hard coding source's shortest path to 0

    while are_visited() == False:
        dijkstra()

    final_path = construct_path(end, source)
    print(final_path)