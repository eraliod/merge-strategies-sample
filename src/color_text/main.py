"""CLI application to print text in a colored box."""
import argparse
from termcolor import colored

def create_parser():
    parser = argparse.ArgumentParser(description='Print text in a colored box.')
    parser.add_argument('text', type=str, help='Text to be printed')
    parser.add_argument('--color', type=str, choices=['white', 'yellow', 'red'], default='yellow', help='Color of the text')
    return parser

def print_boxed_text(text, color):
    text_line = f"| {text} |"
    top_bottom_border = '+' + '-' * (len(text_line) - 2) + '+'
    print(colored(top_bottom_border, color))
    print(colored(text_line, color))
    print(colored(top_bottom_border, color))

def main():
    parser = create_parser()
    args = parser.parse_args()
    print_boxed_text(args.text, args.color)

if __name__ == "__main__":
    main()
