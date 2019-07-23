#!/usr/bin/env python3

import sys
from natlibpy.factory import Factory
from tr_cli.cli import Cli

factory = Factory()
cli = factory.secure(Cli)
args = sys.argv[1:]

if len(args) < 2:
    print('Usage: <command> <arg1> <arg2> ...')
    exit()

response = cli.run(*args)

print(response)
print(response.text)
