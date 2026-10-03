# Quantum Community Detection in Complex Networks via QAOA

![Python Version](https://img.shields.io/badge/python-3.12-blue)
![Package Manager](https://img.shields.io/badge/environment-uv-purple)
![Quantum Framework](https://img.shields.io/badge/framework-Qiskit-6100FF)
![License](https://img.shields.io/badge/license-MIT-green)

Este repositório contém a implementação do projeto de pesquisa voltado à **Detecção de Comunidades em Grafos Complexos** através do **Algoritmo Quântico Aproximado de Otimização (QAOA)**, mapeando a função de **Modularidade de Newman** diretamente para a **Hamiltoniana de Ising**.

O objetivo da pesquisa é avaliar como a densidade de conexões, a topologia de redes complexas e a presença de ruído quântico impactam a taxa de convergência do algoritmo variacional em relação a resoluções clássicas.

---

## 🔬 Fundamentação Teórico-Matemática

A **Modularidade ($Q$)** de uma partição de um grafo não-direcionado $G = (V, E)$ em duas comunidades é dada por:

$$Q = \frac{1}{4m} \sum_{i,j} B_{ij} s_i s_j$$

Onde $B_{ij} = A_{ij} - \frac{k_i k_j}{2m}$ representa a **Matriz de Modularidade de Newman**, $A_{ij}$ é a matriz de adjacência, $k_i$ e $k_j$ são os graus dos nós $i$ e $j$, $m$ é o número total de arestas e $s_i \in \{-1, +1\}$ é a variável de spin clássica.

Para o ambiente quântico, os spins $s_i$ são promovidos a operadores de Pauli $\hat{Z}_i$, gerando a Hamiltoniana de Custo:

$$\hat{H}_C = -\frac{1}{4m} \sum_{i,j} B_{ij} \hat{Z}_i \hat{Z}_j$$

---

## 🛠️ Arquitetura do Repositório

```text
quantum-community-detection/
├── docs/                 # Documentação formal e formulações matemáticas
├── src/                  # Módulos principais do pacote Python
│   ├── graph_utils/      # Manipulação de grafos e matrizes de modularidade
│   ├── hamiltonian/      # Mapeamento do modelo de Ising para operadores Pauli (Qiskit)
│   └── qaoa/             # Circuitos variacionais quânticos e otimizadores
├── notebooks/            # Notebooks de validação e benchmarks
├── tests/                # Testes unitários automatizados (pytest)
└── pyproject.toml        # Configuração do projeto e dependências (uv)
