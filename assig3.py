#isogram

def iso(a):
    return len(a) == len(set(a.lower()))

print(iso("animal"))
print(iso("malayalam"))
print(iso("fruits"))

#Compute the word frequency in given message

def wc(str):  
    wds = str.split()
    c = dict()
    for w in wds:
        if w in c:
            c[w] += 1
        else:
            c[w] = 1

    return c

print( wc('one plus one gives two'))

#Given a number, find the largest number by shuffling the digits
def shuff(a):
    c = 0
    lst1 = []
    while i > 0:
        r = i% 10
        lst1.append(r)
        i //= 10
    lst1.sort(reverse=True)
    x = len(l1)
    for j in l1:
        c += j*pow(10, x-1)
        x -= 1
    return c

#ip into integer //

def ip(s):
    if type(s) == str:
        l = s.split('.')
        r, c = 0,3
        for x in lst:
            if int(i) <= 255:
                r += pow(256, c) * int(x)
                c -= 1
            else:
                return None
            
        return r
    elif type(s) == int:
        st = ""
        c = 3
        while c >=0:
            st += str((s // pow(256, c))%256) + "."
            c-= 1

        return st[:-1]


#malformed time string //
def m_t(t_s):
    st = ""
    l1 = t_s.split(":")
    l2 = []
    for i in l1:
        l2.append(int(i))
    
    if l2[2] >= 60:
        l2[1] += l2[2] // 60
        l2[2] %= 60
    if l2[1] >= 60:
        l2[0] += l2[1] // 60
        l2[1] %= 60
    if l2[0] > 23:
        return None
    
    for i in l2:
        st += str(i) + ":"
    return st[:-1]


#malformed date string //
def m_d(d_s):
    a = ""
    l = d_s.split("/")
    l2 = []
    for i in l:
        l2.append(int(i))
    if l2[2] < 0 or l2[2] > 9999:
        return None
    if l2[1] > 12:
        l2[2] += 2[1] // 12
        l2[1] %= 12
    if (l2[0] > 30 and l2[1] in [4,6,9,11]) or (l2[0] > 31 and l2[1] in [1,3,5,7,8,10,12]) or (l2[0] > 28 and l2[1] == 2):
       l2[1] += l2[0] // 30
        l2[0] %= 30

    for i in l2:
        a+= str(i) + "/"
    return a[:-1]


#mexican wave //
def mex(s):
    l = []
    for i in range(len(s)):
          a=s[:i].lower() + st[i].upper() + s[i+1:].lower()
          l.append(a)
    return l  

#largest number by deleting the single digit //

def m_delete(n):
    l = []
    m = str(n)
    for i in m:
        l.append(int(m.replace(i, '')))

#accumulated strings //
def acc_string(s):
    a = ""
    m= 0
    for i in s:
        a += i.upper() + i.lower()*m
        a += "-"
        m +=1 
    return a[:-1]
    return max(l) 

#RGB TO HEX //
def rth(value):
    n1 = {10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}
    x = "0X"
    flag = 0
    for y in value:
        if y > 255:
            return None
        elif y == 0:
            x += "00"

        while y>0 and y < 256:
            if y < 16 and flag == 0:
                r = y%16
                if r>= 10:
                    x += "0" + n1[r]
                else:
                    x+=  "0" + str(r)
                y //= 16
            elif y< 256:
                flag = 1
                r= y%16
                if r >= 10:
                    x += n1[r]
                else:
                    x+= str(r)
                y //= 16
            
    return x