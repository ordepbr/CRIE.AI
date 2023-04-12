import os

# Instala as dependências necessárias
os.system("pip install -r requirements.txt")

# Executa o pré-processamento do texto de entrada
os.system("python preprocess.py")

# Executa o treinamento do modelo
os.system("python train.py")

# Gera animações a partir do texto de entrada
os.system("python generate.py")

# Move o arquivo gerado para a pasta public
os.system("mv output.mp4 public/output.mp4")

# Copia o arquivo index.html para a pasta public
os.system("cp templates/index.html public/index.html")
