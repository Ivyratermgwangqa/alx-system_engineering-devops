# Regular Expressions (Regex) Tasks

This repository contains Ruby scripts for various regular expression tasks. Each script is designed to match specific patterns using regular expressions.

## Task List

### 0. Simply matching School (0-simply_match_school.rb)
- Matches the string "School" using regular expressions.

### 1. Repetition Token #0 (1-repetition_token_0.rb)
- Matches strings that start with "hbt" followed by 2 to 5 occurrences of the letter "t" and ending with "n".

### 2. Repetition Token #1 (2-repetition_token_1.rb)
- Matches strings that start with "hbt" followed by at least 1 occurrence of the letter "t" and ending with "n".

### 3. Repetition Token #2 (3-repetition_token_2.rb)
- Matches strings that start with "hbt" followed by 0 or more occurrences of the letter "t" and ending with "n".

### 4. Repetition Token #3 (4-repetition_token_3.rb)
- Matches strings that start with "hbt" followed by any character except "n".

### 5. Not quite HBTN yet (5-beginning_and_end.rb)
- Matches strings that start with "h", followed by any single character, and ending with "n".

### 6. Call me maybe (6-phone_number.rb)
- Matches 10-digit phone numbers.

### 7. OMG WHY ARE YOU SHOUTING? (7-OMG_WHY_ARE_YOU_SHOUTING.rb)
- Matches capital letters in a string.

### 8. Textme (100-textme.rb)
- Extracts sender, receiver, and flags information from a log file.

# Regular Expressions (Regex) Cheatsheet

Welcome to the Regex Cheatsheet! Whether you're a beginner or an experienced developer, this comprehensive guide will empower you with the knowledge needed to master Regular Expressions (regex). Regex is a powerful tool for string manipulation and pattern matching, and this cheatsheet covers key concepts, elements, and best practices.

## Table of Contents

1. [Introduction](#introduction)
2. [Basic Concepts](#basic-concepts)
3. [Metacharacters](#metacharacters)
4. [Character Classes](#character-classes)
5. [Quantifiers](#quantifiers)
6. [Groups and Capturing](#groups-and-capturing)
7. [Alternation](#alternation)
8. [Escape Characters](#escape-characters)
9. [Anchors](#anchors)
10. [Modifiers](#modifiers)
11. [Special Characters](#special-characters)
12. [Assertions](#assertions)
13. [Negations](#negations)
14. [Quantifiers (Greedy vs. Lazy)](#quantifiers-greedy-vs-lazy)
15. [Escaped Characters](#escaped-characters)
16. [Useful Resources](#useful-resources)

## Introduction

Regular expressions are sequences of characters that define search patterns. They are employed in various programming languages and tools for tasks like string matching, validation, and text manipulation. While powerful, regex can be complex, and understanding its elements is crucial for effective use.

## Basic Concepts

### 1. Literals

Match literal characters.

```regex
/abc/
```

### 2. Metacharacters

- `.`: Match any character.
- `*`: Match 0 or more occurrences.
- `+`: Match 1 or more occurrences.
- `?`: Match 0 or 1 occurrence.
- `^`: Anchors to the start of a line.
- `$`: Anchors to the end of a line.

### 3. Character Classes

- `[abc]`: Match any one of a, b, or c.
- `[^abc]`: Match any character except a, b, or c.
- `[a-z]`: Match any lowercase letter.
- `[0-9]`: Match any digit.

### 4. Quantifiers

- `{n}`: Match exactly n occurrences.
- `{n,}`: Match n or more occurrences.
- `{n,m}`: Match between n and m occurrences.

### 5. Groups and Capturing

Create a group for capturing.

```regex
/(ab)+/
```

### 6. Alternation

Match either the pattern on the left or the one on the right.

```regex
/apple|orange/
```

### 7. Escape Characters

Escape a metacharacter to match it literally.

```regex
/a\*b/
```

### 8. Anchors

Word boundary.

```regex
/\bword\b/
```

### 9. Modifiers

- `i`: Case-insensitive matching.

```regex
/abc/i
```

### 10. Special Characters

- `\d`: Match any digit.
- `\w`: Match any word character.
- `\s`: Match any whitespace character.

### 11. Assertions

Positive lookahead assertion.

```regex
/a(?=b)/
```

### 12. Negations

Negate a character class.

```regex
/[^0-9]/
```

### 13. Quantifiers (Greedy vs. Lazy)

Make quantifiers lazy.

```regex
*?, +?, ??
```

### 14. Escaped Characters

- `\n`: Newline.
- `\t`: Tab.
- `\\`: Literal backslash.

## Useful Resources

- [regex101](https://regex101.com/): Online regex tester.
- [RegExr](https://regexr.com/): Another online regex tester.
- [MDN Web Docs - Regular Expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions): Detailed guide on regex.

Feel free to explore and experiment with regex using these concepts and tools. Happy coding! 🚀
