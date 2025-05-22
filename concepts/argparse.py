import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--name', help='Enter your name', type=str)
parser.add_argument('--age', help='Enter your age', type=int)

args = parser.parse_args()

print(f"Hello {args.name}, you are {args.age} years old.")