import os
import torch
from model import AnimationGenerator
from data_loader import TextDataset, TextDataLoader
from utils import get_data_loader, generate_animation

# Define os hiperparâmetros
batch_size = 32
num_workers = 2
max_length = 20
hidden_size = 512
num_layers = 2
dropout = 0.5

# Define o caminho para o modelo treinado
model_path = 'models/animation_generator.pth'

# Carrega o modelo treinado
generator = AnimationGenerator(max_length, hidden_size, num_layers, dropout)
generator.load_state_dict(torch.load(model_path))

# Define o dispositivo a ser utilizado
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Define o dataset e o dataloader para a geração de animações
dataset = TextDataset('data/test.txt', max_length)
data_loader = TextDataLoader(dataset, batch_size, num_workers)

# Gera as animações para cada lote de dados do dataloader
for batch in data_loader:
    inputs = batch.to(device)
    outputs = generator.generate(inputs)
    generate_animation(outputs, batch_size)
    
# Move o arquivo gerado para a pasta output
os.system("mv output.mp4 output/output.mp4")
