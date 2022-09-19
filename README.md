# Snake Reinforcement AI Python
Experiment with the Reinforcement tequnice applied to the snake game in a pygame environment
## Technologies
Python, Pygame and PyTorch

## (Deep) Q Learning
https://www.freecodecamp.org/news/diving-deeper-into-reinforcement-learning-with-q-learning-c18d0db58efe/

**Q Value** = Quality of action
0. Init Q Value (= init model)
1. Choose action (model.predict(state))
2. Perform action
3. Measure reward
4. Update Q value (+ train model)
5. Repeat 1.

## Bellman Equation
Update Q-Value using the Bellman Equation

`NewQ(s,a) = Q(s,a) + α[R(s,a) + φ*maxQ'(s',a') - Q(s,a)]`
* NewQ(s,a).. New Q value for that state and that action
* Q(s,a)... Current Q value
* α... Learning rate
* R(s,a).. Reward for taking that action at that state
* φ... Discount rate
* maxQ'(s',a')... Maximum exprected future reward given the new s' and all possible actions at that new state

Q = model.predict(state0)
Qnew = R + φ * max(Q(state1))

### Loss Function for optimization
Mean squared error: loss = (Qnew - Q)^2
# Reinforcement model
## Reward
- eat food: +10
- game over: -10
- else: 0

## Action
- [1, 0, 0] -> straight
- [0, 1, 0] -> right turn
- [0, 0, 1] -> left turn

## State (information about the game-environment) are booleans
- danger straight / danger right / danger left [0,0,0]
- direction left, direction right, direction up, direction down [0,0,0,0]
- food left, food right, food up, food down [0,0,0,0]