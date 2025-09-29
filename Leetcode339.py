from typing import List, Union


class MyList:
    def __init__(self, value: Union[int, List['MyList']]):
        self.value = value


def depthSum(nestedInts: List[MyList]) -> int:

    def dfs(vals: List[MyList], depth: int) -> int:
        total = 0
        for item in vals:
            if isinstance(item.value, int):
                total += item.value * depth
            else:
                total += dfs(item.value, depth + 1)
        return total

    return dfs(nestedInts, 1)



nested = [
    MyList(1),
    MyList([
        MyList(4),
        MyList([
            MyList(6)
        ])
    ])
]


print(depthSum(nested))