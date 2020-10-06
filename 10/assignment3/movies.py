#################
# Mandatory Assignment 3 - IDSP
#################

# Assignment: 	Working with Graphs and Dictionaries
# Author: 		Jonas-Mika Senghaas
# Date: 		23. September 2020
# TA:			Simon Martin Breum

def read_csv(filename: str, delimiter: str):
    lines = []

    with open(filename, "r") as infile:
        for line in infile:
            lines.append(tuple(line.strip().split(delimiter)))

    return lines  # List[Tuples]


def generate_name_map(nodes):
    name_map = {}

    for item in nodes:
        name_map[item[0]] = item[1]

    return name_map


def name_edges(edges: [()], name_map: {}):
    L = []

    for edge in edges:
        L.append((name_map[edge[0]], name_map[edge[1]], edge[2]))

    return L  # [()]


def generate_movie_dictionary(named_edges: [()]):
    movie_dict = {}

    for edge in named_edges:
        if edge[-1] == "ACTS_IN":
            try:
                movie_dict[edge[1]].append(edge[0])
            except KeyError:
                movie_dict[edge[1]] = [edge[0]]

    for movie in movie_dict: # i know that it was not asked for, but i liked the dictionary to be sorted, also because it was sorted in the examples
        movie_dict[movie].sort()

    return movie_dict # dict


def get_actor_friends(movie_dict: dict):
    actors_friends = {}

    for movie in movie_dict:
        for actor in movie_dict[movie]:
            friends = [i for i in movie_dict[movie] if i is not actor]
            try:
                for friend in friends:
                    if friend not in actors_friends[actor]:
                        actors_friends[actor].append(friend)
            except KeyError:
                actors_friends[actor] = friends

    for friends in actors_friends: # same here, sorted again
        actors_friends[friends].sort()

    return actors_friends  # dict


def main():
    nodes = read_csv("nodes.csv", ",")
    edges = read_csv("edges.csv", ",")
    
    # in the edges.csv file there swere duplicates, so i changed the output of the csv file to be a set of tuples
    unique_edges = list(set(edges))
    
    # print(nodes[0])
    # print(edges[0])
    # print(unique_edges)

    ########

    name_map = generate_name_map(nodes)
    # print(name_map["345"])

    ########

    named_edges = name_edges(unique_edges, name_map)
    # print(named_edges[0])

    ########

    movie_dict = generate_movie_dictionary(named_edges)
    # print(movie_dict["The Matrix"])

    ########

    actors_friends = get_actor_friends(movie_dict)
    # print(actors_friends["Keanu Reeves"])


if __name__ == "__main__":
    main()
