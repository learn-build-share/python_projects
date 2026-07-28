def calculate_score(
        matched,
        total
):

    if total == 0:

        return 0

    return round(
        len(matched)/total*100,
        2
    )