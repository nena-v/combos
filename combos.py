"""
combos.py

Generate every combinations of two words from a list of words. The uncombined words (the words in the original list) 
are kept in the output.

Usage:
    python3 combos.py [options]
    
    combos.py can read a list of words from stdin or from a file. By default, outputs to stdout.
    
    The list of words must be made of words separated by newlines.
    
    Options:
        -w / --wordlist : path to a list of words.
        -o / --output-file : path to a file to write the output.
        --no-self : don't do combos with the world itself (with the word "admin", don't do "adminadmin").
        --no-duplicate : detect duplicates in the list of words and don't take them into account more than once.
        --limit N : stop after producing N combos.
"""

import argparse
import sys
from typing import List

def read_wordlist(path: str) -> List[str]:
    """ Reads a list of word from path or from stdin if path is empty."""
    
    if path:
        with open(path, 'r') as f_in:
            in_wordlist = [line.rstrip('\n') for line in f_in if line.rstrip('\n') != '']
    else:
        in_wordlist = [line.rstrip('\n') for line in sys.stdin if line.rstrip('\n') != '']
    
    return in_wordlist

def generate_out_wordlist(in_wordlist: List[str], no_self: bool=False, no_duplicate: bool=False) -> List[str]:
    """ Produces combos of words. """
    
    if no_duplicate:
        unique_words = set()
        in_wordlist = [w for w in in_wordlist if not (w in unique_words or unique_words.add(w))]
    
    out_wordlist = in_wordlist.copy()
    
    for w1 in in_wordlist:
        for w2 in in_wordlist:
            if w1 == w2 and no_self:
                continue
            else:
                out_wordlist.append(w1+w2)
                    
    return out_wordlist

def write_wordlist(path: str, wordlist: List[str]) -> None:
    """ Writes the produced list of words to path or to stdout if path is empty"""
    
    if path:
        with open(path, 'w') as f_out:
            for w in wordlist:
                f_out.write(w + '\n')
    else:
        for w in wordlist:
            sys.stdout.write(w + '\n')

def main():
    p = argparse.ArgumentParser(prog='combos', description='Generate every combinations of two words from a list of words.\
      The uncombined words (the words in the original list) are kept in the output.')
    p.add_argument('-w', '--wordlist', help='Path to a list of words (default: read from stdin).', default="")
    p.add_argument('-o', '--output-file', help='Path to an output file (default: stdout).', default="")
    p.add_argument('--no-self', help='Don\'t do combos with the world itself (with the word \"admin\", don\'t do \"adminadmin\").', action='store_true')
    p.add_argument('--no-duplicate', help='Detect duplicates in the list of words and don\'t take them into account more than once.', action='store_true')
    args = p.parse_args()
    
    in_wordlist = read_wordlist(args.wordlist)
    
    out_wordlist = generate_out_wordlist(in_wordlist, args.no_self, args.no_duplicate)
    
    write_wordlist(args.output_file, out_wordlist)
    

if __name__ == '__main__':
    main()