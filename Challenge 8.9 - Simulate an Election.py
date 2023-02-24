# With some help from the random module and a little conditional logic, you can simulate an election between two
# candidates.
# Suppose two candidates, candidate A and candidate B, are running for mayor in a city with three voting regions.
# The most recent pools show that candidate A has the following chances for winning in each region:
# Region 1: 87 percent chance of winning.
# Region 2: 65 percent chance of winning
# Region 3: 17 percent chance of winning
# Write a program that simulates the election ten thousand times and prints the percentage of times in which
# Candidate A wins.
# To keep things simple, assume that a candidate winds the election if they win in at least two of the three regions.

import random


def unfair_voting(percentage_of_A):
    if random.random() < percentage_of_A:
        return "A"
    else:
        return "B"


A_tally = 0
B_tally = 0
voters = 10_000
for voting1 in range(voters):
    if unfair_voting(.87) == "A":
        A_tally = A_tally + 1
    else:
        B_tally = B_tally + 1
print(f"The total votes of region 1 for candidate A is {(A_tally/voters) * 100} and for candidate B is"
      f" {(B_tally / voters) * 100}")


for voting1 in range(voters):
    if unfair_voting(.65) == "A":
        A_tally = A_tally + 1
    else:
        B_tally = B_tally + 1
print(f"The total votes of region 2 for candidate A is {(A_tally/voters) * 100} and for candidate B is"
      f" {(B_tally / voters) * 100}")


if A_tally > B_tally:
    print(f"Candidate A won the election with the votes of {(A_tally/voters) * 100} votes while candidate B has"
          f" {(B_tally / voters) * 100} votes.")
else:
    print(f"Candidate B won the election with the votes of {(B_tally/voters) * 100} votes while candidate A has"
          f" {(B_tally / voters) * 100} votes.")

for voting1 in range(voters):
    if unfair_voting(.17) == "A":
        A_tally = A_tally + 1
    else:
        B_tally = B_tally + 1

print(f"The total votes of region 3 for candidate A is {(A_tally/voters) * 100} and "
      f" for candidate B is {(B_tally / voters) * 100}")
