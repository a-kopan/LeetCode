def get_key_by_value(dictionary, value):
        for key, val in dictionary.items():
            if val == value:
                return key
def distributeCookies(cookies, k) -> int:
        cookies.sort(reverse=True)
        initial_factor = sum(cookies)/k

        #create a dict with kid:cookies pairs
        pairs = dict()
        for i in range(0,k):
            pairs[i] = 0

        while len(cookies)>0:
            temp_bag = cookies.pop(0)
            found = False
            """
            for each kid check if adding the cookies to curent cookie counter will make his cookie 
            counter bigger  than initial factor, if it doesnt add to any kid then just pick the one with lowest 
            cookie counter
            """
            for kid in pairs:
                if pairs[kid]+temp_bag>initial_factor:
                    continue
                else:
                    found = True
                    pairs[kid]+=temp_bag
                    break
            #if the kid wasn't found, add to the one with lowest counter of cookies
            if not found:
                temp_val = min(pairs.values())
                key = get_key_by_value(pairs, temp_val)
                pairs[key] += temp_bag
        #return max(pairs.values())
        return pairs.items()
    
test = [15,14,8,13,7,2,13,19]
print(distributeCookies(test,3))
