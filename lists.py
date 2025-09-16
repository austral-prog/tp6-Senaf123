# Replace the "ANSWER HERE" with your answer

def remove_elements(list_to_remove_elements):
    len_list = len(list_to_remove_elements)
    if len_list >= 1 and len_list <= 4:
        del list_to_remove_elements[0]
    elif len_list == 5:
        del list_to_remove_elements [4]
        del list_to_remove_elements [0]
    elif len_list > 5:
        del list_to_remove_elements[5]
        del list_to_remove_elements[4]
        del list_to_remove_elements[0]
    return list_to_remove_elements # Remove this line and implement


def add_elements(list_to_add_elements):
    list_to_add_elements.append("Yellow")
    list_to_add_elements.insert(0, "Pink")
    return list_to_add_elements  


def is_empty(list_to_check):
    if len(list_to_check) == 0:
        return True
    else:
        return False

def check_lists(list_to_compare1, list_to_compare2):
    if (len(list_to_compare1) > 2 and len(list_to_compare2) > 2):
        if list_to_compare1[2] == list_to_compare2[2]:
            return True
        else:
            return False 
    return False

    


def list_of_lists(list_of_lists_to_modify):
    del list_of_lists_to_modify[0][2:]
    del list_of_lists_to_modify[1][0::4]
    del list_of_lists_to_modify[2][:-2]
    return list_of_lists_to_modify

