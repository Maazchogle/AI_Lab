'''                                         
                                                EXPERIMENT NO :- 06                         
                                                AIM :- Implementation of Min Max Algorithm                                                             
                                                                                                              


THEORY:
Minimax is a kind of backtracking algorithm that is used in decision making and game theory to find the optimal move for a player, assuming that your opponent also plays optimally. 
It is widely used in two player turn-based games such as Tic-Tac-Toe, Backgammon, Mancala, Chess, etc.
In Minimax the two players are called maximizer and minimizer. 
The maximizer tries to get the highest score possible while the minimizer tries to do the opposite and get the lowest score possible.
Every board state has a value associated with it. 
In a given state if the maximizer has upper hand then, the score of the board will tend to be some positive value. 
If the minimizer has the upper hand in that board state then it will tend to be some negative value. 
The values of the board are calculated by some heuristics which are unique for every type of game.
''' 
import math
 
def minimax (curDepth, nodeIndex,
             maxTurn, scores, 
             targetDepth):
 
    
    if (curDepth == targetDepth): 
        return scores[nodeIndex]
     
    if (maxTurn):
        return max(minimax(curDepth + 1, nodeIndex * 2, 
                    False, scores, targetDepth), 
                   minimax(curDepth + 1, nodeIndex * 2 + 1, 
                    False, scores, targetDepth))
     
    else:
        return min(minimax(curDepth + 1, nodeIndex * 2, 
                     True, scores, targetDepth), 
                   minimax(curDepth + 1, nodeIndex * 2 + 1, 
                     True, scores, targetDepth))
     

scores = [3, 5, 2, 9, 12, 5, 23, 23]
 
treeDepth = math.log(len(scores), 2)
 
print("The optimal value is : ", end = "")
print(minimax(0, 0, True, scores, treeDepth))
 
# OUTPUT :
# The optimal value is : 12 

or


Sure, let's break down the code and its logic step by step:

```python
import math

def minimax(curDepth, nodeIndex, maxTurn, scores, targetDepth):
    if (curDepth == targetDepth): 
        return scores[nodeIndex]
```
Here, we define the `minimax` function which implements the minimax algorithm. It takes six parameters:
- `curDepth`: The current depth of the tree.
- `nodeIndex`: The index of the current node in the tree.
- `maxTurn`: A boolean value indicating whether it's the maximizer's turn or not.
- `scores`: A list containing scores associated with each node in the tree.
- `targetDepth`: The depth of the tree.

If the current depth is equal to the target depth, meaning we have reached the leaf nodes, the function returns the score of the current node.

```python
    if (maxTurn):
        return max(minimax(curDepth + 1, nodeIndex * 2, 
                    False, scores, targetDepth), 
                   minimax(curDepth + 1, nodeIndex * 2 + 1, 
                    False, scores, targetDepth))
```
If it's the maximizer's turn (`maxTurn == True`), the function returns the maximum of the scores of its child nodes. It recursively calls itself to evaluate the child nodes.

```python
    else:
        return min(minimax(curDepth + 1, nodeIndex * 2, 
                     True, scores, targetDepth), 
                   minimax(curDepth + 1, nodeIndex * 2 + 1, 
                     True, scores, targetDepth))
```
If it's the minimizer's turn (`maxTurn == False`), the function returns the minimum of the scores of its child nodes. It recursively calls itself to evaluate the child nodes.

```python
scores = [3, 5, 2, 9, 12, 5, 23, 23]

treeDepth = math.log(len(scores), 2)

print("The optimal value is : ", end = "")
print(minimax(0, 0, True, scores, treeDepth))
```
Finally, we define the scores list and calculate the depth of the tree. We call the `minimax` function with initial parameters, `curDepth=0`, `nodeIndex=0`, `maxTurn=True`, `scores`, and `treeDepth`. This will print the optimal value obtained using the minimax algorithm.

Output:
```
The optimal value is : 12
```

The code essentially builds a binary tree where each node has two child nodes. It then uses the minimax algorithm to find the optimal value.
