import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.layers import Input, Embedding, LSTM, Dense
from tensorflow.keras.models import Model
from flask import Flask, request, render_template

# Define the deep learning model architecture
def build_model(max_len, vocab_size):
    input_layer = Input(shape=(max_len,))
    x = Embedding(input_dim=vocab_size, output_dim=50, input_length=max_len)(input_layer)
    x = LSTM(128)(x)
    x = Dense(128, activation='relu')(x)
    output_layer = Dense(max_len, activation='softmax')(x)
    model = Model(inputs=input_layer, outputs=output_layer)
    model.compile(loss='categorical_crossentropy', optimizer='adam')
    return model
    
# Train the model on input text
def train_model(text):
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts([text])
    sequences = tokenizer.texts_to_sequences([text])[0]
    max_len = max([len(seq) for seq in sequences])
    vocab_size = len(tokenizer.word_index) + 1
    padded_sequences = pad_sequences([sequences], maxlen=max_len, padding='pre')
    x_train = padded_sequences[:, :-1]
    y_train = tf.keras.utils.to_categorical(padded_sequences[:, 1:], num_classes=vocab_size)
    model = build_model(max_len - 1, vocab_size)
    model.fit(x_train, y_train, epochs=20, verbose=0)
    return tokenizer, model

# Generate a text sequence from input text using the trained model
def generate_text_sequence(seed_text, model, tokenizer, sequence_length):
    for _ in range(sequence_length):
        encoded = tokenizer.texts_to_sequences([seed_text])[0]
        encoded = pad_sequences([encoded], maxlen=sequence_length, padding='pre', truncating='pre')
        y_predict = model.predict_classes(encoded, verbose=0)
        predicted_word = ''
        for word, index in tokenizer.word_index.items():
            if index == y_predict:
                predicted_word = word
                break
        seed_text += ' ' + predicted_word
    return seed_text

# Define a Flask web interface for the algorithm
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/generate_sequence', methods=['POST'])
def generate_sequence():
    input_text = request.form['input_text']
    sequence_length = int(request.form['sequence_length'])
    tokenizer, model = train_model(input_text)
    sequence = generate_text_sequence(input_text, model, tokenizer, sequence_length)
    return render_template('sequence.html', sequence=sequence)

if __name__ == '__main__':
    app.run(debug=True)
