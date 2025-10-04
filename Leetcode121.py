'''
You are given two arrays, departures and returns where departures[i] and returns[i] are ticket prices for departing and returning flights.

You want to minimize ytour cost by choosing a single day to buy a departure flight and choosing a different day in the future to buy a returning flight.

Return the min cost you can achieve from a single round-trip flight.



Input: departures = [1, 2, 3, 4]  returns = [4, 3, 2, 1]

Output = 2





Input = [4, 3, 5, 11, 2]  returns = [1, 6, 10, 2, 9]

Output = 3 + 2 = 5

'''

departures = [4, 3, 5, 11, 2]  

returns = [1, 6, 10, 2, 9]


class CheapFlight:

    def travel(self, departures, returns):

        min_depart = departures[0]

        cheapest_price = float("inf")

        for x in range(1, len(departures)):

            cur_price = returns[x] + min_depart

            cheapest_price = min(cheapest_price, cur_price)

            min_depart = min(min_depart, departures[x])

        return cheapest_price
    

test_cases = [
    # 1. Example given
    {
        "departures": [4, 3, 5, 11, 2],
        "returns":    [1, 6, 10, 2, 9],
        "expected": 5   # depart=3 (idx1), return=2 (idx3)
    },

    # 2. Strictly increasing
    {
        "departures": [1, 2, 3, 4, 5],
        "returns":    [6, 7, 8, 9, 10],
        "expected": 8   # depart=1 (idx0), return=7 (idx1)
    },

    # 3. Strictly decreasing
    {
        "departures": [10, 9, 8, 7, 6],
        "returns":    [20, 19, 18, 17, 16],
        "expected": 23   # depart=7 (idx3), return=16 (idx4)
    },

    # 4. Single best pair in the middle (fixed)
    {
        "departures": [8, 12, 7, 20, 30],
        "returns":    [15, 25, 10, 40, 50],
        "expected": 18   # depart=8 (idx0), return=10 (idx2)
    },

    # 5. Equal departures and returns
    {
        "departures": [5, 5, 5, 5],
        "returns":    [5, 5, 5, 5],
        "expected": 10   # any earlier depart=5 + later return=5
    },

    # 6. Early return is cheapest
    {
        "departures": [3, 6, 8, 10],
        "returns":    [12, 7, 9, 15],
        "expected": 10   # depart=3 (idx0), return=7 (idx1)
    },

    # 7. Increasing returns but high departures
    {
        "departures": [10, 12, 15],
        "returns":    [5, 6, 9],
        "expected": 16   # depart=10 (idx0), return=6 (idx1)
    },

    # 8. Large numbers
    {
        "departures": [100, 200, 300],
        "returns":    [400, 500, 600],
        "expected": 600   # depart=100 (idx0), return=500 (idx1)
    },

    # 9. Zigzag pattern
    {
        "departures": [5, 1, 6, 2, 7],
        "returns":    [10, 3, 12, 4, 15],
        "expected": 5   # depart=1 (idx1), return=4 (idx3)
    },

    # 10. Multiple equal minimums
    {
        "departures": [2, 5, 2],
        "returns":    [6, 9, 6],
        "expected": 8   # depart=2 (idx0), return=6 (idx2)
    },
]



def main():
    cheap = CheapFlight()

    for i, case in enumerate(test_cases, 1):
        result = cheap.travel(case["departures"], case["returns"])
        print(f"Test {i}: Result={result}, Expected={case['expected']}, Pass={result == case['expected']}")


if __name__ == "__main__":
    main()


    

