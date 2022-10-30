import thumby
import time # has a funny way of playing jokes on you while you're waiting for what you think you know will happen next

WIDTH = thumby.display.width
HEIGHT = thumby.display.height
WHITE = 1

# Load screen
thumby.display.setFPS(60)
thumby.display.setFont("/lib/font5x7.bin", 5, 7, 1)
thumby.display.drawText("Loading...", 2, 2, WHITE)
thumby.display.update()

# note.png
note_sprite_data = bytearray([0,0,0,0,0,252,252,60,62,62,30,30,30,30,31,31,31,255,0,0,0,0,0,128,128,255,255,0,0,0,0,0,0,128,192,224,224,255,0,0,0,0,15,15,15,7,3,0,0,0,0,0,0,3,7,7,3,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
note_sprite = thumby.Sprite(20, 20, note_sprite_data, 50, 17)

# Music to play
PITCH_TABLE = __import__('/Games/MIDIPlayer/pitch_table').PITCH_TABLE
track = __import__('/Games/MIDIPlayer/track')
TRACK = track.TRACK
FILE_NAME = track.FILE_NAME

bar_width = 0
note_index = 0
start_time = time.ticks_ms()
total_notes = len(TRACK)

#
# Main update step
#
def update():
    global bar_width
    global note_index
    global last_note_start
    
    # Reached the end?
    if (note_index == total_notes):
        print('End of notes')
        time.sleep(2)
        thumby.reset()
        
    # Has next note started yet?
    note = TRACK[note_index]
    _track, pitch, start, end = note
    if (time.ticks_ms() - start_time > start * 1000):
        # Move progress bar (offset by 1 visually)
        bar_width = int(round(WIDTH * (note_index + 1) / total_notes))
        
        # Play next note if it's time
        freq = int(PITCH_TABLE[pitch])
        duration = int((end - start) * 1000)
        print(note, freq, duration)
        thumby.audio.play(freq, duration)
        
        # Go to next note
        note_index = note_index + 1
    
#
# Main draw step
#
def draw():
    thumby.display.fill(0)
    
    # Song name
    thumby.display.drawText(FILE_NAME, 2, 5, WHITE)
    
    # Notes progrss
    SONG_PROGRESS = "" + str(note_index) + "/" + str(total_notes)
    thumby.display.drawText(SONG_PROGRESS, 2, 15, WHITE)
    
    # Progress bar
    thumby.display.drawFilledRectangle(0, 0, bar_width, 2, WHITE)
    
    # Icon
    thumby.display.drawSprite(note_sprite)

# Game
try:
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