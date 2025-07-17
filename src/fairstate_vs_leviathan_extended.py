import graphviz

# Extended diagram: FairState vs Leviathan (version 2)
dot = graphviz.Digraph(format='svg')
dot.attr(rankdir='LR', size='12,7')

# Main blocks
dot.node('FS', '🌱 FairState\nCivic NeoState\nFractal Autonomy\nDecentralized Ethics', shape='box', style='filled', fillcolor='#d5f5e3')
dot.node('LV', '🦑 Leviathan\nGlobal Megastructure\nCentralized Control\nPsyOps Engine', shape='box', style='filled', fillcolor='#fadbd8')

# Arrows between main blocks
dot.edge('LV', 'FS', label='⚔️ Coercion\nCensorship\nPsy-pressure', color='red', penwidth='2')
dot.edge('FS', 'LV', label='🌊 Resilience\nSubversion\nCultural Memes', color='green', penwidth='2')

# FairState MEMEPLEXES
dot.node('MythsFS', '🔮 Mythos: Prometheus,\nRobin Hood, Siddhartha', shape='ellipse', style='filled', fillcolor='#aed6f1')
dot.node('MemeFS', '📢 Memeplex: Fairness,\nHacker Ethic, Open Culture', shape='ellipse', style='filled', fillcolor='#abebc6')
dot.edge('MythsFS', 'FS', label='Narrative Seed')
dot.edge('MemeFS', 'FS', label='Memetic Engine')

# Leviathan MEMEPLEXES
dot.node('MythsLV', '👑 Mythos: Hobbes,\nDivine Right, Empire', shape='ellipse', style='filled', fillcolor='#f5b7b1')
dot.node('MemeLV', '🧢 Memeplex: Obedience,\nProfit, Surveillance', shape='ellipse', style='filled', fillcolor='#f1948a')
dot.edge('MythsLV', 'LV', label='Dominant Narrative')
dot.edge('MemeLV', 'LV', label='Mass Conditioning')

# Feedback loops
dot.edge('LV', 'MemeLV', label='Broadcast\nControl', style='dashed', color='darkred')
dot.edge('FS', 'MemeFS', label='Bottom-up\nCulture', style='dashed', color='darkgreen')

# Fractal control effects
dot.node('FractalFS', '🧬 Fractal Meshes\n(Autonomous Cells)', shape='ellipse', style='filled', fillcolor='#d4efdf')
dot.node('FractalLV', '🕸 Fractal Control\n(Subsidiary Surveillance)', shape='ellipse', style='filled', fillcolor='#fadbd8')
dot.edge('FractalFS', 'FS')
dot.edge('FractalLV', 'LV')

# Influence indicators/tools
dot.node('ToolFS', '🛠 Shadow Systems:\nDAO, MoT, Darknets', shape='ellipse', style='filled', fillcolor='#a9dfbf')
dot.node('ToolLV', '📡 Surveillance Tech:\nAI, PRISM, Palantir', shape='ellipse', style='filled', fillcolor='#f9e79f')
dot.edge('ToolFS', 'FS')
dot.edge('ToolLV', 'LV')

# Symbols for context
dot.node('Chaos', '♾ Chaos Field', shape='ellipse', style='filled', fillcolor='#f2f3f4')
dot.edge('Chaos', 'FS', label='Creative Emergence', style='dotted')
dot.edge('Chaos', 'LV', label='Control Panic', style='dotted')

# Generate SVG
dot.render('/mnt/data/fairstate_vs_leviathan_extended', cleanup=False)
'/mnt/data/fairstate_vs_leviathan_extended.svg'