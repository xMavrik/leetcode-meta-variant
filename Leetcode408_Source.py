


# Prompt Description:

"""
LeetCode Problem 408: Valid Word Abbreviation (with Wildcard Twist)

Given a non-empty string `word` and an abbreviation `abbr`, return whether the string matches the given abbreviation.

A string such as "word" contains only lowercase English letters 'a'-'z'.

A non-empty string `abbr` by definition is valid if it can be constructed by the following rules:
- Replace one or more characters from the original word with a number representing the number of characters replaced.
- Wildcards ('*') in the abbreviation can match any single character in the word.

Note:
- **Leading zeros are not allowed in the abbreviation except for zero itself.**
- **Wildcards cannot represent empty sequences.**


Example 1:

word = "helzzpme"
abbr = "h2*p*me"
"""

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:

        word_ptr = 0
        abbr_ptr = 0

        star = -1     # last index of '*' in abbr (if any)
        match = -1    # position in word that '*' has expanded to

        while word_ptr < len(word):

            # If digits: parse full number and skip in word
            if abbr_ptr < len(abbr) and abbr[abbr_ptr].isdigit():
                skip = 0
                while abbr_ptr < len(abbr) and abbr[abbr_ptr].isdigit():
                    skip = skip * 10 + int(abbr[abbr_ptr])
                    abbr_ptr += 1
                word_ptr += skip
                if word_ptr > len(word):
                    return False
                continue

            # If both have a character and they match, advance with a while loop
            if abbr_ptr < len(abbr) and word_ptr < len(word) and abbr[abbr_ptr] == word[word_ptr]:
                while abbr_ptr < len(abbr) and word_ptr < len(word) and abbr[abbr_ptr] == word[word_ptr]:
                    word_ptr += 1
                    abbr_ptr += 1
                continue

            # If '*' in abbr: record star and try matching empty first
            if abbr_ptr < len(abbr) and abbr[abbr_ptr] == '*':
                star = abbr_ptr
                match = word_ptr
                abbr_ptr += 1  # let '*' initially match zero characters
                continue

            # Mismatch: try to use previous '*' to absorb one more char
            if star != -1:
                match += 1      # '*' eats one more character
                word_ptr = match
                abbr_ptr = star + 1    # continue matching after '*'
                continue

            # No '*' to rescue: fail
            else:
                return False

        # Word consumed; remaining abbr must be only '*' remaining
        while abbr_ptr < len(abbr) and abbr[abbr_ptr] == '*':
            abbr_ptr += 1

        return abbr_ptr == len(abbr) and word_ptr == len(word)


def test():
    sol = Solution()
    assert sol.validWordAbbreviation("internationalization", "i12iz4n") == True
    assert sol.validWordAbbreviation("helzzpme", "h2*p*me") == True
    assert sol.validWordAbbreviation("apple", "a2e") == False
    assert sol.validWordAbbreviation("substitution", "s10n") == True
    assert sol.validWordAbbreviation("connection", "c2nec*ion") == True
    assert sol.validWordAbbreviation("flexible", "fl*xible") == True
    print("All test cases passed!")

if __name__ == "__main__":
    test()


"""

When you have a previous '*' and you hit a mismatch:

Let '*' absorb one more character from the word (match += 1, word_ptr = match).

Reset abbr_ptr to just after the '*' (abbr_ptr = star + 1) and retry the same abbr suffix.

If it still mismatches, repeat step 1.

Stop if you either:

eventually match the abbr suffix, or

run out of word (then fail unless the remaining abbr is only '*'s).

"""