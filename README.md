System Requirements
=============================================================================

    - Python 3.x with all normally pre-installed modules
        Specifically requires 'platform' module.

    - Pyglet
        Download and installation instructions below.

    - A supported operating system
        Currently support exists for Windows, OSx, and Linux


Installing Pyglet (Windows)
---------------------------
    1) Add python to your system path
        1.1) Navigate to System Properties -> Advanced -> Environment
             Variables
        1.2) In the System Variables section, select a system variable
             labelled Path, then select Edit
        1.3) On the right-hand side, select new, then add the file path
             to your current version of python.
        1.4) Confirm a successful addition to the Path by opening a
             command prompt window and typing "python" (no quotation 
             marks). A python command line should be launched.
        1.5) Type "exit()" to exit the python command line.
    2) Use pip to get and install pyglet
        2.1) Type the command "python -m pip install pyglet"
        2.2) If you already have pyglet, a message will appear stating
             this, if not, the module will be downloaded and installed.
        2.3) Once the installation is complete, type "python".
        2.4) In the python command line type "import pyglet". If no
             error messages appear, then the module has been properly
             installed.


Installing Pyglet (Mac)
-----------------------
    Note: This assumes you have a version of OSx with python pre-installed
          and therefore already added to the command line path.
    1) Getting pip
        Note: Some versions of OSx come with a trimmed-down distribution
              of python. This version does not include pip, hence why we
              must first install it.
        1.1) Open the Terminal and type "sudo easy_install pip". The
             system should check if you have pip, and if not, begin the
             download.
    2) Use pip to get and install pyglet
        2.1) Type the command "sudo pip install pyglet" into the already
             open Terminal
        2.2) If you already have pyglet, a message will appear stating
             this, if not, the module will be downloaded and installed.
        2.3) Once the installation is complete, type "python".
        2.4) In the python command line type "import pyglet". If no
             error messages appear, then the module has been properly
             installed.


Installing Pyglet (Linux)
-------------------------
    1) Getting pip
        - Debian / Ubuntu
            1.1) For python 3, open the command prompt and type the command 
                 "apt install python3-pip". The system will check for pip
                 and install it if it cannot find pip.
        - CentOS / RHEL
            1.1) Open the command prompt and type the command "yum install
                 epel-release". This is needed because pip is not included
                 in the official software reprositories at the time of 
                 writing.
            1.2) Once the system is done installing the above, type in "yum
                 install python-pip". The system will check for pip and 
                 install it if it cannot find pip.
        - Fedora
            1.1) For python 3, open the command prompt and type the command
                 "dnf install python3". The system will check for pip and 
                 install it if it cannot find pip.
        - Arch Linux
            1.1) Open the command prompt and type the command "pacman -S
                 python-pip". The system will check for pip and install it 
                 if it cannot find pip.
        - openSUSE
            1.1) Open the command prompt and type the command "zypper
                 install python3-pip". The system will check for pip and 
                 install it if it cannot find pip.
    2) Use pip to get and install pyglet
        2.1) On the command prompt, type the command "pip install pyglet".
        2.2) If you already have pyglet, a message will appear stating
             this, if not, the module will be downloaded and installed.
        2.3) Once the installation is complete, type "python".
        2.4) In the python command line type "import pyglet". If no
             error messages appear, then the module has been properly
             installed.


Launching Asteroids
=============================================================================

    1) Navigate to the file "main.py" in the same file directory as this
       ReadMe document.
    2) Double click on the "main.py" file, selecting run with python if
       necessary.


Game Mechanics
=============================================================================

General Principle
-----------------
    The game of asteroids is about surviving as long as possible in
    progressively more difficult levels that are filled with asteroids. Each
    asteroids, when shot, will break apart into a random number of pieces
    twice before finally having that portion of the asteroid disappear. To
    complete a level, you need to destroy all asteroids that are present in
    that level.


Controls
--------

    Up Arrow		Accelerate forward. Note that this does not mean move
                        forward at a constant rate, therefore holding the key
                        down will result in a progressively faster speed.

    Left Arrow 		Rotate counter clockwise at a constant speed.

    Right Arrow 	Rotate clockwise at a constant speed.

    Spacebar 		Shoot. This is used to fire projectiles which will
                        destroy the asteroids

    Enter / Return 	Used to continue when either a) navigating to a new
                        level or b) having died and needing to restart.


Score
-----
    Each successful hit on that a bullet makes with an asteroid gives the
    player a certain number of points. The number of points is based off of
    the size of the asteroid hit.

    Large Asteroid 	100 pts
    Medium Asteroid 	50 pts
    Small Asteroid 	25 pts


Edge of the Window
------------------
    This version of Asteroids incorporates a screen wrap effect, meaning that
    once any game object reaches the edge of the screen, it will continue in
    its trajectory from the side of the screen opposite to the one it was
    just at.

    Do note that sometimes an object will just have a small region of its
    image visible and the rest will be beyond the window. This is by design.


Images
------
    It may be noted from time to time that there is a large black rectangle
    around the image for some game object. At current, this is due to
    limitations and issues with the current graphics design software: Windows
    Paint.


Legal
=============================================================================
All game content was created by Connor Kingdon in Python with the use of two
modules: pyglet and platform. January 30, 2018
    
This content was created in python version 3.6.3150.1013 and has only been
verified in that version.

This content is intended for personal use only.

The distribution of this content is restricted baring the creator's
permissions.
