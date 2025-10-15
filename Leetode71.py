# Problem: Simplify Path with Twist

# Given two strings, `absolute` and `relative`, representing an absolute path 
# and a relative path respectively, your task is to simplify the paths by applying 
# the relative path instructions to the absolute path.

# The absolute path is always valid and starts with a `/`, indicating the root directory. 
# The relative path, although starting with `/`, must be treated as if it was applied 
# on top of the given absolute path.

# Write a function `simplifyPath(absolute: str, relative: str) -> str` that returns 
# the simplified canonical path as it would appear after applying the relative changes.


class PathSimplifier:
    def simplifyPath(self, cwd: str, cd: str) -> str:
        
        if not cd:
            return cwd

        # Determine if cd is absolute
        if cd.startswith("/"):
            parts = []
            
        else:
            # Split cwd into usable pieces
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
