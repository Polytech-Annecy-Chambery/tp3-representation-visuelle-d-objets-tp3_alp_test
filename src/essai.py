import pygame
import OpenGL.GL as gl
import OpenGL.GLU as glu
if __name__ == '__main__':
    pygame.init()
    display=(600,600)
    pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)
    
    # Sets the screen color (white)
    gl.glClearColor(1, 1, 1, 1)
    # Clears the buffers and sets DEPTH_TEST to remove hidden surfaces
    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)                  
    gl.glEnable(gl.GL_DEPTH_TEST)    
    
    # Placer ici l'utilisation de gluPerspective.

    while True:
        for event in pygame.event.get():
        	if event.type == pygame.QUIT:
        		pygame.quit()
                exit()
