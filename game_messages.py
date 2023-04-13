
def named_egg_msg(chosen_name):
    """This message will show after a player names a commandogotchi
    at the start of a new game."""

    print(f'''
          Congratulations! {chosen_name} will hatch from an egg
          soon. Please take good care of {chosen_name} and do not
          let {chosen_name} die.
          ''')


def hatch_messages():
    """Returns a list of messages. These messages will display while the user
    waits for the new commandogotchi egg to hatch."""

    hatch_messages = ["A new egg! Cool! What will hatch from it?",
                      "Hmm, is hasn't hatched yet, but it should soon.",
                      "Oh look! The egg is moving!",
                      "There are cracks on the egg! Any minute now!",
                      "...", ]
    return hatch_messages
