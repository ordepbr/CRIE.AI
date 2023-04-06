from jinja2 import Environment, FileSystemLoader
import os

# definir o caminho para o diretório dos templates
path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates'))
env = Environment(loader=FileSystemLoader(path), trim_blocks=True)

# renderizar o template com as variáveis
template = env.get_template('home.html')
output = template.render(title=video_title, description=video_description)

# escrever o output para o arquivo index.html
with open('index.html', 'w') as f:
    f.write(output)
