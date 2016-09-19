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
button_bass = Button(17)

# Samples
drum = Sound("samples/factory/Bassdrum.wav")
snare_one = Sound('samples/factory/Snare 1.wav')
hit_hat = Sound('samples/factory/Open Hat.wav')
bass = Sound('samples/factory/Bass.wav')

arrange = [drum, snare_one, hit_hat, bass]



def play_sound (sound):
    print('Play sound ' + str(sound))
    arrange[sound].play()

# Press buttons
button_drum.when_pressed = play_sound(0)
button_snare.when_pressed = play_sound(1)
button_hihat.when_pressed = play_sound(2)
button_bass.when_pressed = play_sound(3)


pause()