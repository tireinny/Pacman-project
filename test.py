import sys
import pygame
 
''' Example to show fps with pygame 12.01.2022 - python 3.10 '''
 
def text_on_screen(content, font, w, h):
	''' Renders content with font '''
	fps_surface = font.render(content, 1, pygame.Color("white"))
	text_width = fps_surface.get_width()
	if w + text_width > screen.get_width():
		start = 0
		for word in content.split():
			wr = font.render(word + " ", 1, pygame.Color("white"))
			if w + start + wr.get_width() < screen.get_width():
				screen.blit(wr, (w + start, h))
				start += wr.get_width()
			else:
				start = 0
				h = h + 20
				screen.blit(wr, (w + start, h))
				start += wr.get_width()
	else:
		screen.blit(fps_surface, (w, h))
 
 
timer = 0 #                                             counter increase each frame
def show_timer(max_frame_rate):
	global timer
 
	fps = f"Fps: {int(clock.get_fps())}" #               FPS
	fps += f" Timer: {timer//max_frame_rate}" #                      TIMER
	text_on_screen(fps, fps_font, 0, 0) #                       call to blit fps
	timer += 1 #                                        UPDATE COUNTER
 
 
# each line is a slide
txt_slides = """This is
a text
seen with timing
Bye
""".splitlines()
 
 
txt_cnt = 0 # counter for the slides in txt variables (lines)
def mainloop(max_frame_rate=60):
	''' loop where thing happens every frame '''
	global txt_cnt
 
	# while loop that makes things go on on screen
	while True:
		screen.fill(0) # clear the screen with black
		show_timer(max_frame_rate)
		text_on_screen(txt_slides[txt_cnt], fps_font, 100, 100)
		for event in pygame.event.get(): #                   USER EVENTS HANDLER
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		if timer % 60 == 0:
			txt_cnt += 1
		if txt_cnt > len(txt_slides) - 1:
			txt_cnt = 0
		clock.tick(max_frame_rate) #                         MAX FRAME RATE (60 is default)
		pygame.display.update() #                            UPDATE DISPLAY
 
 
# the engine initialization
pygame.init()
screen = pygame.display.set_mode((600, 400)) #             the screen surface
size = 60
fps_font = pygame.font.SysFont("Arial", size) #                font
clock = pygame.time.Clock() #                                FRAME RATE OBJECT
mainloop()