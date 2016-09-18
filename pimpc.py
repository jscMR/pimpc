#!/usr/local/bin/python

import pygame.mixer
from pygame.mixer import Sound
from gpiozero import Button
from signal import pause

pygame.mixer.init()

button = Button(2)
drum = Sound("samples/factory/Bassdrum.wav")
snare_one = Sound('samples/factory/Snare 1.wav')

button.when_pressed = drum.play

pause()