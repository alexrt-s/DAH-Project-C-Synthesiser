import numpy as np
import pygame, time, math
import pylab as pl
from DAH import MCP23S17
import os
from time import sleep
from alive_progress import alive_bar


mcp0 = MCP23S17(chip=0, address=0x20)

# Some constants
outputRate = 44100
maxAmplitude = np.iinfo( np.int16 ).max

# Create an array containing a sine wave
def SineWave( pitch, volume, duration ):

    global outputRate, maxAmplitude

    # Create the output buffer
    totalSamples = int( outputRate * duration )
    outputBuffer = np.zeros( ( totalSamples, 2 ), dtype=np.int16 )

    # Calculate amplitude
    amplitude = int( maxAmplitude * volume )

    # Calculate change in the wave for each output sample
    waveStep = float( pitch / outputRate ) * 2.0 * math.pi

    # Fill buffer
    for i in range( totalSamples ):

        # Left channel
        outputBuffer[i][0] = amplitude * np.sin( i * waveStep )

        # Right channel
        outputBuffer[i][1] = amplitude * np.sin( i * waveStep )


    return outputBuffer

# Create an array containing a square wave
def SquareWave( pitch, volume, duration ):

    global outputRate, maxAmplitude

    # Create the output buffer
    totalSamples = int( outputRate * duration )
    outputBuffer = np.zeros( ( totalSamples, 2 ), dtype=np.int16 )

    # Calculate amplitude
    amplitude = int( maxAmplitude * volume )

    # Calculate change in the wave for each output sample
    waveStep = float( pitch / outputRate ) * 2.0 * math.pi

    # Fill buffer
    for i in range( totalSamples ):

        # Left channel
        outputBuffer[i][0] = amplitude * np.sin(i*waveStep)
        if outputBuffer[i][0] > 0:
            outputBuffer[i][0] = 1 * amplitude
        if outputBuffer[i][0] < 0:
            outputBuffer[i][0] = 0 * amplitude
        

        # Right channel
        outputBuffer[i][1] = amplitude * np.sin(i*waveStep)
        if outputBuffer[i][1] > 0:
            outputBuffer[i][1] = 1 * amplitude
        if outputBuffer[i][1] < 0:
            outputBuffer[i][1] = 0 * amplitude


    return outputBuffer

def load_notes():
    # Set up the audio output - only once!
    # 2-channel (stereo), 16-bit signed integer value output at 44khz
    pygame.mixer.init( frequency=outputRate, channels=2, size=-16)

    print('Initialising ...')

    #create each musical note that is to be used. this takes ~ 3 minutes,
    #thus a progress bar (which does not noticeably reduce the speed at which 
    #the notes load) has been added.
    for total in 8,:
        with alive_bar(total,bar='notes') as bar:
            for _ in range(1):

                C4 = SineWave( 262, 1.0, 1.0 )
                D4 = SineWave( 294, 1.0, 1.0 )
                E4 = SineWave( 330, 1.0, 1.0 )
                F4 = SineWave( 349, 1.0, 1.0 )
                G4 = SineWave( 392, 1.0, 1.0 )
                A4 = SineWave( 440, 1.0, 1.0 )
                B4 = SineWave( 494, 1.0, 1.0 )
                noteC4 = pygame.mixer.Sound( buffer=C4 )
                noteD4 = pygame.mixer.Sound( buffer=D4 )
                noteE4 = pygame.mixer.Sound( buffer=E4 )
                noteF4 = pygame.mixer.Sound( buffer=F4 )
                noteG4 = pygame.mixer.Sound( buffer=G4 )
                noteA4 = pygame.mixer.Sound( buffer=A4 )
                noteB4 = pygame.mixer.Sound( buffer=B4 )
                notes4 = [noteC4,noteD4,noteE4,noteF4,noteG4,noteA4,noteB4]
                bar()

                C3 = SineWave( 262/2, 1.0, 1.0 )
                D3 = SineWave( 294/2, 1.0, 1.0 )
                E3 = SineWave( 330/2, 1.0, 1.0 )
                F3 = SineWave( 349/2, 1.0, 1.0 )
                G3 = SineWave( 392/2, 1.0, 1.0 )
                A3 = SineWave( 440/2, 1.0, 1.0 )
                B3 = SineWave( 494/2, 1.0, 1.0 )
                noteC3 = pygame.mixer.Sound( buffer=C3 )
                noteD3 = pygame.mixer.Sound( buffer=D3 )
                noteE3 = pygame.mixer.Sound( buffer=E3 )
                noteF3 = pygame.mixer.Sound( buffer=F3 )
                noteG3 = pygame.mixer.Sound( buffer=G3 )
                noteA3 = pygame.mixer.Sound( buffer=A3 )
                noteB3 = pygame.mixer.Sound( buffer=B3 )
                notes3 = [noteC3,noteD3,noteE3,noteF3,noteG3,noteA3,noteB3]
                bar()

                C2 = SineWave( 262/4, 1.0, 1.0 )
                D2 = SineWave( 294/4, 1.0, 1.0 )
                E2 = SineWave( 330/4, 1.0, 1.0 )
                F2 = SineWave( 349/4, 1.0, 1.0 )
                G2 = SineWave( 392/4, 1.0, 1.0 )
                A2 = SineWave( 440/4, 1.0, 1.0 )
                B2 = SineWave( 494/4, 1.0, 1.0 )
                noteC2 = pygame.mixer.Sound( buffer=C2 )
                noteD2 = pygame.mixer.Sound( buffer=D2 )
                noteE2 = pygame.mixer.Sound( buffer=E2 )
                noteF2 = pygame.mixer.Sound( buffer=F2 )
                noteG2 = pygame.mixer.Sound( buffer=G2 )
                noteA2 = pygame.mixer.Sound( buffer=A2 )
                noteB2 = pygame.mixer.Sound( buffer=B2 )
                notes2 = [noteC2,noteD2,noteE2,noteF2,noteG2,noteA2,noteB2]
                bar()

                C5 = SineWave( 262*2, 1.0, 1.0 )
                D5 = SineWave( 294*2, 1.0, 1.0 )
                E5 = SineWave( 330*2, 1.0, 1.0 )
                F5 = SineWave( 349*2, 1.0, 1.0 )
                G5 = SineWave( 392*2, 1.0, 1.0 )
                A5 = SineWave( 440*2, 1.0, 1.0 )
                B5 = SineWave( 494*2, 1.0, 1.0 )
                noteC5 = pygame.mixer.Sound( buffer=C5 )
                noteD5 = pygame.mixer.Sound( buffer=D5 )
                noteE5 = pygame.mixer.Sound( buffer=E5 )
                noteF5 = pygame.mixer.Sound( buffer=F5 )
                noteG5 = pygame.mixer.Sound( buffer=G5 )
                noteA5 = pygame.mixer.Sound( buffer=A5 )
                noteB5 = pygame.mixer.Sound( buffer=B5 )
                notes5 = [noteC5,noteD5,noteE5,noteF5,noteG5,noteA5,noteB5]
                bar()

                notes_tot = [notes2,notes3,notes4,notes5]

                sC4 = SquareWave( 262, 1.0, 1.0 )
                sD4 = SquareWave( 294, 1.0, 1.0 )
                sE4 = SquareWave( 330, 1.0, 1.0 )
                sF4 = SquareWave( 349, 1.0, 1.0 )
                sG4 = SquareWave( 392, 1.0, 1.0 )
                sA4 = SquareWave( 440, 1.0, 1.0 )
                sB4 = SquareWave( 494, 1.0, 1.0 )
                snoteC4 = pygame.mixer.Sound( buffer=sC4 )
                snoteD4 = pygame.mixer.Sound( buffer=sD4 )
                snoteE4 = pygame.mixer.Sound( buffer=sE4 )
                snoteF4 = pygame.mixer.Sound( buffer=sF4 )
                snoteG4 = pygame.mixer.Sound( buffer=sG4 )
                snoteA4 = pygame.mixer.Sound( buffer=sA4 )
                snoteB4 = pygame.mixer.Sound( buffer=sB4 )
                snotes4 = [snoteC4,snoteD4,snoteE4,snoteF4,snoteG4,snoteA4,snoteB4]
                bar()

                sC3 = SquareWave( 262/2, 1.0, 1.0 )
                sD3 = SquareWave( 294/2, 1.0, 1.0 )
                sE3 = SquareWave( 330/2, 1.0, 1.0 )
                sF3 = SquareWave( 349/2, 1.0, 1.0 )
                sG3 = SquareWave( 392/2, 1.0, 1.0 )
                sA3 = SquareWave( 440/2, 1.0, 1.0 )
                sB3 = SquareWave( 494/2, 1.0, 1.0 )
                snoteC3 = pygame.mixer.Sound( buffer=sC3 )
                snoteD3 = pygame.mixer.Sound( buffer=sD3 )
                snoteE3 = pygame.mixer.Sound( buffer=sE3 )
                snoteF3 = pygame.mixer.Sound( buffer=sF3 )
                snoteG3 = pygame.mixer.Sound( buffer=sG3 )
                snoteA3 = pygame.mixer.Sound( buffer=sA3 )
                snoteB3 = pygame.mixer.Sound( buffer=sB3 )
                snotes3 = [snoteC3,snoteD3,snoteE3,snoteF3,snoteG3,snoteA3,snoteB3]
                bar()

                sC2 = SquareWave( 262/4, 1.0, 1.0 )
                sD2 = SquareWave( 294/4, 1.0, 1.0 )
                sE2 = SquareWave( 330/4, 1.0, 1.0 )
                sF2 = SquareWave( 349/4, 1.0, 1.0 )
                sG2 = SquareWave( 392/4, 1.0, 1.0 )
                sA2 = SquareWave( 440/4, 1.0, 1.0 )
                sB2 = SquareWave( 494/4, 1.0, 1.0 )
                snoteC2 = pygame.mixer.Sound( buffer=sC2 )
                snoteD2 = pygame.mixer.Sound( buffer=sD2 )
                snoteE2 = pygame.mixer.Sound( buffer=sE2 )
                snoteF2 = pygame.mixer.Sound( buffer=sF2 )
                snoteG2 = pygame.mixer.Sound( buffer=sG2 )
                snoteA2 = pygame.mixer.Sound( buffer=sA2 )
                snoteB2 = pygame.mixer.Sound( buffer=sB2 )
                snotes2 = [snoteC2,snoteD2,snoteE2,snoteF2,snoteG2,snoteA2,snoteB2]
                bar()

                sC5 = SquareWave( 262*2, 1.0, 1.0 )
                sD5 = SquareWave( 294*2, 1.0, 1.0 )
                sE5 = SquareWave( 330*2, 1.0, 1.0 )
                sF5 = SquareWave( 349*2, 1.0, 1.0 )
                sG5 = SquareWave( 392*2, 1.0, 1.0 )
                sA5 = SquareWave( 440*2, 1.0, 1.0 )
                sB5 = SquareWave( 494*2, 1.0, 1.0 )
                snoteC5 = pygame.mixer.Sound( buffer=sC5 )
                snoteD5 = pygame.mixer.Sound( buffer=sD5 )
                snoteE5 = pygame.mixer.Sound( buffer=sE5 )
                snoteF5 = pygame.mixer.Sound( buffer=sF5 )
                snoteG5 = pygame.mixer.Sound( buffer=sG5 )
                snoteA5 = pygame.mixer.Sound( buffer=sA5 )
                snoteB5 = pygame.mixer.Sound( buffer=sB5 )
                snotes5 = [snoteC5,snoteD5,snoteE5,snoteF5,snoteG5,snoteA5,snoteB5]

                snotes_tot = [snotes2,snotes3,snotes4,snotes5]

                #the notes are added to a 2d array: Notes[0] contains all of the sine
                #wave notes and Notes[1] all of the square waves
                Notes = [notes_tot,snotes_tot]
                bar()

                print('sounds loaded!')

                return Notes

def synthesiser(Notes):

    #count is a dummy variable that keeps track of the octave that the synthesiser is in
    #count2 keeps track of whether the output is a square or sinusoidal wave.
    count = 1
    count2 = 1
    #the synthesiser runs indefinitely
    while True:
        print('count: ', count)

        #if the button connected to channel 13 is pushed, count increases by 1.
        #Increasing the value of count shifts the pitch of the notes up by one octave
        #If the value of count = 2 when the button is pressed, it is reset and the 
        #notes return to the lowest octave.
        if mcp0.digitalRead(13) is True:
            if count != 2:
                count +=1
                sleep(2)
            else:
                count = -1
                sleep(2)
        #selecting the correct octave based on the value of count
        if count == 1:
            notes1 = 2
        elif count == 0:
            notes1 = 1
        elif count == -1:
            notes1 = 0
        elif count ==2:
            notes1 =3
             
        print('count2: ', count2)

        #if the button connected to channel 14 is pushed, count2 increases by 1.
        #Changing the value of count2 alternates the output between sine waves
        #and square waves. If count2 = 2, the value is reset
        if mcp0.digitalRead(14) is True:
            if count2 != 2:
                count2 +=1
                sleep(2)
            else:
                count2 = 1
                sleep(2)
        if count2 ==1:
            notes0 = 0
        if count2 == 2:
            notes0 = 1
        notes = Notes[notes0][notes1]
        
        '''
        #If the output is square waves, this would turn on an LED connected to channel 12.
        #It is commented out because the LED was determined to be unnecessary and thus was
        #removed from the breadboard.

        if count2 == 2:
            mcp0.digitalWrite(12,True)
        else:
            mcp0.digitalWrite(12,False)
        '''   
            
        
        #simultaneously reads in the input from all of the pins
        # in 16 bit binary
        read_in = format(mcp0.portRead(),'016b')
        print(read_in)
        binary = np.array([])
        
        #selects only the inputs from the pins that are connected to buttons
        # that are associated with musical notes.
        for digit in read_in[8:16]:
            binary = np.append(binary,digit)
            
        print(binary)
        
        #for each button that corresponds to a note, if the button is pressed,
        #the reading will be 1, or 0 if it is not
        #if the reading is 1, the note is played
        #there is very little time between the iterations which allows
        #there to be multiple notes played effectively simultaneously
        for i in range (0,len(binary)):
            if int(binary[i]) == 1:
                notes[i-1].play()


def main():
    #loads the notes in and then starts the infinite loop that allows the synthesiser to be 
    #played
    synthesiser(load_notes)



main()