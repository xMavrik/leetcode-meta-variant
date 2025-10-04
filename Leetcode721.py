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

from collections import defaultdict


class AccountsMerge:
    def __init__(self):
        pass

    #--------------------------------------------------------------------
    
    def merge_accounts(self, accounts):
        graph = defaultdict(list)
        email_to_ids = defaultdict(list)

        # Map each email to its account IDs
        for acc_id, emails in accounts.items():
            for email in emails:
                email_to_ids[email].append(acc_id)

        # Build edges: if two accounts share an email, connect them
        for email, ids in email_to_ids.items():
            for i in range(1, len(ids)):
                graph[ids[0]].append(ids[i])
                graph[ids[i]].append(ids[0])

        visited = set()
        result = []

        def dfs(node, component):
            visited.add(node)
            component.append(node)
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei, component)

        # Run DFS to get connected components
        for acc_id in accounts:
            if acc_id not in visited:
                component = []
                dfs(acc_id, component)
                result.append(component)

        return result
    
    #--------------------------------------------------------------------


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
