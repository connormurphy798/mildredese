# Dhemiudre

> **dhemiudre**, _noun_
>
> small cat speech

Dhemiudre (or Mildredese in English) is an in-development [conlang](https://en.wikipedia.org/wiki/Constructed_language) inspired by my cat, Mildred.

The language is designed to facilitate improvisational singing, particularly with regard to cats and their activities.
Its attributes are intended to ease constructing logical sentences while meeting the constraints inherent to writing lyrics in Western music.

This repository includes:

| File/Directory | Description |
| - | - |
| `lexicon/` | Dhemiudre's lexicon. An in-progress Dhemiudre-to-English dictionary can be found in `lexicon/dictionary`. |
| `generate.ipynb` | Code for my own use in generating valid Dhemiudre syllables. |


## Phonology

Dhemiudre's consonant and vowel inventories are below. Phonemes are given as their orthographical representation in Dhemiudre.

<table>
  <tr>
    <th></th>
    <th>Bilabial</th>
    <th>Dental</th>
    <th>Alveolar</th>
    <th>Palatal</th>
    <th>Velar</th>
    <th>Glottal</th>
  </tr>
  <tr>
    <th>Nasal</th>
    <td>m</td>
    <td>n</td>
    <td></td>
    <td>nj</td>
    <td>ng</td>
    <td></td>
  </tr>
  <tr>
    <th>Plosive</th>
    <td>p b</td>
    <td>t d</td>
    <td></td>
    <td></td>
    <td>k g</td>
    <td></td>
  </tr>
  <tr>
    <th>Fricative</th>
    <td>f v</td>
    <td>th dh</td>
    <td>s z</td>
    <td></td>
    <td>kh gh</td>
    <td>h</td>
  </tr>
  <tr>
    <th>Lateral fricative</th>
    <td></td>
    <td></td>
    <td>l</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <th>Tap</th>
    <td></td>
    <td></td>
    <td>rh r</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <th>Approximant</th>
    <td>w</td>
    <td></td>
    <td></td>
    <td>j</td>
    <td></td>
    <td></td>
  </tr>
</table>

Phonemes sharing a manner and place of articulation differ in voicing (fricatives, taps) or aspiration (plosives). All nasals and approximants are voiced, while *h* and *l* are voiceless.

<table>
  <tr>
    <th></th>
    <th>Front</th>
    <th>Central</th>
    <th>Back</th>
  </tr>
  <tr>
    <th>Close</th>
    <td>i y</td>
    <td></td>
    <td>u</td>
  </tr>
  <tr>
    <th>Mid</th>
    <td>e ø</td>
    <td></td>
    <td>o</td>
  </tr>
  <tr>
    <th>Open</th>
    <td></td>
    <td>a</td>
    <td></td>
  </tr>
</table>

Front vowels are distinguished on roundedness. Back vowels are rounded, while the central vowel is unrounded.

Dhemiudre employs the following syllable structure:

    (C)(C)(S)V(S)

where C denotes consonants, S semivowels, and V vowels. A detailed overview of Dhemiudre's phonotactic rules can be found in `generate.ipynb`.