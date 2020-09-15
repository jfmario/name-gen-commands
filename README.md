
*Commands for generating a fake language based on an input file and generating fake names based on them.*

This repository includes two commands. In order to use them, copy them into your path:

```
cp buildlang /usr/local/bin/
cp namegen /usr/local/bin/
```

The `buildlang` command expects the name of a file, the name of the language
(as you will reference it with the other command), and an optional strictness.
The input file should be a list of names or words in your fake language. There
should be many of them. It will save a Markov chain file to `~/.namelangs/`.

The `namegen` command takes the name of a language (that you have built) and 
prints a number of names generated using a Markov chain. It expects the name
of the language and an optional number of names to output (defaults to 10).

Example:

```
$ buildlang ./path/to/name_list.txt MyLang
$ namegen MyLang 3
lykoros
kokoumpina
romana
```

- John Marion