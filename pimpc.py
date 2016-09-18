#!/usr/local/bin/python

import pygame.mixer
from pygame.mixer import Sound

pygame.mixer.init()

drum = Sound("samples/factory/Bassdrum.wav")
snare_one = Sound('samples/factory/Snare 1.wav')

while True:
    drum.play()