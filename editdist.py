def diff(s,t,i,j):
  assert(i <= len(s))
  assert(j <= len(t))
  if (s[i] != t[j]): return 1
  return 0

def ed(s,t): # return edit distance s,t
  n, m = len(s), len(t)
  print s, " ", t, 
  E = [[0 for j in xrange(m+1)] for k in xrange(n+1)]
  print len(E), len(E[0])
  for j in range(n+1):
    E[j][0] = j
  for k in range(1,m+1):
    E[0][k] = k
  for j in range(n):
    for k in range(m):
      E[j+1][k+1] = min( E[j][k+1] + 1,
                         E[j+1][k] + 1,
                         E[j][k] + diff(s,t,j,k) )
  for j in range(n+1):
    for k in range(m+1):
      print E[j][k],
    print ''
  return E[n][m]
                        
s,t = "c", "he"
print ed(s,t)
s,t = "cat", "hate"
print ed(s,t)
print ed(s,s)
print ed(t,t)
s,t = "exponential", "polynomial"
print ed(s,t)
s,t = "polynomial", "exponential"
print ed(s,t)
