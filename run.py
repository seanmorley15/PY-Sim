import tkinter as tk
import math
import random

ball_count = 0  # Global variable to keep track of ball count

class Ball:
    def __init__(self, canvas, x, y, radius, color):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.vx = random.uniform(-5, 5)
        self.vy = random.uniform(-5, 5)
        self.ball_id = canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=color)
        self.has_collided = False  # Track if a collision has occurred
        self.collision_cooldown = False  # Cooldown after collision

    def move(self):
        self.canvas.move(self.ball_id, self.vx, self.vy)
        self.x += self.vx
        self.y += self.vy
        self.check_boundary_collision()

    def check_boundary_collision(self):
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        if self.x - self.radius <= 0 or self.x + self.radius >= canvas_width:
            self.vx *= -1
        if self.y - self.radius <= 0 or self.y + self.radius >= canvas_height:
            self.vy *= -1

    def check_collision(self, other_ball):
        distance = ((self.x - other_ball.x) ** 2 + (self.y - other_ball.y) ** 2) ** 0.5
        return distance <= self.radius + other_ball.radius

    def handle_collision(self, other_ball):
        global ball_count
        if not self.has_collided and not self.collision_cooldown:
            angle = math.atan2(other_ball.y - self.y, other_ball.x - self.x)
            angle_rad = math.radians(angle)

            bounciness = .8
            self.vx = bounciness * (self.vx * math.cos(angle_rad) + self.vy * math.sin(angle_rad))
            self.vy = bounciness * (self.vy * math.cos(angle_rad) - self.vx * math.sin(angle_rad))
            other_ball.vx = bounciness * (other_ball.vx * math.cos(angle_rad) - other_ball.vy * math.sin(angle_rad))
            other_ball.vy = bounciness * (other_ball.vy * math.cos(angle_rad) + other_ball.vx * math.sin(angle_rad))

            new_ball = Ball(self.canvas, random.uniform(0, self.canvas.winfo_width()), random.uniform(0, 100), self.radius, random.choice(["red", "blue", "green"]))
            new_ball.vx = random.uniform(-5, 5)
            new_ball.vy = random.uniform(1, 5)
            balls.append(new_ball)
            ball_count += 1  # Increment ball count
            print(f"Collision occurred! Ball count: {ball_count}")  # Print ball count when collision occurs
            self.has_collided = True
            self.collision_cooldown = True
            self.canvas.after(5000, self.reset_cooldown)  # Cooldown for 5 seconds


    def reset_cooldown(self):
        self.collision_cooldown = False
        self.has_collided = False

# The rest of your code remains the same...



def adjust_gravity():
    global gravity
    for ball in balls:
        ball.vy += gravity

def animate():
    for ball in balls:
        ball.move()
        for other_ball in balls:
            if ball != other_ball and ball.check_collision(other_ball):
                ball.handle_collision(other_ball)
            else:
                ball.has_collided = False  # Reset has_collided attribute
    root.after(20, animate)
    adjust_gravity()

def create_initial_balls(num_balls):
    for _ in range(num_balls):
        color = random.choice(["red", "blue", "green"])
        x = random.uniform(0, 600)
        y = random.uniform(0, 100)
        radius = random.uniform(5, 15)
        ball = Ball(canvas, x, y, radius, color)
        ball.vx = random.uniform(-5, 5)
        ball.vy = random.uniform(-5, 5)
        balls.append(ball)

root = tk.Tk()
root.title("Physics Simulation")
canvas = tk.Canvas(root, width=600, height=600, bg="black")
canvas.pack()

balls = []

gravity = 1  # Define gravity here

# Set the initial number of balls
initial_ball_count = 5
create_initial_balls(initial_ball_count)

animate()
root.mainloop()
