import thumby
import sys
import time # has a funny way of playing jokes on you while you're waiting for what you think you know will happen next
TRACK = __import__('/Games/MIDIPlayer/track').TRACK
PITCH_TABLE = __import__('/Games/MIDIPlayer/pitch_table').PITCH_TABLE

WIDTH = thumby.display.width
HEIGHT = thumby.display.height
WHITE = 1
SONG_NAME = 'Still Alive'

bar_progress = 0
note_index = 0

#
# Setup game
#
def setup():
    thumby.display.setFPS(30)
    thumby.display.setFont("/lib/font5x7.bin", 5, 7, 1)

#
# Main update step
#
def update():
    global bar_progress
    global note_index
    
    total_notes = len(TRACK)
    if (note_index == total_notes):
        print('End of notes')
        time.sleep(2)
        thumby.reset()
    
    # Move progress bar (offset by 1 visually)
    bar_progress = int(round(WIDTH * (note_index + 1) / total_notes))
    
    # Play next note
    freq = int(PITCH_TABLE[TRACK[note_index][1]])
    duration = int((TRACK[note_index][3] - TRACK[note_index][2]) * 1000)
    print(TRACK[note_index], freq, duration)
    thumby.audio.playBlocking(freq, duration)
    note_index = note_index + 1
    
#
# Main draw step
#
def draw():
    thumby.display.fill(0)
    thumby.display.drawText(SONG_NAME, 5, 16, WHITE)
    thumby.display.drawFilledRectangle(0, 0, bar_progress, 2, WHITE)

# Game
try:
    setup()
    while(True):
        update()
        draw()
        thumby.display.update()
    print('exited')
except Exception as e:
    print(e)
    f = open("/crash.log", "w")
    f.write(str(e))
    f.close()