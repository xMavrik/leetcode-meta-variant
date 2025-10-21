


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
        pass


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