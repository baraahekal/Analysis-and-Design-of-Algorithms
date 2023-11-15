def generate_power_set(original_set, index=0, current_set=[]):
    n = len(original_set)

    if index == n:
        return [current_set]

    with_current = generate_power_set(original_set, index + 1, current_set + [original_set[index]])
    without_current = generate_power_set(original_set, index + 1, current_set)

    return with_current + without_current


if __name__ == '__main__':
    print(generate_power_set(["a1", "a2", "a3"]))

