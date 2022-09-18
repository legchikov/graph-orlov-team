import networkx as nx
import csv


def calculate_neighbour(graph: nx.Graph) -> dict:
    """
    считатет соседей узла
    """
    result = {}
    for user in graph.nodes:
        neighbour = [n for n in graph.neighbors(user)]  # Возвращает итератор по всем соседям узла n.
        result[user]=len(neighbour)
    return result


def create_graph() -> nx.Graph:
    """
    создаёт граф из csv фйала
    """
    graph = nx.Graph()
    with open('users_graph.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            user = row[0]
            graph.add_node(user)
            for similar_user in row[1].split(","):
                graph.add_edge(user, similar_user)
    return graph


def main():
    graph = create_graph()
    neighbour = calculate_neighbour(graph)
    print(neighbour)


if __name__ == "__main__":
    main()