# combos.py

Generate every combinations of two words from a list of words. The uncombined words (the words in the original list) are kept in the output.

## Usage:

```bash
**python3 combos.py [options]**
```

combos.py can read a list of words from stdin or from a file. By default, outputs to stdout.
    
The list of words must be made of words separated by newlines.

###Options:

- -w / --wordlist : path to a list of words.
- -o / --output-file : path to a file to write the output.
- --no-self : don't do combos with the world itself (with the word "admin", don't do "adminadmin").
- --no-duplicate : detect duplicates in the list of words and don't take them into account more than once.
