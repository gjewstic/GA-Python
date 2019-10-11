# Count how many times a word is used in a sentence
'''
words = str(input('Enter a sentence: '))
split = words.split(' ')
for s in split:
    print(s + ': ' + str(split.count(s)))
'''
# create a dictionary
frequency = {

}
# break a sentence  into words (tokenize)
sentence = input('Enter a sentence: ')
words = sentence.split(' ')
# loop over words
for word in words:
    # Check if in dictionary already
    if word in frequency:
        frequency[word] += 1
    else:
        # creates a new key and sets value to 1
        frequency[word] = 1

print(frequency)
