import pygame
import time

pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
pygame.display.set_caption("Mouse Clock")

right_arm = pygame.image.load(r"C:\destination\Rauan_Tuken_PP2\lab7\clock_images\rightarm.png")
left_arm = pygame.image.load(r"C:\destination\Rauan_Tuken_PP2\lab7\clock_images\leftarm.png")
main_clock = pygame.transform.scale(pygame.image.load(r"C:\destination\Rauan_Tuken_PP2\lab7\clock_images\clock.png"), (width, height))

done=False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    current_time = time.localtime()
    min = current_time.tm_min
    sec = current_time.tm_sec

    min_angle = min*6 + (sec/60)*6
    sec_angle = sec*6

    screen.fill((0,0,0))
    screen.blit(main_clock,(0,0))

    rotated_rightarm = pygame.transform.rotate(right_arm, -min_angle)
    rightarm_rect = rotated_rightarm.get_rect(center=(width//2, height//2))
    screen.blit(rotated_rightarm, rightarm_rect)

    rotated_leftarm = pygame.transform.rotate(left_arm, -sec_angle)
    leftarm_rect = rotated_leftarm.get_rect(center=(width//2, height//2))
    screen.blit(rotated_leftarm, leftarm_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()