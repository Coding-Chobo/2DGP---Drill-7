from pico2d import *
import random
# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
    
    def draw(self):
        self.image.draw(400,30)

    def update(self):
        pass

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100,700),90
        self.frame = random.randint(0,7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self. x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100,0,100,100,self.x,self.y)

class SmallBall:
    def __init__(self):
        self.x, self.y = random.randint(100,700),599
        self.speed = random.randint(4,7)
        self.image = load_image('ball21x21.png')

    def update(self):
        if self.y > 60 :
            self.y -= self.speed
        else:
            self.y = 60

    def draw(self):
        self.image.draw(self.x,self.y)

class BigBall:
    def __init__(self):
        self.x, self.y = random.randint(100,700),599
        self.speed = random.randint(4,7)
        self.image = load_image('ball41x41.png')

    def update(self):
        if self.y > 70 :
            self.y -= self.speed
        else:
            self.y = 70

    def draw(self):
        self.image.draw(self.x,self.y)




def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
def reset_world():
    global running
    global grass
    global smallballs
    global bigballs
    global world
    global team

    running = True
    world = []

    grass = Grass()
    world.append(grass)

    smallballs = [SmallBall() for i in range(10)]
    bigballs = [BigBall() for i in range(10)]
    team = [Boy() for i in range(10)]
    world += smallballs
    world += bigballs
    world += team
def update_world():
    for o in world:
        o.update()
    pass

def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()

open_canvas()

# initialization code
reset_world()
# game main loop code

while running :
    handle_events()
    update_world()
    render_world()
    delay(0.05)
# finalization code

close_canvas()
