import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--name', default='world')
args = parser.parse_args()
print("Hello, {name}!".format(name=args.name))


# $ python arg_name.py -h

# $ python arg_name.py -n 'Perfect Python'
# Hello, Perfect Python!

# $ python arg_name.py
# Hello, world!
