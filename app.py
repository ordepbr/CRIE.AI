from flask import Flask, render_template, request, redirect, url_for
from moviepy.editor import *
import os

app = Flask(__name__)

# Rota da página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota da página de resultado
@app.route('/result', methods=['POST'])
def result():
    # Salva o arquivo enviado pelo usuário
    video_file = request.files['file']
    video_file.save('input.mp4')
    
    # Configurações do vídeo de saída
    subclip_duration = 5
    duration = VideoFileClip('input.mp4').duration
    video_clip = VideoFileClip('input.mp4')
    
    # Gera os subclips e aplica o algoritmo em cada um
    subclips = [video_clip.subclip(i, i + subclip_duration) for i in range(0, int(duration), subclip_duration)]
    results = [detect_faces(subclip) for subclip in subclips]
    
    # Concatena os resultados em um único vídeo
    final_clip = concatenate_videoclips(results)
    
    # Exporta o vídeo final
    final_clip.write_videofile("output.mp4", audio_codec='aac')
    
    # Remove o arquivo de entrada
    os.remove('input.mp4')
    
    return render_template('result.html')

# Função para detectar os rostos em um vídeo
def detect_faces(clip):
    # Aplica o algoritmo de detecção de faces
    faces = (VideoFileClip.detect_faces)(clip, detector='hog')

    # Desenha os retângulos ao redor dos rostos detectados
    for face in faces:
        x, y, w, h = face['box']
        clip = (clip.fx(vfx.draw_rect, x, y, w, h, color=(255, 0, 0)))

    return clip

if __name__ == '__main__':
    app.run(debug=True)
