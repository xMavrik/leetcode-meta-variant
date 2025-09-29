'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "racecarX", include = [r, X]
Output: false
Explanation: "rrX" is not a palindrome.
Example 2:

Input: s = "Yo, banana boY!", include = [Y, o, b, a, n]
Output: true
Explanation: "YobananaboY" is a palindrome.
Example 3:

'''

def isPalindrome(s: str, include: list) -> bool:
        
        left = 0

        right = len(s) - 1

        while left < right:

            while left < right and s[left] not in include:
                left += 1
            while left < right and s[right] not in include:
                right -= 1

            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True

s1 = "racecarX"
include1 = ['r', 'X']
print(isPalindrome(s1, include1))

s2 = "Yo, banana boY!" 
include2 = ['Y', 'o', 'b', 'a', 'n']
print(isPalindrome(s2, include2))