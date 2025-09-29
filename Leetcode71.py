"""

Leetcode 71. Simplify Path

You are given an absolute path for a Unix-style file system. You are also given a relative path "cd", which instructs a change 
to the current working directory. Your task is to determine the and output the simplified canonical path that will result.



Example 1:

Input: cwd = "/a/b/c", cd = "/d/./e

Output: "/d/e"



Example 2:

Input: cwd = "", cd = "/d/./e"

Output: "/d/e"



Example 3:

Input: cwd = "/a/b/c", cd = ""

Output: "/a/b/c"



Example 4:

Input: cwd = "/a/b", cd = ".//c/../../d/f"

Output: "/a/d/f"


"""

def simplifyPath(cwd, cd):


    cwdStack = []

    folder = ""

    for x in cwd + "/":

        if x == "/":
            if folder:
                cwdStack.append(folder)
                folder = ""
        else:
            folder += x
            

    if cd[0] == "/":
        cwdStack = []

    folder = ""

    for y in cd + "/":

        if y == "/":

            if len(folder) > 0:

                if folder == "..":
                    if cwdStack:
                        cwdStack.pop()

                elif folder != ".":
                    cwdStack.append(folder)

                folder = ""

        else:
            folder += y

    
    return "/" + "/".join(cwdStack)

cwd = "/a/b"
cd = ".//c/../../d/f"
# /a/d/f

cwd2 = "/a/b/c"
cd2 = "/d/./e"
# /d/e


cwd3 = "/a/b"
cd3 = "c/d/e"
# a/b/c/d/e

print(simplifyPath(cwd3, cd3))