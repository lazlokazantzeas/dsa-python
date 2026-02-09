# Arrays & Strings

## Core idea
Arrays store elements contiguously in memory, allowing O(1) access by index.
Strings behave like arrays of characters, but mutability depends on the language.

## Key tradeoff
- Fast access
- Fixed order
- Expensive inserts/removals in the middle

## Patterns
- Two pointers
- Prefix sums
- Hash-based lookups

## Common mistakes
- Using nested loops when a hash map would do
- Forgetting that strings are immutable in Python

## Representative problems
- Two Sum
- Valid Anagram
- Best Time to Buy and Sell Stock
