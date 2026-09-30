# Emerging-Topic Detection: Reproducible Experiment (ML-T2-008)

This is the exact code and data behind the 17-month lead-time result reported
in the technical paper for Problem ML-T2-008 ("prompt engineering" case study).

## Files
- `experiment.py` — main script: loads the corpus, runs the literal-term volume
  baseline, runs the TF-IDF + agglomerative-clustering semantic detector under
  an expanding-window (hindsight-free) protocol, and prints/saves the results.
- `make_chart.py` — regenerates the lead-time comparison chart (Figure 1 in the paper).
- `prompt_engineering_corpus.csv` — the 20-paper real dataset (title, year, month,
  arXiv ID where applicable, literal-term flag). This is also hardcoded inside
  `experiment.py`, so the CSV is provided for convenience/inspection, not as a
  required input.
- `expanding_window_results.csv` — the full 18-snapshot measurement log produced
  by the last run (Appendix B in the paper).
- `lead_time_chart.png` — the chart produced by `make_chart.py`.

## Requirements
Python 3.9+, with:
```
pip install scikit-learn pandas matplotlib
```
No paid API, no internet access, and no GPU are required — everything runs
locally on CPU in a few seconds.

## How to run
```
python experiment.py
```
This reprints the volume-baseline detection point, the semantic-detector
detection point, the computed lead time (months), and saves
`prompt_engineering_corpus.csv` / `expanding_window_results.csv`.

To regenerate the chart:
```
python make_chart.py
```

## Notes for extending it
- The similarity threshold (`0.08`) and number of clusters are set near the
  top of `experiment.py` — change these to test sensitivity (Section 6.9-style
  analysis in the paper covers this for the sibling question-generation project;
  the same idea applies here).
- To test on a different topic, replace the `papers` list in `experiment.py`
  with a different set of (title, year, month, arXiv ID) tuples and re-run —
  the rest of the pipeline is topic-agnostic.
- The corpus is deliberately small (N=20) and single-topic; see Section 9 of
  the paper ("Threats to Validity") for exactly what would need to change to
  trust this at scale.
