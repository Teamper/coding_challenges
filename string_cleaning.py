# Python 2
# Your spy, Beta Rabbit, has managed to infiltrate a lab of mad scientists who are turning rabbits into zombies. 
# He sends a text transmission to you, but it is intercepted by a pirate, who jumbles the message by repeatedly 
# inserting the same word into the text some number of times. At each step, he might have inserted the word anywhere, 
# including at the beginning or end, or even into a copy of the word he inserted in a previous step. By offering the pirate a dubloon, 
# you get him to tell you what that word was. A few bottles of rum later, he also tells you that the original text was 
# the shortest possible string formed by repeated removals of that word, and that the text was actually the lexicographically earliest string 
# from all the possible shortest candidates. Using this information, can you work out what message your spy originally sent?

# For example, if the final chunk of text was "lolol," and the inserted word was "lol," the shortest possible strings are "ol" (remove "lol" from the beginning) 
# and "lo" (remove "lol" from the end). The original text therefore must have been "lo," the lexicographically earliest string.

# Write a function called answer(chunk, word) that returns the shortest, lexicographically earliest string that can be formed by 
# removing occurrences of word from chunk. Keep in mind that the occurrences may be nested, and that removing one occurrence might result in another. 
# For example, removing "ab" from "aabb" results in another "ab" that was not originally present. Also keep in mind that your spy's original message 
# might have been an empty string.

# chunk and word will only consist of lowercase letters [a-z]. chunk will have no more than 20 characters. word will have at least one character, 
# and no more than the number of characters in chunk.

import re

def answer(chunk, word):
    def get_chunk_combinations(chunk, word):
        '''Get all possible chunks if a given word was removed once from the occurrence.'''
        word_locations = find_word_locations(chunk, word)
        chunk_combinations = []
        for index_start in word_locations:
            chunk_combinations.append(build_new_chunk(chunk, index_start, len(word) + index_start))
        return(chunk_combinations)

    def find_word_locations(chunk, word):
        '''Find starting indices of all occurrences of a given substring in a given string.'''
        return [m.start() for m in re.finditer('(?=%)'.format(word), chunk)]

    def build_new_chunk(chunk, index_start, index_end):
        '''Return a new string with a given range of characters to remove based on a starting and ending index.'''
        return chunk[:index_start] + chunk[index_end:]

    # Perform iterative depth-first-search
    stack = [chunk]
    discovered = []
    smallest_chunks = []
    while len(stack) != 0:
        vertex = stack.pop()
        
        if vertex not in discovered:
            discovered.append(vertex)
            edges = get_chunk_combinations(vertex, word)
            
            if len(edges) == 0:
                smallest_chunks.append(vertex)    
            else:
                for combo in edges:
                    stack.append(combo)
                    
    smallest_chunks.sort()
    return smallest_chunks[0]
