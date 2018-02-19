# Imports
import pyglet
from game import resources, load, player, bullet, asteroid, reference

# Defining location of all sprite images
pyglet.resource.path = ['resources']
pyglet.resource.reindex()

# Creating batch for all objects in the game
main_batch = pyglet.graphics.Batch()

# Creating the player's ship
player_ship = player.Player(x=1000/2, y=800/2, batch=main_batch)

# Defining the game_window and enabling support for keyboard inputs in the main.py file
game_window = pyglet.window.Window(1000,800)
keys = pyglet.window.key.KeyStateHandler()
game_window.push_handlers(player_ship.key_handler)
game_window.push_handlers(keys)

# Creating other objects within the game
lives = load.player_lives(player_ship.lives, main_batch)
score_label = pyglet.text.Label(text='Score: {}'.format(player_ship.score), x=10, y=800-25, batch=main_batch)
level_label = pyglet.text.Label(text='Level: {}'.format(player_ship.level), x=1000-40, y=800-25, anchor_x='center', batch=main_batch)
death_label = pyglet.text.Label(text='You have been killed. You have {} lives remaining. Press Enter to continue.'.format(
                                player_ship.lives), x=game_window.width/2, y=game_window.height/2-200, anchor_x='center',
                                anchor_y='center')
complete_label = pyglet.text.Label(text='You have completed level {}. Press enter to continue.'.format(player_ship.level),
                                   x=game_window.width/2, y=game_window.height/2, anchor_x='center', anchor_y='center')
highscore_label = pyglet.text.Label(text='1st:  {0} \n2nd:  {1} \n3rd:  {2} \n4th:  {3} \n5th:  {4} \n6th:  {5} \n7th:  {6} \n8th:  {7} \n9th:  {8} \n10th {9}'.format(
                                    *reference.load()), x=game_window.width/2, y=game_window.height/2+100, anchor_x='center',
                                    anchor_y='center', width=100, multiline=True)
asteroids = load.asteroids(3, player_ship.position, main_batch)
game_objects = [player_ship] + asteroids


def refresh(keep_values):
    """
    Refreshes the game when either the player has lost or the level is completed. This is
    illustrated by all asteroids having been destroyed. The *args are used to transfer
    characteristics of the last player_ship onto the new one, such as the lives remaining
    and the player's score.

    Inputs
    ======================================================================================
    *args           Boolean; qualities to move over to the new character. Currently
                    only player_lives and player_score are supported.

    Outputs
    ======================================================================================
    None
    """
    global asteroids, game_objects, player_ship, lives
    game_objects.clear()

    # All characteristics of the player_ship
    player_ship.visible = True
    player_ship.dead = False
    player_ship.x = 1000/2
    player_ship.velocity_x = 0
    player_ship.y = 800/2
    player_ship.velocity_y = 0
    if keep_values:
        pass
    else:
        player_ship.lives = 3
        player_ship.score = 0
        player_ship.level = 1

    # Redrawing the various indicators
    lives.clear()
    lives = load.player_lives(player_ship.lives, main_batch)
    score_label.text = 'Score: %d' %player_ship.score
    level_label.text = 'Level: %d' %player_ship.level

    # Respawning the asteroids
    asteroids = load.asteroids(max(player_ship.level, 3), player_ship.position, main_batch)

    # Re-establishin the new game_objects
    game_objects = [player_ship] + asteroids

def update(dt):
    """
    Master function which interfaces all queued actions and spawns with the OSD window. Is
    responsible for calling for object updates, object removal, collision handling, death
    transition, and level completion.

    Inputs
    =======================================================================================
    dt              Integer; the input necessary for pyglet.clock.schedule_interval to call
                    the update function repeatedly and at specific times.

    Outputs
    =======================================================================================
    None
    """
    global game_objects, death_label, complete_label, highscore_label
    # Clear everything on the screen
    game_window.clear()
    # Collisions
    for i in range(len(game_objects)):
        for j in range(i+1, len(game_objects)):
            obj_1 = game_objects[i]
            obj_2 = game_objects[j]
            if not obj_1.dead and not obj_2.dead:
                # Checking to see if a collision will occur
                if obj_1.collides_with(obj_2):
                    # Initiating collision response
                    obj_1.handle_collision_with(obj_2)
                    obj_2.handle_collision_with(obj_1)
                    # Special case to handle player_ship extra value changes
                    if type(obj_1) == player.Player:
                        if len(lives) != 0:
                            lives.pop(-1)
                        if player_ship.lives != 0:
                            player_ship.lives -= 1
                        death_label.text = 'You have been killed. You have {} lives remaining. Press Enter to continue.'.format(player_ship.lives)
                        death_label.batch = main_batch
                        if player_ship.lives <= 0:
                            reference.save(player_ship.score)
                            highscore_label = pyglet.text.Label(text='1st:  {0} \n2nd:  {1} \n3rd:  {2} \n4th:  {3} \n5th:  {4} \n6th:  {5} \n7th:  {6} \n8th:  {7} \n9th:  {8} \n10th {9}'.format(
                                    *reference.load()), x=game_window.width/2, y=game_window.height/2+100, anchor_x='center',
                                    anchor_y='center', width=100, multiline=True, batch=main_batch)
                    # Special case to handle the destruction of an asteroid
                    elif type(obj_1) == asteroid.Asteroid and type(obj_2) == bullet.Bullet:
                        player_ship.score += 100*obj_1.scale
                        score_label.text='Score: %d' %player_ship.score
    # Check if player is ready to continue after death
    if player_ship.dead:
        if keys[pyglet.window.key.ENTER] or keys[pyglet.window.key.RETURN]:
            if player_ship.lives > 0:
                keep_values = True
            else:
                keep_values = False
            highscore_label.delete()   
            death_label.delete()
            refresh(keep_values)
    # Update and determine new objects
    to_add = []
    for obj in game_objects:
        obj.update(dt)
        to_add.extend(obj.new_objects)
        obj.new_objects = []
    # Removing dead objects
    for to_remove in [obj for obj in game_objects if obj.dead]:
        to_remove.delete()
        game_objects.remove(to_remove)
    # Updating objects
    game_objects.extend(to_add)
    # Checking number of asteroids remaining
    if all( isinstance(i, (player.Player, bullet.Bullet)) for i in game_objects):
        complete_label.text = 'You have completed level %d. Press enter to continue.' %player_ship.level
        complete_label.batch = main_batch
        if keys[pyglet.window.key.ENTER] or keys[pyglet.window.key.RETURN]:
            complete_label.delete()
            player_ship.level += 1
            level_label.text = 'Level: %d' %player_ship.level
            refresh(True)

# Drawing all main_batch objects
@game_window.event
def on_draw():
    """
    Draws all objects in the main_batch for each event that occurs in the game.

    Inputs
    ====================================================================================
    None

    Outputs
    ====================================================================================
    None

    """
    main_batch.draw()

if __name__ == '__main__':
    # Module function calls below are used to a) call the update function and b) start everything
    pyglet.clock.schedule_interval(update, 1/120.0)
    pyglet.app.run()
