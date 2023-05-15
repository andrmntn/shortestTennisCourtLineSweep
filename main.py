# Naive Implementation:
# Make a DFS through a undirected, weighted graph and only consider path weights of those paths, that go through all essential edges.
# Take path with minimum path weight
adj = [[None]]*8

def main():

    # Model the Graph
    adj[0] = [0, 1, 1, 5.48, 0, 6.85, 0, 0, ] 
    adj[1] = [1, 0, 0, 0, 5.48, 6.85, 1, 0, ] 
    adj[2] = [1, 0, 0, 6.4, 0, 0, 0, 4.1, ] 
    adj[3] = [5.48, 0, 6.4, 0, 1, 4.11, 0, 7.606, ]
    adj[4] = [0, 5.48, 0, 1, 0, 4.11, 6.4, 7.606, ] 
    adj[5] = [6.85, 6.85, 0, 4.11, 4.11, 0, 0, 1, ] 
    adj[6] = [0, 1, 0, 0, 6.4, 0, 0, 4.1, ] 
    adj[7] = [0, 0, 4.1, 7.606, 7.606, 1, 4.1, 0, ]

    # 1 means the path is one of the court lines
    minweight = 1000000
    minpath = []
    #choose every vertex as starting point
    for i in range(8):
        #print("Calculating minimal path weight of vertex", i)
        #Do DFS from this point and return minimal pathweight
        tuple = dfs(i, 0, 0, [])
        pweight = tuple[0]
        path = tuple[1]

        #print("Path weight of vertex "+str(i)+" is: "+str(pweight))
        if(pweight < minweight):
            minweight = pweight
            minpath = path 

    # -5 at the end because essential lines have weight 1 each
    print(minweight-5, minpath)

def wentSamePath(v, w, path):
    for i in range(len(path)-1):
        if(path[i] == v and path[i+1]==w):
            return True
        if(path[i] == w and path[i+1]==v):
            return True
    return False



def dfs(v, pweight, essentialCount, path):
    #print(v, pweight, essentialCount, path)

    newpath = path[:]
    newpath.append(v)

    minWeight = 1000
    minpath = newpath

    if(essentialCount == 5):
        minWeight = pweight
        minpath = newpath
    

    #go through all possible neighbours of vertex
    for i in range(8):
        nweight = adj[v][i]
        if(nweight == 0):
            continue
        
        if(not wentSamePath(v, i, newpath)):
            #print("Neighbour from "+str(v)+" to "+str(i))
            if(nweight == 1):
                tuple = dfs(i, pweight+nweight, essentialCount+1, newpath)
            else:
                tuple = dfs(i, pweight+nweight, essentialCount, newpath)
                
            weight = tuple[0]
            npath = tuple[1]
            if(weight < minWeight):
                minWeight = weight
                minpath = npath

    
    return (minWeight, minpath)





if __name__ == "__main__":
    main()











