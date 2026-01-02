import turtle as t

PIXEL_SIZE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self, starting_coords = (+ PIXEL_SIZE, 0.0)):
        for i in range(3):
            current_coords = (starting_coords[0] - PIXEL_SIZE * i, starting_coords[1])
            self.add_segment(current_coords)

    def add_segment(self, position):
        segment = t.Turtle("square")
        segment.color("white")
        segment.pu()
        spawn_coords = (position[0], position[1])
        segment.teleport(x=spawn_coords[0], y=spawn_coords[1])
        self.snake.append(segment)

    def extend(self):
        # Adds a new segment to the snake
        self.add_segment(self.snake[-1].pos())

    def move(self):
        for seg_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[seg_num - 1].xcor()
            new_y = self.snake[seg_num - 1].ycor()
            self.snake[seg_num].goto(new_x, new_y)
        self.head.forward(PIXEL_SIZE)

    def up(self):
        if self.head.heading() != DOWN and self.head.pos()[1] + PIXEL_SIZE != self.snake[1].pos()[1]:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP and self.head.pos()[1] - PIXEL_SIZE != self.snake[1].pos()[1]:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT and self.head.pos()[0] - PIXEL_SIZE != self.snake[1].pos()[0]:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT and self.head.pos()[0] + PIXEL_SIZE != self.snake[1].pos()[0]:
            self.snake[0].setheading(RIGHT)

    def reset(self):
        for seg in self.snake:
            seg.hideturtle()
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]

