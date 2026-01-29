.PHONY: run-py run-rust lint format

# Run pytest for a single module or problem
# Usage: make run-py TARGET=modules/dsa/arrays/prefix-sum/python
run-py:
	@if [ -z "$(TARGET)" ]; then \
		echo "Usage: make run-py TARGET=<path-to-python-dir>"; \
		exit 1; \
	fi
	pytest $(TARGET) -q

# Run cargo test for a single Rust crate
# Usage: make run-rust MANIFEST=problems/dsa/arrays/two-sum/rust/Cargo.toml
run-rust:
	@if [ -z "$(MANIFEST)" ]; then \
		echo "Usage: make run-rust MANIFEST=<path-to-Cargo.toml>"; \
		exit 1; \
	fi
	cargo test --manifest-path $(MANIFEST)

# Optional: lint Python with ruff
lint:
	ruff check .

# Optional: format Python with ruff
format:
	ruff format .
