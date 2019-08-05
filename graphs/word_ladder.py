"""
Word Ladder Problem: You are given 2 words A and B, both of the same length. Your task is to transform one word to another changing only one letter each time. Each intermediate word should be a valid word in the dictionary. Print out the length of the path. (Alternate version: print out the intermediate words)

A = CAB, B = DOG 
Result: 4 (CAB -> COB -> COG -> DOG)

"""

from nltk.corpus import words


dictionary = set(words.words())

def get_valid_transformations(word):
    words = set()
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for i, char in enumerate(word):
        for letter in letters:
            if letter == char:
                continue
            
            new_word = list(word)
            new_word[i] = letter
            new_word = "".join(new_word)

            if new_word in dictionary:
                words.add(new_word)

    return words

    

def word_ladder(start, end):
    levels = {start: 0}
    frontier = [start]
    i = 1
    while frontier:
        next = []
        for word in frontier:
            words = get_valid_transformations(word)

            for word in words:
                if word == end:
                    return i + 1
                elif word not in levels:
                    levels[word] = i
                    next.append(word)
        
        frontier = next
        i += 1


"""
Instead, print the path taken
"""
def word_ladder_path(start, end):
    parents = {start: None}
    frontier = [start]
    
    while frontier:
        next = []

        for w in frontier:
            words = get_valid_transformations(w)
            parent = w

            if end in words:
                lst = [end]
                while parent in parents:
                    lst.append(parent)
                    parent = parents[parent]
                lst.reverse()
                return ' -> '.join(lst)
                
            for word in words:
                if word not in parents:
                    parents[word] = parent
                    next.append(word)

        frontier = next