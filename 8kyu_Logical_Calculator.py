def logical_calc(array, op):
    result = array[0]
    for i in array[1:]:
        if op == "AND":
            result &= i
        elif op == "OR":
            result |= i
        else:
            result ^= i
        
    return result #boolean
