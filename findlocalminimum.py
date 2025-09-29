import math

def calculateMinTrucks(quantity, truckCapacity, max_parcels_of_same_type):
    
    trucks_needed = 0

    quantity = sorted(quantity, reverse=True)
    
    while sum(quantity) > 0:

        trucks_needed += 1

        curr_capacity = truckCapacity

        for x in range(len(quantity)):

            count = min(quantity[x], max_parcels_of_same_type, curr_capacity)

            if curr_capacity - count == 0:
                quantity[x] -= count
                break

            elif curr_capacity - count < 0:
                quantity[x] -= abs(curr_capacity - count)
                break
                
            else: 
                curr_capacity -= count
                quantity[x] -= count

    return trucks_needed

# Sample Input
test_quantity_1 = [4, 4, 3]
test_capacity_1 = 3
test_max_parcels_of_same_type_1 = 3

test_quantity_2 = [2, 4]
test_capacity_2 = 3
test_max_parcels_of_same_type_2 = 2

# Function Call
result_1 = calculateMinTrucks(test_quantity_1, test_capacity_1, test_max_parcels_of_same_type_1)
print(result_1)  # Expected Output: 4

result_2 = calculateMinTrucks(test_quantity_2, test_capacity_2, test_max_parcels_of_same_type_2)
print(result_2)  # Expected Output: 2