import sys
import game
import stack
import queue
import random
import time
import heapq
from game import Game

goal_list = [0,1,2,3,4,5,6,7,8]

def heapsort(q):
    i=-1
    temp=q
    new=[]
   
    while temp:
        heapq.heapify(temp)
        heapq.heappush(new,heapq.heappop(temp))
        #heapq.heapify(new)
        #print(str(i)+" "+str(temp[0].h))
        #heapq.heappop(q)
        #temp=q
        i=i+1 
    heapq.heapify(new)        
    return new


def AStarSearchManhattan(StartState,Z):
    t0=time.process_time()
    Puzzle= game.Game(StartState,Z)
    #puzzle_state.heuristic()
    q=[Puzzle]
    heapq.heapify(q)
    explored = set()  #to store already explored puzzle lists
    i=0
    
    while q[0]:
        #state=q[0]
        state=heapq.heappop(q)
        explored.add(tuple(state.list))
        if (state.list==goal_list):
            print("\n SUCCESS!!!!!!!!!!")
            WriteInFile(state,i,"A star search,Manhattan Heuristic",time.process_time()-t0,state.depth)
            return 1 
        children=state.expand() 
        
        for states in children:
            old=states
            states=states.heuristic1()
            #states.expand()
            states.g=states.h+state.cost
            if (tuple(states.list) not in (explored)) and (states not in (q)):   
                heapq.heappush(q,states)
                #q=heapsort(q)
            elif states in (q):
                    #print("h "+str(old.h)+" "+str(states.h))
                    if old.h > states.h:
                        old.h=states.h
                        #heapq.heappop(q,old)
                        heapq.heappush(q,old)          
                        
        q=heapsort(q)
        i = i+1
    print("\n FAILURE!!!!!!!!!")

    
def AStarSearchEuclidian(StartState,Z):
    t0=time.process_time()
    Puzzle = game.Game(StartState,Z)
    
    q=[Puzzle]
    heapq.heapify(q)
    explored = set()  #to store already explored puzzle lists
    i=0
    
    while q[0]:
        #state=q[0]
        state=heapq.heappop(q)
        explored.add(tuple(state.list))
        if (state.list==goal_list):
            print("\n SUCCESS!!!!!!!!!!")
            WriteInFile(state,i,"A star search,Eculidian Heuristic",time.process_time()-t0,state.depth)
            return 1 
        children=state.expand() 
        
        for states in children:
            old=states
            states=states.heuristic2()
            #states.expand()
            states.g=states.h+state.cost
            if (tuple(states.list) not in (explored)) and (states not in (q)):   
                heapq.heappush(q,states)
                #q=heapsort(q)
            elif states in (q):
                    #print("h "+str(old.h)+" "+str(states.h))
                    if old.h > states.h:
                        old.h=states.h
                        #heapq.heappop(q,old)
                        heapq.heappush(q,old)          
                        
        q=heapsort(q)
        i = i+1
    print("\n FAILURE!!!!!!!!!")
    


def DFSSearch(StartState,Z):
    t0=time.process_time()
    Puzzle = game.Game(StartState,Z)
    stck = stack.Stack()

    depth_limit = 100
    i=0
    explored = set()  #to store already explored puzzle lists
    stck.push(Puzzle)
    state = Puzzle

    while (state.cost < depth_limit) or (not stck.isEmpty()):
        state = stck.pop() 
        print("iteration : ",i)    
        ##print(state.list)
        explored.add(tuple(state.list))

        if(state.list == goal_list):
            print("\n SUCCESS!!!!!!!!!!")
            WriteInFile(state,i,"DFS",run_time,state.depth)
            return 1

        children = []
        children.extend(state.expandDFS())
        children.reverse()    

        if (state.cost < depth_limit):
            for states in children:
                if tuple(states.list) not in (explored.union(stck.state)):
                    stck.push(states)

        i = i+1
        run_time=time.process_time()-t0
    print("\n FAILURE!!!!!!!!!")


def BFSSearch(StartState,Z):
    t0=time.process_time()
    Puzzle = game.Game(StartState,Z)
    
    q = queue.Queue()
    
    q.enqueue(Puzzle)
    explored = set()  #to store already explored puzzle lists
    i=0

    while not q.isEmpty():
        state = q.dequeue()
        #print("iteration : ",i)
        #print(state.list)
                
        
            
        explored.add(tuple(state.list))
             

        if(state.list == goal_list):
            print("\n SUCCESS!!!!!!!")
            WriteInFile(state,i,"BFS",run_time,state.depth)
            return 1

        children = state.expand()
        
        for states in children:
            if tuple(states.list) not in (explored.union(q.state)):
                q.enqueue(states)
                
        i = i+1
        
        
        run_time=time.process_time()-t0
    print("\n FAILURE!!!!!!!!")  

def WriteInFile(state,i,string,run_time,depth):
    
    cost = "Path Cost : " + str(state.cost)
    nodes = "Nodes Expanded :" + str(i)
    action_list = []
    fofa=[]
    x=[]
    m=[]
    g=[0,1,2,3,4,5,6,7,8]
    for i in range(state.cost):
        action_list.append(state.action)
        state = state.p
        fofa.append(state.list)
        
    action_list.reverse()
    fofa.reverse()
    
    
    for f in fofa:
       
        x=f
        print("\n")
        for i in x[0:3]:
            
            i=str(i).replace('0',' ')
            print(i, end = '|')
            
        print("\n" + "------")    
        for i in x[3:6]: 
            i=str(i).replace('0',' ')
            print(i, end = '|')
            
        print("\n" + "------")    
        for i in x[6:9]:
            i=str(i).replace('0',' ')
            print(i, end = '|')        
                      
       # print("\n"+ str(f))
    print("\n")
   
    
    print(" |1|2|"+"\n"+"------"+"\n"+ "3|4|5|"+"\n"+"------"+"\n"+"6|7|8|")   
    
    
    Text = [cost+"\n",nodes+"\n"]
    with open("ArtificialIntelligence.txt","w") as file1:
        #file1.write("First State = "+ StartState +"\n")
        file1.write("You Chose = " + string +"\n")
        for line in Text:
            
            file1.write(line)
        file1.write("Written Path = [ ")
        for each in action_list:
            file1.write(each+", ")
        file1.write( "]")
        file1.write("\n"+"Depth= " + str(depth))
        file1.write("\n"+ "Run Time =" + str(run_time))
        
        for f in fofa:
            file1.write("\n"+ str(f))
            
        file1.write("\n" + str(g))
        



def main():

    goal= [0,1,2,3,4,5,6,7,8]
    print("Please Enter you list of 9 non-repeated numbers")
    #StartState=goal
    # random.shuffle(StartState)
    
    #StartState=[1,4,2,0,3,5,6,7,8]
    #print (StartState)
   
    
    a = [int(x) for x in input().split(",")]
    print(a)
    
    if(not len(a)==9):
        print("Please Enter 9 number to play the game...")
        sys.exit()    
    
      
    def FindDuplicates(in_list):  
        unique = set(in_list)  
        for each in unique:  
            count = in_list.count(each)  
            if count > 1:  
                print ('There are duplicates in this list' ) 
                sys.exit()    
    FindDuplicates(a)
    
    for i,state in enumerate(a):
        if state == 0:
            Z = i 
    alg=input("Please Enter the algorithm with which you want to play: ")
    print("You Chose"+ ' ' + alg)
    
    if alg == 'bfs' or alg=='BFS':
        #print("BFS")
        BFSSearch(a,Z)
    
    if alg == 'dfs' or alg=='DFS':
        #print("DFS")
        DFSSearch(a,Z)     
    
    if alg == 'ast' or alg=='AST':
        #print("A*")
        AStarSearchManhattan(a,Z)
        AStarSearchEuclidian(a,Z)
    
    

if __name__ == '__main__':

    main()