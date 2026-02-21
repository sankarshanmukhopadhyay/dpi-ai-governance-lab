.PHONY: setup lint validate smoke release-check

setup:
	python -m pip install --upgrade pip
	pip install .

lint:
	dpi-lab lint .

validate:
	dpi-lab validate reviews/examples-batch

smoke:
	mkdir -p /tmp/dpi-lab-smoke
	# Replace with an actual PDF path when running locally
	@echo "Run: dpi-lab review --engine local --pdf <paper.pdf> --slug smoke --out /tmp/dpi-lab-smoke && dpi-lab validate /tmp/dpi-lab-smoke/smoke"

release-check: setup lint validate
	@echo "Release check complete (add smoke test with a real PDF)."
