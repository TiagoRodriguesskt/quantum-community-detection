"""Testes unitários para o módulo de modularidade."""

import networkx as nx
import numpy as np
from src.graph_utils.modularity import (
    calculate_classical_modularity,
    compute_modularity_matrix,
)


def test_modularity_matrix_sum_zero():
    """Propriedade fundamental da matriz de Newman: a soma das linhas e colunas deve ser 0."""
    # Grafo em anel simples com 4 nós
    graph = nx.cycle_graph(4)
    matrix = compute_modularity_matrix(graph)

    # A soma de qualquer linha de B_ij deve ser igual a 0 (dentro de margem de precisão flutuante)
    np.testing.assert_allclose(
        matrix.sum(axis=1), np.zeros(4), atol=1e-12
    )


def test_perfect_bipartite_partition():
    """Valida a modularidade de dois triângulos conectados por uma ponte."""
    graph = nx.disjoint_union(nx.complete_graph(3), nx.complete_graph(3))
    graph.add_edge(2, 3)  # Aresta ligando os dois grupos

    # Partição ideal: Comunidade A (+1) para nós 0,1,2 e Comunidade B (-1) para 3,4,5
    partition = np.array([1, 1, 1, -1, -1, -1])

    modularity = calculate_classical_modularity(graph, partition)

    # A partição ideal de dois clusters bem definidos deve gerar Q > 0
    assert modularity > 0.0
