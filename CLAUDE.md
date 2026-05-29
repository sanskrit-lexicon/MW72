# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**MW72** is the corrections and research repository for the Cologne digitization of the 1872 first edition of Monier-Williams's *Sanskrit-English Dictionary* (distinct from the better-known 1899 expanded edition `MW`). The canonical source lives in `csl-orig/v02/mw72/mw72.txt`.

## Architecture

| Directory | Purpose |
|---|---|
| `20161107/` | Preparatory work from November 2016 for proposed changes to the mw72 digitization (see [issue #3](https://github.com/sanskrit-lexicon/MW72/issues/3)) |

Issues and corrections are tracked via the [GitHub issue tracker](https://github.com/sanskrit-lexicon/MW72/issues).

## Common Commands

### Apply line-level corrections (standard pattern)
```bash
python updateByLine.py <input_file> <changein_file> <output_file>
```

### Rebuild and validate XML (from `csl-pywork/v02/`)
```bash
sh generate_dict.sh mw72 ../../MW72Scan/2020
sh xmlchk_xampp.sh mw72
```

## Dependencies

- **Python 3**
- **mw72.txt** — in `$BASE/cologne/csl-orig/v02/mw72/mw72.txt`

## Data format

MW72 entries use standard CDSL Sanskrit-lexicography markup, with **English** glosses. The original digitization used the AS scheme; conversion to SLP1/modern IAST is tracked in issues #3/#4.

| Tag | Role | Example |
|---|---|---|
| `<L>NNNN` | Entry begin, with `<pc>` print page-column ref | `<L>1<pc>0001-a` |
| `<k1>`, `<k2>` | Primary / secondary headword (SLP1) | `<k1>a<k2>a` |
| `<h>N` | Homonym number | `<h>1` |
| `<LEND>` | Entry end | |
| `{#…#}` | Sanskrit text (SLP1) | `{#a#}` |
| `{%…%}` | English gloss / italic display | `{%a,%}` |

Annotated example — the first entry of `mw72.txt`:
```
<L>1<pc>0001-a<k1>a<k2>a<h>1       # entry 1; print page 0001 col a; headword "a"; homonym 1
{#a#} 1¦. {%a,%} the first letter of the alphabet; ...   # SLP1 headword ¦ English gloss
<LEND>                             # entry end
```

## GitHub Issue Conventions

This repository uses the Cologne dictionary-repo issue taxonomy. Every issue has exactly one **type**, one **severity**, and one **milestone**:

- **Type** (9): link-target, link-splitting, markup, text-correction, content-enhancement, encoding, scan-quality, bug, question
- **Severity** (3): minor, medium, hard
- **Milestone** (4): Dictionary to Book, Digitization Quality, Structured Data, Major Enhancements

See the [Cologne issue runbook](https://github.com/sanskrit-lexicon/csl-observatory/blob/main/runbook/cologne-issue-runbook.md) for label definitions and the type→milestone mapping.
