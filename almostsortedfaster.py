def almostSorted(arr: list) -> None:
    # Add a negative and positive infinity buffer so that we can get around out-of-bounds errors and still use list comprehension
    sorted_copy = [x for x in arr]
    sorted_copy.sort()
    ascending_check = [sorted_copy[idx] == val for idx, val in enumerate(arr)]

    if all(ascending_check) is True:
        print("No need, its sorted")
        return

    if ascending_check.count(False) == 2:
        # We first need to check if swapping the elements solves the sort

        # We can have up to 4 mismatches depending on spacing but were only concered with the first maxima and last minima
        incorrect_positions = [idx for idx, val in enumerate(ascending_check) if val == False]

        input_copy = [x for x in arr]
        input_copy[incorrect_positions[0]], input_copy[incorrect_positions[1]] = input_copy[incorrect_positions[1]], input_copy[incorrect_positions[0]]

        if sorted_copy == input_copy:
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

        if input_copy == sorted_copy:
            print("yes")
            print(f"reverse {incorrect_positions[0] + 1} {incorrect_positions[-1] + 1}")
            return

    print("no")
    return


if __name__ == '__main__':
    test_cases = [[1,2,3,5,4,6],[7,6,5,4,3],[11,2,3,4,5]]
    [almostSorted(case) for case in test_cases]
