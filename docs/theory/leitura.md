# Guia de leitura

Trilha de estudo para o projeto **Quantum Community Detection in Complex Networks via QAOA**.
As chaves entre crases (por exemplo, `newman2006modularity`) correspondem às entradas de [`../references.bib`](../references.bib).

> Entradas do `.bib` marcadas com `A VERIFICAR` foram escritas de memória e precisam de conferência
> de volume, páginas e DOI antes de qualquer citação em texto submetido.

## Como usar este guia

Cada fase termina com um **marco de código**: o que você deve ser capaz de escrever depois de ler.
A ordem importa, porque cada fase alimenta a seguinte. Marque os itens ao concluir.

---

## Fase 1: da modularidade ao Hamiltoniano de Ising

**Objetivo:** entender de onde vem cada termo de H_C, para escrever `src/qcd/hamiltonian/ising_mapper.py` sem copiar fórmulas às cegas.

- [ ] **Newman (2006), *Modularity and community structure in networks*** (`newman2006modularity`)
  Define a matriz de modularidade B e mostra a modularidade como forma quadrática dos spins.
  Acesso aberto: [arXiv:physics/0602124](https://arxiv.org/abs/physics/0602124) · [PMC](https://pmc.ncbi.nlm.nih.gov/articles/pmid/16723398)
  *O que procurar:* a dedução de Q = (1/4m) sᵀBs a partir da definição por arestas internas; por que as linhas de B somam zero.

- [ ] **Newman (2006), *Finding community structure in networks using the eigenvectors of matrices*** (`newman2006eigenvectors`)
  Versão longa, com a bisseção espectral. É o seu baseline clássico mais barato.
  [arXiv:physics/0605087](https://arxiv.org/abs/physics/0605087)
  *O que procurar:* a analogia com o Laplaciano do grafo; como o autovetor dominante de B gera uma bisseção.

- [ ] **Lucas (2014), *Ising formulations of many NP problems*** (`lucas2014ising`)
  Guia de referência para converter problemas de grafos em Ising.
  [arXiv:1302.5843](https://arxiv.org/abs/1302.5843) · [Frontiers](https://www.frontiersin.org/journals/physics/articles/10.3389/fphy.2014.00005/full)
  *O que procurar:* introdução, a forma geral do modelo de Ising e as formulações de particionamento e corte. As de coloração e TSP ficam para a fase de generalização.

- [ ] **IBM Quantum Learning, tutorial *Quantum approximate optimization algorithm*** (`ibm2026qaoatutorial`)
  Fluxo completo de Max-Cut com Qiskit.
  [tutorial](https://quantum.cloud.ibm.com/docs/tutorials/quantum-approximate-optimization-algorithm)
  *O que procurar:* a construção do Hamiltoniano com `SparsePauliOp.from_sparse_list` e o uso do `EstimatorV2`.

- [ ] **IBM Quantum Learning, tutorial *Warm-start QAOA with the Optimization Mapper addon*** (`ibm2026warmstart`)
  Mostra a conversão grafo → QUBO → `SparsePauliOp` com o pacote `qiskit-addon-opt-mapper`.
  [tutorial](https://quantum.cloud.ibm.com/docs/tutorials/warm-start-qaoa)
  *O que procurar:* se vale escrever o mapeador à mão ou apoiar-se no pacote; como ele trata a constante do operador.

**Pontos para anotar enquanto lê:**

1. A soma em Σᵢⱼ conta cada par duas vezes: qual é o coeficiente de cada termo ZᵢZⱼ (i<j)?
2. O termo diagonal Bᵢᵢ·Zᵢ² é constante (Z² = I). Onde ele entra: no operador ou num deslocamento de energia separado?
3. Qual é a relação de sinal entre maximizar Q e minimizar ⟨H_C⟩?

**Marco de código:** `ising_mapper.py` com o teste `⟨s|H_C|s⟩ = −Q(s)` para todas as 2ⁿ partições de um grafo pequeno.

---

## Fase 2: o algoritmo QAOA

**Objetivo:** entender a estrutura do circuito e o papel de p, γ e β, para escrever `src/qcd/qaoa/circuit.py` e `optimizer.py`.

- [ ] **Farhi, Goldstone & Gutmann (2014), *A Quantum Approximate Optimization Algorithm*** (`farhi2014qaoa`)
  O artigo original.
  [arXiv:1411.4028](https://arxiv.org/abs/1411.4028)
  *O que procurar:* a definição do estado |γ,β⟩; a seção de p fixo; a análise do Max-Cut em grafos regulares como exemplo de cálculo analítico.

- [ ] **Farhi, Goldstone & Gutmann (2014), *QAOA applied to a bounded occurrence constraint problem*** (`farhi2014bounded`)
  Segunda aplicação, útil como exemplo adicional de análise em p = 1.
  [arXiv:1412.6062](https://arxiv.org/abs/1412.6062)
  *Leitura opcional na primeira passada.*

- [ ] **Zhou, Wang, Choi, Pichler & Lukin (2020), *QAOA: Performance, Mechanism, and Implementation on Near-Term Devices*** (`zhou2020qaoa`)
  Estudo de desempenho no Max-Cut e estratégias de inicialização dos parâmetros.
  [arXiv:1812.01041](https://arxiv.org/abs/1812.01041)
  *O que procurar:* os padrões observados nos parâmetros ótimos e as heurísticas de inicialização; a análise de recursos com ruído de projeção.

- [ ] **Hadfield et al. (2019), *From the QAOA to a Quantum Alternating Operator Ansatz*** (`hadfield2019qaoa`, **A VERIFICAR**)
  Generaliza o ansatz para problemas com restrições.
  *Leitura para a fase k > 2 comunidades, não agora.*

**Pontos para anotar:**

1. Quantos parâmetros tem o circuito para p camadas? Quantas portas de dois qubits por camada, dado que B é densa?
2. Qual inicialização você vai usar (aleatória, ou heurística de Zhou et al.)? Isso afeta a comparação de convergência.
3. Qual otimizador clássico (COBYLA, SPSA, L-BFGS-B) e com quantos shots por avaliação?

**Marco de código:** QAOA com p = 1 em um grafo pequeno (por exemplo, Zachary Karate Club), com `statevector` exato, comparando a energia final com o ótimo clássico.

---

## Fase 3: o trabalho mais próximo do seu projeto

**Objetivo:** posicionar sua pesquisa em relação ao que já foi feito em detecção de comunidades quântica.

- [ ] **Shaydulin et al. (2018), *Community Detection Across Emerging Quantum Architectures*** (`shaydulin2018across`)
  Estrutura híbrida quântico-clássica para detecção de comunidades, avaliada com annealing quântico e com computação quântica baseada em portas.
  [arXiv:1810.07765](https://arxiv.org/abs/1810.07765)
  *O que procurar:* como o problema global é dividido em subproblemas que cabem no dispositivo; como o subproblema é codificado.

- [ ] **Shaydulin et al. (2019), *Network Community Detection on Small Quantum Computers*** (`shaydulin2019small`)
  Resolve a detecção de 2 comunidades em grafos de até 410 vértices com um dispositivo IBM de 16 qubits e com o D-Wave 2000Q.
  [arXiv:1810.12484](https://arxiv.org/abs/1810.12484)
  *O que procurar:* as métricas de comparação com o ótimo e os conjuntos de dados usados (para reproduzir ou comparar).

**Perguntas para o seu projeto:**

1. O que o seu trabalho acrescenta: o efeito do ruído? da topologia? da densidade de conexões? Escreva isso em duas frases.
2. Quais grafos e métricas permitem comparação direta com esses dois artigos?

---

## Fase 4: baselines, limites e reprodutibilidade

**Objetivo:** montar a comparação clássica e entender os limites do método antes dos experimentos de ruído.

**Baselines clássicos (`src/qcd/baselines/`):**

- [ ] `newman2006eigenvectors` (já lido na Fase 1): bisseção espectral.
- [ ] `blondel2008louvain` e `traag2019leiden` (**A VERIFICAR**): Louvain e Leiden.
- [ ] `goemans1995maxcut` (**A VERIFICAR**): referência de razão de aproximação para Max-Cut.

**Limites da própria modularidade:**

- [ ] `fortunato2007resolution` (**A VERIFICAR**): limite de resolução; pode distorcer comparações entre partições.
- [ ] `brandes2008modularity` (**A VERIFICAR**): maximizar a modularidade é NP-difícil.

**Treinabilidade e ruído:**

- [ ] `mcclean2018barren` (**A VERIFICAR**): *barren plateaus*.
- [ ] `cerezo2021vqa` (**A VERIFICAR**): revisão de algoritmos variacionais.
- [ ] `wang2021noise` (**A VERIFICAR**): platôs induzidos por ruído, diretamente ligados ao seu objetivo de medir o efeito do ruído na convergência.

**Reprodutibilidade de software:**

- [ ] **Cardinal et al., *Migrating QAOA from Qiskit 1.x to 2.x*** (`cardinal2025migrating`)
  [arXiv:2512.08245](https://arxiv.org/abs/2512.08245)
  *O que procurar:* o efeito do orçamento de shots sobre os resultados. Registre o número de shots de cada experimento.

**Marco de código:** comparação QAOA × Louvain/Leiden × espectral × solução exata em grafos pequenos, com NMI/ARI contra comunidades planejadas.

---

## Registro de leitura

Use esta tabela para anotar o andamento. Uma linha por documento.

| Chave | Lido em | Principal aprendizado | Impacto no código |
|---|---|---|---|
| `newman2006modularity` | | | |
| `lucas2014ising` | | | |
| `farhi2014qaoa` | | | |
| `zhou2020qaoa` | | | |
| `shaydulin2019small` | | | |
| `cardinal2025migrating` | | | |

---

## Convenções

- Cite sempre pela chave BibTeX, nos notebooks e na documentação.
- Ao ler um artigo que ainda não está no `.bib`, adicione a entrada no mesmo commit em que usar a ideia no código.
- Quando uma entrada marcada `A VERIFICAR` for conferida, remova o campo `note`.
