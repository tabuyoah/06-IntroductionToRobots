"""
An opportunity to explore how to make an EV3 Robot make sounds.

Authors: Dave Fisher, David Mutchler, Vibha Alangar,
         their colleagues, and PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import simple_rosebotics as rb


# ------------------------------------------------------------------------------
# TODO: 2.  This is an   ** OPTIONAL **   exercise.
#   Using the DOT trick, add code to  make_sounds  to make the robot
#   make sounds in various ways:  Beep, Tone, Speech, Song.
# ------------------------------------------------------------------------------
def main():
    fun_song = [(392, 350, 100), (392, 350, 100), (392, 350, 100),
                (311.1, 250, 100), (466.2, 25, 100), (392, 350, 100),
                (311.1, 250, 100), (466.2, 25, 100), (392, 700, 100),
                (587.32, 350, 100), (587.32, 350, 100), (587.32, 350, 100),
                (622.26, 250, 100), (466.2, 25, 100), (369.99, 350, 100),
                (311.1, 250, 100), (466.2, 25, 100), (392, 700, 100),
                (784, 350, 100), (392, 250, 100), (392, 25, 100),
                (784, 350, 100), (739.98, 250, 100), (698.46, 25, 100),
                (659.26, 25, 100), (622.26, 25, 100), (659.26, 50, 400),
                (415.3, 25, 200), (554.36, 350, 100), (523.25, 250, 100),
                (493.88, 25, 100), (466.16, 25, 100), (440, 25, 100),
                (466.16, 50, 400), (311.13, 25, 200), (369.99, 350, 100),
                (311.13, 250, 100), (392, 25, 100), (466.16, 350, 100),
                (392, 250, 100), (466.16, 25, 100), (587.32, 700, 100),
                (784, 350, 100), (392, 250, 100), (392, 25, 100),
                (784, 350, 100), (739.98, 250, 100), (698.46, 25, 100),
                (659.26, 25, 100), (622.26, 25, 100), (659.26, 50, 400),
                (415.3, 25, 200), (554.36, 350, 100), (523.25, 250, 100),
                (493.88, 25, 100), (466.16, 25, 100), (440, 25, 100),
                (466.16, 50, 400), (311.13, 25, 200), (392, 350, 100),
                (311.13, 250, 100), (466.16, 25, 100), (392.00, 300, 150),
                (311.13, 250, 100), (466.16, 25, 100), (392, 700)]

    talker = rb.Speech('Hayden has ligma')
    rb.Song(fun_song).play()
    talker.speak()

main()
