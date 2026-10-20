def largestOddNumber(s: str) -> str:
    num = int(s)

    if num % 2 != 0:
        return s
    else:
        while num > 0:
            rem = num % 10
            if rem % 2 != 0:
                return str(num)
            num = num // 10

    return ""
