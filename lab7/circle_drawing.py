import pygame

pygame.init()
width_height=(800, 600)
screen=pygame.display.set_mode(width_height)
pygame.display.set_caption("Circle")
circle_position=[300, 400]
circle_color=pygame.Color('red')
circle_radius=25
speed=20
background_color=pygame.Color('white')

done = False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    keys=pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        circle_position[1]=max(circle_position[1]-speed, circle_radius)
    if keys[pygame.K_DOWN]:
        circle_position[1]=min(circle_position[1]+speed, width_height[1]-circle_radius)
    if keys[pygame.K_LEFT]:
        circle_position[0]=max(circle_position[0]-speed, circle_radius)
    if keys[pygame.K_RIGHT]:
        circle_position[0]=min(circle_position[0]+speed, width_height[0]-circle_radius)
    screen.fill(background_color)
    pygame.draw.circle(screen, circle_color, circle_position, circle_radius)
    pygame.display.flip()
    pygame.time.Clock().tick(24)