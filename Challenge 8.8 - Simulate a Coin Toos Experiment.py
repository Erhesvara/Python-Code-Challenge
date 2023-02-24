# Suppose you flip a fair coin repeatedly until it lands on heads and tails at least one time each. In other word,
# after the first flip, you continue to flip the coin until it lands on the other side.
# Doing this generates a sequence of heads and tails. For example, the first time you do this experiment, the sequence
# might be heads, heads, tails.
# on average, how many flips are needed for the sequence to contain both heads and tails?
# write a simulation that runs ten thousand trials of the experiment and prints the average number of flip per trial.

import random


def coin_flip():
    if random.randint(0, 1) == 0:
        return "heads"
    else:
        return "tails"


heads_tally = 0
tail_tally = 0
flip = 0
roll = 10_000

while (heads_tally and tail_tally) != 1:
    for n in range(roll):
        if coin_flip() == "heads":
            heads_tally = heads_tally + 1
            flip = flip + 1
        else:
            tail_tally = tail_tally + 1
            flip = flip + 1
    break

print(f"The heads count: {heads_tally} and the tails count {tail_tally}")
print(f"The average flip is {flip / roll}")

# The answer of this experiment in resources
# import random
#
#
# def coin_flip():
#     """Randomly return 'heads' or 'tails'."""
#     if random.randint(0, 1) == 0:
#         return "heads"
#     else:
#         return "tails"
#
#
# flips = 0
# num_trials = 10_000
#
# for trial in range(num_trials):
#     if coin_flip() == "heads":
#         # Increment the number of flips by 1
#         flips = flips + 1
#         while coin_flip() == "heads":
#             # Keep incrementing the total number of flips
#             # until "tails" is returned by coin_flip()
#             flips = flips + 1
#         # Once coin_flip() return "tails", the loop will exit,
#         # but we need to add one more to flips to track the
#         # last flip that generated "tails"
#         flips = flips + 1
#     else:
#         # coin_flip() returned "tails" on the first flip.
#         # Increment the number of flips by 1
#         flips = flips + 1
#         while coin_flip() == "tails":
#             # Keep incrementing the total number of flips
#             # until "heads" is returned by coin_flip()
#             flips = flips + 1
#         # Once coin_flip() returns "heads", the loop will exit,
#         # but we need to add one more to flips to track the
#         # last flip that generated "heads"
#         flips = flips + 1
#
# avg_flips_per_trial = flips / num_trials
# print(f"The average number of flips per trial is {avg_flips_per_trial}.")


