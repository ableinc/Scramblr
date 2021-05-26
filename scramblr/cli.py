from module import Scramblr
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Encryption tool')
    parser.add_argument('--scramble', help='The phrase to be scrambled',
                        default=None)
    parser.add_argument('--unscramble', help='The phrase to be unscrambled',
                        required=False)
    parser.add_argument('reverse', type=bool, help='Use the scramblr in reverse. Unscramble with original phrase, against the scrambled phrase', nargs='*', default=False)
    parser.add_argument('special_chars', metavar='specialchars', type=bool, nargs='*',
                    help='Whether or not to use special characters', default=False)
    args = parser.parse_intermixed_args()
    scramblr = Scramblr(args.special_chars)
    if args.scramble is not None:
        print('Original Phrase: ', args.scramble)
        print('Scrambled: ', scramblr.scramble(args.scramble))
    else:
        try:
            print('Unscrambled: ', scramblr.unscramble(args.unscramble, args.reverse[0]))
        except TypeError:
            print('Unscrambled: ', scramblr.unscramble(args.unscramble, args.reverse))
