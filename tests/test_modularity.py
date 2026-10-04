"""Testes unitários para o módulo de modularidade."""

import networkx as nx
import numpy as np

from src.qcd.graph_utils.modularity import (
    calculate_classical_modularity,
    compute_modularity_matrix,
)


def test_modularity_matrix_sum_zero():
    """Propriedade fundamental da matriz de Newman: a soma das linhas deve ser 0."""
    graph = nx.cycle_graph(4)
    matrix = compute_modularity_matrix(graph)
    np.testing.assert_allclose(matrix.sum(axis=1), np.zeros(4), atol=1e-12)


def test_perfect_bipartite_partition():
    """Valida a modularidade de dois triângulos conectados por uma ponte."""
    graph = nx.disjoint_union(nx.complete_graph(3), nx.complete_graph(3))
    graph.add_edge(2, 3)

    partition = np.array([1, 1, 1, -1, -1, -1])
    modularity = calculate_classical_modularity(graph, partition)

    assert modularity > 0.0
    # Valor analítico: 2 * (3/7 - (7/14)^2) = 5/14
    np.testing.assert_allclose(modularity, 5 / 14, atol=1e-12)


def test_matches_networkx_modularity():
    """Compara Q com a implementação de referência do NetworkX (Karate Club)."""
    karate = nx.karate_club_graph()
    # Grafo sem pesos, para casar com a convenção da implementação
    graph = nx.Graph()
    graph.add_nodes_from(sorted(karate.nodes()))
    graph.add_edges_from(karate.edges())

    nodes = list(graph.nodes())
    partition = np.array(
        [1 if karate.nodes[n]["club"] == "Mr. Hi" else -1 for n in nodes]
    )
    communities = [
        {n for n, s in zip(nodes, partition) if s == 1},
        {n for n, s in zip(nodes, partition) if s == -1},
    ]
    expected = nx.community.modularity(graph, communities)

    np.testing.assert_allclose(
        calculate_classical_modularity(graph, partition), expected, atol=1e-12
    )
