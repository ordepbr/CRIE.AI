import numpy as np
import string

from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

def preprocess_text(text, max_seq_length=100):
    """
    Função responsável por realizar o pré-processamento do texto de entrada.
    """
    # Remover pontuações e transformar todas as letras em minúsculas
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    
    # Tokenizar o texto e transformá-lo em sequências de números
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts([text])
    sequences = tokenizer.texts_to_sequences([text])[0]
    
    # Padronizar as sequências para que todas tenham o mesmo tamanho
    padded_sequences = pad_sequences([sequences], maxlen=max_seq_length, padding='post', truncating='post')
    
    return np.array(padded_sequences)
