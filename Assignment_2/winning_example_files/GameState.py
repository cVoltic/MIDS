"""
## Given a float n, and two players
## At each turn, a player can choose to subtract 1 from the number or divide the number by 2
## When the number falls bellow 1, the game is over and the player who choose the last option looses
## A game state is said to be at a hot state when the player has a winning strategy
## A game state is said to be cold otherwise
"""


def determine_state(n):
    """
        Recursive Rule:
            - any n bellow 1 is cold because the player who go will loose
            - The number n is hot if at least one case (n-1 or n/2) is cold

    """

    # base recursive case
    if n < 1:
        return "cold"
    else:
        state_1 = determine_state(n-1)
        state_2 = determine_state(n/2)
        if state_1 == 'cold' or state_2 == 'cold':
            return "hot"
        else: return "cold"


# main function
if __name__ == '__main__':
    with open("input.txt", "r") as f:
        lines = f.readlines()
        with open("output_kt.txt", "w") as of:

            for n in lines:
                game_state = determine_state(float(n))
                print(game_state)
                of.write(game_state+"\n")

        of.close()
    f.close()