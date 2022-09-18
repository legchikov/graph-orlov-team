import networkx as nx
import csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


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


def draw_histogram_for_number_of_neighbour(neighbour):
    df = pd.DataFrame.from_dict(neighbour, orient="index")  # create dataframe and paste neighbour
    df = df.rename(columns={0: "number of neighbour"})
    sns.displot(df, x="number of neighbour")
    plt.savefig('ex1.pdf')


def draw_histogram_for_features():
    df = pd.read_csv('users_float_features.csv', index_col="user")
    for i in df.columns:

        sns.displot(df, x=i, kind="kde", fill=True)
        plt.savefig(f'ex{i}.pdf')


def main():
    graph = create_graph()
    neighbour = calculate_neighbour(graph)
    print(neighbour.values())
    #draw_histogram_for_number_of_neighbour(neighbour)
    draw_histogram_for_features()


if __name__ == "__main__":
    main()