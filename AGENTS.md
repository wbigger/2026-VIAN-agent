# AGENTS.md

## Project overview
This repository contains a small Python CLI for analyzing literary text for writing support.

- Main implementation: `analizzatore.py`
- Tests: `test_analizzatore.py`

## Working conventions
- Keep the CLI behavior simple and terminal-friendly.
- Prefer small, testable functions in `analizzatore.py`.
- Add or update tests in `test_analizzatore.py` whenever behavior changes.
- Preserve the current output style for the terminal report.

## Verification
Run the test suite before claiming completion:

```sh
./.venv/bin/python -m unittest -v
```

If you change CLI behavior, also verify the command-line path with sample input:

```sh
printf 'Luna osservava il mare.\n' | ./.venv/bin/python analizzatore.py
```

## Notes for AI agents
- The project is intentionally minimal; do not introduce heavy dependencies unless strictly necessary.
- Focus on readable Python and reliable metrics for narrative text.
- When adding new features, keep them modular and easy to test.
