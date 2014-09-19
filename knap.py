import random, operator
# dynamic programming array K uses row/col 0, so
# vector indices start at 1
def genvector(n):  
  v = [-1] # dummy value, will not be used
  for j in range(n): v.append(random.randint(n,2*n))
  return v

def showRows(a,b,K): # last b-a rows
  print "..."
  for w in range(a,b):
    print w, ; print K[w]

def sack(n,W,K):  # get 0/1 solution vector
  inSolution = [0 for j in xrange(n)]
  ndx,w  = n,W
  while (w>0) and (ndx>0):
    while (ndx>0) and (K[w][ndx]==K[w][ndx-1]):
      ndx-=1
    if (ndx>0):
      w -= wt[ndx]
      ndx -= 1
      inSolution[ndx] = 1
  return inSolution

def solveknapsack(val,wt,W): 
  n = len(val) -1 # ignore dummy value
  K = [[0 for j in xrange(n+1)] for w in xrange(W+1)]
  for j in range(1,n+1):
    for w in range(W+1):
      if wt[j]>w: K[w][j] = K[w][j-1]
      else: K[w][j] = max(K[w][j-1], K[w-wt[j]][j-1]+val[j])
  lastfew = 25   
  showRows(W+1-lastfew,W+1,K) # print last few rows of K
  solvec = sack(n,W,K)
  print sum(map(operator.mul, solvec, val[1:])), "   ", solvec
    
n = 10
W = (n*n*3)/4
val,wt = genvector(n),genvector(n)
print 'val  ', ; print(val[1:])
print 'wt   ', ; print(wt[1:])
solveknapsack(val,wt,W)
