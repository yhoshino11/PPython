import sys
import argparse


def greeting(args):
    print("Hello, {name}!".format(name=args.name))


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest='subparser_name')
subparser = subparsers.add_parser("greeting")
subparser.add_argument('-n', '--name', default='world')
args = parser.parse_args()

if not args.subparser_name:
    parser.print_help()
    sys.exit(1)

if args.subparser_name == "greeting":
    greeting(args)


# $ python subcommand.py greeting
# Hello, world!

# $ python subcommand.py greeting -n 'yhoshino11'
# Hello, yhoshino11!
