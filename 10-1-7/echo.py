import sys


def echo(in_, out):
    for line in in_:
        out.write(line)

echo(sys.stdin, sys.stdout)
