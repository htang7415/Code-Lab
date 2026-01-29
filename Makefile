.PHONY: run-py run-rust lint format

# Run pytest for a single module or problem
# Usage: make run-py PATH=modules/dsa/arrays/prefix-sum/python
run-py:
	@if [ -z "$(PATH_TARGET)" ] && [ -z "$(PATH)" ]; then \
		echo "Usage: make run-py PATH=<path-to-python-dir>"; \
		exit 1; \
	fi
	pytest $(or $(PATH_TARGET),$(PATH)) -q

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
