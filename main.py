from turtle import Turtle, Screen
from border import Border
from sprite import Sprite, Player, Ball, Block
from txt import Scoreboard, Level, GameOver
import random
import math
import time


#------------------- Basic Setup -------------------#
# vars
timer = 0.001
blocks_to_render = []

# Create and setup screen & Pen (for Sprites)
screen = Screen()
screen.setup(500, 900)
screen.bgcolor('#AAD3CB')
screen.title('Breakout')
screen.bgpic()
screen.tracer(0)
#
pen = Turtle()
pen.speed(0)
pen.hideturtle()


# Register Shapes
screen.register_shape('assets/player.gif')
screen.register_shape('assets/block_a.gif')
screen.register_shape('assets/block_b.gif')
screen.register_shape('assets/block_c.gif')
screen.register_shape('assets/block_d.gif')
screen.register_shape('assets/block_e.gif')
screen.register_shape('assets/ball.gif')
blocks = ['assets/block_a.gif', 'assets/block_b.gif', 'assets/block_c.gif', 'assets/block_d.gif', 'assets/block_e.gif']


#------------------- Create objects on screen -------------------#
# Create border
border = Border()

# Create player
player = Player(0, -400, 59, 20, 'assets/player.gif')
player.render(pen)
# Player movement
screen.listen()
player.dx = 50
screen.onkey(player.move_right, 'Right')
screen.onkey(player.move_left, 'Left')

# Create blocks
def create_blocks():
    start_y = 350
    for i in range(5):
        start_x = -185
        block = Block(start_x, start_y, 80, 25, blocks[i])
        blocks_to_render.append(block)
        for t in range(4):
            start_x += 90
            block = Block(start_x, start_y, 80, 25, blocks[i])
            blocks_to_render.append(block)
        start_y = start_y - 35
    random.shuffle(blocks_to_render)

# Create ball & parameters
ball = Ball(0, -381, 17, 17, 'assets/ball.gif') # Ball itself

#Create lifes
life_x = 210
lives_list = []
for i in range(0, player.lives):
    life = Ball(life_x, 422, 17, 17, 'assets/ball.gif')
    lives_list.append(life)
    life_x -= 30

#Create scoreboard
scoreboard = Scoreboard()

#Create level
level = Level()



#------------------- Main Game loop -------------------#
game_on = True
while game_on:
    pen.clear()

    # If no bloks, create bloks
    if len(blocks_to_render) == 0:
        create_blocks()

    # Start game, ball goes left or right
    if ball.ab == '': # if it is end game event
        if player.x != 0: # Start moving only after player moved
            ball.n_gen() # generate number and set ball speed
    if ball.ab == 1:
        ball.move_left()
    else:
        ball.move_right()

    #Render lifes
    for life in lives_list:
        life.render(pen)


    # Collision with wall
    ## Left and right
    if ball.x >= 226 or ball.x <= -235:
        ball.bounce_x()
    ## Top
    if ball.y >= 390:
        ball.bounce_y()

    player.render(pen)
    ball.render(pen)

    for block in blocks_to_render:
        block.render(pen)

    #Collision with player
    if ball.is_aabb_collision(player):
        player.get_cor()
        ball.get_cor()
        if -1 <= (ball.border_lower - player.border_higher) <= 1:
            ball.bounce_y()


    #Collision with block
    for block in blocks_to_render:
        if ball.is_aabb_collision(block): # Detect collision with any side
            ball.get_cor()
            print(f'Ball x is {ball.x}')
            print(f'Ball y is {ball.y}')
            print(f'Ball width is {ball.width}')
            print(f'Ball height is {ball.height}')
            print('----------------------')
            print(f'Ball higher border is {ball.border_higher}')
            print(f'Ball lower border is {ball.border_lower}')
            print(f'Ball left border is {ball.border_left}')
            print(f'Ball right border is {ball.border_right}')
            print('----------------------')
            print(f'Block x is {block.x}')
            print(f'Block y is {block.y}')
            print(f'Block width is {block.width}')
            print(f'Block height is {block.height}')
            print('----------------------')
            print(f'Block higher border is {block.border_higher}')
            print(f'Block lower border is {block.border_lower}')
            print(f'Block left border is {block.border_left}')
            print(f'Block right border is {block.border_right}')
            print('----------------------')

            if (-1 <= (block.border_lower - ball.border_higher) <= 1) or \
                    (-1 <= (block.border_higher - ball.border_lower) <= 1): # Collision with lower / higher border
                ball.bounce_y()
                block.del_block(pen)
                blocks_to_render.remove(block)
                scoreboard.update_score()
                print('Block destroyed')
                print('----------------------')
                print('----------------------')
                print('----------------------')
            elif (-1 <= (block.border_left == ball.border_right) <= 1) or \
                    (-1 <= (block.border_right == ball.border_left) <= 1): # Collision with left / right border
                ball.bounce_x()
                block.del_block(pen)
                blocks_to_render.remove(block)
                scoreboard.update_score()
                print('Block destroyed')
                print('----------------------')
                print('----------------------')
                print('----------------------')
            else:
                print('Something went wrong')
                print('----------------------')
                print('----------------------')
                print('----------------------')

    # No bloks - new level
    if len(blocks_to_render) == 0:
        ball.reset()
        player.reset()
        level.update_level()
        timer *= 1.2

    # End Game events
    # Player missed ball
    if ball.y < -430:
        ball.reset()
        player.reset()
        if len(lives_list) > 0:
            del lives_list[-1]
        if player.lives == 0:
            game_on = False


    screen.update()
    time.sleep(timer)

over = GameOver()

screen.mainloop()

