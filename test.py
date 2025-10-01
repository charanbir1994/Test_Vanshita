def add(args: str)-> int:
    """Calculate the sum of all positive numbers in a list.

    Args:
        args (str): An any deliminator as seprator string of numbers.
        on minus numbers will be ignored and raise exception.

    Returns:
        float: The sum of the numbers.
    """
    is_continuity: bool = False
    number_list: list[float] = []
    all_numbers = ['0','1','2','3','4','5','6','7','8','9','.']
    temp_number: str = ""
    for num in args:
        if num in all_numbers:
            is_continuity = True
            temp_number += num
        else:
            if is_continuity:
                number_list.append(float(temp_number))
                temp_number = ""
            if num == '-':
                temp_number = "-"
            is_continuity = False
    if is_continuity: number_list.append(float(temp_number))
    negatives = [x for x in number_list if x < 0]
    if len(negatives) > 0:
        raise ValueError(f"Negatives not allowed: {', '.join([str(x) for x in negatives])}")
    else:
        sun_float = sum(number_list)
        return int(sun_float)

if __name__ == "__main__":
    # start of execution
    try:
        result = add("1, 2, 3, 6")
        print(f"The result is: {result}")
    except ValueError as e:
        print(e)