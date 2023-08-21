#!/usr/bin/python
import sys
import math
import argparse
import random
import curses

GRADIENTS = {
    'rainbow': {
        'red': lambda i, freq: math.sin(freq * i) * 127 + 128,
        'green': lambda i, freq: math.sin(freq * i + 2 * math.pi / 3) * 127 + 128,
        'blue': lambda i, freq: math.sin(freq * i + 4 * math.pi / 3) * 127 + 128
    },
    'ocean': {
        'red': lambda i, freq: math.sin(freq * i) * 127 + 128,
        'green': lambda i, freq: math.sin(freq * i + 5 * math.pi / 6) * 127 + 128,
        'blue': lambda i, freq: 255
    }
    # Add other gradient styles as needed
}

def lolcat(text: str, frequency: float=0.5, gradient='rainbow'):
    frequency = 0.1 * (2 ** frequency) - 0.1
    phase_offset = random.uniform(0, 2 * math.pi)
    colored_text = ''
    for i in range(len(text)):
        gradient_funcs = GRADIENTS.get(gradient, GRADIENTS['rainbow'])
        red = gradient_funcs['red'](i + phase_offset, frequency)
        green = gradient_funcs['green'](i + phase_offset, frequency)
        blue = gradient_funcs['blue'](i + phase_offset, frequency)
        colored_text += "\033[38;2;{};{};{}m{}".format(int(red), int(green), int(blue), text[i])
    print(colored_text, end='')

def initcli():
    parser = argparse.ArgumentParser(description="Rainbow-fy your text!")
    parser.add_argument('files', metavar='FILE', type=str, nargs='*', help="files to read, if empty, stdin is used")
    parser.add_argument('-f', '--frequency', type=float, default=1, help="set color frequency, default is 1")
    parser.add_argument('-g', '--gradient', type=str, choices=GRADIENTS.keys(), default='rainbow', help="choose a gradient style")
    parser.add_argument('-i', '--interactive', action='store_true', help="interactive mode")
    return parser.parse_args()

# Parse files
def parsefiles(files: list, freq: float):
    for filename in files:
        try:
            with open(filename, 'r') as f:
                for line in f:
                    lolcat(line, freq)
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.", file=sys.stderr)
        except PermissionError:
            print(f"Error: Permission denied for '{filename}'.", file=sys.stderr)
        except IsADirectoryError:
            print(f"Error: '{filename}' is a directory.", file=sys.stderr)
        except (UnicodeDecodeError, UnicodeError, UnicodeEncodeError, UnicodeTranslateError):
            print(f"Error: '{filename}' is not a text file.", file=sys.stderr)
        except Exception as e:
            print(f"Error: An unexpected error occurred while reading '{filename}': {e}", file=sys.stderr)

# Main function
def main():
    args = initcli()

    if args.interactive:
        print("Interactive mode. Type and see the rainbow. Press CTRL+D to exit.")
        while True:
            try:
                user_input = input()
                lolcat(user_input + '\n', args.frequency, args.gradient)
            except EOFError:
                break
            except KeyboardInterrupt:
                print("\nQuitting...")
                break

    elif args.files:
        parsefiles(args.files, args.frequency, args.gradient)
    
    elif not sys.stdin.isatty():
        for line in sys.stdin:
            lolcat(line, args.frequency, args.gradient)
    
    else:
        print("usage: lolpy [-h] [-f FREQUENCY] [-g GRADIENT] [-i] [FILE ...]", file=sys.stderr)

if __name__ == "__main__":
    main()
