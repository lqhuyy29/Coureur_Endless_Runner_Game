import pygame
import random
from game_state import game_state

car_img = pygame.image.load('assets/obstacles/car.png')
truck_img = pygame.image.load('assets/obstacles/truck.png')
bus_img = pygame.image.load('assets/obstacles/bus.png')

class Obstacle:
    """
    Represents an obstacle in the game.
    """
    def __init__(self, image, lane, speed):
        self.image = image
        self.rect = self.image.get_rect()
        self.lane = lane
        self.rect.bottom = 360 + (lane * 120) + 120 - 16
        self.rect.left = 1280  # Sử dụng chiều rộng màn hình từ SCREEN_WIDTH
        self.speed = speed * game_state.game_speed_rate

    def update(self):
        """
        Updates the position of the obstacle based on its speed.
        """
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()

    def kill(self):
        """
        Removes the obstacle from the game state when it goes off-screen.
        """
        game_state.obstacles.remove(self)

class Car(Obstacle):
    default_speed = 8
    def __init__(self, lane):
        super().__init__(car_img, lane, self.default_speed)

class Truck(Obstacle):
    default_speed = 7
    def __init__(self, lane):
        super().__init__(truck_img, lane, self.default_speed)

class Bus(Obstacle):
    default_speed = 6
    def __init__(self, lane):
        super().__init__(bus_img, lane, self.default_speed)

def add_obstacle():
    """
    Adds a random obstacle to the game state.
    """
    lane = random.randint(0, 2)
    if not any(obstacle.lane == lane for obstacle in game_state.obstacles):
        vehicle_type = random.choice([Car, Truck, Bus])
        obstacle = vehicle_type(lane)
        game_state.obstacles.append(obstacle)