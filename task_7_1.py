"""
    Task 1

    Make a program that has some sentence (a string) on input and returns a
     dict containing all unique words as keys and the number of occurrences
     as values. """

any_sentence = input("Enter your sentence: ").split()
dictionary = {item: value for value, item in enumerate(any_sentence, start=1)}
print(dictionary)
