def generate_power_set_reverse(input_set, index):
    if index < 0:
        return [[]]

    current_set=[]
    for sub in generate_power_set_reverse(input_set, index - 1):
        current_set.append(sub + [input_set[index]])
        current_set.append(sub)
    
    return current_set



if __name__ == '__main__':
    input_set = ['a', 'b', 'c']
    index = len(input_set) - 1  
    print(generate_power_set_reverse(['a', 'b', 'c'], index))

