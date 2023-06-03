"""
Input is a vector of F's and B's, in terms of forwards and backwards caps
Output is a set of commands (printed out) to get either all F's or all B's
Fewest commands are the goal!

Please see the problem write-up to get more details
"""

caps = ["F", "F", "B", "B", "B", "F", "B", "B", "B", "F", "F", "B", "F"]
cap2 = ["F", "F", "B", "B", "B", "F", "B", "B", "B", "F", "F", "F", "F"]


def pleaseConform(caps):
    """
    caps: a list of caps represented as 'F': forward, 'B': backward

    goal: minimize the number of commands you have to shout out 
    """
    # * observation: number of commands for flipping a type of cap is simply 
    # the number of separate blocks of that type of cap. a block is defined 
    # as consecutive caps of same type.
    # * ["F", "F", "B", "B", "B", "F", "B", "B", "B", "F", "F", "B", "F"] would have:
    # * number of commands for F: 4
    # * number of command for B: 3
    # -> idea: simply count the number of commands for both F and B, 
    # and then take the minimum between them.

    # * implementation:
    # * initialize 2 arrays for 2 types of blocks: block F and block B
    # * initialize current block with caps[0] as the first element
    # * loop through caps. if current cap is different from current block[0], 
    # then push current block onto corresponding block(F or B). then initialize 
    # new current block with current block[0] = current cap
    # * after done looping through caps, find the block with min length. loop
    # through min block and print('people in positions...')
    # * finished.
    pass


pleaseConform(caps)
##pleaseConform(cap2)
