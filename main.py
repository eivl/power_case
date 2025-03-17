import pandas


df = pandas.read_csv("data.csv")

MAXIMUM_WATER_LEVEL = 100
STEADY_UPSTREAM_WATER_AMOUNT = 30


def is_valid_time_series(
    data: pandas.DataFrame,
    series: pandas.Series | list,
    current_water_level=100,
) -> bool:
    """
    Check if a time series or list is valid. data contains the dataframe with MW
    and water level data, series contains the dataframe with water level data.
    ```python
    is_valid_time_series(
        df,
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10,],
        )
    ```
    gives a valid result because every hour produces a valid amount of power and at the end,
    :param data:
    :param series:
    :param current_water_level:
    :return:
    """
    if len(series) != len(data):
        return False
    for hour, water_level_index in enumerate(series):
        water_level = data.iloc[hour].iloc[
            water_level_index + 1
        ]  # water_level_index + 1 is required because the first row of the dataframe
        # is the time as a string.
        current_water_level -= water_level
        current_water_level += STEADY_UPSTREAM_WATER_AMOUNT

        if current_water_level < 0:
            return False
        if current_water_level > MAXIMUM_WATER_LEVEL:
            current_water_level = MAXIMUM_WATER_LEVEL
    return True


def is_optimal(
    data: pandas.DataFrame,
    series: pandas.Series | list,
    current_water_level=100,
    empty_water_end_of_day=True,
) -> bool:
    """
    Checks if water levels overflow or exhausts, and if there are any water left
    after the first day. This only works for one day and
    :param data:
    :param series:
    :param current_water_level:
    :param empty_water_end_of_day:
    :return:
    """
    if len(series) != len(data):
        return False
    for hour, water_level_index in enumerate(series):
        water_level = data.iloc[hour].iloc[
            water_level_index + 1
        ]  # water_level_index + 1 is required because the first row of the dataframe
        # is the time as a string.
        current_water_level -= water_level
        current_water_level += STEADY_UPSTREAM_WATER_AMOUNT

        if current_water_level < 0:
            # Not Optimal, water level below 0
            return False
        if current_water_level > MAXIMUM_WATER_LEVEL:
            # Not Optimal, water level overflowing above MAXIMUM_WATER_LEVEL
            return False
    if empty_water_end_of_day and current_water_level > 0:
        # There are still water left in the resorviour
        return False
    return True


test_series = [
    3,
    3,
    3,
    3,
    3,
    3,
    3,
    1,
    1,
    1,
    1,
    0,
    0,
    0,
    3,
    3,
    0,
    0,
    0,
    0,
    3,
    3,
    0,
    2,
]
assert is_valid_time_series(df, test_series) == True
assert is_optimal(df, test_series) == False


# Find and optimal solution that produces the highest score.
# Score is calculated based on the water_level_index, or in what column
# a valid and optimal input is based on.

# If you modify the test_series last entry from a `2` to a `3` to use all
# the water left in the resorviour, you will find one valid and optimal solution.

test_series[-1] = 3

assert is_valid_time_series(df, test_series) == True
assert is_optimal(df, test_series) == True

# Find other optimal solutions
print(f"One optimal solution has the score {sum(test_series)}")

# Write your own solution under to see if there are any other optimal solutions.
