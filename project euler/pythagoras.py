#print([(i,j,k) for i,j,k in range(1000) if (i < j < k and i+j+k == 1000)])
print([(i,j,k) for i in range(1000) for j in range(i+1,1000) for k in range(j+1,1000) if (i<j<k and i*i + j*j == k*k and i + j + k ==1000)])
