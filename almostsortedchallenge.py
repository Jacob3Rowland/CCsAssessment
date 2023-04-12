def almostSorted(arr: list) -> None:
    # Add a negative and positive infinity buffer so that we can get around out-of-bounds errors and still use list comprehension
    buf_list =  [float('-inf')] + arr + [float('inf')]
    ascending_check = [buf_list[idx - 1] < val < buf_list[idx + 1] for idx, val in enumerate(buf_list) if idx not in [0, len(buf_list) -1]]

    if all(ascending_check) is True:
        print("No need, its sorted")
        return

    if ascending_check.count(False) <= 4:
        # We first need to check if swapping the elements solves the sort

        # We can have up to 4 mismatches depending on swap digit spacing but were only concered with the first maxima and last minima
        maxima_check = [idx - 1 for idx, val in enumerate(buf_list) if idx not in [0, len(buf_list) -1] and buf_list[idx - 1] < val and val > buf_list[idx + 1]]
        minima_check = [idx - 1 for idx, val in enumerate(buf_list) if idx not in [0, len(buf_list) -1] and buf_list[idx - 1] > val and val < buf_list[idx + 1]]

        incorrect_positions = [maxima_check[0], minima_check[-1]]
        input_copy = [x for x in arr]
        input_copy[incorrect_positions[0]], input_copy[incorrect_positions[1]] = input_copy[incorrect_positions[1]], input_copy[incorrect_positions[0]]
        buf_list = [float('-inf')] + input_copy + [float('inf')]
        check_if_correct = [buf_list[idx - 1] < val < buf_list[idx + 1] for idx, val in enumerate(buf_list) if
                           idx not in [0, len(buf_list) - 1]]
        if all(check_if_correct) is True:
            print(f"yes")
            print(f"swap {incorrect_positions[0] + 1} {incorrect_positions[-1] + 1}")
            return

    if ascending_check.count(False) > 2:
        # If the first check does not pass then we try reversing all indexes that failed the ascending criteria
        incorrect_positions = [idx for idx, val in enumerate(ascending_check) if val == False]
        input_copy = [x for x in arr]

        potentially_reversed = input_copy[incorrect_positions[0]:incorrect_positions[-1] + 1]
        potentially_reversed.reverse()

        input_copy[incorrect_positions[0]:incorrect_positions[-1] + 1] = potentially_reversed
        buf_list = [float('-inf')] + input_copy + [float('inf')]
        check_if_correct = [buf_list[idx - 1] < val < buf_list[idx + 1] for idx, val in enumerate(buf_list) if
                            idx not in [0, len(buf_list) - 1]]

        if all(check_if_correct) is True:
            print("yes")
            print(f"reverse {incorrect_positions[0] + 1} {incorrect_positions[-1] + 1}")
            return

    print("no")
    return


if __name__ == '__main__':
    test_cases = [[1,2,3,5,4],[7,6,5,4,3],[11,2,3,4,5]]
    [almostSorted(case) for case in test_cases]
