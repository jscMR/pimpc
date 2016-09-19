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

def play_sound (index):
    print('Play sound ' + str(index))
    arrange[index].play()

# -----------------
# Press buttons
# -----------------

while True:
    # Drum
    if button_drum.is_pressed:
        print("Drum is pressed")
        play_sound(0)
    
    if button_snare.is_pressed:
        print('Snare is pressed')
        play_sound(1)
    
    if button_hihat.is_pressed:
        print('Hihat is pressed')
        play_sound(2)
    
    if button_bass.is_pressed:
        print('Bass is pressed')
        play_sound(3)
    
