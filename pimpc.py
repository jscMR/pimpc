#!/usr/local/bin/python

import pygame.mixer
from pygame.mixer import Sound
from gpiozero import Button
from signal import pause

pygame.mixer.init()

# Buttons
button_drum = Button(2)
button_snare = Button(3)
button_hihat = Button(4)

# Samples
drum = Sound("samples/factory/Bassdrum.wav")
snare_one = Sound('samples/factory/Snare 1.wav')
hit_hat = Sound('samples/factory/Open Hat.wav')


# Press buttons
button_drum.when_pressed = drum.play
button_snare.when_pressed = snare_one.play
button_hihat.when_pressed = hit_hat.play

pause()