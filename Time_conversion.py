def convertSeconds(total_seconds: int) -> str:
    hours = total_seconds // 3600
    remain = total_seconds % 3600
    minutes = remain // 60
    seconds = remain % 60

    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
