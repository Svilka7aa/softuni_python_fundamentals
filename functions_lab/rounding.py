def convert_list(base_list):
    final_list = []
    for n in base_list:
        final_n = round(float(n))
        final_list.append(final_n)
    return final_list


input_list = input().split(" ")
peint(convert_list(input_list))
