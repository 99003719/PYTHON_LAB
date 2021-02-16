#find the missing element

l1=[1,2,3,4]
l2=[1,2,3,4,5]
l3=set(l2) - set(l1)
print(l3)

#element close to mean //
def close_to_mean(l):
    s= 0
    for x in l:
        s+= x
    m = s / len(l)
    cmp = abs(m - l[0])
    for x in l:
        if abs(m-x) < abs(cmp):
            cmp = m- x
            r = x
    return r


# In a given list, count  elements smaller than their mean

def element_small_than_mean(l):
    s = 0
    l2 = []
    for x in l:
        s += x
    m = s / len(l)
    for x in l:
        if m >= i:
            l2.append(i)
    return l2



#  Find the no.of people in a bus, given the data of people onboarding & alighting at each station

def bus(n,t):
    for i in t:
        n+=i[1]-i[2]
        print(n)
bus(25,((1,2,3),(2,3,3)))


#Find the average speed of vehicle, given the distance travelled for fixed time intervals

def a_s(l, time): 
    t = l[0]
    c = len(l)
    for x in range(len(l)-1):
        t+= l[x+1] - l[x]
    return round(t/(c*time)* 60, 3)


#difference between 2 lowest numbers in the list //
def diff(l):
    s1 = l[0]
    for x in l:
        if x < s1:
            s1 = x
    l.remove(s1)
    s2 = l[0]
    for x in l:
        if x < s2:
            s2 = x
    
    return s2 - s1



# odd one out 
def odd(l):
    for x in range(1,len(l)):
        if l[x] != l[x-1]:
            if l[x] != l[x+1]:
                return l[x]
            else:
                return l[x-1]


#no of elements smaller than mean //
def number(l):
    s = 0
    r = 0
    for x in l:
        s += x
    m = s/ len(l)
    for x in l:
        if m >= x:
            r+= 1
    return r
