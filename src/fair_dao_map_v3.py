import graphviz
from PIL import Image
import cairosvg

# Создание диаграммы
dot = graphviz.Digraph(format='svg')
dot.attr(rankdir='LR', size='12,7')

# Главные блоки
dot.node('FairDAO', '🧬 Fair DAO\n(Post-monetary)', shape='box', style='filled', fillcolor='#d5f5e3')
dot.node('Community', '🌐 Community\nFractal Action\nNon-linear Consensus', shape='ellipse', style='filled', fillcolor='#abebc6')
dot.node('Money', '💰 Money\nUniversal Metric\nExchange Medium', shape='ellipse', style='filled', fillcolor='#f9e79f')
dot.node('Resonance', '🎵 Resonance\nEmergent Alignment', shape='ellipse', style='filled', fillcolor='#aed6f1')

# Связи
dot.edge('Community', 'FairDAO', label='Agreement\nwithout vote')
dot.edge('Resonance', 'FairDAO', label='Core logic')
dot.edge('Money', 'FairDAO', label='Bypassed\nor Shadowed', style='dashed', color='gray')

# Аннотированные идеи
dot.node('MetaModel', '🕸 Metamodel\nI2P / Fractal Mesh\nZero Admins', shape='ellipse', style='filled', fillcolor='#d6eaf8')
dot.edge('MetaModel', 'FairDAO', label='Infrastructure\nBackbone')

# Фоновые смыслы
dot.node('PostMonetary', '🌿 Post-monetary\nFractal Framework\nDAO = Environment', shape='note', style='filled', fillcolor='#fef9e7')
dot.edge('PostMonetary', 'FairDAO', style='dotted')

# Генерация SVG
svg_path = "/mnt/data/fair_dao_map.svg"
png_path = "/mnt/data/fair_dao_map.png"
dot.render(svg_path, cleanup=False)

# Конвертация SVG в PNG
cairosvg.svg2png(url=svg_path, write_to=png_path)

svg_path, png_path
