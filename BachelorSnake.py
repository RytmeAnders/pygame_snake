from pygame.locals import *
import pygame
import time
import random


class BachelorSnake:
    x = [0]
    y = [0]
    foodX = [0]
    foodY = [0]
    direction = 0
    desiredDirection = 0
    size = 50
    length = 1
    speed = 0.2
    isFoodEaten = True
    isGameOver = False
    width = 800
    height = 600

    def __init__(self):
        self._running = True
        self._display_surf = None
        # self._image_surf = None

    def on_init(self):
        pygame.init()
        pygame.display.set_caption('Snakezzz')
        pygame.font.init()  # you have to call this at the start if you want to use this module.

        self._running = True
        self._display_surf = pygame.display.set_mode((self.width, self.height), pygame.HWSURFACE)
        # self._image_surf = pygame.image.load("fun.jpg").convert()

        self.x[0] = 200
        self.y[0] = 200

    def update(self):
        # Direction is now final
        self.direction = self.desiredDirection

        # Check if the game is over...
        # Screen edges
        if self.x[0] < 0 or self.x[0] == self.width or self.y[0] < 0 or self.y[0] == self.height:
            self.isGameOver = True

        # Draw snake, check if it collides with itself
        for i in range(0, self.length):
            pygame.draw.rect(self._display_surf, (200, 200, 200), (self.x[i] + 2, self.y[i] + 2, self.size - 4, self.size - 4))
            if i != 0 and self.x[0] == self.x[i] and self.y[0] == self.y[i]:
                self.isGameOver = True

        # Display score, which is the length of snake - 1
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        textsurface = myfont.render('Score: ' + str(self.length - 1), False, (255, 255, 255))
        self._display_surf.blit(textsurface, (0, 0))

        # Restart the game
        if self.isGameOver:
            self.isGameOver = False
            self.length = 1
            self.isFoodEaten = True
            self.direction = 0
            self.desiredDirection = 0
            self.x.clear()
            self.y.clear()
            self.x.append(200)
            self.y.append(200)

        # Check for food
        if self.x[0] == self.foodX[0] and self.y[0] == self.foodY[0]:
            self.isFoodEaten = True
            self.length = self.length + 1
            self.x.append(self.x[0])
            self.y.append(self.y[0])

        # Move the whole snake
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        # Update position of head of snake
        if self.direction == 0:
            self.x[0] = self.x[0] + self.size
        if self.direction == 1:
            self.x[0] = self.x[0] - self.size
        if self.direction == 2:
            self.y[0] = self.y[0] - self.size
        if self.direction == 3:
            self.y[0] = self.y[0] + self.size

        # display images
        # self._display_surf.blit(self._image_surf, (self.x[0], self.y[0]))

        # Chack if snake collides with food
        if self.isFoodEaten == True:
            self.foodX[0] = random.randrange(0, self.width - 25, 50)
            self.foodY[0] = random.randrange(0, self.height - 25, 50)
            self.isFoodEaten = False

        # Draw food
        pygame.draw.rect(self._display_surf, (20, 200, 20), (self.foodX[0], self.foodY[0], self.size, self.size))
        pygame.display.flip()
        self._display_surf.fill((0, 0, 0))

    # Start game loop
    def run(self):
        myTime = time.time()

        if self.on_init() == False:
            self._running = False

        while self._running:
            pygame.event.pump()

            self.move()

            if (time.time() - myTime > self.speed):
                myTime = time.time()
                self.update()

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[K_RIGHT] and self.direction != 1:
            self.moveRight()
            return
        if keys[K_LEFT] and self.direction != 0:
            self.moveLeft()
            return
        if keys[K_UP] and self.direction != 3:
            self.moveUp()
            return
        if keys[K_DOWN] and self.direction != 2:
            self.moveDown()
            return
        if keys[K_ESCAPE]:
            self._running = False

    def on_cleanup(self):
        pygame.quit()

    def draw(self, surface, image):
        for i in range(0, self.length):
            surface.blit(image, (self.x[i], self.y[i]))

    def moveRight(self):
        self.desiredDirection = 0

    def moveLeft(self):
        self.desiredDirection = 1

    def moveUp(self):
        self.desiredDirection = 2

    def moveDown(self):
        self.desiredDirection = 3


if __name__ == "__main__":
    bachelorSnake = BachelorSnake()
    bachelorSnake.run()
