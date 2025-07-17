import graphviz
import cairosvg

# Повторная генерация диаграммы с указанием точных путей
dot = graphviz.Digraph(format='svg', directory="/mnt/data")
dot.attr(rankdir='LR', size='12,7')

# Узлы
dot.node('FairDAO', '🧬 Fair DAO\n(Post-monetary)', shape='box', style='filled', fillcolor='#d5f5e3')
dot.node('Community', '🌐 Community\nFractal Action\nNon-linear Consensus', shape='ellipse', style='filled', fillcolor='#abebc6')
dot.node('Money', '💰 Money\nUniversal Metric\nExchange Medium', shape='ellipse', style='filled', fillcolor='#f9e79f')
dot.node('Resonance', '🎵 Resonance\nEmergent Alignment', shape='ellipse', style='filled', fillcolor='#aed6f1')
dot.node('MetaModel', '🕸 Metamodel\nI2P / Fractal Mesh\nZero Admins', shape='ellipse', style='filled', fillcolor='#d6eaf8')
dot.node('PostMonetary', '🌿 Post-monetary\nFractal Framework\nDAO = Environment', shape='note', style='filled', fillcolor='#fef9e7')

# Связи
dot.edge('Community', 'FairDAO', label='Agreement\nwithout vote')
dot.edge('Resonance', 'FairDAO', label='Core logic')
dot.edge('Money', 'FairDAO', label='Bypassed\nor Shadowed', style='dashed', color='gray')
dot.edge('MetaModel', 'FairDAO', label='Infrastructure\nBackbone')
dot.edge('PostMonetary', 'FairDAO', style='dotted')

# Сохраняем в SVG
svg_filename = "fair_dao_map"
svg_path = f"/mnt/data/{svg_filename}.svg"
png_path = f"/mnt/data/{svg_filename}.png"
dot.render(filename=svg_filename)

# Конвертация SVG → PNG
cairosvg.svg2png(url=svg_path, write_to=png_path)

svg_path, png_path
