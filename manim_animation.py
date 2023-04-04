from manim import *
import random

class TextScene(Scene):
    def construct(self, text):
        text = Text(text, font="Arial")
        self.play(Write(text))
        self.wait(2)
        self.play(Unwrite(text))

class ManimAnimation:
    def __init__(self, text):
        self.text = text

    def generate_animation(self):
        scene = TextScene(self.text)
        animation = scene.animate.run_time(2)
        return animation
