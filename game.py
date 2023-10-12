import sys
from random import randint
import pygame
import time
from pygame.locals import QUIT, Rect, KEYDOWN, K_SPACE, K_LEFT, K_RIGHT, K_DOWN, K_UP 

pygame.init()
pygame.key.set_repeat(5, 5)
SURFACE = pygame.display.set_mode((512, 768))
fps = pygame.time.Clock()

sound = pygame.mixer.Sound("C:/Users/chamvit/Desktop/WORK/Python/gameclear.mp3") # 다른 컴퓨터에서 사용시 이 코드 두줄은 주석 처리 or 디렉토리 변경
sound.set_volume(1.0)

def main():
    # main
    #professor = pygame.image.load("bang.png")
    back_ground = pygame.image.load("back.png")
    ghost = pygame.image.load("gh.png")
    professor = pygame.image.load("profess.png")
    student = pygame.image.load("stu.png")
    ship = pygame.image.load("ship.png")

    #speed = 5
    x, y = 0, 0
    gh_x, gh_y = 300, 350
    pr_x, pr_y = 350, 350
    door = pygame.Rect(70, 70, 70, 70)

    GAME_OVER = False
    GAME_CLEAR = False
    MEET = False
    ghost_percent = 2

    font = pygame.font.Font(None, 70)
    text_render = font.render("GAME CLEAR!!!", True, (255, 0, 0))

    while True:
        fps.tick(60)

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    pygame.quit()
                               
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and x >= 0:
            x -= 5
        if keys[pygame.K_RIGHT] and x <= 392:
            x += 5
        if keys[pygame.K_DOWN] and y <= 678:
            y += 5
        if keys[pygame.K_UP] and y >= 30:
            y -= 5

        # 점멸 귀신
        random_percent = randint(0, 100)
        if random_percent <= ghost_percent:
            gh_x, gh_y = randint(0,512), randint(0, 768)

        # 이동 귀신

        # 귀신과 충돌
        student_rect = pygame.Rect(x, y, student.get_width(), student.get_height())
        #ghost_rect = pygame.Rect(gh_x, gh_y, ghost.get_width(), ghost.get_height())
        if student_rect.collidepoint(gh_x, gh_y):
            GAME_OVER = True


        # 교수 충돌        
        if student_rect.collidepoint(pr_x, pr_y):
            pr_x, pr_y = [x + 30, y]
            MEET = True

        if MEET:
            pr_x, pr_y = [x + 30, y]

        if student_rect.colliderect(door) and MEET == True:
            GAME_CLEAR = True


        # 그리기
        SURFACE.blit(back_ground, (0, 0))
        SURFACE.blit(professor, (pr_x, pr_y))
        SURFACE.blit(ghost, (gh_x, gh_y))
        SURFACE.blit(student, (x, y))
        #SURFACE.blit(ship, (70, 70))

        pygame.display.flip()
        pygame.display.update() 


        if GAME_OVER:
            pygame.quit()

        if GAME_CLEAR:
            sound.play(2, 0, 0)



if __name__ == '__main__':
    main()
