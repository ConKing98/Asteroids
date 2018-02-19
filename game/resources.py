import pyglet

# Determining the file path to the game images
pyglet.resource.path = ['resources']
pyglet.resource.reindex()

def center_image(image):
    """
    Sets the image anchor to its center.
    
    Inputs
    =======================================================================
    image           pyglet handled image; the image that is to be anchored
                    by its center. Should be input in the form:
                    pyglet.resource.image('___file path___') for best
                    results.

    Outputs
    =======================================================================
    image           pyglet handled image; the image, now with its anchor 
                    set to be its center instead of the corner.
    """
    image.anchor_x = image.width/2
    image.anchor_y = image.height/2
    return image

def engine_offset(image):
    """
    Sets the image anchor offset for the engine animation
    
    Inputs
    =======================================================================
    image           pyglet handled image; the image that is to be anchored
                    outside of the image boundaries such that the engine
                    animation is properly located with respect to the ship.

    Outputs
    =======================================================================
    image           pyglet handled image; the image now with its anchor set
                    to be outside of the image boundaries so that it looks
                    proper next to the ship.
    """
    image.anchor_x = image.width/2
    image.anchor_y = image.height*2
    return image

# The various images used throughout the game.
player_image = center_image(pyglet.resource.image('player.png'))
asteroid_image = center_image(pyglet.resource.image('asteroid.png'))
bullet_image = center_image(pyglet.resource.image('bullet.png'))
engine_image = engine_offset(pyglet.resource.image('engine.png'))
