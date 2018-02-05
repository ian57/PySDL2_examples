"""Graphical Gui Test"""
import sys
import os

from sdl2 import *
import sdl2.ext

# Create a resource, so we have easy access to the example images.
RESOURCES = sdl2.ext.Resources(__file__, "resources")
uifactory = 0
spriterenderer = 0
spriteBG = 0
buttonNext = 0
buttonPrevious = 0
buttonShutdown = 0
running = True
spriteArray = ["320-LP_480x320.jpg", "320-lmag_480x320.jpg", "320-hackable_480x320.jpg"]
numImg = 0

# A callback for the Button.click event.
def onclickNext(button, event):
    global numImg, spriterenderer,  buttonNext, buttonPrevious
    numImg=numImg+1
    if numImg >2:
        numImg = 0
    print("Button Next was clicked!")
    buttonNextClicked =  uifactory.from_image(sdl2.ext.BUTTON,RESOURCES.get_path("buttonNextClicked.png"))
    buttonNextClicked.position = 370, 76
    spriterenderer.render((buttonNextClicked, buttonPrevious))
    timer.SDL_Delay(100)
    image = uifactory.from_image(sdl2.ext.BUTTON, RESOURCES.get_path(spriteArray[numImg]))
    image.position = 20,40
    spriterenderer.render((buttonNext, buttonPrevious, image))

# A callback for the Button.click event.
def onclickPrevious(button, event):
    global numImg, spriterenderer,  buttonNext, buttonPrevious
    numImg=numImg-1
    if numImg < 0:
        numImg = 2
    print("Button Previous was clicked!")
    buttonPreviousClicked =  uifactory.from_image(sdl2.ext.BUTTON,RESOURCES.get_path("buttonPreviousClicked.png"))
    buttonPreviousClicked.position = 370, 112
    spriterenderer.render((buttonNext, buttonPreviousClicked))
    timer.SDL_Delay(100)
    image = uifactory.from_image(sdl2.ext.BUTTON, RESOURCES.get_path(spriteArray[numImg]))
    image.position = 20,40
    spriterenderer.render((buttonNext, buttonPrevious, image))

# A callback for the Button.click event.
def onclickShutdown (button, event):
    global numImg, spriterenderer,  buttonNext, buttonPrevious, buttonShutdown
    print("Button Shutdown was clicked!")
    buttonShutdownClicked =  uifactory.from_image(sdl2.ext.BUTTON,RESOURCES.get_path("buttonShutDownClicked.png"))
    buttonShutdownClicked.position = 370, 148
    spriterenderer.render((buttonNext, buttonPrevious, buttonShutdownClicked))
    timer.SDL_Delay(300)
    spriterenderer.render((buttonNext, buttonPrevious, buttonShutdown))
    #os.system('sudo halt')

def run():
    # You know those from the helloworld.py example.
    # Initialize the video subsystem, create a window and make it visible.
    global window, factory, running, spriteArray, numImg, uifactory,  spriterenderer , spriteBG, buttonNext, buttonPrevious, buttonShutdown
    
    sdl2.ext.init()
    #sdl2.mouse.SDL_ShowCursor(0) #hide cursor
    window = sdl2.ext.Window("Gui Test 0.1", size=(480, 320))
    window.show()

    # Create a sprite factory that allows us to create visible 2D elements
    # easily. Depending on what the user chosses, we either create a factory
    # that supports hardware-accelerated sprites or software-based ones.
    # The hardware-accelerated SpriteFactory requres a rendering context
    # (or SDL_Renderer), which will create the underlying textures for us.
    if "-hardware" in sys.argv:
        print("Using hardware acceleration")
        renderer = sdl2.ext.Renderer(window)
        factory = sdl2.ext.SpriteFactory(sdl2.ext.TEXTURE, renderer=renderer)
    else:
        print("Using software rendering")
        factory = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)

    # Create a UI factory, which will handle several defaults for
    # us. Also, the UIFactory can utilises software-based UI elements as
    # well as hardware-accelerated ones; this allows us to keep the UI
    # creation code clean.
    uifactory = sdl2.ext.UIFactory(factory)

    # Create a simple Button sprite, which reacts on mouse movements and
    # button presses and fill it with a white color. All UI elements
    # inherit directly from the TextureSprite (for TEXTURE) or SoftwareSprite
    # (for SOFTWARE), so everything you can do with those classes is also
    # possible for the UI elements.
    #spriteBG = factory.from_image(RESOURCES.get_path("background.png"))
    spriteBG = uifactory.from_image(sdl2.ext.BUTTON, RESOURCES.get_path("backgroundPySDL2.png"))
    spriteBG.position = 0, 0
    
    buttonNext = uifactory.from_image(sdl2.ext.BUTTON, RESOURCES.get_path("buttonNext.png"))
    buttonNext.position = 370, 76

    buttonPrevious = uifactory.from_image(sdl2.ext.BUTTON, RESOURCES.get_path("buttonPrevious.png")) 
    buttonPrevious.position = 370, 112
    
    buttonShutdown = uifactory.from_image(sdl2.ext.BUTTON, RESOURCES.get_path("buttonShutDown.png")) 
    buttonShutdown.position = 370, 148

    image = uifactory.from_image(sdl2.ext.BUTTON, RESOURCES.get_path(spriteArray[numImg]))
    image.position = 20,40
    
    # Bind some actions to the button's event handlers. Whenever a click
    # (combination of a mouse button press and mouse button release), the
    # onclick() function will be called.
    # Whenever the mouse moves around in the area occupied by the button, the
    # onmotion() function will be called.
    # The event handlers receive the issuer of the event as first argument
    # (the button is the issuer of that event) and the SDL event data as second
    # argument for further processing, if necessary.
    
    
    buttonNext.click += onclickNext
    buttonPrevious.click += onclickPrevious
    buttonShutdown.click += onclickShutdown

    # Since all gui elements are sprites, we can use the
    # SpriteRenderSystem class, we learned about in helloworld.py, to
    # draw them on the Window.
    spriterenderer = factory.create_sprite_render_system(window)


    # Create a new UIProcessor, which will handle the user input events
    # and pass them on to the relevant user interface elements.
    uiprocessor = sdl2.ext.UIProcessor()
    
    spriterenderer.render((spriteBG, buttonNext, buttonPrevious, buttonShutdown, image))
    

    while running:
        window.refresh()
        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                running = False
                break
            if event.key.keysym.sym == sdl2.SDLK_ESCAPE:
                running = False
                break
            uiprocessor.dispatch([buttonNext, buttonPrevious, buttonShutdown], event)
    sdl2.ext.quit()
    return 0


if __name__ == "__main__":
    sys.exit(run())




