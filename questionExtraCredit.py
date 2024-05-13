
word = input("Enter a word: ")

word = word.lower()


length_word = len(word)

letters = 0
for index in range(len(word)):
    if word[index] == word[-1-index]:
        letters += 1
if letters == length_word:
    print(word, "is a palindrome.")
else:
    print(word, "is not a palindrome.")