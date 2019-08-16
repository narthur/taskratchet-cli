#!/usr/bin/env python3

"""TaskRatchet CLI.

Usage:
  taskratchet.py <method> <endpoint> [--staging]

Options:
  -h --help     Show this screen.
  --staging     Use staging server.

"""

from natlibpy.factory import Factory
from tr_cli.cli import Cli
from docopt import docopt

factory = Factory()
cli = factory.secure(Cli)
args = docopt(__doc__)

print(args)

response = cli.run(args)

print(response)
print(response.text)
