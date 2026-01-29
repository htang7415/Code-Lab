#!/bin/sh
# Scaffold a new problem from templates/problem
# Usage: ./scripts/new_problem.sh <track> <topic> <slug>
# Example: ./scripts/new_problem.sh dsa arrays three-sum

set -e

if [ $# -ne 3 ]; then
  echo "Usage: $0 <track> <topic> <slug>"
  echo "Example: $0 dsa arrays three-sum"
  exit 1
fi

TRACK="$1"
TOPIC="$2"
SLUG="$3"

# Rust crate names with hyphens become underscores in use statements
RUST_NAME=$(echo "$SLUG" | tr '-' '_')

ID="${TRACK}-${TOPIC}-${SLUG}"
DEST="problems/$TRACK/$TOPIC/$SLUG"
TEMPLATE_DIR="templates/problem"

if [ -d "$DEST" ]; then
  echo "Error: $DEST already exists"
  exit 1
fi

mkdir -p "$DEST/python"
mkdir -p "$DEST/rust/src"
mkdir -p "$DEST/rust/tests"

# meta.json
sed -e "s/{{ID}}/$ID/g" \
    -e "s/{{SLUG}}/$SLUG/g" \
    -e "s/{{TRACK}}/$TRACK/g" \
    -e "s/{{TOPIC}}/$TOPIC/g" \
    "$TEMPLATE_DIR/meta.json" > "$DEST/meta.json"

# problem.md
sed "s/{{SLUG}}/$SLUG/g" \
    "$TEMPLATE_DIR/problem.md" > "$DEST/problem.md"

# Python files
cp "$TEMPLATE_DIR/python/solution.py" "$DEST/python/solution.py"
cp "$TEMPLATE_DIR/python/test_solution.py" "$DEST/python/test_solution.py"

# Rust files
sed "s/{{SLUG}}/$SLUG/g" \
    "$TEMPLATE_DIR/rust/Cargo.toml" > "$DEST/rust/Cargo.toml"
cp "$TEMPLATE_DIR/rust/src/lib.rs" "$DEST/rust/src/lib.rs"
sed "s/{{RUST_NAME}}/$RUST_NAME/g" \
    "$TEMPLATE_DIR/rust/tests/solution_test.rs" > "$DEST/rust/tests/solution_test.rs"

echo "Created problem at $DEST"
echo "  pytest $DEST/python -q"
echo "  cargo test --manifest-path $DEST/rust/Cargo.toml"
