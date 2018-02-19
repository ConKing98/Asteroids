import pyglet, math

def distance(point_1=(0, 0), point_2=(0, 0)):
    """
    Returns the distance between two points
    
    Inputs
    ======================================================================
    point_1         vector; the location in terms of x and y coordinates
                    of object 1
    point_2         vector; the location in terms of x and y coordinates
                    of object 2

    Outputs
    ======================================================================
    Distance        float; the distance in pixels between the two objects
    """
    return math.sqrt((point_1[0] - point_2[0]) ** 2 +
                     (point_1[1] - point_2[1]) ** 2)