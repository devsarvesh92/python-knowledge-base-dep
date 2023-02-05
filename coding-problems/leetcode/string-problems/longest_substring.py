from dataclasses import dataclass

@dataclass
class Input:
    ip_str:str
    curr_substr:str
    formulated_substrs:list[str]
    index:int


def find_longest_substring_rec(input:Input):
    if input.index > len(input.ip_str)-1:
        return sorted(input.formulated_substrs,key=len,reverse=True)[0] if input.formulated_substrs else None
    else:
        current_alpha = input.ip_str[input.index]
        if current_alpha not in input.curr_substr:
            input.curr_substr+=current_alpha
            if input.index == len(input.ip_str)-1:
                input.formulated_substrs.append(input.curr_substr)
        else:
            input.formulated_substrs.append(input.curr_substr)
            input.curr_substr=current_alpha
            
        input.index+=1
        return find_longest_substring_rec(Input(ip_str=input.ip_str,curr_substr=input.curr_substr,formulated_substrs=input.formulated_substrs,index=input.index))


def find_longest_substring_iter(input:str):
    result = 0
    window= ''
    for c in input:
        window = window[window.find(c)+1:] + c
        result = max(result, len(window))
    return result
    


print(find_longest_substring_iter("dvdf"))



            



            





    


    
    

    

