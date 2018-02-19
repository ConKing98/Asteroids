import pyglet
from game import physicalobject, resources

class Bullet(physicalobject.PhysicalObject):
    """Bullets fired from the player"""

    def __init__(self, *args, **kwargs):
        """
        Initialization function called when creating an object of type Bullet.

        Inputs
        ======================================================================
        Varied          *args and **kwargs; can take infinite inputs

        Outputs
        ======================================================================
        None
        """
        super(Bullet, self).__init__(resources.bullet_image, *args, **kwargs)
        pyglet.clock.schedule_once(self.die, 0.8)
        self.is_bullet = True

    def die(self, dt):
        """
        Called to kill / remove a bullet. It is called by the
        pyglet.clock.schedule_once function in the Buller __init__ function by
        default. Base state is to make a bullet die after 0.8 seconds.

        Inputs
        ======================================================================
        dt              int; the function input required for any function to
                        be linked to the time management function in main.py:
                        pyglet.clock.schedule_interval

        Outputs
        ======================================================================
        None
        """
        self.dead = True