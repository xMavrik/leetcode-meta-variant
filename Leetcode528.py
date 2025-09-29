"""

You are given a 0-indexed array of pairs city_populations, where each pair consists of a string representing the name of the ith city, and an integer representing the population of the ith city (in millions, but treat these values as if in ones for computation purposes).

You need to implement the function pickIndex(), which randomly picks a person in and returns the name of the city the person is in.


Example 1:

Input
["Solution", "pickIndex", "pickIndex"]
[[["Seattle", 500], ["New York", 900], ["Los Angeles", 400]], [], []]

Output
[null, "New York", "Los Angeles"]


Explanation: New York has a probability of 900 / (900 + 400 + 500)

"""

# 500 + 900 + 400 = 1800

#400 / 1800 LA

# [500, 900, 400] --> [500, 1400, 1800]

# 0, 1800

#499 --> 0

#985 --> 2

#prefix_sum[mid] < randomNumber


from collections import defaultdict
import random


class Solution:

    def __init__(self, cities):

        self.cities = cities
        
        self.prefix_sum = []

        self.total = 0

        for x in cities:
            self.total += x[1]
            self.prefix_sum.append(self.total)


    def pickIndex(self):

        randomNum = random.uniform(0, self.total)

        left = 0

        right = len(self.prefix_sum) - 1


        while left < right:

            mid = (left + right) // 2

            if self.prefix_sum[mid] < randomNum:
                left = mid + 1

            else:
                right = mid

        return self.cities[right][0]






if __name__ == "__main__":
    cities = [["Seattle", 500], ["New York", 900], ["Los Angeles", 400]]
    sol = Solution(cities)

    trials = 100000
    results = defaultdict(int)

    for _ in range(trials):
        results[sol.pickIndex()] += 1

    print("Selection distribution after", trials, "trials:")
    for city, count in results.items():
        print(f"{city}: {count} times ({(count / trials) * 100:.2f}%)")