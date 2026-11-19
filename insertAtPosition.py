def  insertAtPosition(arr: List[int], X: int, P: int) -> List[int]:
    # Write your solution here
    arr.insert(P,X)
    arr.pop()

    return arr
    pass
