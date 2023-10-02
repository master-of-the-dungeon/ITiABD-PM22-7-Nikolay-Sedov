import matplotlib.pyplot as plt
import networkx as nx

# Create a new graph
G = nx.Graph()

# Add nodes for entities
entities = ['Издание', 'Читатель', 'Пакет изданий', 'Пользователь']
for entity in entities:
    G.add_node(entity, color='lightblue')

# Add nodes for relationships
relationships = ['Читатель-Издание', 'Пакет изданий-Издание', 'Пользователь-Издание']
for rel in relationships:
    G.add_node(rel, color='lightgray')

# Add edges
edges = [
    ('Издание', 'Читатель-Издание'),
    ('Читатель', 'Читатель-Издание'),
    ('Издание', 'Пакет изданий-Издание'),
    ('Пакет изданий', 'Пакет изданий-Издание'),
    ('Издание', 'Пользователь-Издание'),
    ('Пользователь', 'Пользователь-Издание')
]
G.add_edges_from(edges)

# Draw the graph
pos = nx.spring_layout(G)
colors = [G.nodes[node]['color'] for node in G.nodes]

plt.figure(figsize=(12, 8))
nx.draw(G, pos, with_labels=True, node_color=colors, node_size=3000)
plt.title('ER-диаграмма "Библиотека вуза"')
plt.show()
