'''return the pig latin equivalent for the word that 
is add ay if starting with consonant and way if starting with vowel'''

test = input("\nEnter a word to continue with:\n")

if test[0].lower() in ['a','e','i','o','u']:
    print(f"Your Pig latin equivalent is: {test+'way'}")
else:
    print(f"Your Pig latin equivalent is: {test[1:] + test[0]+'ay'}")
print('\n')
