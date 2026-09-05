_Created: 22-05-2026 · Last updated: 05-09-2026_

### Location

Counterpart of https://github.com/sanskrit-lexicon/PWG/issues/175 (PWG) and https://github.com/sanskrit-lexicon/PWK/issues/113 (PWK) for `mw72.txt`.

I ran the same two-job recipe over `csl-orig/v02/mw72/mw72.txt`: auto-fix the few things with a single safe resolution; audit everything else with line refs. Added `08_markup_fix.py` plus outputs to a new `mw72issues/markup_fix/` folder on the branch `markup-fix-audit`.

@funderburkjim @Andhrabharati — please review the findings listed below.

## Markup fixer + audit for `mw72.txt`

### What it auto-fixes

| Pattern | Result |
|---|---|
| `<ab><ab>X</ab> Y</ab>` | `<ab>X Y</ab>` |
| `<nsi> word </nsi>` | `<nsi>word</nsi>` |
| `<lang> word </lang>` | `<lang>word</lang>` |
| `<F> word </F>` | `<F>word</F>` |

Whitespace trimming applies to all 4 paired tag(s) in `mw72.txt`: `<nsi>`, `<lang>`, `<F>`, `<s>`. The original file is never modified — output goes to `mw72_fixed.txt`, with the full diff in `markup_fix_changes.txt` (updateByLine format). 24 line(s) changed.

### Closing-tag inventory in current `mw72.txt`

| Tag | Count |
|---|---:|
| `</nsi>` | 5 |
| `</728)>` | ? |
| `</lang>` | 1 |
| `</744)>` | ? |
| `</F>` | 34 |
| `</s>` | 1 |

### What it found in current `mw72.txt`

- 24 whitespace trims applied: leading/trailing spaces in `<nsi>` (1 lead + 12 trail) and `<lang>` (1 lead + 11 trail) tags.
- 0 adjacent `</ab> <ab>` — no `<ab>` tag in mw72.txt.
- 0 `<ab n="…">` attributes.
- 62 `{{old → new || …}}` correction records present.

### Usage

```
cd mw72issues/markup_fix
python 08_markup_fix.py                        # uses csl-orig/v02/mw72/mw72.txt by default
python 08_markup_fix.py IN.txt OUT.txt         # custom paths
```

Outputs: `mw72_fixed.txt`, `markup_fix_changes.txt`, `markup_audit.txt`.

### Summary

<nsi> is MW72-specific paired tag. No <ab> or <ls>.

### Severity

`minor`

_Dr. Mārcis Gasūns_
