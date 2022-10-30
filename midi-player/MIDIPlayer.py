import thumby
import time # has a funny way of playing jokes on you while you're waiting for what you think you know will happen next
import os
import gc

WIDTH = thumby.display.width
HEIGHT = thumby.display.height
WHITE = 1

TRACKS = os.listdir('/Games/MIDIPlayer/tracks')
NUM_TRACKS = len(TRACKS)

# Load screen
thumby.display.setFont("/lib/font5x7.bin", 5, 7, 1)
thumby.display.drawText("Controls:", 2, 2, WHITE)
thumby.display.drawText("L/R: Change", 2, 11, WHITE)
thumby.display.drawText(str(NUM_TRACKS) + " tracks", 2, 32, WHITE)
thumby.display.update()
while not thumby.buttonA.justPressed():
    pass

# Static data
NOTE_SPRITE_DATA = bytearray([0,0,0,0,0,252,252,60,62,62,30,30,30,30,31,31,31,255,0,0,0,0,0,128,128,255,255,0,0,0,0,0,0,128,192,224,224,255,0,0,0,0,15,15,15,7,3,0,0,0,0,0,0,3,7,7,3,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
NOTE_SPRITE = thumby.Sprite(20, 20, NOTE_SPRITE_DATA, 50, 17)
PITCH_TABLE = __import__('/Games/MIDIPlayer/pitch_table').PITCH_TABLE

thumby.display.setFPS(60)

# Music to play
TRACK = None
FILE_NAME = None

# Player state
bar_width = 0
track_index = 0
note_index = 0
start_time = 0
total_notes = 0
        
#
# Restart track playing progress
#
def restart_track():
    global note_index
    global start_time
    global bar_width

    note_index = 0
    bar_width = 0
    start_time = time.ticks_ms()
    thumby.display.update()
    
#
# Load a track at given index
def load_track(index):
    global track_index
    global TRACK
    global FILE_NAME
    global total_notes
    
    thumby.audio.stop()
    
    # Show process
    thumby.display.fill(0)
    thumby.display.drawText("Loading...", 2, 2, WHITE)
    thumby.display.update()
    
    # Try and free
    TRACK = None
    print('Free pre-gc: ' + str(gc.mem_free()))
    gc.collect()
    print('Free after gc: ' + str(gc.mem_free()))
    
    # Load next
    track_index = index
    loaded = __import__('/Games/MIDIPlayer/tracks/' + TRACKS[track_index].split('.')[0])
    print('Free after load: ' + str(gc.mem_free()))
    TRACK = loaded.TRACK
    FILE_NAME = loaded.FILE_NAME
    total_notes = len(TRACK)
    restart_track()
    
#
# Handle updating playback
#
def update_playback():
    global bar_width
    global note_index
    global last_note_start
    
    # Reached the end?
    if (note_index == total_notes):
        print('End of notes')
        return
        
    _track, pitch, start, end = TRACK[note_index]
    
    # Has next note started yet?
    if (time.ticks_ms() - start_time >= start * 1000):
        print(start_time, _track, pitch, start, end)

        # Move progress bar (offset by 1 visually)
        bar_width = int(round(WIDTH * (note_index + 1) / total_notes))
        
        # Play next note if it's time
        freq = int(PITCH_TABLE[pitch])
        duration = int((end - start) * 1000)
        thumby.audio.play(freq, duration)
        
        # Go to next note
        note_index = note_index + 1

# Handle input
def update_input():
    global note_index

    # Previous track
    if thumby.buttonL.justPressed():
        # Restart song instead
        if track_index == 0:
            restart_track()
            return
        
        # Go back a track
        load_track(track_index - 1)
        
    # Next track
    if thumby.buttonR.justPressed():
        if (track_index < NUM_TRACKS - 1):
            load_track(track_index + 1)

#
# Main update step
#
def update():
   update_playback()
   update_input()

#
# Main draw step
#
def draw():
    thumby.display.fill(0)
    
    # Song name
    thumby.display.drawText(FILE_NAME, 2, 5, WHITE)
    
    # Notes progrss
    song_progress = "" + str(note_index) + "/" + str(total_notes)
    thumby.display.drawText(song_progress, 2, 15, WHITE)
    
    # Progress bar
    thumby.display.drawFilledRectangle(0, 0, bar_width, 2, WHITE)
    
    # Icon
    thumby.display.drawSprite(NOTE_SPRITE)

# Game
try:
    # init
    load_track(track_index)
    start_time = time.ticks_ms()

    while(True):
        update()
        draw()
        thumby.display.update()
except Exception as e:
    print(e)
    f = open("/crash.log", "w")
    f.write(str(e))
    f.close()
    thumby.display.fill(0)
    thumby.display.drawText('Crashed :(', 2, 5, WHITE)
    thumby.display.update()