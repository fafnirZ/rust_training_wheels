
# to ensure it is a clean install
# must deleve .venv first
# must delete uv.lock since hash will change
# when our maturin .whl updates
develop:
	rm -r .venv
	rm uv.lock 
	uv venv
	uv pip install -e .