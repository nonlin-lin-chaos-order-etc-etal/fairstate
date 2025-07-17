import graphviz

# Create a Graphviz DOT diagram
dot = graphviz.Digraph(format='svg')
dot.attr(rankdir='LR', size='10,5')

# Nodes: FairState
dot.node('FS', '🌱 FairState\nDecentralized\nFluid\nCivic\nResilient', shape='box', style='filled', fillcolor='#d5f5e3')

# Nodes: Leviathan
dot.node('LV', '🦑 Leviathan\nCentralized\nOpaque\nCoercive\nGlobal', shape='box', style='filled', fillcolor='#fadbd8')

# Connections
dot.edge('LV', 'FS', label='⚔️ Surveillance\nPressure\nCensorship', color='red')
dot.edge('FS', 'LV', label='🛠 Dissent\nDecentralization\nShadow Systems', color='green')

# FairState subnodes
dot.node('MoT', '🔗 Mesh of Things (MoT)', shape='ellipse', style='filled', fillcolor='#abebc6')
dot.node('DAO', '🧬 Fair DAO (Non-monetary)', shape='ellipse', style='filled', fillcolor='#abebc6')
dot.node('Media', '📡 Independent Media Alliances', shape='ellipse', style='filled', fillcolor='#abebc6')
dot.edge('FS', 'MoT')
dot.edge('FS', 'DAO')
dot.edge('FS', 'Media')

# Leviathan subnodes
dot.node('Gov', '🏛 State Institutions\nHard Law', shape='ellipse', style='filled', fillcolor='#f5b7b1')
dot.node('Corp', '🏢 Corporations\nSoft Power', shape='ellipse', style='filled', fillcolor='#f5b7b1')
dot.node('Mind', '🧠 Mind Control\nNarratives', shape='ellipse', style='filled', fillcolor='#f5b7b1')
dot.edge('LV', 'Gov')
dot.edge('LV', 'Corp')
dot.edge('LV', 'Mind')

# Return result
dot.render('/mnt/data/fairstate_vs_leviathan', cleanup=False)
'/mnt/data/fairstate_vs_leviathan.svg'
