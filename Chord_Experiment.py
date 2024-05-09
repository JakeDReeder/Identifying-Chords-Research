# Jake Reeder - May 9, 2024

# This code serves as some sort of proof of concept, to see if my hunch about what
# comparing chords will look like is correct. I will be commenting code as I am working
# all of this out so you can see the thought process. All snippets of code between comments
# were executed in a jupyter notebook.

# BACKGROUND INFO

# In music, chords are the when three or more musical notes are played simultaneously.
# The quality of the chord (whether it is major, minor, or diminisheed) is defined by
# distance between each note or interval. 

# HOW I THINK THIS WILL GO:

# My hypothesis (which may be elementary to some) is if you take two chords that have the 
# same quality, and normalize their frequency and amplitude, they will essentially be the same. 
# Test this hypothesis, for now, I will simulates chords using a sin function to mimic the 
# behavior of a sound wave. 

# SIN FUNCTION DEFINITION: f(t) = amplitude * sin((2pi * frequency * t) + phi)
#   amplitude - the volume of the sound (how loud the sound is)
#   2pi - serves as a conversion of the frequency from herts to radians
#   frequency - how often a phase or pattern of the wave repeats 
#   phi - the starting position of the phase. 
#   t - represents time in seconds
# this function will be used to simulate the notes contained a chord

# TESTING OUT THE SIN FUNCTION - BLOCK 1

import numpy as np 
import matplotlib.pyplot as plt

# defining sound wave function
def musical_note(t, frequency, amplitude=0.2, phi = 0):
    return amplitude * np.sin((2 * np.pi * frequency * t) + phi)

# generating time points 
t = np.linspace(0, 0.01, 1000) # 10 ms of time

# frequency of C in octave 4
c_freq = 261.63 # Hz

# generating wave C
c = musical_note(t, c_freq)

# plotting the sound wave of C
plt.plot(t, c)
plt.title("Sine Wave for Musical Note C (261.63 Hz)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()

# LOOKS LIKE IT WORKS! COOL!
# MOVING ON!

# EXPERIMENT

# since a musical chord is just the combination of three or more notes,
# we can think of it as one note + another note + another

# BLOCK 2

# C Major chord contains the notes C + E + G
e_freq = 329.63 # frequency of E in octave 4 in Hz
g_freq = 392.0 # frequency of G in octave 4 in Hz

e = musical_note(t, e_freq)
g = musical_note(t, g_freq)

#defining a C Major Chord
c_major = c + e + g

# plotting soundwave of c major chord
plt.plot(t, c_major)
plt.title("Sine Wave for Musical Chord C Major")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()


# BLOCK 3

# Now lets make an F Major chord contains the notes F + A + C
f_freq = 174.61 # frequency of F in octave 3 in Hz
a_freq = 220.0 # frequency of A in octave 3 in Hz

f = musical_note(t, f_freq)
a = musical_note(t, a_freq)

#defining a C Major Chord
f_major = f + a + c

# plotting soundwave of f major chord
plt.plot(t, f_major)
plt.title("Sine Wave for Musical Chord F Major")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()

# GREAT! WE NOW HAVE TWO CHORDS TO COMPARE!

# BLOCK 4

# Normalizing chords to compare them
c_major_norm = c_major / np.sum(c_major)
f_major_norm = f_major / np.sum(f_major)

# plotting soundwave of  normalized c major chord
plt.plot(t, c_major_norm)
plt.title("Normalized Sine Wave for Musical Chord C Major")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()

# plotting soundwave of  normalized f major chord
plt.plot(t, f_major_norm)
plt.title("Normalized Sine Wave for Musical Chord F Major")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()