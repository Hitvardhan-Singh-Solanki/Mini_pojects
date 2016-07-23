
import simplegui
import random
radius=10

width=1000
height=500

vel_p1=[0,0]
vel_p2=[0,0]
check=1

score1=0
score2=0
direction='right'


player1='Player 1'
player2='Player 2'

ball_position=[width/2, height/2 + 20]
initial_velocity=[0,0]
ball_velocity=[0,0]
color="White"
message=" "
message_speed="Select Speed"


message_width= 102
paddle_width=8
paddle_height= 80

paddle1=[[4, (height/2 - paddle_height/2)], [4, (height/2 + paddle_height/2)]]

paddle2=[[(width-paddle_width +4), (height/2 - paddle_height/2)], [(width-paddle_width+4), (height/2 + paddle_height/2)]]


def restart():
    global score1, score2, message, ball_color

    score1=0
    score2=0





def moonwalk():
    global initial_velocity, ball_velocity, shift, message_speed, message_width
    message_speed= 'Moon Walk'
    message_width= frame.get_canvas_textwidth(str(message_speed), 20)
    ball_velocity[0]=random.randrange(60,120)/20
    ball_velocity[1]=random.randrange(60,120)/25
    initial_velocity[0]=random.randrange(60,120)/20
    initial_velocity[1]=random.randrange(60,120)/25



    new_game()

def surf():
    global initial_velocity, ball_velocity, shift, message_speed, message_width
    message_speed= 'Surf'
    message_width= frame.get_canvas_textwidth(str(message_speed), 20)
    ball_velocity[0]=random.randrange(120,160)/20
    ball_velocity[1]=random.randrange(120,160)/25
    initial_velocity[0]=random.randrange(120,160)/20
    initial_velocity[1]=random.randrange(120,160)/25


    new_game()

def blitzer():
    global initial_velocity, ball_velocity, shift, message_speed, message_width
    message_speed= 'Blitzer'
    message_width= frame.get_canvas_textwidth(str(message_speed), 20)
    ball_velocity[0]=random.randrange(180,240)/20
    ball_velocity[1]=random.randrange(180,240)/25
    initial_velocity[0]=random.randrange(180,240)/20
    initial_velocity[1]=random.randrange(180,240)/25
    new_game()

def new_game():
    global check, message
    check=1
    message=" "
    spawn(direction)



def spawn(direction):
    global ball_position, initial_position, ball_velocity, color, ball_color
    color="White"
    message=" "


    initial_position=[width/2, height/2]


    if direction=='left':
        ball_position=initial_position
        ball_velocity[0]=-initial_velocity[0]
        ball_velocity[1]= -initial_velocity[1]

    if direction=='right':
        ball_position=initial_position
        ball_velocity[0]=-initial_velocity[0]
        ball_velocity[1]=-initial_velocity[1]

def draw(canvas):
    global paddle1, paddle2, score1, score2, ball_position, ball_velocity, direction, color, message, message_speed, nessage_width

     #BP1- Ball's motion
    ball_position[0]= ball_position[0] + ball_velocity[0]
    ball_position[1]= ball_position[1] + ball_velocity[1]

    #Check - Paddle's Motion
    if paddle1[0][1]<=81+2:

        paddle1[0][1]=81


        paddle1[1][1]=paddle_height +81

    elif paddle1[0][1]>=(height-paddle_height):
        paddle1[0][1]=height-paddle_height
        paddle1[1][1]=height

    if paddle2[0][1]<=81:
        paddle2[0][1]=81
        paddle2[1][1]=paddle_height + 81

    elif paddle2[0][1]>=(height-paddle_height):
        paddle2[0][1]=height-paddle_height
        paddle2[1][1]=height

    #Paddle's motion
    paddle1[0][1] += vel_p1[1]
    paddle1[1][1] += vel_p1[1]

    paddle2[0][1] += vel_p2[1]
    paddle2[1][1] += vel_p2[1]

    #Gutters - Red in color
    canvas.draw_line((paddle1[0][0], 80), (paddle1[0][0], height), paddle_width, 'White')
    canvas.draw_line((paddle2[0][0], 80), (paddle2[0][0], height), paddle_width, 'White')

    #Paddles - White in color
    canvas.draw_line(paddle1[0], paddle1[1], paddle_width, 'Red')
    canvas.draw_line(paddle2[0], paddle2[1], paddle_width, 'Red')


    #BALL PHYSICS



    #BP2- Bouncing
    if ball_position[1]<=80+radius:
        ball_velocity[1] = -ball_velocity[1]
    elif ball_position[1]>= height - radius:
        ball_velocity[1] = - ball_velocity[1]

    if (ball_position[0] - radius)<=paddle1[0][0]:
        if paddle1[0][1] < ball_position[1] and paddle1[1][1] > ball_position[1]:
            ball_velocity[0] = - ball_velocity[0]
        else:
            score2=score2+1
            direction='left'
            initial_velocity[0]=ball_velocity[0]
            stop()

    if (ball_position[0] + radius)>=(paddle2[0][0]-paddle_width):
        if paddle2[0][1] < ball_position[1] and paddle2[1][1] > ball_position[1]:
            ball_velocity[0] = - ball_velocity[0]
        else:
            score1=score1 + 1
            direction='right'
            initial_velocity[0]=ball_velocity[0]
            stop()

    if score1>score2:
        if score1==10:
            message=str(player1) + " WINS"
            color="Black"
            ball_color='Black'
            stop()
            restart()



    if score2==10:
            message=str(player2) + " WINS"
            color="Black"
            stop()
            restart()





    canvas.draw_text(str(message), (400,300), 40, 'Teal')
    canvas.draw_line((width/2,80), (width/2, height), 6, color)
    canvas.draw_circle(ball_position, radius, 3, 'Teal', 'Teal')
    canvas.draw_line((0, 80), (width, 80), 8, 'White')
    canvas.draw_line((0, height-4), (width, height-4), 9, 'White')
    canvas.draw_text(str(score1), (235, 60), 20, 'White')
    canvas.draw_text(str(score2), (730,60), 20, 'White')
    canvas.draw_text(str(player1), (220,30), 30, 'White')
    canvas.draw_text(str(player2), (715,30), 30, 'White')
    canvas.draw_text(str(message_speed), ((width/2 - message_width/2), 30), 20, 'Green')





def key_down(key):
        global shift, check

        if key==simplegui.KEY_MAP['W']:
            vel_p1[1] -=6
        elif key==simplegui.KEY_MAP['S']:
            vel_p1[1] +=6

        if key==simplegui.KEY_MAP['up']:
            vel_p2[1] -=6
        elif key==simplegui.KEY_MAP['down']:
            vel_p2[1] +=6

        if key==simplegui.KEY_MAP['space']:
            if check==0:
                new_game()

def key_up(key):
    vel_p1[1]=0
    vel_p2[1]=0


def player_1(text1):
    global player1
    player1=str(text1)

def player_2(text2):
    global player2
    player2=str(text2)

def stop():
    global ball_velocity, ball_position, check
    check=0
    ball_velocity=[0,0]
    ball_position=[width/2, height/2]

#Create Frame
frame=simplegui.create_frame("Pong", width, height)

#Register Event Handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(key_down)
frame.set_keyup_handler(key_up)
text1=frame.add_input("Player 1", player_1, 150)
text2=frame.add_input("Player 2", player_2, 150)
frame.add_label(" ")
frame.add_label("Select Speed")
frame.add_button("Moon Walk", moonwalk, 100)
frame.add_button("Surf", surf, 100)
frame.add_button("Blitzer", blitzer, 100)
frame.add_label(" ")
frame.add_button("Reset Score", restart, 100)
frame.add_button("Stop", stop, 100)
frame.add_label(" ")
frame.add_label("Hit space to Start after selecting the speed or to Resume")
frame.start()
