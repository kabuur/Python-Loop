# By now you are familiar with two important concepts: 1)
#  counting with for loops and 2) 
# the dictionary get method.
#  These two can actually be combined to create a
#  useful counter dictionary, something you will
#  likely come across again. For example, 
# we can create a dictionary, word_counter,
#  that keeps track of the total count of each word in a string.
book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']



word_counter = {}

for word in book_title:
    if word in word_counter:
        
        word_counter[word] += 1 
    else:
         word_counter[word] = 1


print(word_counter)