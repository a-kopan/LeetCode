def isSubsequence(s, t):
        #t_list = list(t)
        s_list = list(s)
        # for let in t:
        #     if not let in s:
        #         t_list.remove(let)

        for let in t:
            if len(s_list)==0:
                return True
            if let==s_list[0]:
                s_list.pop(0)
        if len(s_list)==0:
            return True
        else:
            return False
                
t1 = ("abc","achbgdc")          
t2 = ("axc","ahbgdc")      
tests = [t1,t2]

[print(x,": ",isSubsequence(x[0],x[1])) for x in tests]