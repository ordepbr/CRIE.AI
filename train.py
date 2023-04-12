import numpy as np
import argparse

from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout
from keras.callbacks import ModelCheckpoint

from preprocess import preprocess_text

def train_model(X_train, y_train, vocab_size, max_seq_length, num_epochs, batch_size, model_filename):
    """
    Função responsável por treinar o modelo.
    """
    # Criar a arquitetura do modelo
    model = Sequential()
    model.add(LSTM(128, input_shape=(max_seq_length, vocab_size)))
    model.add(Dropout(0.5))
    model.add(Dense(vocab_size, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam')
    print(model.summary())
    
    # Definir callbacks para salvar o modelo periodicamente durante o treinamento
    checkpoint = ModelCheckpoint(model_filename, monitor='loss', verbose=1, save_best_only=True, mode='min')
    callbacks_list = [checkpoint]
    
    # Treinar o modelo
    model.fit(X_train, y_train, epochs=num_epochs, batch_size=batch_size, callbacks=callbacks_list)
    
    return model


if __name__ == '__main__':
    # Definir argumentos da linha de comando
    parser = argparse.ArgumentParser(description='Treina modelo de animação a partir de texto de entrada')
    parser.add_argument('text_file', type=str, help='arquivo com o texto de entrada')
    parser.add_argument('--max_seq_length', type=int, default=100, help='tamanho máximo das sequências')
    parser.add_argument('--num_epochs', type=int, default=50, help='número de épocas de treinamento')
    parser.add_argument('--batch_size', type=int, default=64, help='tamanho do batch de treinamento')
    parser.add_argument('--model_filename', type=str, default='model.h5', help='nome do arquivo do modelo')
    args = parser.parse_args()
    
    # Carregar texto de entrada
    with open(args.text_file, 'r') as f:
        text = f.read()
    
    # Pré-processar o texto de entrada
    X = preprocess_text(text, max_seq_length=args.max_seq_length)
    
    # Preparar os
