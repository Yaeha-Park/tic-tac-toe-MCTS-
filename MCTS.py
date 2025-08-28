import random
import math
from TTT import ttt

class MCTSNode:
    def __init__(self, state: ttt, parent = None, move = None):
        self.state = state
        self.parent = parent
        self.move = move
        self.children = []
        self.visits = 0
        self.value = 0
        self.valid = state.get_valid_moves()

    # Check if new MCTS node needs to be created
    def full(self):
        return len(self.valid) == 0
    
    # Makes new MCTS node
    def grow(self):
        move = self.valid.pop()
        new = self.state.make_move(move)
        child = MCTSNode(new, parent = self, move = move)
        self.children.append(child)
        return child
    
    # Calculates upper confidence bounds for trees, higher score has priority for node visit
    def bestnode(self, c_param = 1.41):

        choices = []

        for child in self.children:

            if child.visits == 0:

                score = float('inf')

            else:

                score = (child.value / child.visits) + c_param * math.sqrt(math.log(self.visits) / child.visits)

            choices.append(score)

        return self.children[choices.index(max(choices))]

    def extend(self):
        current = copy.deepcopy(self.state)
        while current.get_winner() != None:
            move = random.choice(current.get_valid_moves())
            current = current.make_move(move)
        winner = current.get_winner()

        if winner == 'Draw':
            return 0
        elif winner == self.state.player:
            return 1
        else: 
            return -1
        
    def backpropagate(self, result):
        self.visits += 1
        self.score += result
        if self.parent != None:
            self.parent.backpropagate(-result)
  
    def runMCTS(rootstate, iterations = 1000):
        root = MCTSNode(rootstate)

        for in range(iterations):
            node = root

            while node.full() and node.children:
                node = node.bestnode()

            if not node.full():
                node = node.grow()

            result = node.extend()
            node.backpropagate(result)

        return max(root.children, key = lambda visit_count: children.visits).move

    
    

