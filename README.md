# Lanki
Lanki (for *Inflection [Anki](https://apps.ankiweb.net/)*) is meant to assist those who use Anki to learn a language. Going beyond the memorization of vocabulary words, I used cards with full sentences in order to learn and practice grammer, syntax and so on. However, these sentence cards contained a lot of information, and sooner or later I realized that therein was a problem of "overfitting", to borrow a term from machine learning. With some cards I kept on making some sort of mistakes, marking them as wrong, but overtime I saw them ofen enough that I'd remember the sentences by heart. At that point it was no longer a "can I conjugate the verb correctly" but a "do I remember the sentence correctly" problem. Instead of being a "linguistic computation" task as intended, it became a problem of cache retrieval, if you will. And the sentences have really cloyed after a while.

Given that it is usually only one or few parts of the sentences that I need to learn, and going with the principle of having minimal information being queried by any one card, I'd decided to move to cloze deletion cards. And this is where Lanki comes in.

## Generate cloze deletion cards for word inflection
Currently Lanki is a python script that takes text files as input and outputs a text file formatted such that can be imported into Anki to create cloze cards. Lanki can help those who wish to learn language in context by creating cards that query about minimal grammatical information and therefore are quicker and easier to review. The blanks hint on the part of speech that they are masking (noun, verb, adjective &c).

## usage
!python lanki.py output.txt input.txt [input2.txt ... ]

## Current state
Just being initiated, Lanki is at a very early stage, and poorly documented. Currently it employs (and therefore requires) Spacy in order to parse the text. Currently it only processes German texts, but I plan to introduce more langauges soon (at least Spanish and French)
