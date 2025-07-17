import graphviz
from cairosvg import svg2png

# Create a directed graph with left-to-right orientation
dot = graphviz.Digraph(format='svg')
dot.attr(rankdir='LR', size='14,8')

# === Define main entities ===

# FairState (NeoState of Civic Fractals)
dot.node('FS', '🌱 FairState\nCivic NeoState\nFractal Autonomy\nDecentralized Ethics',
         shape='box', style='filled', fillcolor='#d5f5e3')

# Leviathan (Centralized System of Control)
dot.node('LV', '🦑 Leviathan\nGlobal Megastructure\nCentralized Control\nPsyOps Engine',
         shape='box', style='filled', fillcolor='#fadbd8')

# Main dynamic arrows
dot.edge('LV', 'FS', label='⚔️ Coercion\nCensorship\nPsy-pressure', color='red', penwidth='2')
dot.edge('FS', 'LV', label='🌊 Resilience\nSubversion\nCultural Memes', color='green', penwidth='2')

# === Narrative foundations (Mythos and Memes) ===

# FairState narratives
dot.node('MythsFS', '🔮 Mythos: Prometheus,\nRobin Hood, Siddhartha',
         shape='ellipse', style='filled', fillcolor='#aed6f1')
dot.node('MemeFS', '📢 Memeplex: Fairness,\nHacker Ethic, Open Culture',
         shape='ellipse', style='filled', fillcolor='#abebc6')
dot.edge('MythsFS', 'FS', label='Narrative Seed')
dot.edge('MemeFS', 'FS', label='Memetic Engine')

# Leviathan narratives
dot.node('MythsLV', '👑 Mythos: Hobbes,\nDivine Right, Empire',
         shape='ellipse', style='filled', fillcolor='#f5b7b1')
dot.node('MemeLV', '🧢 Memeplex: Obedience,\nProfit, Surveillance',
         shape='ellipse', style='filled', fillcolor='#f1948a')
dot.edge('MythsLV', 'LV', label='Dominant Narrative')
dot.edge('MemeLV', 'LV', label='Mass Conditioning')

# Feedback loops (broadcast or emergent)
dot.edge('LV', 'MemeLV', label='Broadcast\nControl', style='dashed', color='darkred')
dot.edge('FS', 'MemeFS', label='Bottom-up\nCulture', style='dashed', color='darkgreen')

# === Structural topology ===

dot.node('FractalFS', '🧬 Fractal Meshes\n(Autonomous Cells)',
         shape='ellipse', style='filled', fillcolor='#d4efdf')
dot.node('FractalLV', '🕸 Fractal Control\n(Subsidiary Surveillance)',
         shape='ellipse', style='filled', fillcolor='#fadbd8')
dot.edge('FractalFS', 'FS')
dot.edge('FractalLV', 'LV')

# === Technological tools ===

dot.node('ToolFS', '🛠 Shadow Systems:\nDAO, MoT, Darknets',
         shape='ellipse', style='filled', fillcolor='#a9dfbf')
dot.node('ToolLV', '📡 Surveillance Tech:\nAI, PRISM, Palantir',
         shape='ellipse', style='filled', fillcolor='#f9e79f')
dot.edge('ToolFS', 'FS')
dot.edge('ToolLV', 'LV')

# === Chaos field (source of randomness) ===

dot.node('Chaos', '♾ Chaos Field',
         shape='ellipse', style='filled', fillcolor='#f2f3f4')
dot.edge('Chaos', 'FS', label='Creative Emergence', style='dotted')
dot.edge('Chaos', 'LV', label='Control Panic', style='dotted')

# === Biosphere Security DAO ===

dot.node('BSD', '🛡️ Biosphere Security DAO\nEthical Surveillance\nFractal Vigilance',
         shape='ellipse', style='filled', fillcolor='#82e0aa')
dot.edge('BSD', 'FS', label='Feedback & Defense', color='darkgreen', penwidth='1.5')
dot.edge('FS', 'BSD', label='Civic Mandate', style='dotted', color='gray')

# === Render SVG and PNG ===

# Export SVG directly from source
svg_code = dot.pipe(format='svg')

# Save SVG file
svg_path = "/mnt/data/fairstate_with_biosphere_security.svg"
with open(svg_path, "wb") as f:
    f.write(svg_code)

# Convert to PNG
png_path = "/mnt/data/fairstate_with_biosphere_security.png"
svg2png(bytestring=svg_code, write_to=png_path)

(svg_path, png_path)

