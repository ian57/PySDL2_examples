import sys
import ctypes
from sdl2 import *
from sdl2.sdlimage import *
#import necessairea pour l'utilisation de pySDL
#et pour la chargement d'image autre que le format BMP
def main():
    SDL_Init(SDL_INIT_VIDEO)
    window = SDL_CreateWindow(b"Hello World",
                              SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED,
                              480, 320, SDL_WINDOW_SHOWN)
    windowsurface = SDL_GetWindowSurface(window)
    SDL_ShowCursor(SDL_DISABLE)
    #image = SDL_LoadBMP(b"resources/hello.bmp")
    image = IMG_Load(b"resources/LP_480x320.jpg")
    
    destrect= rect.SDL_Rect(0, 40, 320, 240)

    SDL_BlitScaled(image, None, windowsurface, destrect)

    SDL_UpdateWindowSurface(window)
    SDL_FreeSurface(image)

    running = True
    event = SDL_Event()
    SDL_ShowCursor(SDL_DISABLE)
    while running:
        SDL_UpdateWindowSurface(window)
        while SDL_PollEvent(ctypes.byref(event)) != 0:
            if event.type == SDL_QUIT:
                running = False
                break
            if event.key.keysym.sym == SDLK_ESCAPE:
                running = False
                break

    SDL_DestroyWindow(window)
    SDL_Quit()
    return 0

if __name__ == "__main__":
    sys.exit(main())
