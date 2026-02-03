#!/bin/sh
# Run cargo test for one Rust crate
# Usage: ./scripts/run_rust.sh <path-to-Cargo.toml>
# Example: ./scripts/run_rust.sh modules/dsa/arrays/prefix-sum/rust/Cargo.toml

set -e

if [ $# -ne 1 ]; then
  echo "Usage: $0 <path-to-Cargo.toml>"
  echo "Example: $0 modules/dsa/arrays/prefix-sum/rust/Cargo.toml"
  exit 1
fi

cargo test --manifest-path "$1"
