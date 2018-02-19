import pyglet
from game import util

class PhysicalObject(pyglet.sprite.Sprite):
    """ All objects in the game that must physically interact with one another. """
    def __init__(self, *args, **kwargs):
        """
        Initialization function called when creating an object of type PhysicalObject

        Input
        =============================================================================
        Varied          *args and **kwargs; can take infinite inputs

        Outputs
        =============================================================================
        None
        """
        super(PhysicalObject, self).__init__(*args, **kwargs)
        self.velocity_x, self.velocity_y = 0.0, 0.0
        self.dead = False
        self.new_objects = []
        self.reacts_to_bullets = True
        self.is_bullet = False

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
        self.x += self.velocity_x*dt
        self.y += self.velocity_y*dt
        self.check_bounds()

    def check_bounds(self):
        """
        Determines if a game object is still located within the game window. If it is
        not, then the object is repositioned to be on the other side of the game
        window.

        Inputs
        ==============================================================================
        None

        Outputs
        ==============================================================================
        None
        """
        min_x = -self.image.width/2
        min_y = -self.image.height/2
        max_x = 1000 + self.image.width/2
        max_y = 800 + self.image.height/2
        if self.x < min_x:
            self.x = max_x
        elif self.x > max_x:
            self.x = min_x
        if self.y < min_y:
            self.y = max_y
        elif self.y > max_y:
            self.y = min_y

    def collides_with(self, other_object):
        """
        Used to determine if any two game objects are about to collide. If they are,
        then this function is used to initiate handling of that collision.

        Inputs
        ==============================================================================
        other_object        game object; the other item in the game window that it is
                            being determined whether there will be a collision between
                            the object calling the function and this other_object

        Outputs
        ==============================================================================
        True / False        boolean; true for if there will be a collision and false
                            if there will not be.
        """
        # Special conditions for collision between a bullet and the player
        if not self.reacts_to_bullets and other_object.is_bullet:
            return False
        if self.is_bullet and not other_object.reacts_to_bullets:
            return False
        collision_distance = self.image.width/2 + other_object.image.width/2
        actual_distance = util.distance(self.position, other_object.position)
        return(actual_distance <= collision_distance)

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
        if type(self) == type(other_object):
            self.dead = False
        else:
            self.dead = True