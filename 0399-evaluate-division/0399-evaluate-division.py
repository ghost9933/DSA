class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # print(equations)
        # print(values)
        # print(queries)
        variables=dict()
        knowValues=dict()

        for i in range(len(equations)):
            x,y=equations[i][0],equations[i][1]
            knowValues[(x,y)]=values[i]
            knowValues[(y,x)]=1/values[i]
            for m in variables:
                if (m,x) in knowValues and (y,m) in knowValues:
                    # print(x,m,y)
                    knowValues[(x,y)]=knowValues[(m,y)]*knowValues[(x,m)]
            if x not in variables:
                variables[x]=[y]
            else:
                variables[x].append(y)
                # variables[x].append((y,x))
            if y not in variables:
                variables[y]=[x]
            else:
                variables[y].append(x)
                # variables[y].append((y,x))
        def bfs(graph, start, goal):
            queue = deque([[start]])
            
            while queue:
                path = queue.popleft()
                node = path[-1]
                print(path)
                
                if node == goal:
                    return path
                
                for neighbor in graph.get(node, []):
                    if neighbor not in path:
                        new_path = list(path)
                        new_path.append(neighbor)
                        queue.append(new_path)
            
            return None
        


        # print(knowValues)
        # print(variables)
        ans=[0]*len(queries)
        for i in range(len(queries)):
            x=queries[i][0]
            y=queries[i][1]
            
                
            if x not in variables or y not in variables:
                ans[i]=-1
            elif x==y:
                ans[i]=1
            else:
                if (x,y) in knowValues:
                    ans[i]=knowValues[(x,y)]
                else:
                    # find if a path exist between x and y
                    # if no assign -1 else use the path to find the val
                    path=bfs(variables,x,y)
                    
                    if path:
                        start=path[0]
                        middle=path[1]
                        val=knowValues[(start,middle)]
                        for m2 in path[2:]:
                            if m2==start:
                                break
                            val=val*knowValues[(middle,m2)]
                            middle=m2
                        ans[i]=val
                    else:
                        ans[i]=-1               
        return(ans)
