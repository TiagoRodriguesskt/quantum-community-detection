"""Módulo para cálculo da Matriz de Modularidade de Newman e funções associadas a grafos."""

import networkx as nx
import numpy as np


def compute_modularity_matrix(graph: nx.Graph) -> np.ndarray:
    """Calcula a matriz de modularidade B_ij para um grafo não-direcionado.

    B_ij = A_ij - (k_i * k_j) / (2 * m)

    Onde:
        A_ij: Matriz de adjacência
        k_i, k_j: Grau dos vértices i e j
        m: Número total de arestas no grafo

    Args:
        graph (nx.Graph): Grafo do NetworkX.

    Returns:
        np.ndarray: Matriz B de dimensão (N, N).
    """
    adj_matrix = nx.to_numpy_array(graph)
    degrees = np.array([deg for _, deg in graph.degree()])
    num_edges = graph.number_of_edges()

    if num_edges == 0:
        raise ValueError("O grafo não possui arestas para calcular a modularidade.")

    # Produto externo dos graus: k_i * k_j
    degree_product = np.outer(degrees, degrees)

    # Matriz de Modularidade de Newman B_ij
    modularity_matrix = adj_matrix - (degree_product / (2 * num_edges))

    return modularity_matrix


def calculate_classical_modularity(
    graph: nx.Graph, partition: np.ndarray
) -> float:
    """Calcula o valor escalar da modularidade Q para uma dada partição de spins.

    Q = (1 / (4 * m)) * sum_{i,j} B_ij * s_i * s_j

    Args:
        graph (nx.Graph): Grafo de entrada.
        partition (np.ndarray): Vetor de spins s_i in {-1, +1} para cada nó.

    Returns:
        float: Valor de modularidade Q (quanto maior, melhor a divisão em comunidades).
    """
    modularity_matrix = compute_modularity_matrix(graph)
    num_edges = graph.number_of_edges()

    # Q = (1 / 4m) * s^T * B * s
    q_value = (1.0 / (4.0 * num_edges)) * np.dot(
        partition, np.dot(modularity_matrix, partition)
    )

    return float(q_value)
