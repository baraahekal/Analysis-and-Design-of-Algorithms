def gen_power_set(input_set, index):
    if index < 0:
        return [[]]

    current_set = []
    for sub_set in gen_power_set(input_set, index - 1):
        current_set.append(sub_set + [input_set[index]])
        current_set.append(sub_set)
    
    return current_set


if __name__ == '__main__':
    input_set = ['a', 'b', 'c']
    index = len(input_set) - 1  
    print(gen_power_set(['a', 'b', 'c'], index))

