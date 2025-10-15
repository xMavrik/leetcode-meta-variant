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



class PathSimplifier:
    def simplifyPath(self, cwd: str, cd: str) -> str:
        
        if not cd:
            return cwd
        
        parts = []

        # Determine if cd is absolute
        if not cd.startswith("/"):
            parts = [p for p in cwd.split("/") if p and p != "."]

        # Process cd path
        for token in cd.split("/"):
            if token in ("", "."):
                continue
            elif token == "..":
                if parts:
                    parts.pop()
            else:
                parts.append(token)

        # Build final result
        return "/" + "/".join(parts)


# Test cases
def run_tests():
    ps = PathSimplifier()
    
    tests = [
        ("/a/b/c", "/d/./e", "/d/e"),
        ("/home/", "/../usr/bin/", "/usr/bin"),
        ("/a/b/c", "/../../x/y/z", "/x/y/z"),
        ("/a/b/c", "././.", "/a/b/c"),
        ("/a/b/c", "/././.", "/"),
        ("/var/log", "../lib/././udev", "/var/lib/udev")
    ]

    for i, (cwd, cd, expected) in enumerate(tests):
        result = ps.simplifyPath(cwd, cd)
        assert result == expected, f"Test case {i+1} failed: expected {expected}, got {result}"
    
    print("All test cases passed!")

# Run tests
run_tests()
