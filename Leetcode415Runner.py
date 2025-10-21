"""
INTERVIEW PROMPT — Add Strings (Decimals Allowed)


You are given two non-negative numbers as strings, num1 and num2. The numbers may be integers
(e.g., "123") or decimals containing exactly one optional decimal point (e.g., "12.34"). There are
no signs (no '+' or '-'), no scientific notation, and the strings contain only digits and at most
one decimal point.


num1 = "123.45"
num2 = "678.55"

output = "134.61"

"""

class Solution:
    def add_string_main(self, num1: str, num2: str) -> str:
        pass

if __name__ == "__main__":
    solution = Solution()
    # Only Whole Numbers
    assert solution.add_string_main("11", "123") == "134"
    assert solution.add_string_main("456", "77") == "533"
    assert solution.add_string_main("0", "0") == "0"
    assert solution.add_string_main("0", "2983435243982343") == "2983435243982343"
    assert solution.add_string_main("99999999", "2983435243982343") == "2983435343982342"
    assert solution.add_string_main("99999999", "99999999999") == "100099999998"

    # Both Decimals With And Without Carry
    assert solution.add_string_main("123.53", "11.2") == "134.73"
    assert solution.add_string_main("687345.3434321", "389457248.24374657243") == "390144593.58717867243"
    assert solution.add_string_main(".56", ".12") == ".68"
    assert solution.add_string_main(".5995495049556", ".12") == ".7195495049556"
    assert solution.add_string_main(".9479823748932", ".716400040030") == "1.6643824149232"
    assert solution.add_string_main(".00009479823748932", ".000000716400040030") == ".000095514637529350"
    assert solution.add_string_main(".00009479823748932", ".00000071640004003000000") == ".00009551463752935000000"
    assert solution.add_string_main("110.12", "9.") == "119.12"
    assert solution.add_string_main("111111110.0013430430433434454001", "9.") == "111111119.0013430430433434454001"
    assert solution.add_string_main("111111110.0013430430433434454001", "993483400013438854.") == "993483400124549964.0013430430433434454001"
    assert solution.add_string_main("910.99999", "999.9999") == "1910.99989"
    assert solution.add_string_main("999999.99999", "999999.9999") == "1999999.99989"
    assert solution.add_string_main("123.525", "11.2") == "134.725"
    assert solution.add_string_main("1234540458475845.", "8348736.") == "1234540466824581"

    # # One Decimal, One Whole Number
    assert solution.add_string_main("110.75", "9") == "119.75"
    assert solution.add_string_main("110.75", "9999999") == "10000109.75"
    assert solution.add_string_main("150423434.00000000000", "9999999.") == "160423433.00000000000"
    assert solution.add_string_main("150423434.0000009184837483", "9999999.") == "160423433.0000009184837483"
    assert solution.add_string_main("110.9010479382798527", "9999999.") == "10000109.9010479382798527"

    print("-----PASSED-----")