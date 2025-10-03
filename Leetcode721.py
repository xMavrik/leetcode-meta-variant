"""

You are given a map where each key is an account ID and its value is a list of emails belonging to that account. Your task is to identify and group accounts that belong to the same person based on matching email addresses. Return the grouped account IDs as a list of lists, where each subgroup contains account IDs that are connected through common emails.

Example Input:

{
'101': ['a@gmail.com', 'b@gmail.com'],
'102': ['b@gmail.com', 'c@gmail.com'],
'103': ['d@gmail.com'],
'104': ['c@gmail.com']
}



Expected Output:
[['101', '102', '104'], ['103']]


"""



class AccountsMerge:
    def __init__(self):
        pass
    
    def merge_accounts(self, accounts_map):
        # Implement your logic here

        return []  # Return list of lists of grouped account IDs


def main():
    accounts_map = {
        '101': ['a@gmail.com', 'b@gmail.com'],
        '102': ['b@gmail.com', 'c@gmail.com'],
        '103': ['d@gmail.com'],
        '104': ['c@gmail.com'],
    }

    expected_output = [['101', '102', '104'], ['103']]

    merger = AccountsMerge()
    result = merger.merge_accounts(accounts_map)

    print("Result:", result)
    print("Expected:", expected_output)
    print("Pass:", sorted(map(sorted, result)) == sorted(map(sorted, expected_output)))


if __name__ == "__main__":
    main()
