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


def travel(departures, returns):

    min_cost = float("inf")

    min_departure_cost = departures[0]

    for x in range(1, len(returns) - 1):

        min_cost = min(min_cost, min_departure_cost + returns[x])

        min_departure_cost = min(min_departure_cost, departures[x])

    return min_cost


print(travel(departures, returns))

