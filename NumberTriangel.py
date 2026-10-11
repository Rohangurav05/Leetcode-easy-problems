def numberTrianglePattern(n: int) -> list[str]:
    result = []

    for i in range(1, n + 1):
        row = ""

        for j in range(1, i + 1):
            row += str(j) + " "

        result.append(row.strip())

    return result
