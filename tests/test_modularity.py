"""Matriz de modularidade de Newman e modularidade clássica Q."""

import networkx as nx
import numpy as np


def compute_modularity_matrix(graph: nx.Graph) -> np.ndarray:
    """Calcula B_ij = A_ij - k_i k_j / (2m).

    Os nós são ordenados por `sorted(graph.nodes())`, de modo que o índice
    i da matriz corresponde ao i-ésimo nó nessa ordem. Suporta pesos
    (atributo 'weight'): k_i é a força do nó e m a soma dos pesos das arestas.
    """
    nodes = sorted(graph.nodes())
    adjacency = nx.to_numpy_array(graph, nodelist=nodes, weight="weight")

    degrees = adjacency.sum(axis=1)
    two_m = degrees.sum()
    if two_m == 0:
        raise ValueError("O grafo não possui arestas: a modularidade não é definida.")

    return adjacency - np.outer(degrees, degrees) / two_m


def calculate_classical_modularity(graph: nx.Graph, partition: np.ndarray) -> float:
    """Calcula Q = (1 / 4m) * s^T B s para uma partição em duas comunidades.

    `partition` é um vetor de spins s_i em {-1, +1}, na mesma ordem de
    `sorted(graph.nodes())`.
    """
    spins = np.asarray(partition, dtype=float)
    if spins.shape != (graph.number_of_nodes(),):
        raise ValueError("O vetor de partição deve ter um elemento por nó.")
    if not np.all(np.isin(spins, (-1.0, 1.0))):
        raise ValueError("Os spins devem assumir apenas os valores -1 ou +1.")

    matrix = compute_modularity_matrix(graph)
    two_m = nx.to_numpy_array(graph, nodelist=sorted(graph.nodes()), weight="weight").sum()

    return float(spins @ matrix @ spins / (2.0 * two_m))