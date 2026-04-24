# Autocomplete System

## How to Run
1. Make sure Python is installed
2. Place dictionary.txt in the same folder
3. Run:
   python autoCompSys.py

## Input
User enters a prefix

## Output
Program prints all words starting with that prefix

## Algorithm
Uses a Trie (prefix tree) to store words efficiently.
Search is done by traversing the prefix, then collecting all child words.

## Time Complexity
Insert: O(n)
Search prefix: O(p)
Collect suggestions: O(k)

Where:
n = word length
p = prefix length
k = number of results
