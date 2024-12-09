import pgzrun
import random

WIDTH=800
HEIGHT=600
CENTRE_X= WIDTH/2
CENTRE_Y= HEIGHT/2
CENTRE=(CENTRE_X, CENTRE_Y)
FINAL_LEVEL=10
START_SPEED=10
ITEMS=["virus","corona","cvirus","redvirus"]

game_over=False
game_complete=False
current_level=1
items=[]
animations=[]

def draw():
    global items, current_level, game_over, game_complete
    screen.clear()
    screen.blit("back",(0,0))
    if game_over:
        screen.draw.text("Game Over", fontsize=50, center=CENTRE, color="black")
        screen.draw.text("Try Again", fontsize=50, center=(CENTRE_X, CENTRE_Y + 20), color="black")
    if game_complete:
        screen.draw.text("Good Job", fontsize=50, center=CENTRE, color="black")
        screen.draw.text("Round 2?", fontsize=50, center=CENTRE, color="black")


def get_option_to_create(number_of_extra_items):
    items_to_create=["safe"]
    for i in range(0,number_of_extra_items):
        random_option=random.choice(ITEMS)
        items_to_create.append(random_option)
    return items_to_create
def create_items(items_to_create):
    new_items=[]
    for i in items_to_create:
        it=Actor(i+"img")
        new_items.append(it)
    return new_items

def layout_items(items_to_layout):
    number_of_gaps=len(items_to_layout)+1
    random.shuffle(items_to_layout)
    gap_size=WIDTH/number_of_gaps
    for index,item in enumerate(items_to_layout):
        X_pos=(index +1)*gap_size
        item.x=X_pos

def animate_items(items_to_animate):
    global animations
    for i in items_to_animate:
        dur= max(1, START_SPEED - current_level)
        i.anchor=("center","bottom")
        animation= animate(i,duration=dur,on_finished=handle_game_over,y=HEIGHT+100)
        animations.append(animation)
def handle_game_over():
    global game_over
    game_over=True
def on_mouse_down(pos):
    global items,current_level
    for item in items:
        if item.collidepoint(pos):
            if "safe" in item.image:
                handle_game_complete()
            else:
                handle_game_over()
def handle_game_complete():
    global current_level,items,animations,game_complete
    stop_animations(animations)
    if current_level== FINAL_LEVEL:
        game_complete=True
    else:
        current_level=current_level +1
        items=[]
        animations=[]
def update():
    global items
    if len(items)==0:
        items= make_items(current_level)
def make_items(number_of_extra_items):
    items_to_create=get_option_to_create(number_of_extra_items)
    new_items=create_items(items_to_create)
    layout_items(new_items)
    animate_items(new_items)
    return new_items

def stop_animations(animations_to_stop):
    for animation in animations_to_stop:
        if animation.running:
            animation.stop()


pgzrun.go()
