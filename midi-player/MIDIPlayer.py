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
start_time = time.ticks_ms()

#
# Setup game
#
def setup():
    thumby.display.setFPS(60)
    thumby.display.setFont("/lib/font5x7.bin", 5, 7, 1)

#
# Main update step
#
def update():
    global bar_progress
    global note_index
    global last_note_start
    
    total_notes = len(TRACK)
    if (note_index == total_notes):
        print('End of notes')
        time.sleep(2)
        thumby.reset()
        
    # Has next note started?
    note = TRACK[note_index]
    if (time.ticks_ms() - start_time > note[2] * 1000):
        # Move progress bar (offset by 1 visually)
        bar_progress = int(round(WIDTH * (note_index + 1) / total_notes))
        
        # Play next note if it's time
        freq = int(PITCH_TABLE[note[1]])
        duration = int((note[3] - note[2]) * 1000)
        print(note, freq, duration)
        thumby.audio.playBlocking(freq, duration)
        
        # Go to next note
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