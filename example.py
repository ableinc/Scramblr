from scramblr.module import Scramblr

scramblr = Scramblr(use_special_chars=True)
phrase = input('Enter phrase: ')
print('Original Phrase: ', phrase)
scrambled = scramblr.scramble(phrase)
print('Scrambled: ', scrambled)

print('-------------')

print('Unscrambled: ', scramblr.unscramble(scrambled))
print('Unscrambled Reverse: ', scramblr.unscramble(phrase, True))
        