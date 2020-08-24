# For the added sake of ease, we ignore all case issues (any could be solved simply by making all characters lower case)


# 1.1
def uniqueCheck_no_extras(s): # brute force O(n^2)
    for i in range(len(s)):
        charToCheck = s[i]
        for j in range(i+1, len(s)):
            if charToCheck == s[j]:
                return False
    return True

def uniqueCheck_extras(s):  # O(n)
    s2 = set(s)
    if len(s) == len(s2):
        return True
    return False

assert(uniqueCheck_no_extras('helo') == True)
assert(uniqueCheck_no_extras('hello') == False)
assert(uniqueCheck_no_extras('') == True)
assert(uniqueCheck_no_extras('lol') == False)

assert(uniqueCheck_extras('helo') == True)
assert(uniqueCheck_extras('hello') == False)
assert(uniqueCheck_extras('') == True)
assert(uniqueCheck_extras('lol') == False)

# 1.2
def permuation_check_first(s1, s2): # O(n log n)
    s1 = sorted(s1) # O(n log n)
    s2 = sorted(s2) # O(n log n)
    if len(s1) != len(s2):
        return False
    for i in range(len(s1)): # O (n)
        if s1[i] != s2[i]:
            return False
    return True
    
def permuation_check_second(s1, s2): # O(n) could cut down on space by using one hash and substraction
    dictS1 = {}
    dictS2 = {}
    for i in s1: # O(n)
        if i not in dictS1.keys():
            dictS1[i] = 0
        else:
            dictS1[i] = dictS1[i] + 1
    for i in s2: # O(n)
        if i not in dictS2.keys():
            dictS2[i] = 0
        else:
            dictS2[i] = dictS2[i] + 1
    if len(dictS1.keys()) != len(dictS2.keys()):
        return False
    for i in dictS1.keys():
        try:
            if dictS1[i] != dictS2[i]:
                return False
        except:
            return False
    return True 

assert(permuation_check_first('dog', 'god') == True)
assert(permuation_check_first('dog', 'gd') == False)
assert(permuation_check_first('', 'gd') == False)
assert(permuation_check_first('','') == True)

assert(permuation_check_second('dog', 'god') == True)
assert(permuation_check_second('dog', 'gd') == False)
assert(permuation_check_second('', 'gd') == False)
assert(permuation_check_second('','') == True)

# 1.3
def urlify(s): # O(n)
    s = list(s)
    for i in range(len(s)): # O(n)
        if s[i] == ' ':
            s[i] = '%20'
    return ''.join(s)

assert(urlify('Hello world') == 'Hello%20world')
assert(urlify('') == '')
assert(urlify('   ') == '%20%20%20')

# 1.4
def palindromeCheck(s): #O(n)
    lets = {}
    hingeFlag = False
    for i in s:
        if i == ' ':
            continue
        if i not in lets.keys():
            lets[i] = 1
        else:
            lets[i] = lets[i] + 1
    for i in lets.keys():
        if lets[i] % 2 != 0:
            if not hingeFlag:
                hingeFlag = True
            else:
                return False
    return True

assert(palindromeCheck('taco cat') == True)
assert(palindromeCheck('racecar') == True)
assert(palindromeCheck('') == True)
assert(palindromeCheck('hello') == False)


    



    