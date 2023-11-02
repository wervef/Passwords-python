def password_rotater(input_list):
    reversed_list = []
    for item in input_list:
        reversed_item = item[::-1]  # Reverse the string using slicing
        reversed_list.append(reversed_item)
    print("Original List:", input_list)
    print("Reversed List:", reversed_list)