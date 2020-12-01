import pygame
import pygame.gfxdraw as gfx
import simplexnoise as sn
import sys

x_max = 512
y_max = 512

def gen_map():
    persistence = 0.5
    octaves = 5
    frequency = .01
    heightmap = []

    for x in range(x_max):
        row = []
        for y in range(y_max):
            p = sn.octave_noise_2d(octaves, persistence, frequency, x, y)
            p = scale(p, -1, 1, 0, 255)
            row.append(p)

        heightmap.append(row)

    return heightmap

def scale(inp, in_min, in_max, out_min, out_max):
    return (inp - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def draw_map(surface, heightmap):

    pxarray = pygame.PixelArray(surface)

    for x in range(len(heightmap)):
        for y in range(len(heightmap)):
            height = round(heightmap[x][y])
            pxarray[x, y] = (height, height, height)
        percent = round(100 * 1.0 * x / x_max)
        if percent % 10 == 0:
            print("drawing " + str(percent))

def main():
    pygame.init() # initialize pygame
    
    WINDOWWIDTH = x_max
    WINDOWHEIGHT = y_max
    
    # colors
    BLACK = (0,0,0)
    
    # create display window
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('perlin')

    print("generating map")
    heightmap = gen_map()

    print("drawing")
    draw_map(DISPLAYSURF, heightmap)

    pygame.display.flip()


    while True: # main game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


 
if __name__ == "__main__":
    main()