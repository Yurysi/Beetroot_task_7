"""
    Task 1

    Make a program that has some sentence (a string) on input and returns a
     dict containing all unique words as keys and the number of occurrences
     as values. """

any_sentence = input("Enter your sentence: ")
dictionary = {}
a = 0
word = ''
for sentece in any_sentence:
    if sentece != ' ':
        word = ''.join(any_sentence[:id(any_sentence.find(' '))+1])

dictionary[word] = len(word)
print(dictionary)
