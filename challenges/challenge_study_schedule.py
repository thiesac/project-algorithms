def study_schedule(permanence_period, target_time):
    counter = 0
    if (
        target_time is None
        or not isinstance(target_time, int)
        or not (0 <= target_time <= 24)
    ):
        return None
    for period in permanence_period:
        if any(
            x is None or not isinstance(x, int) or not (0 <= x <= 24)
            for x in period
        ):
            return None
        elif target_time in range(period[0], period[1] + 1):
            counter += 1
    return counter
