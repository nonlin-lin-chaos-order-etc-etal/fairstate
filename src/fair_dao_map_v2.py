import graphviz

# Воссоздание графа после сброса состояния
dot = graphviz.Digraph(format='svg')
dot.attr(rankdir='LR', size='15,10')

# Главный узел
dot.node('FAIR_DAO', '🧬 FAIR DAO\nNon-Monetary\nFractal Coordination', shape='box', style='filled', fillcolor='#d5f5e3')

# Ветви концепта
concepts = {
    'RESONANCE': '🎶 Resonance,\nnot Voting',
    'MEMBRANE': '🫧 Soft Membrane\nof Coherence',
    'BIONET': '🌱 Biosphere\nSecurity Cells',
    'NARRATIVE': '📖 Narrative\nLegitimacy',
    'SHADOW': '💱 Shadow\nLocal Currencies\n(optional)',
    'MESH': '🕸 Mesh-ready:\nLANs / Darknets',
    'NO_TOKENS': '🚫 No Tokens,\nNo Capital Core',
    'NO_VOTES': '🚫 No Votes,\nNo Majority Rule'
}

colors = {
    'RESONANCE': '#abebc6',
    'MEMBRANE': '#aed6f1',
    'BIONET': '#f9e79f',
    'NARRATIVE': '#f5cba7',
    'SHADOW': '#d7bde2',
    'MESH': '#fadbd8',
    'NO_TOKENS': '#f1948a',
    'NO_VOTES': '#f1948a'
}

for key, label in concepts.items():
    dot.node(key, label, shape='ellipse', style='filled', fillcolor=colors[key])
    dot.edge('FAIR_DAO', key)

# Сохранение диаграммы в SVG и PNG
svg_path = "/mnt/data/fair_dao_map.svg"
png_path = "/mnt/data/fair_dao_map.png"
dot.render(svg_path[:-4], format='svg', cleanup=False)
dot.render(png_path[:-4], format='png', cleanup=False)

svg_path, png_path
