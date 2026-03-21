import random

cities = ['A','B','C','D','E','F','G','H']

cost = [
[0,10,15,20,25,30,35,40],
[12,0,35,15,20,25,30,45],
[25,30,0,10,40,20,15,35],
[18,25,12,0,15,30,20,10],
[22,18,28,20,0,15,25,30],
[35,22,18,28,12,0,40,20],
[30,35,22,18,28,32,0,15],
[40,28,35,22,18,25,12,0]
]

n = len(cities)


def tour_cost(t):
    c = 0
    for i in range(n-1):
        c += cost[t[i]][t[i+1]]
    c += cost[t[-1]][t[0]]
    return c



def neighbor(t):
    a,b = random.sample(range(n),2)
    t = t[:]
    t[a],t[b] = t[b],t[a]
    return t


def beam_search(k, iterations=200):

    states = [random.sample(range(n),n) for _ in range(k)]

    for _ in range(iterations):

        candidates = []

        for s in states:
            candidates.append(s)

            for _ in range(5):
                candidates.append(neighbor(s))

        candidates.sort(key=tour_cost)

        states = candidates[:k]

    best = min(states,key=tour_cost)

    return best, tour_cost(best)


def create_population(size):
    return [random.sample(range(n), n) for _ in range(size)]


def select(pop):
    pop = sorted(pop,key=tour_cost)
    return pop[:len(pop)//2]



def one_point(p1,p2):

    point = random.randint(1,n-2)

    child = p1[:point]

    for x in p2:
        if x not in child:
            child.append(x)

    return child



def two_point(p1,p2):

    a,b = sorted(random.sample(range(n),2))

    child = [None]*n
    child[a:b] = p1[a:b]

    ptr = 0

    for x in p2:

        if x not in child:

            while child[ptr] != None:
                ptr += 1

            child[ptr] = x

    return child


# ---- Mutation ----

def mutate(t):

    a,b = random.sample(range(n),2)
    t[a],t[b] = t[b],t[a]

    return t


def genetic(crossover="one", generations=200, pop_size=30):

    pop = create_population(pop_size)

    for _ in range(generations):

        parents = select(pop)
        children = []

        while len(children) < pop_size:

            p1,p2 = random.sample(parents,2)

            if crossover == "one":
                child = one_point(p1,p2)
            else:
                child = two_point(p1,p2)

            if random.random() < 0.2:
                child = mutate(child)

            children.append(child)

        pop = children

    best = min(pop,key=tour_cost)

    return best, tour_cost(best)



print("\nLOCAL BEAM SEARCH\n")

for k in [3,5,10]:

    path,c = beam_search(k)

    print("k =",k)
    print("Path:",[cities[i] for i in path])
    print("Cost:",c)
    print()


print("\nGENETIC ALGORITHM\n")

path,c = genetic("one")

print("One Point Crossover")
print("Path:",[cities[i] for i in path])
print("Cost:",c)
print()


path,c = genetic("two")

print("Two Point Crossover")
print("Path:",[cities[i] for i in path])
print("Cost:",c)