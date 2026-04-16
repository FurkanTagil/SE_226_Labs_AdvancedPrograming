def remove_duplicates(data_list):
    unique = []
    for item in data_list:
        if item not in unique:
            unique.append(item)
    return unique


def strip_whitespaces(string_list):
    return [s.strip() for s in string_list]