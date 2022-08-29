from turtle import Turtle

STARTING_POSITIONS = [(380, -20), (380, 0), (380, 20)]
MOVE_FORWARD = 20
UP = 90
DOWN = 270


class Paddle2:

    def __init__(self):
        self.paddle_blocks = []
        self.create_paddle()
        self.head = self.paddle_blocks[0]
        self.tail = self.paddle_blocks[2]
        self.head.setheading(UP)
        self.head.forward(MOVE_FORWARD)

        # Creates Snake Blocks

    def create_paddle(self):
        """Creates new snake"""
        for position in STARTING_POSITIONS:
            new_block = Turtle("square")
            new_block.color("white")
            new_block.penup()
            new_block.goto(position)
            self.paddle_blocks.append(new_block)

    def move(self):
        """Defines the movement of the snake by moving last block"""
        for block_num in range(len(self.paddle_blocks) - 1, 0, -1):
            new_x = self.paddle_blocks[block_num - 1].xcor()
            new_y = self.paddle_blocks[block_num - 1].ycor()
            self.paddle_blocks[block_num].goto(new_x, new_y)
        self.head.forward(MOVE_FORWARD)

        if self.head.ycor() > 260:
            self.down()

        elif self.head.ycor() < -260:
            self.up()

    def up(self):
        self.head.setheading(UP)

    def down(self):
        self.head.setheading(DOWN)


