###DANIELE TRAVERSA
###ID: 0000830457

import random

def test():
      testNumber = [5,10,15,20,25]
      m = random.choice(testNumber)
      S = [random.randint(1,10) for x in range(1,m+1)]
      U = [random.randint(1,10) for y in range(1,m+1)]
        
      print('the number of databases is:',m)
      print('The array S contains the following sizes:',S)
      print('The array U contains the following utilities:',U)
      for e in range(3*m,7*m):
            n = e
            print('The total amount of mamory available is:',n)
            print('EXHAUSTIVE SEARCH')
            ES = ExhaustiveSearch(n,m,S,U)
            print(ES)
            print('BRANCH AND BOUND')
            BB = BranchAndBound(n,m,S,U)
            print(BB)
            print('Are they equal?', ES==BB)

      return ''

######EXHAUSTIVE SEARCH#####

def setsPos(m):
      result = [[],] + [[y,] for y in m]
      permu = [[x,] for x in m]
      while len(result[-1]) != len(m):
            volPermu = []
            for e in permu:
                  end = m.index(e[-1])
                  i = end+1
                  while i < len(m):
                        vol = []
                        vol = e + [m[i],]
                        volPermu += [vol,]
                        i+= 1
            result += volPermu
            permu = volPermu

      return result

def ExhaustiveSearch(n,m,S,U):
      
    databases = [z for z in range(m)] 
    sets = setsPos(databases)
    maxU = 0
    database = []
    for e in sets:
        volS = 0
        volU = 0
        for i in e:
            search = databases.index(i)
            volS += S[search]
            volU += U[search]
        if volS <= n and volU > maxU:
              maxU = volU
              database = e

    return database

#####BRANCH AND BOUND ######

def OverPass(node,m):    
      if node[-1] == m-1:     
            back = node[:-1]      
            back[-1] += 1
            return back
      else:
            node[-1] += 1     
            return node

def NextNode(node,m):   
      if node[-1] == m-1:      
            back = node[:-1]       
            back[-1] += 1
            return back
      else:
            node = node + [node[-1] +1]    
            return node
      
def ComputeSums(node, S, U):   
      capacity = 0                           
      utility = 0
      for e in node:
            capacity += S[e]
            utility += U[e]
      return capacity,utility
            
def BranchAndBound(n,m,S,U):   
      finalQual = 0
      output = []
      for x in range(m-1):
            node = [x]
            capacity = S[x]
            utility = U[x]
            while True:
                  if node == [x,m-1] or node == [m-1]:  
                        break                                                
                  if capacity > n:                                
                        node = OverPass(node,m)                      
                        newSums = ComputeSums(node,S,U)
                        capacity = newSums[0]
                        utility = newSums[1]
                  else:
                        if utility > finalQual:        
                              finalQual = utility
                              output += [node[:],]
                              
                        node = NextNode(node,m)               
                        newSums = ComputeSums(node,S,U)   
                        capacity = newSums[0]
                        utility = newSums[1]

      if len(output)==0:    #special case when m=1
            if S[0] < n:
                  return [m-1,]
            else:
                  return None

      return output[-1]

print(test())
