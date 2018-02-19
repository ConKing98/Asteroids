import math, pyglet
from game import physicalobject, resources, bullet
from pyglet.window import key

class Player(physicalobject.PhysicalObject):
    """ The class used for the player ship and holding all player values. """
    def __init__(self, *args, **kwargs):
        """
        Initialization function called when creating an object of type Player.

        Inputs
        =============================================================================
        Varied          *args and **kwargs; can take infinite inputs

        Outputs
        =============================================================================
        None
        """
        super(Player, self).__init__(img=resources.player_image, *args, **kwargs)
        # Used to handle keyboard inputs in the Player update function
        self.key_handler = key.KeyStateHandler()
        self.engine_sprite = pyglet.sprite.Sprite(img=resources.engine_image, *args, **kwargs)
        # Basic starting characteristics
        self.thrust = 300.0
        self.rotate_speed = 200.0
        self.engine_sprite.visible = False
        self.visible = True
        self.new_objects = []
        self.bullet_speed = 700.00
        self.reacts_to_bullets = False
        self.lives = 3
        self.score = 0
        self.level = 1

    def fire(self):
        """
        The calculations used to determine how a bullet will fire from the player.

        Inputs
        ============================================================================
        None

        Outputs
        ============================================================================
        None
        """
        # Angle of attack
        angle_radians = math.pi/2-math.radians(self.rotation)
        # Starting position
        ship_radius = self.image.width/2
        bullet_x = self.x + math.cos(angle_radians)*ship_radius
        bullet_y = self.y + math.sin(angle_radians)*ship_radius
        # Creating the bullet
        new_bullet = bullet.Bullet(bullet_x, bullet_y, batch=self.batch)
        # Velocity
        bullet_vx = (self.velocity_x + math.cos(angle_radians)*self.bullet_speed)
        bullet_vy = (self.velocity_y + math.sin(angle_radians)*self.bullet_speed)
        new_bullet.velocity_x = bullet_vx
        new_bullet.velocity_y = bullet_vy
        # Adding the to the draw list
        self.new_objects.append(new_bullet)

    def handle_collision_with(self, other_object):
        """
        Used to initiate the result of collides_with determining that there will be a
        collision. Will set the two objects to be dead unless they are of the same
        type. This condition is so that there are no asteroid - asteroid collisions.

        Inputs
        ==============================================================================
        other_object        game object; the other item in the game window that it is
                            being determined whether there will be a collision between
                            the object calling the function and this other_object

        Outputs
        ==============================================================================
        None
        """
        super(Player, self).handle_collision_with(other_object)

    def update(self, dt):
        """
        Determines the new characteristics to be demonstrated in the game window

        Inputs
        =============================================================================
        dt              int; the function input required for any function to
                        be linked to the time management function in main.py:
                        pyglet.clock.schedule_interval

        Outputs
        =============================================================================
        None
        """
        super(Player, self).update(dt)
        # Space bar to fire bullets
        if self.key_handler[key.SPACE] and not self.dead:
                self.fire()
                # Setting to False so that spawning is not continuous
                self.key_handler[key.SPACE] = False
        # Left arrow to rotate left
        if self.key_handler[key.LEFT]:
            self.rotation -= self.rotate_speed*dt
        # Right arrow to rotate right
        if self.key_handler[key.RIGHT]:
            self.rotation += self.rotate_speed*dt
        # Up arrow to move in that direction
        if self.key_handler[key.UP]:
            angle_radians = math.pi/2-math.radians(self.rotation)
            force_x = math.cos(angle_radians)*self.thrust*dt
            force_y = math.sin(angle_radians)*self.thrust*dt
            self.engine_sprite.rotation = self.rotation
            self.engine_sprite.x = self.x
            self.engine_sprite.y = self.y
            self.engine_sprite.visible = True
            self.velocity_x += force_x
            self.velocity_y += force_y
        else:
            self.engine_sprite.visible = False

    def delete(self):
        """
        Called upon death to make sure that no component of the destroyed ship
        will be displayed while the player is marked as dead.

        Inputs
        ======================================================================
        None

        Outputs
        ======================================================================
        None
        """
        self.engine_sprite.visible = False
        self.visible = False