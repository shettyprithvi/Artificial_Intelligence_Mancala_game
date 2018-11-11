import time
import random 
import io

class key:
    def key(self):
        return "10jifn2eonvgp1o2ornfdlf-1230"

class ai:
    def __init__(self):
        pass

    class state:
        def __init__(self, a, b, a_fin, b_fin):
            self.a = a
            self.b = b
            self.a_fin = a_fin
            self.b_fin = b_fin

    # Kalah:
    #         b[5]  b[4]  b[3]  b[2]  b[1]  b[0]
    # b_fin                                         a_fin
    #         a[0]  a[1]  a[2]  a[3]  a[4]  a[5]
    # Main function call:
    # Input:
    # a: a[5] array storing the stones in your holes
    # b: b[5] array storing the stones in opponent's holes
    # a_fin: Your scoring hole (Kalah)
    # b_fin: Opponent's scoring hole (Kalah)
    # t: search time limit (ms)
    # a always moves first
    #
    # Return:
    # You should return a value 0-5 number indicating your move, with search time limitation given as parameter
    # If you are eligible for a second move, just neglect. The framework will call this function again
    # You need to design your heuristics.
    # You must use minimax search with alpha-beta pruning as the basic algorithm
    # use timer to limit search, for example:
    # start = time.time()
    # end = time.time()
    # elapsed_time = end - start
    # if elapsed_time * 1000 >= t:
    #    return result immediately 
    
    #Human is a flag differentiating between AI move and human move.
    
    #Human=0 means that the AI is playing while Human = 1 implies human is playing
    def create_child(self,a,b,move,a_fin, b_fin,a_score,human=0):


        a_score=[]
        #Creating a copy by slicing
        ao = a[:]
        #All the states are tracked in the variable all
        all = a[move:] + [a_fin] + b + a[:move]
        
        #Count is used to keep a track of the stones in the hole
        count = a[move]
        all[0] = 0
        p = 1
        while count > 0:
            all[p] += 1
            p = (p + 1) % 13
            count -= 1
        a_fin = all[6 - move]

        b = all[7 - move:13 - move]
        a = all[13 - move:] + all[:6 - move]
        cagain = bool()
        ceat = False
        p = (p - 1) % 13
        if p == 6 - move:
            cagain = True
        if p <= 5 - move and ao[move] < 14:
            id = p + move
            if (ao[id] == 0 or p % 13 == 0) and b[5 - id] > 0:
                ceat = True
        elif p >= 14 - move and ao[move] < 14:
            id = p + move - 13
            if (ao[id] == 0 or p % 13 == 0) and b[5 - id] > 0:
                ceat = True
        if ceat:
            a_fin += a[id] + b[5 - id]
            b[5 - id] = 0
            a[id] = 0
        if sum(a) == 0:
            b_fin += sum(b)
        if sum(b) == 0:
            a_fin += sum(a)

        #If human move just return the total value of the Kalah AI score
        if human==1:
            return a_fin


        a_score.append(a_fin)


        #To consider the case when the stone lands in the goal position and gets a repeat chance
        if cagain==True:

            a_score=[]
            r=[]

            int_final=[]

            for i in range(6):
                if a[i] != 0:
                    r.append(i)
            for index, value in enumerate(r):
                int_final.append(self.create_child_recursive(a, b, value, a_fin, b_fin,a_score))
            
            #Choosing the best possible move to get the maximum move
            return max(int_final)
        #If the turn is not repeated, the turn changes normally to Human 
        else:

            r2 = []
            for i in range(6):
                if b[i] != 0:
                    r2.append(i)
            b_score = []
            for index, value in enumerate(r2):
                b_score.append(self.create_child(b, a, value, b_fin, a_fin, b_score,human=1))
                
        
            #Applying minmax logic with heuristic as the difference in maximum scores of both the human and AI. This heuristic thus considers the worst possible move by human for the AI to tackle.
            if (len(b_score) == 0):
                print("Best possible move outcome is", max(a_score))
                return max(a_score)
            else:
                print("Best possible move outcome is", max(a_score)-max(b_score))
                return max(a_score)-max(b_score)
      
    
    def move(self, a, b, a_fin, b_fin, t):

        r = []
        r2=[]

        for i in range(6):
            if a[i] != 0:
                r.append(i)
            elif a[i]==0:
                r2.append(i)

        a_score=[]

        for index, x in enumerate(r):

            a_score.append(self.create_child(a,b,x,a_fin, b_fin,a_score))

            
        #R2 maintains the list of all blank positions
           #Replacing all the values in R2 by a high negative number : so as to not select them during max function
        if len(a_score)<=5:

            for i in r2:

                a_score[i:i] = [-50]

            return a_score.index(max(a_score))

        else:

            return a_score.index(max(a_score))




    #Calling minimax function
    def minimax(self, b_score, a_fin):

        if (len(b_score) != 0):

            return a_fin - max(b_score)

        else:

            return a_fin

        
    #Recursive function to generate states    
    def create_child_recursive(self,a,b,move,a_fin, b_fin,a_score):

        ao = a[:]
        all = a[move:] + [a_fin] + b + a[:move]
        count = a[move]
        all[0] = 0
        p = 1
        while count > 0:
            all[p] += 1
            p = (p + 1) % 13
            count -= 1
        a_fin = all[6 - move]
        b = all[7 - move:13 - move]
        a = all[13 - move:] + all[:6 - move]
        cagain = bool()
        ceat = False
        p = (p - 1) % 13
        if p == 6 - move:
            cagain = True
        if p <= 5 - move and ao[move] < 14:
            id = p + move
            if (ao[id] == 0 or p % 13 == 0) and b[5 - id] > 0:
                ceat = True
        elif p >= 14 - move and ao[move] < 14:
            id = p + move - 13
            if (ao[id] == 0 or p % 13 == 0) and b[5 - id] > 0:
                ceat = True
        if ceat:
            a_fin += a[id] + b[5 - id]
            b[5 - id] = 0
            a[id] = 0
        if sum(a) == 0:
            b_fin += sum(b)
        if sum(b) == 0:
            a_fin += sum(a)
            
        #To find all the holes which are not empty
        r = []
        for i in range(6):
            if b[i] != 0:
                r.append(i)
        
        b_score = []
        for index, value in enumerate(r):
            b_score.append(self.create_child(b, a, value, b_fin, a_fin, b_score,human=1))
               
        #Minimax to get the best move possible :
        #Heurisitic is the highest difference between the scores of AI and human
        
        print("Best possible move is", self.minimax(b_score,a_fin))
        return self.minimax(b_score,a_fin)
        
        
