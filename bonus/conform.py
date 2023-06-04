"""
Input is a vector of F's and B's, in terms of forwards and backwards caps
Output is a set of commands (printed out) to get either all F's or all B's
Fewest commands are the goal!

Please see the problem write-up to get more details
"""

caps = ["F", "F", "B", "B", "B", "F", "B", "B", "B", "F", "F", "B", "F"]
cap2 = ["F", "F", "B", "B", "B", "F", "B", "B", "B", "F", "F", "F", "F"]
cap3 = ["F", "F", "B", "H", "B", "F", "B", "B", "B", "F", "H", "F", "F"]


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

    # F/B_blocks: 2D array (blocks)
    F_blocks = []
    B_blocks = []
    # cur_block: 1D array consisting of indices
    cur_block = [0]
    cur_block_cap = caps[0]

    for i in range(len(caps)):
        cap = caps[i]

        # if current cap is different from current block
        if cap != cur_block_cap:
            # push current block onto corresponding blocks
            # if the current block has indicies of people with 'H',
            # then don't push anywhere (basically, ignore 'H' blocks)

            if cur_block_cap == "B":
                B_blocks.append(cur_block)
            elif cur_block_cap == "F":
                F_blocks.append(cur_block)

            # create new current block with current index
            cur_block = [i]
            # update current block's representative cap
            cur_block_cap = caps[i]

        # if current cap belongs to current block
        else:
            cur_block.append(i)

    # find F/B_blocks that has min length -> the target blocks for voice commands
    if len(F_blocks) < len(B_blocks):
        target_blocks = F_blocks
    else:
        target_blocks = B_blocks

    # loop through target blocks to print out voice commands
    for block in target_blocks:
        # if block only has 1 index, print 'Person'
        if len(block) == 1:
            print("Person at position %d flip your cap!" % block[0])
        else:
            print(
                "People in position %d through %d flip your caps!"
                % (block[0], block[-1])
            )


pleaseConform(caps)
# pleaseConform(cap2)
# pleaseConform(cap3)
