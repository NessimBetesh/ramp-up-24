def reverse(word):
    reverseWord = word[::-1]
    
    vowels = 'AEIOUaeiou'
    vowelCount = 0
    for char in reverseWord:
        if char in vowels:
            vowelCount+=1
    print("Original word: ", word)
    print("Reversed word: ", reverseWord)
    print("Vowel Count: ", vowelCount)

reverse(input("Write a word \n"))