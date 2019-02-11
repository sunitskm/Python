def seq(n):
    iter = 0
    while(n!=1):
        if n % 2 == 0:
            n=n/2
        else:
            n = 3*n+1
        iter += 1
    return(iter)
max = 0
n1 = 0
print(seq(999999))
for i in range(1,1000000):
    m_iter = seq(i)
    if (m_iter>max):
        max = m_iter
        n1 = i
print(max)
print(n1)
