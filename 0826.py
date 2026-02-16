s='(((()))'

def solution(s):
    open_list=[]
    
    if s[0] == '(':
        for i in s:

            if i == "(":
                open_list.append(i)
            else:
                if len(open_list) == 0:
                    return False
                else:
                    open_list.pop()

        if len(open_list) == 0:
            return True
        else:
            return False
    else:
        return False