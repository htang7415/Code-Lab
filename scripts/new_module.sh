#!/bin/sh
# Scaffold a new module from templates/module
# Usage: ./scripts/new_module.sh <track> <topic> <slug>
# Example: ./scripts/new_module.sh dsa arrays sliding-window

set -e

if [ $# -ne 3 ]; then
  echo "Usage: $0 <track> <topic> <slug>"
  echo "Example: $0 dsa arrays sliding-window"
  exit 1
fi

TRACK="$1"
TOPIC="$2"
SLUG="$3"

# Convert slug to snake_case for Python filenames
PY_NAME=$(echo "$SLUG" | tr '-' '_')

DEST="modules/$TRACK/$TOPIC/$SLUG"
TEMPLATE_DIR="templates/module"

if [ -d "$DEST" ]; then
  echo "Error: $DEST already exists"
  exit 1
fi

mkdir -p "$DEST/python"

# README
sed -e "s/{{SLUG}}/$SLUG/g" \
    -e "s/{{TRACK}}/$TRACK/g" \
    -e "s/{{TOPIC}}/$TOPIC/g" \
    "$TEMPLATE_DIR/README.md" > "$DEST/README.md"

# Python files
sed "s/{{PY_NAME}}/$PY_NAME/g" \
    "$TEMPLATE_DIR/python/module.py" > "$DEST/python/${PY_NAME}.py"

sed "s/{{PY_NAME}}/$PY_NAME/g" \
    "$TEMPLATE_DIR/python/test_module.py" > "$DEST/python/test_${PY_NAME}.py"

echo "Created module at $DEST"
echo "  pytest $DEST/python -q"
