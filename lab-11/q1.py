graph = {

    "Kutch": ["Banaskantha", "Surendranagar", "Jamnagar"],

    "Banaskantha": ["Kutch", "Patan", "Sabarkantha"],

    "Patan": ["Banaskantha", "Mehsana", "Surendranagar"],

    "Mehsana": ["Patan", "Sabarkantha", "Gandhinagar", "Ahmedabad"],

    "Sabarkantha": ["Banaskantha", "Mehsana", "Gandhinagar"],

    "Gandhinagar": ["Mehsana", "Sabarkantha", "Ahmedabad", "Kheda"],

    "Ahmedabad": ["Gandhinagar", "Mehsana", "Kheda", "Anand", "Surendranagar"],

    "Kheda": ["Gandhinagar", "Ahmedabad", "Anand", "Panchmahal"],

    "Anand": ["Ahmedabad", "Kheda", "Vadodara"],

    "Vadodara": ["Anand", "Panchmahal", "Narmada", "Bharuch"],

    "Panchmahal": ["Kheda", "Vadodara", "Dahod"],

    "Dahod": ["Panchmahal"],

    "Narmada": ["Vadodara", "Bharuch"],

    "Bharuch": ["Vadodara", "Narmada", "Surat"],

    "Surat": ["Bharuch", "Navsari"],

    "Navsari": ["Surat", "Valsad", "Dangs"],

    "Valsad": ["Navsari", "Dangs"],

    "Dangs": ["Valsad", "Navsari"],

    "Surendranagar": ["Kutch", "Patan", "Ahmedabad", "Rajkot"],

    "Rajkot": ["Surendranagar", "Jamnagar", "Junagadh", "Amreli"],

    "Jamnagar": ["Kutch", "Rajkot", "Porbandar"],

    "Porbandar": ["Jamnagar", "Junagadh"],

    "Junagadh": ["Rajkot", "Porbandar", "Amreli"],

    "Amreli": ["Rajkot", "Junagadh", "Bhavnagar"],

    "Bhavnagar": ["Amreli", "Ahmedabad"]
}

colors = ['r','g', 'b']


def is_safe(node, color, assignment, graph):
    for neighbor in graph[node]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    
    return True

def solve(graph, assignment= {}):

    if len(graph) == len(assignment):
        return assignment
    
    node = list(graph.keys())[len(assignment)]
    for color in colors:

        if is_safe(node,color, assignment, graph):
            assignment[node] = color
            result = solve(graph,assignment)
            if result:
                return result
            del assignment[node]

    return None

solution = solve(graph)
print(solution)


    


    