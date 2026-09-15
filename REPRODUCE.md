# Minimal Reproduction

The public reference layer uses only the Python standard library.

From the repository root, run:

```bash
python -m unittest discover -s tests -v
```

Expected public-reference result:

```text
Ran 7 tests
OK
```

The tests verify only the public governance/reference layer. They do not reproduce the scientific adjudication of all 38 manuscript cases, infer scientific materiality from raw evidence, or substitute for the retained archival evidence reported in the manuscript and Online Resource 1.

The worked C05 rendering is available at `examples/C05_WORKED_EXAMPLE.json`.
