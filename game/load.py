import pyglet, random, math
from game import resources, physicalobject, util, asteroid

def asteroids(num_asteroids, player_position, batch=None):
    """
    Used to spawn the asteroids in valid locations. Valid locations are defined
    by not being too close to the player that there is a collision instantly
    but not being so far away as to be beyond the game window.

    Inputs
    ============================================================================
    num_asteroids           int; the number of asteroids to be spawned at this
                            function call
    player_position         vector; the x and y coordinates, measured in pixels,
                            of where the player_ship is located
    batch                   pyglet batch; the name of the batch which the
                            asteroids are meant to be a part of

    Outputs
    ============================================================================
    asteroids               list; a reference to all of the asteroid game
                            objects that are present in the game window.
    """
    asteroids = []
    for i in range(num_asteroids):
        asteroid_x, asteroid_y = player_position
        while util.distance((asteroid_x, asteroid_y), player_position) < 100:
            asteroid_x = random.randint(0, 1000)
            asteroid_y = random.randint(0, 800)
        new_asteroid = asteroid.Asteroid(x=asteroid_x, y=asteroid_y, batch=batch)
        new_asteroid.rotation = random.randint(0, 360)
        new_asteroid.velocity_x = random.random()*40
        new_asteroid.velocity_y = random.random()*40
        asteroids.append(new_asteroid)
    return asteroids

def player_lives(num_icons, batch=None):
    """
    Used to spawn in the player lives icons in the upper right corner of the
    screen based off of the number of lives remaining for the player. This 
    is determined by player_ship.lives. Each player_lives sprite is a scaled
    down version of the player_ship sprite.

    Inputs
    =============================================================================
    num_icons               int; the number of lives that the player has left.
                            This will be equal to the number of icons spawned in.
    batch                   pyglet batch; the name of the batch which the 
                            player_lives are meant to be a part of

    Outputs
    =============================================================================
    player_lives            list; a list referecning all of the player life
                            sprites that are spawned in.

    """
    player_lives = []
    for i in range(num_icons):
        new_sprite = pyglet.sprite.Sprite(
            img=resources.player_image, x=1000-100-i*30, y=800-25, batch=batch)
        new_sprite.scale = 0.5
        player_lives.append(new_sprite)
    return player_lives 