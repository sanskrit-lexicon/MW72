# MW72 front matter (Vorspann) — OCR + translations

Faithful OCR of the **front matter** of Monier Monier-Williams's *A Sanskrit-English Dictionary*, **first edition, Oxford: Clarendon Press, 1872** (the dictionary digitized in this repo as `mw72`, distinct from the 1899 `MW`). Title page, the seven-section Preface (Sections 1–7), the Directions, the Abbreviations table, and the Nāgarī/Indo-Romanic letter-order table — transcribed from the Cologne csldoc scans, with a Russian translation of every page.

- **Source language:** English. Because the base text is already English, there are **no `.en.md` files** — the base `mw72prefNN.md` *is* the English. Russian (`.ru.md`) is provided for every page.
- **Signature / date found:** the Preface is signed **MONIER WILLIAMS**, dated **Oxford, May 1872** (page xxv = [mw72pref22.md](mw72pref22.md)).
- **Editions covered:** one volume (vol. 1).
- **Digitizer stamps omitted:** the running header/footer that the Cologne scanner adds to every page are *not* part of the original and were not transcribed.

Cologne source index: <https://sanskrit-lexicon.uni-koeln.de/scans/csldev/csldoc/build/dictionaries/prefaces/mw72pref.html>

## File conventions

| Suffix | Meaning |
|---|---|
| `mw72prefNN.md` | Page NN, source language (English), faithful transcription |
| `mw72prefNN.ru.md` | Russian translation of page NN |
| `mw72pref_all.en.md` | All pages, English (consolidated, with table of contents) |
| `mw72pref_all.ru.md` | All pages, Russian (consolidated, with table of contents) |
| `build_combined.py` | Reproducible builder for the two `*_all.*` files |
| `scans/` | The Cologne csldoc source PNG scans |

## Consolidated editions

| Edition | File | Builder |
|---|---|---|
| English (source) | [mw72pref_all.en.md](mw72pref_all.en.md) | [build_combined.py](build_combined.py) |
| Russian | [mw72pref_all.ru.md](mw72pref_all.ru.md) | [build_combined.py](build_combined.py) |

Rebuild: `python build_combined.py` (or `DICT=mw72 python build_combined.py`).

## Contents

| Page | Section | Vol. | Source | Russian |
|---|---|---|---|---|
| 01 | Title | 1 | [md](mw72pref01.md) | [ru](mw72pref01.ru.md) |
| 02 | Preface — Reasons for undertaking a New Sanskrit Dictionary, 1 (Sec. 1) | 1 | [md](mw72pref02.md) | [ru](mw72pref02.ru.md) |
| 03 | Reasons, 2 | 1 | [md](mw72pref03.md) | [ru](mw72pref03.ru.md) |
| 04 | Reasons, 3 | 1 | [md](mw72pref04.md) | [ru](mw72pref04.ru.md) |
| 05 | Plan and Arrangement of the Present Work, 1 (Sec. 2) | 1 | [md](mw72pref05.md) | [ru](mw72pref05.ru.md) |
| 06 | Plan, 2 | 1 | [md](mw72pref06.md) | [ru](mw72pref06.ru.md) |
| 07 | Plan, 3 | 1 | [md](mw72pref07.md) | [ru](mw72pref07.ru.md) |
| 08 | Plan, 4 | 1 | [md](mw72pref08.md) | [ru](mw72pref08.ru.md) |
| 09 | Extent of Sanskrit Literature comprehended, 1 (Sec. 3) | 1 | [md](mw72pref09.md) | [ru](mw72pref09.ru.md) |
| 10 | Extent, 2 | 1 | [md](mw72pref10.md) | [ru](mw72pref10.ru.md) |
| 11 | Extent, 3 | 1 | [md](mw72pref11.md) | [ru](mw72pref11.ru.md) |
| 12 | Alphabet and System of Transliteration employed, 1 (Sec. 4) | 1 | [md](mw72pref12.md) | [ru](mw72pref12.ru.md) |
| 13 | Alphabet, 2 | 1 | [md](mw72pref13.md) | [ru](mw72pref13.ru.md) |
| 14 | Alphabet, 3 | 1 | [md](mw72pref14.md) | [ru](mw72pref14.ru.md) |
| 15 | Alphabet, 4 | 1 | [md](mw72pref15.md) | [ru](mw72pref15.ru.md) |
| 16 | Alphabet, 5 | 1 | [md](mw72pref16.md) | [ru](mw72pref16.ru.md) |
| 17 | Principal Sources drawn upon in the Process of Compilation, 1 (Sec. 5) | 1 | [md](mw72pref17.md) | [ru](mw72pref17.ru.md) |
| 18 | Principal Sources, 2 (bibliography) | 1 | [md](mw72pref18.md) | [ru](mw72pref18.ru.md) |
| 19 | Aids and Encouragements received, 1 (Sec. 6; bibliography cont.) | 1 | [md](mw72pref19.md) | [ru](mw72pref19.ru.md) |
| 20 | Defects and Inconsistencies acknowledged, 1 (Sec. 7) | 1 | [md](mw72pref20.md) | [ru](mw72pref20.ru.md) |
| 21 | Defects, 2 | 1 | [md](mw72pref21.md) | [ru](mw72pref21.ru.md) |
| 22 | Defects, 3 (signed *Monier Williams, Oxford, May 1872*) | 1 | [md](mw72pref22.md) | [ru](mw72pref22.ru.md) |
| 23 | Directions to be studied before using this dictionary | 1 | [md](mw72pref23.md) | [ru](mw72pref23.ru.md) |
| 24 | Abbreviations and symbols | 1 | [md](mw72pref24.md) | [ru](mw72pref24.ru.md) |
| 25 | Dictionary order of the Nāgarī letters (transliteration table) | 1 | [md](mw72pref25.md) | [ru](mw72pref25.ru.md) |

## Notes

- Sanskrit terms, work-titles, and bibliographic abbreviation keys are left verbatim in their original Roman transliteration; the Nāgarī column on page 25 is given in Unicode Devanāgarī.
- Russian translations follow scholarly register: personal names in Cyrillic with no redundant Latin parentheses (Böhtlingk = Бётлингк, Roth = Рот, Wilson = Уилсон, Whitney = Уитни, Müller = Мюллер, Benfey = Бенфей, Goldstücker = Гольдштюкер, Curtius = Курциус, etc.); bibliographic work-titles kept in their original script.
- Uncertain readings are marked `[?]`; the dense three-column Abbreviations and bibliography pages were OCR'd at native-resolution crops.

Produced by the `/cologne-preface-ocr` skill.
