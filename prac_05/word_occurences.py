"""
CP1404/CP5632 Practical 5
Word Occurrences Counter
Estimate: 15 minutes
Actual:   17 minutes
"""

counted_words = {}
string = input("please enter a string:")
words = string.split()

for word in words:
    try:
        counted_words[word] += 1
    except:
        counted_words[word] = 1

words = list(counted_words.keys())
words.sort()

max_length = max((len(word) for word in words))
for word in words:
    print(f"{word:{max_length}} : {counted_words[word]}")



