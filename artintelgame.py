class Game(object):
    def __init__(self,list,Z,action="Initial",parent=False , cost = 0):
        self.list = list
        self.Z = Z
        self.children = []
        self.cost = cost
        self.h=0
        self.g=0
      
        if parent== False:
            self.p = False
            self.depth = 0
            self.action = ''
           
        else:
            self.p = parent
            self.depth = parent.depth + 1
            self.action = action 
         
           
  
    def __lt__(self, other):
        return self.g < other.g
   
        
        
    def up(self):
        if self.Z >= 3:
            a = self.Z - 3
            list1 = self.move(a) #move the tiles
            return Game(list1, a,"Up",self,self.cost + 1)
            
            
        else:
            return None

    def down(self):
        if self.Z <=5:
            a = self.Z + 3
            list1 = self.move(a) 
            return Game(list1, a, "Down", self,self.cost + 1)

        else:
            return None

    def right(self):
        if (self.Z % 3 == 2):
            return None
        else:
            a = self.Z + 1
            list1 = self.move(a)
            return Game(list1, a, "Right", self, self.cost + 1)

    def left(self):
        if (self.Z % 3 == 0):
            return None
        else:
            a = self.Z - 1
            list1 = self.move(a)
            return Game(list1, a, "Left",self, self.cost + 1)

    def move(self,number):
        copy = self.list[:]
        temp = copy[self.Z]
        copy[self.Z] = copy[number]
        copy[number] = temp
        
        return copy
    
    def heuristic1(self):
        #heuristic function, Manhattan distance
        #return node with h(n) value
        
        for i in self.list:
            dX = abs(int(i/3) - int(int(self.list[i])/3))
            dY = abs(i % 3 - int(self.list[i]) % 3)
            d = dX + dY
            self.h = d + self.h
            
        return self
    def heuristic2(self):
        #heuristic function, Manhattan distance
        for i in range(len(self.list)):
            dX=int(self.Z/3)**2
            dY=abs(self.Z % 3)
            d=(dX+dY)**0.5
            self.h=d+self.h
        return self
    

     
    
    def expandDFS(self):
        """expand the node"""
        # add child nodes in order of Up Left Down Right
      
        if len(self.children) == 0:

            up_child = self.up()
            if up_child is not None:
                self.children.append(up_child)
                
                
    
            left_child = self.left()
            if left_child is not None:
                self.children.append(left_child)            

            down_child = self.down()
            if down_child is not None:
                self.children.append(down_child)

            right_child = self.right()
            if right_child is not None:
                self.children.append(right_child)
       
        #print("depth = " + str(self.depth))
        
        return self.children 
        
    def expand(self):
        """expand the node"""
        # add child nodes in order of Up Down Left Right
      
        if len(self.children) == 0:

            up_child = self.up()
            if up_child is not None:
                self.children.append(up_child)
                
            down_child = self.down()
            if down_child is not None:
                self.children.append(down_child)
    
            left_child = self.left()
            if left_child is not None:
                self.children.append(left_child)            

            

            right_child = self.right()
            if right_child is not None:
                self.children.append(right_child)
       
        #print("depth = " + str(self.depth))
        
        return self.children   
    