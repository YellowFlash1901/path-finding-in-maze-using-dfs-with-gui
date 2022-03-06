from pyamaze import maze,agent,COLOR


def DFS(m):
    start=(m.rows,m.cols) #from this our maze will start (5,5)
    explored=[start]
    frontier=[start]
    
    dfspath={}

    while len(frontier)>0:
        Currcell = frontier.pop()
        if Currcell == (1,1):
            break
        for d in 'ESNW':
            if m.maze_map[Currcell][d]==True:
                if d=='E':
                    childCell=(Currcell[0],Currcell[1]+1)
                elif d=='W':
                    childCell=(Currcell[0],Currcell[1]-1)
                elif d=='S':
                     childCell=(Currcell[0]+1,Currcell[1])
                elif d=='N':
                     childCell=(Currcell[0]-1,Currcell[1])
                if childCell in explored:
                    continue
                explored.append(childCell)
                frontier.append(childCell)
                dfspath[childCell]=Currcell
    fwdPath={}
    cell=(1,1)
    while cell!=start:
        fwdPath[dfspath[cell]]=cell
        cell=dfspath[cell]
    return fwdPath


m = maze(5,5) #creating maze
m.CreateMaze() #create random maze
path = DFS(m)
a=agent(m,footprints=True)#to see the path
m.tracePath({a:path})


m.run() # to run the simulation