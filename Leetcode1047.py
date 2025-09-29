"""

You are given a string of lowercase letters. Return the final string after all duplicates have been removed.




Input: s = "abbbacxdd"

Output: "cx"


"""




def removeDuplicates(s):


    stack = []

    for c in s:
        if stack and stack[-1][0] == c:
            stack[-1][1] += 1
        else:
            if stack and stack[-1][1] > 1:
                stack.pop()
                if stack and stack[-1][0] == c:
                    stack[-1][1] += 1
                    continue
            stack.append([c, 1])

    # Final clean up if duplicates are at the end
    if stack and stack[-1][1] > 1:
        stack.pop()

    return ''.join(c * count for c, count in stack if count == 1)


assert removeDuplicates("abbaca") == "ca"
assert removeDuplicates("aaaa") == ""
assert removeDuplicates("abc") == "abc"
assert removeDuplicates("abbbacxdd") == "cx"


print("--------PASS--------")