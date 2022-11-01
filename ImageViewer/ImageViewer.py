import thumby
import os
import gc

WIDTH = thumby.display.width
HEIGHT = thumby.display.height
WHITE = 1

IMAGES = os.listdir('/Games/ImageViewer/images')
print(IMAGES)
NUM_IMAGES = len(IMAGES)

# Load screen
thumby.display.setFont("/lib/font5x7.bin", 5, 7, 1)
thumby.display.drawText("Controls:", 2, 2, WHITE)
thumby.display.drawText("L/R: Change", 2, 11, WHITE)
thumby.display.drawText(str(NUM_IMAGES) + " images", 2, 32, WHITE)
thumby.display.update()
while not thumby.buttonA.justPressed():
    pass

thumby.display.setFPS(1)

# Music to play
IMAGE = None

# Player state
image_index = 0
    
#
# Load a image at given index
def load_image(index):
    global image_index
    global IMAGE
    
    # Show process
    thumby.display.fill(0)
    thumby.display.drawText("Loading...", 2, 2, WHITE)
    thumby.display.update()
    
    # Try and free
    IMAGE = None
    print('Free pre-gc: ' + str(gc.mem_free()))
    gc.collect()
    print('Free after gc: ' + str(gc.mem_free()))
    
    # Load next
    image_index = index
    IMAGE = thumby.Sprite(72, 40, "/Games/ImageViewer/images/" + IMAGES[image_index], 0, 0)
    print('Free after load: ' + str(gc.mem_free()))
    
# Handle input
def update_input():
    # Previous image
    if thumby.buttonL.justPressed():
        # Do nothing
        if image_index == 0:
            return
        
        # Go back a track
        load_image(image_index - 1)
        
    # Next image
    if thumby.buttonR.justPressed():
        if (image_index < NUM_IMAGES - 1):
            load_image(image_index + 1)

#
# Main update step
#
def update():
   update_input()

#
# Main draw step
#
def draw():
    thumby.display.fill(0)
    
    # Image
    thumby.display.drawSprite(IMAGE)

# Game
try:
    # init
    load_image(image_index)

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
