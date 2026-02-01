init python:
    heart_spawn_min = 1.2
    heart_spawn_max = 1.21
    heart_success_range = 200
    heart_speed = 6
    heart_time = 15.0

    def check_image_pos(hearts, check_left):
        global total_good
        global total_bad
        closest_heart = None
        for heart in hearts:
            # we want to make sure we are checking hearts in the right direction
            if (heart.move_left == check_left):
                # Calculate the closest heart to the middle of the screen
                if (closest_heart is None):
                    closest_heart = heart
                elif (abs(closest_heart.x - config.screen_width / 2) > abs(heart.x - config.screen_width / 2)):
                    closest_heart = heart
        
        # If we actually have a heart on the specific side, we should check if the skill check was good
        if (closest_heart is not None):
            dist_to_middle = abs(closest_heart.x - config.screen_width / 2)
            if (dist_to_middle < heart_success_range):
                print("Good!")
                total_good += 1
            else:
                print("Bad!")
                total_bad += 1

            hearts.remove(closest_heart)
        closest_heart = None
        return

    def spawn_heart(hearts, spawn_left):
        xpos = 0 if spawn_left else config.screen_width
        Heart = MovingHeart(xpos, spawn_left)
        hearts.append(Heart)

    def tick_hearts(hearts):
        hearts_to_delete = []
        for heart in hearts:
            dir = 1 if heart.move_left else -1
            heart.x = heart.x + (heart_speed * dir)
            reached_end = heart.x - config.screen_width / 2 < 0

            # We dont want hearts that have passed the middle
            if (reached_end != heart.move_left):
                hearts_to_delete.append(heart)
        
        # delete hearts that have reached/passed the middle of the screen
        for heart in hearts_to_delete:
            hearts.remove(heart)
                
    def spawn_random_heart(hearts):
        if (renpy.random.choice([True, False])):
            dir = renpy.random.choice([True, False])
            spawn_two = renpy.random.choice([True, False])
            
            spawn_heart(hearts, dir)
            if (spawn_two):
                spawn_heart(hearts, not dir)

    def randomize_heart_rate():
        heartdelay = renpy.random.uniform(heart_spawn_min, heart_spawn_max)

    def update_game_time():
        global time_elapsed
        global total_bad
        time_elapsed += 0.1

    class MovingHeart:
        def __init__(self, x, move_left):
            self.x = x
            self.move_left = move_left
        
image heart_left = "images/heart_game/Heart_Left.png"
image heart_right = "images/heart_game/Heart_Right.png"
image heart_middle = "images/heart_game/Heart_Middle.png"
label heartgame:
    default hearts = []

    show screen spawnhearts
    show screen tickhearts
    show screen gametime
    call screen heartimages

    hide screen gametime
    hide screen tickhearts
    hide screen spawnhearts
    return total_bad <= 0

label losegame:
    my talk "You died! RIP"
    return False

screen tickhearts:
    timer 0.01:
        repeat True
        action Function(tick_hearts, hearts)

default time_elapsed = 0.0
screen gametime:
    timer 0.1:
        repeat True
        action Function(update_game_time)

define heartdelay = 0.5
default total_good = 0
default total_bad = 0

screen spawnhearts:
    timer heartdelay:
        repeat True
        action [Function(spawn_random_heart, hearts), Function(randomize_heart_rate)]

screen heartimages:
    for heart in hearts:
        if (heart.move_left):
            add "heart_left":
                xpos heart.x
                ypos 0.5
                anchor (0.5, 0.5)
        else:
            add "heart_right":
                xpos heart.x
                ypos 0.5
                anchor (0.5, 0.5)
        

    add "heart_middle":
        xpos 0.5
        ypos 0.5
        anchor (0.5, 0.5)
    
    key "mouseup_1" action Function(check_image_pos, hearts, True)
    key "mouseup_3" action Function(check_image_pos, hearts, False)

    if (time_elapsed >= heart_time or total_bad > 5):
        timer 0.1 action Return(0)