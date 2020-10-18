import pygame, sys
import random
pygame.init()
pygame.font.init()

clock = pygame.time.Clock()

screen_x = 1280
screen_y = 720
win = pygame.display.set_mode((screen_x, screen_y))
pygame.display.set_caption("PONG")
scoreRight = 0
scoreLeft = 0

hitEffect = pygame.mixer.Sound("hitEffect.wav")

class Rect:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitBox = (self.x, self.y, self.width, self.height)
    @staticmethod
    def draw(player, player2):
        pygame.draw.rect(win, (200, 200, 200), player)
        pygame.draw.rect(win, (200, 200, 200), player2)




class Ball:
    def __init__(self,x ,y ,radius, velx, vely):
        self.x = x
        self.y = y
        self.radius = radius
        self.facing = 1
        self.facingy = 1
        self.velx = velx
        self.vely = vely
        self.center_x = self.x + radius/2
        self.center_y = y + radius/2
        self.visible = True
    def mov(self):
        if self.facing == 1:
            self.x += self.velx
        elif self.facing == -1:
            self.x -= self.velx
        self.y += self.vely * self.facingy

def collisionCheck(circle, leftPlayer, rightPlayer):
    global scoreRight
    global scoreLeft
    if leftPlayer.right > circle.x:
        if leftPlayer.bottom >= circle.y >= leftPlayer.top:
            hitEffect.play()
            circle.facing *= -1
            circle.velx += 1
            circle.vely += 0.50
    if rightPlayer.left < circle.x:
        if rightPlayer.bottom >= circle.y >= rightPlayer.top:
            hitEffect.play()
            circle.facing *= -1
            circle.velx += 1
            circle.vely += 0.50

    if circle.y >= screen_y :
        circle.facingy *= -1

    if circle.y <= 0:
        circle.facingy *= -1

    if circle.x >= screen_x :
        scoreLeft += 1
        circle.visible = False
    if circle.x <= 0 :
        scoreRight += 1
        circle.visible = False

leftRect = Rect(30, screen_y/2 - 50, 10, 150)
rightRect = Rect(screen_x - 50, screen_y/2 - 50, 10, 150)
circle = Ball(screen_x/2, screen_y/2, 10, 6, 3)


def redrawGameWindow():
    scoreFont = pygame.font.SysFont("arial", 30, True)
    leftscoreText = scoreFont.render("Score = {}".format(scoreLeft), True, (200, 200, 200))
    rightscoreText = scoreFont.render("Score = {}".format(scoreRight), True, (200, 200, 200))
    leftPlayer = pygame.Rect(leftRect.x, leftRect.y, leftRect.width, leftRect.height)
    rightPlayer = pygame.Rect(rightRect.x, rightRect.y, rightRect.width, rightRect.height)
    collisionCheck(circle, leftPlayer, rightPlayer)
    win.fill((30,30,30))
    Rect.draw(leftPlayer, rightPlayer)
    pygame.draw.circle(win, (200, 200, 200), (int(circle.x), int(circle.y)), circle.radius)
    win.blit(leftscoreText, (20, 20))
    win.blit(rightscoreText, (screen_x - (20 + rightscoreText.get_width()), 22))
    pygame.display.update()

def playAgain():
    if not circle.visible:
        for _ in range (200):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.time.wait(10)
        circle.visible = True
        circle.x = screen_x/2
        circle.y = screen_y/2
        circle.velx = 6
        circle.vely = 3


# main
while True:
    global leftPlayer
    global rightPlayer
    clock.tick(60)
    redrawGameWindow()
    Ball.mov(circle)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        if rightRect.y > 0:
            rightRect.y -= 7
    if keys[pygame.K_DOWN]:
        if rightRect.y + rightRect.height < screen_y:
            rightRect.y += 7
    if keys[pygame.K_w]:
        if leftRect.y> 0:
            leftRect.y -= 7
    if keys[pygame.K_s]:
        if leftRect.y + leftRect.height < screen_y:
            leftRect.y += 7


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    playAgain()