#! python3

import sys

if len(sys.argv) > 1:
    print("Hello %s!" % " and ".join(sys.argv[1:]))
else:
    print("Hello you!")
