def is_str_palidrome(s:str):
    s = s.lower()
    middle = (len(s)-1)//2
    if len(s) % 2 ==0:
        return s[0:middle+1] == s[middle+1:][::-1]
    else:
        return s[0:middle] == s[middle+1:][::-1]


def longest_palidrome_substr(s:str):

    if not s:
        return ""

    palidrome_substrs:dict[int,str] = {}
    longes_sub_str_len = 0
    
    for id,c in enumerate(s):
        cons_str = c
        for next_c in s[id+1:]:
            cons_str+=next_c
            if cons_str == cons_str[::-1] and len(cons_str) not in palidrome_substrs and len(cons_str) > longes_sub_str_len:
                longes_sub_str_len=len(cons_str)
                palidrome_substrs[longes_sub_str_len] = cons_str

    return palidrome_substrs[longes_sub_str_len]



print(longest_palidrome_substr('wsgdzojcrxtfqcfkhhcuxxnbwtxzkkeunmpdsqfvgfjhusholnwrhmzexhfqppatkexuzdllrbaxygmovqwfvmmbvuuctcwxhrmepxmnxlxdkyzfsqypuroxdczuilbjypnirljxfgpuhhgusflhalorkcvqfknnkqyprxlwmakqszsdqnfovptsgbppvejvukbxaybccxzeqcjhmnexlaafmycwopxntuisxcitxdbarsicvwrvjmxsapmhbbnuivzhkgcrshokkioagwidhmfzjwwywastecjsolxmhfnmgommkoimiwlgwxxdsxhuwwjhpxxgmeuzhdzmuqhmhnfwwokgvwsznfcoxbferdonrexzanpymxtfojodcfydedlxmxeffhwjeegqnagoqlwwdctbqnuxngrgovrjesrkjrfjawknbrsfywljscfvnjhczhyeoyzrtbkvvfvofykkwoiclgxyaddhpdoztdhcbauaagjmfzkkdqexkczfsztckdlujgqzjyuittnudpldjvsbwbzcsazjpxrwfafievenvuetzcxynnmskoytgznvqdlkhaowjtetveahpjguiowkiuvikwewmgxhgfjuzkgrkqhmxxavbriftadtogmhlatczusxkktcsyrnwjbeshifzbykqibghmmvecwwtwdcscikyzyiqlgwzycptlxiwfaigyhrlgtjocvajcnqyenxrnjgogeqtvkxllxpuoxargzgcsfwavwbnktchwjebvwwhfghqkcjhuhuqwcdsixrkfjxuzvhjxlyoxswdlwfytgbtqbeimzzogzrlovcdpseoafuxfmrhdswwictsctawjanvoafvzqanvhaohgndbsxlzuymvfflyswnkvpsvqezekeidadatsymbvgwobdrixisknqpehddjrsntkqpsfxictqbnedjmsveurvrtvpvzbengdijkfcogpcrvwyf'))


