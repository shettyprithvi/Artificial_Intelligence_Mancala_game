# Artificial_Intelligence_Mancala_game
## Playing 2 player Mancala game using AI. See ai.py for implementation using Minmax algorithm with Alpha-Beta pruning.

See the pdf for the report with further details.![alt text](https://github.com/shettyprithvi/Artificial_Intelligence_Mancala_game/blob/master/Assignment%203%20Kalah%20Game.pdf)

![alt text](https://github.com/shettyprithvi/Artificial_Intelligence_Mancala_game/blob/master/mancala.jpeg)

### Overview: 
Mancala is a two – player game which is turn-based. 
The board has 12 holes and one goal hole for each player. 
Each player has 6 holes on their side assigned to themselves. Each hole has 6 stones at start in each thus there are total 72 stones at the start. 
The player whose turn it is chooses one of the 6 holes they own which is not empty. The stones in the hole are held completely and distributed one by one into the subsequent holes moving anti-clockwise, skipping only the goal of the opposite player. 

### Aim: The final aim is to collect as many stones as possible in their own goal or Kalah.

## Rules: 
1.The game will end when one of the sides (6 holes) are completely empty.
2.The player exceeds a score of 36
3.If the last stone lands on the goal of the player, the player gets an extra chance.
4.If the last stone lands on an empty goal, then the player gets all the stones from the exact opposite hole to his goal.




### Heuristic function used: 

1.	Difference in the maximum score possible by the AI and the maximum score possible by the human.

Reason:  The reason I have chosen this heuristic is that it will consider the best possible move of the AI after taking into account that the human has taken the best possible move to increase its score.

 

2.	The number of stones on each side of the player. 

Reason: The more the number of stones on each side, the more the moves for that player. This directly increases the probability for winning.










### Working of the heuristic:
1.	The first step is to take the input move by the human and branch out the possible states.

The blank stones are maintained in another list which is later used for selection of the maximum score and the best possible move.


  







2.	All the possible children are created till the depth provided. For example, if the depth is 3. The AI will consider all the possibilities from the action it takes till the next two turns, which is the human turn and the next AI possible move.
 

3.	After the possible states have been created. The minmax function finds out if the value returned satisfies the best possible heuristic and correspondingly returns the best possible move for the AI.

 
3.Example:
 
The final move of 33 was chosen which resulted in the AI winning the game against the human.
 

4.Experiments: 
Infrastructure : 2.4 GHz CoreI5 , 16 GB RAM.
Level	Time taken for each move
1	.0009s
2	.0045
3	.01
4	.03


### Heuristics
I considered my first heuristic and competed it against a heuristic of just choosing the maximum score for best possible move and not the difference between human and AI scores.
Result:  The AI was better and won every time against the old AI.

 

### Deduction:

1)Heuristic of the game must always consider the worst possible move of the opponent for the AI to perform the best.
2) As depth increase, the performance decreases as well. Alpha beta pruning plays a great role to increase the efficiency and skip unwanted traversals.





