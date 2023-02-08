def revstr(ip:str,index:int,rev:str):
    if index==0 or len(ip) == 0:
        return rev
    
    return revstr(ip,index-1,rev+ip[index-1])

print(revstr("sarvesh",len("sarvesh"),""))

def search_item_index(items:list[int],search:int):

    if not items:
        return
    
    items.sort()

    middle_idx = len(items)//2

    if items[middle_idx] == search:
        return True
    elif search < items[middle_idx]:
        return search_item_index(items[:middle_idx],search)
    else:
        return search_item_index(items[middle_idx+1:],search)

print(search_item_index([1,23,4,5,6],4))


def cnt_consonants(ip:str,cnt_vwel:int,index:int):
    if not ip or index == 0:
        return cnt_vwel

    if ip[index-1].lower().isalpha() and ip[index-1].lower() not in ["a","e","i","o","u"]:
        cnt_vwel+=1
    
    return cnt_consonants(ip,cnt_vwel,index-1)

print(cnt_consonants("sarvesh",cnt_vwel=0,index=len("sarvesh")))
