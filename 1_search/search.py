# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""
##renamed tkinter to everything lower case

import util

from queue import Queue

from queue import PriorityQueue

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    
    ##implements LIFO through stack 
    stack = []
    
    stack.append((problem.getStartState(), []))
    
    visited = [] # set()
    
    while len(stack) != 0:
        state, actions = stack.pop()
        
        if not state in visited: 
            visited.append(state)
        
        if problem.isGoalState(state): #check if at goal state 
            return actions 
        
        else:
            successors = problem.getSuccessors(state)
        
            unVisited = False
        
            for node, action, cost in successors:
                if node not in visited:
                    unVisited = True
                    stack.append((node, actions + [action]))
        
            if not unVisited:
                visited.remove(state)
                
    return actions
    
    
    util.raiseNotDefined()
    

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    queue = Queue()
    
    queue.put((problem.getStartState(), []))
    
    visited = [] ##visited node list 
    
    while not queue.empty():
        state, actions = queue.get()
        
        if state in visited:
            continue
        
        if problem.isGoalState(state): #check if at goal state 
            return actions 
        
        else:
        
            visited.append(state)  ##add node to visited list 
        
            successors = problem.getSuccessors(state)
    
            unVisited = []
        
            for node, action, cost in successors:
                if node not in visited:  
                    unVisited.append((node, actions + [action]))
            
            for node, nextActions in unVisited: 
                queue.put((node, nextActions))
            
        
    return actions
    util.raiseNotDefined()
    

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    visited = []
    priority = util.PriorityQueue()
    priority.push((problem.getStartState(), []) ,0) ##state and actions, cost 
    
    while not priority.isEmpty():
        state, actions = priority.pop()
        
        if problem.isGoalState(state):  ##if reached, quit 
            return actions
        
        else: 
            if state not in visited:  ###if hasnt been visited yet 
                visited.append(state) 
                successors = problem.getSuccessors(state)

                for node, action, cost in successors: ### the tuple cotaining the node, list and cost
                    if node not in visited:
                        steps = actions + [action]
                        cost =+ problem.getCostOfActions(steps)
                        priority.push((node, steps), cost) 
    return actions
    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    
    priority = util.PriorityQueue()
    visited = []
    
    ##add first node
    priority.push((problem.getStartState(), []), heuristic(problem.getStartState(), problem))
    
    while not priority.isEmpty():
        state, actions = priority.pop()
        
        if problem.isGoalState(state):
            return actions
        
        else: 
        
            if state not in visited: 
                visited.append(state)
                successors = problem.getSuccessors(state) ##set current nodes successors here 
            
                for node, action, cost in successors:
                    nodeActions = actions + [action]
                    cost =+ problem.getCostOfActions(nodeActions) + heuristic(node, problem)
                    priority.push((node, actions + [action]), cost)
                
    return actions
    util.raiseNotDefined()
    


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
