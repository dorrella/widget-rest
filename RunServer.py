#!/usr/bin/env python3

from WebApp import run_app

import argparse
import os

parser = argparse.ArgumentParser()

parser.add_argument("--port", dest="port", action="store", default="8080")
parser.add_argument("--db", dest="db", action="store", default="my_db")
parser.add_argument("--log", dest="log", action="store", default="log.txt")

args = parser.parse_args()

# delete old log for sanity
# todo optional
if os.path.exists(args.log):
    os.remove(args.log)

run_app(args.port, args.db, args.log)
