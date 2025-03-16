import pygame
import os

pygame.init()

playlist=[]
music_path="C:\\destination\\Rauan_Tuken_PP2\\lab7\\musics"
list_music=os.listdir(music_path)
for song in list_music:
    if song.endswith("mp3"):
        playlist.append(os.path.join(music_path, song))

width, height=800, 500
screen=pygame.display.set_mode((width, height))
pygame.display.set_caption("Tame Impala Playlist")
clock=pygame.time.Clock()

song_name=pygame.font.SysFont(None, 50)
instruction_font=pygame.font.SysFont(None, 30)

index=0
if playlist:
    pygame.mixer.music.load(playlist[index])
    pygame.mixer.music.play()
play=True

Run=True
while Run:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            Run=False
            pygame.quit()
            exit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                if play:
                    play=False
                    pygame.mixer.music.pause()
                else:
                    play=True
                    pygame.mixer.music.unpause()
            elif event.key==pygame.K_RIGHT:
                index=(index+1)%len(playlist)
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play()
            elif event.key==pygame.K_LEFT:
                index=(index-1)%len(playlist)
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play()
    song_text=song_name.render(os.path.basename(playlist[index]), True, (255, 255, 255))
    text_rect=song_text.get_rect(center=(width//2, 50))
    inctruction_text=instruction_font.render("Press -> to change | Press SPACE to pause | Press <- to go back", True, (255, 255, 255))
    inctruction_rect=inctruction_text.get_rect(center=(width//2, height-30))
    screen.blit(song_text, text_rect)
    screen.blit(inctruction_text, inctruction_rect)
    
    pygame.display.update()
    clock.tick(24)