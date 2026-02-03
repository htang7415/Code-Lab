#!/bin/sh
# Run pytest for one module
# Usage: ./scripts/run_py.sh <path-to-python-dir>
# Example: ./scripts/run_py.sh modules/dsa/arrays/prefix-sum/python

set -e

if [ $# -ne 1 ]; then
  echo "Usage: $0 <path-to-python-dir>"
  echo "Example: $0 modules/dsa/arrays/prefix-sum/python"
  exit 1
fi

pytest "$1" -q
