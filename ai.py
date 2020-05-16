import copy

# Problem or Intial State
problem = [
    ["1", "5", "2"],
    ["4", " ", "3"],
    ["7", "8", "6"],
]

# Goal state
goal = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", " "],
]

# Types Of Action
# 1. Up
# 2. Down
# 3. Left
# 4. Right

notReachedGoal = True
visitedStates = []
state = []
actions = []

class Node:
    def __init__(self, state, parent, action, pathCost):
        self.state = state
        self.parent = parent
        self.action = action
        self.pathCost = pathCost

# Breadth First Search Approach
class QueueFrontier:
    def __init__(self):
        self.frontier = []
    
    def addNode(self, node):
        self.frontier.append(node)
        

    def removeNode(self):
        node = self.frontier[0]
        visitedStates.append(node.state)
        if len(self.frontier) > 1:
            self.frontier = self.frontier[1: ]
        else:
            self.frontier = []
        return node


    def checkForGoal(self, node):
        global notReachedGoal
        if (node.state == goal):
            print("reached goal state")
            notReachedGoal = False
            return True
        return False

    def solve(self, node):
        spaceRowCoord = 0
        spaceColCoord = 0
        stateForSolving = copy.deepcopy(node.state)
        for i in range(0, 3):
            for j in range(0, 3):
                if(stateForSolving[i][j] == " "):
                    spaceRowCoord = i
                    spaceColCoord = j
        
        # print("spaceColCoord " + str(spaceColCoord))
        # print("spaceRowCoord " + str(spaceRowCoord))

        if(spaceRowCoord == 2 and spaceColCoord == 2):
            # down
            stateForSolving = copy.deepcopy(node.state)
            # print(stateForSolving)
            temp = node.state[1][2]
            stateForSolving[2][2] = temp
            stateForSolving[1][2] = " "

            # for m in visitedStates:
            #     print(m)

            if not stateForSolving in visitedStates:
                self.frontier.append(Node(stateForSolving, node, "down", node.pathCost + 1))

            # right
            stateForSolving = copy.deepcopy(node.state)
            temp = node.state[2][1]
            stateForSolving[2][2] = temp
            stateForSolving[2][1] = " "
            
            if not stateForSolving in visitedStates:
                self.frontier.append(Node(stateForSolving, node, "right", node.pathCost + 1))


        elif(spaceRowCoord == 0 and spaceColCoord == 0):
            # up
            stateForSolving = copy.deepcopy(node.state)
            temp = node.state[1][0]
            stateForSolving[0][0] = temp
            stateForSolving[1][0] = " "
            if not stateForSolving in visitedStates:
                self.frontier.append(Node(stateForSolving, node, "up", node.pathCost + 1))

            # left
            stateForSolving = copy.deepcopy(node.state)
            temp = node.state[0][1]
            stateForSolving[0][0] = temp
            stateForSolving[0][1] = " "
            if not stateForSolving in visitedStates:
                self.frontier.append(Node(stateForSolving, node, "left", node.pathCost + 1))



        elif(spaceRowCoord == 2 and spaceColCoord == 0):
            # down
            stateForSolving = copy.deepcopy(node.state)
            temp = node.state[1][0]
            stateForSolving[2][0] = temp
            stateForSolving[1][0] = " "
            if not stateForSolving in visitedStates:
                self.frontier.append(Node(stateForSolving, node, "down", node.pathCost + 1))

            # left
            stateForSolving = copy.deepcopy(node.state)
            temp = node.state[2][1]
            stateForSolving[2][0] = temp
            stateForSolving[2][1] = " "
            if not stateForSolving in visitedStates:
                self.frontier.append(Node(stateForSolving, node, "left", node.pathCost + 1))


        elif(spaceRowCoord == 0 and spaceColCoord == 2):
            # up
            stateForSolving = copy.deepcopy(node.state)
            temp = node.state[1][2]
            stateForSolving[0][2] = temp
            stateForSolving[1][2] = " "
            if not stateForSolving in visitedStates:
                self.frontier.append(Node(stateForSolving, node, "up", node.pathCost + 1))

            # right
            stateForSolving = copy.deepcopy(node.state)
            temp = node.state[0][1]
            stateForSolving[0][2] = temp
            stateForSolving[0][1] = " "
            if not stateForSolving in visitedStates:
                self.frontier.append(Node(stateForSolving, node, "right", node.pathCost + 1))

        elif(spaceRowCoord == 1 and spaceColCoord == 0 or spaceColCoord == 2):
            # up
            stateForSolving = copy.deepcopy(node.state)
            temp = node.state[spaceRowCoord + 1][spaceColCoord]
            stateForSolving[spaceRowCoord][spaceColCoord] = temp
            stateForSolving[spaceRowCoord + 1][spaceColCoord] = " "
            if not stateForSolving in visitedStates:
                self.frontier.append(Node(stateForSolving, node, "up", node.pathCost + 1))

            # down
            stateForSolving = copy.deepcopy(node.state)
            temp = node.state[spaceRowCoord - 1][spaceColCoord]
            stateForSolving[spaceRowCoord][spaceColCoord] = temp
            stateForSolving[spaceRowCoord - 1][spaceColCoord] = " "
            if not stateForSolving in visitedStates:
                self.frontier.append(Node(stateForSolving, node, "down", node.pathCost + 1))
            
            # left
            if spaceColCoord == 0:
                stateForSolving = copy.deepcopy(node.state)
                temp = node.state[spaceRowCoord][spaceColCoord + 1]
                stateForSolving[spaceRowCoord][spaceColCoord] = temp
                stateForSolving[spaceRowCoord][spaceColCoord + 1] = " "
                if not stateForSolving in visitedStates:
                    self.frontier.append(Node(stateForSolving, node, "left", node.pathCost + 1))
            
             #  right
            if spaceColCoord == 2:
                stateForSolving = copy.deepcopy(node.state)
                temp = node.state[spaceRowCoord][spaceColCoord - 1]
                stateForSolving[spaceRowCoord][spaceColCoord] = temp
                stateForSolving[spaceRowCoord][spaceColCoord - 1] = " "
                if not stateForSolving in visitedStates:
                    self.frontier.append(Node(stateForSolving, node, "right", node.pathCost + 1))

        elif spaceRowCoord == 2 or spaceRowCoord == 0 and spaceColCoord == 1:
            # right
            stateForSolving = copy.deepcopy(node.state)
            temp = node.state[spaceRowCoord][spaceColCoord - 1]
            stateForSolving[spaceRowCoord][spaceColCoord] = temp
            stateForSolving[spaceRowCoord][spaceColCoord - 1] = " "
            if not stateForSolving in visitedStates:
                self.frontier.append(Node(stateForSolving, node, "right", node.pathCost + 1))
            
            # left
            stateForSolving = copy.deepcopy(node.state)
            temp = node.state[spaceRowCoord][spaceColCoord + 1]
            stateForSolving[spaceRowCoord][spaceColCoord] = temp
            stateForSolving[spaceRowCoord][spaceColCoord + 1] = " "
            if not stateForSolving in visitedStates:
                self.frontier.append(Node(stateForSolving, node, "left", node.pathCost + 1))

            # up
            if spaceRowCoord == 0:
                stateForSolving = copy.deepcopy(node.state)
                temp = node.state[spaceRowCoord + 1][spaceColCoord]
                stateForSolving[spaceRowCoord][spaceColCoord] = temp
                stateForSolving[spaceRowCoord + 1][spaceColCoord] = " "
                if not stateForSolving in visitedStates:
                    self.frontier.append(Node(stateForSolving, node, "up", node.pathCost + 1))

            # down
            if spaceRowCoord == 2:
                stateForSolving = copy.deepcopy(node.state)
                temp = node.state[spaceRowCoord - 1][spaceColCoord]
                stateForSolving[spaceRowCoord][spaceColCoord] = temp
                stateForSolving[spaceRowCoord - 1][spaceColCoord] = " "
                if not stateForSolving in visitedStates:
                    self.frontier.append(Node(stateForSolving, node, "down", node.pathCost + 1))
        else:
            # up
            stateForSolving = copy.deepcopy(node.state)
            temp = node.state[spaceRowCoord + 1][spaceColCoord]
            stateForSolving[spaceRowCoord][spaceColCoord] = temp
            stateForSolving[spaceRowCoord + 1][spaceColCoord] = " "
            if not stateForSolving in visitedStates:
                self.frontier.append(Node(stateForSolving, node, "up", node.pathCost + 1))

            # down
            stateForSolving = copy.deepcopy(node.state)
            temp = node.state[spaceRowCoord - 1][spaceColCoord]
            stateForSolving[spaceRowCoord][spaceColCoord] = temp
            stateForSolving[spaceRowCoord - 1][spaceColCoord] = " "
            if not stateForSolving in visitedStates:
                self.frontier.append(Node(stateForSolving, node, "down", node.pathCost + 1))

            # left
            stateForSolving = copy.deepcopy(node.state)
            temp = node.state[spaceRowCoord][spaceColCoord + 1]
            stateForSolving[spaceRowCoord][spaceColCoord] = temp
            stateForSolving[spaceRowCoord][spaceColCoord + 1] = " "
            if not stateForSolving in visitedStates:
                self.frontier.append(Node(stateForSolving, node, "left", node.pathCost + 1))

            # right
            stateForSolving = copy.deepcopy(node.state)
            temp = node.state[spaceRowCoord][spaceColCoord - 1]
            stateForSolving[spaceRowCoord][spaceColCoord] = temp
            stateForSolving[spaceRowCoord][spaceColCoord - 1] = " "
            if not stateForSolving in visitedStates:
                self.frontier.append(Node(stateForSolving, node, "right", ++node.pathCost + 1))

class StackFrontier(QueueFrontier):
    def removeNode(self):
        node = self.frontier[-1]
        visitedStates.append(node.state)
        if len(self.frontier) > 1:
            self.frontier = self.frontier[:-1]
        else:
            self.frontier = []
        return node



my = QueueFrontier()
my.addNode(Node(problem, None, None, 0))
totalMovementCost = 0

while(notReachedGoal):
    totalMovementCost += 1
    if len(my.frontier) == 0:
       pass
    else:
        node = my.removeNode()
        if not my.checkForGoal(node):
            my.solve(node)
        else:
            myNode = node
            while(not myNode == None):
                state.append(myNode.state)
                actions.append(myNode.action)
                myNode = myNode.parent
            state.reverse()
            actions.pop()
            actions.reverse()

for i in state:
    print(i)
    print()

for i in actions:
    print(i)
    print()

for i in visitedStates:
    print(i)
    print()

print(totalMovementCost)
