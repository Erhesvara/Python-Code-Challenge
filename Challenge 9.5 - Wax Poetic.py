# In this challenge, you'll write a program that generates poetry.

# Create five lists of different word types:
# 1. Nouns: ["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla"]
# 2. Verbs: ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]
# 3. Adjectives: ["furry", "balding", "incredulous", "fragrant", "exuberant", "glistening"]
# 4. Prepositions: ["against", "after", "into", "beneath", "upon", "for", "in", "like", "over", "within"]
# 5. Adverbs: ["curiously", "extravagantly", "tantalizingly", "furiously", "sensuously"]

# Randomly Select the following number of elements from each list:
# - Three nouns, Three verbs, Three adjectives, Two prepositions, One adverb

# You can do this with the choice() function in the random module. This function takes a list as input and return a
#   randomly selected element of the list.

# for example, here's how to use random.choice() to get random element from the list ["a", "b", "c"]:
# import random
# random_element = random.choice(["a", "b", "c"])

# Using the randomly selected words, generate and display a poem with the following structure
# inspired by Clifford Pickover:
# {A/an} {adj1} {noun1}
# {A/an} {adj1} {noun1} {verb1} {prep1} the {adj2} {noun2}
# {adverb1}, the {noun1} {verbs2}
# the {noun2} {verbs3} {prep2} a {adj3} {noun}

# Here, adj stands for adjective and prep for preposition.
# Here's an example of the kind of poem your program might generate:
# A furry horse
# A furry horse curdles within the fragrant mango
# extravagantly, the horse slurps
# the mango meows beneath a balding extrovert

# each time it runs, it must generate a new poem.

# answer:
import random

Nouns = ["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla"]
Verbs = ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]
Adjectives = ["furry", "balding", "incredulous", "fragrant", "exuberant", "glistening"]
Prepositions = ["against", "after", "into", "beneath", "upon", "for", "in", "like", "over", "within"]
Adverbs = ["curiously", "extravagantly", "tantalizingly", "furiously", "sensuously"]

# randomly select words from each list
noun1, noun2, noun3 = random.sample(Nouns, 3)
verb1, verb2, verb3 = random.sample(Verbs, 3)
adj1, adj2, adj3 = random.sample(Adjectives, 3)
prep1, prep2 = random.sample(Prepositions, 2)
adverb1 = random.choice(Adverbs)

if noun1[0] in "aeiou":
    article = "An"
else:
    article = "A"

# print the poem
print(f"{article} {adj1} {noun1}\n")
print(f"{article} {adj1} {noun1} {verb1} {prep1} the {adj2} {noun2}")
print(f"{adverb1}, the {noun1} {verb2}")
print(f"The {noun2} {verb3} {prep2} a {adj3} {noun3}")
