


def swap_chars(input:str):
    ip = list(input)
    for id in range(0,len(input)-2,2):
        ip[id],ip[id+1] = ip[id+1],ip[id]
    return "".join(ip)

print(swap_chars('sarvesh'))