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
