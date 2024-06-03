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
t = np.linspace(0, 0.1, 1000) # 10 ms of time

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

# At this point I attempted to normalize the frequency of both the chords
# to see if they matched in pattern, but this proved to be difficult. 
# I took the time to carefully compare the two chord visuals and they seem to
# have the same pattern WHICH IS GREAT!

# BLOCK 4
# for kicks and giggles, lets spice things up by comparing two minor 7 chords

t = np.linspace(0, 0.05, 1000) # 10 ms of time

# a E minor 7 chord contains E + G + B + D
e_freq = 329.63 # frequency of E in octave 4 in Hz
g_freq = 392.0 # frequency of G in octave 4 in Hz
b_freq = 493.88 # frequency of B in octave 4 in Hz
d_freq = 587.33 # frequency of D in octave 5 in Hz

e = musical_note(t, e_freq)
g = musical_note(t, g_freq)
b = musical_note(t, b_freq)
d = musical_note(t, d_freq)

e_min7 = e + g + b + d

# plotting soundwave of e minor 7 chord
plt.plot(t, e_min7)
plt.title("Sine Wave for Musical Chord E minor 7")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()

# adjust time to adjust for difference in frequency
t = np.linspace(0, 0.075, 1000) # 10 ms of time

# a A minor 7 chord contains A + C + E + G
a_freq = 220.0 # frequency of A in octave 3 in Hz
c_freq = 261.63 # frequency of C in octave 4 in Hz

a = musical_note(t, a_freq)
c = musical_note(t, c_freq)

a_min7 = a + c + e + g

# plotting soundwave of a minor 7 chord
plt.plot(t, a_min7)
plt.title("Sine Wave for Musical Chord A minor 7")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()

# Seems these two graphs match the same pattern as well!!!

# CONCLUSION: 
# Since chords of the same types have the same pattern when graphed as sin waves, I believe it can be assumed
# that a Neural Network may be able to learn these patterns and be able to identify chord types! We shall see!

# END of experiement 1
