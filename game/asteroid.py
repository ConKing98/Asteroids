import pyglet, random
from game import resources, physicalobject

class Asteroid(physicalobject.PhysicalObject):
    """ The class used for the asteroids that are to be destroyed """
    def __init__(self, *args, **kwargs):
        """
        Initialization function called when creating an object of type Asteroid.

        Inputs
        =============================================================================
        Varied          *args and **kwargs; can take infinite inputs

        Outputs
        =============================================================================
        None
        """
        super(Asteroid, self).__init__(resources.asteroid_image, *args, **kwargs)
        self.rotate_speed = random.random()*100.0-50.0

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
        super(Asteroid, self).handle_collision_with(other_object)
        # Condition used to determine if the asteroid should break into smaller pieces
        if self.dead and self.scale > 0.25:
            # The number of asteroids to be broken into
            num_asteroids = random.randint(2,5)
            for i in range(num_asteroids):
                # Each new asteroid gets a random collection of properties
                new_asteroid = Asteroid(x=self.x, y=self.y, batch=self.batch)
                new_asteroid.rotation = random.randint(0,360)
                new_asteroid.velocity_x = random.random()*70+self.velocity_x
                new_asteroid.velocity_y = random.random()*70+self.velocity_y
                new_asteroid.scale = self.scale/2
                # Adding to the draw object list
                self.new_objects.append(new_asteroid)

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
        super(Asteroid, self).update(dt)
        self.rotation += self.rotate_speed*dt