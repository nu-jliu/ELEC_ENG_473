---
geometry: margin=2cm
# author: Allen Liu
# title: Deep Reinforce Learning Homework 1
---

# EE473 Deep Reinforcement Learning Homework 1
**Author**: Allen Liu

## Excercise 3.1
 - The deep reinforcement learning can be applied to how to drive along a road.
   - *State*: The velocity, position, stearing of the vehicle.
   - *Action*: The power applied to the engine, the force applied to the steering. 
   - *Reward*: The reward will +1 when it passes a checkpoint.

 - The deep reinforcement learning can be applied to how to invest money
   - *State*: State is how much money have in the account.
   - *Action*: How much money to invest to a company.
   - *Reward*: Number of profits gained from the investment.

 - The deep reinforcement learning can be applied to how to maintain proper room temperature.
   - *State*: The room temperature
   - *Action*: Power applied to the state and the heater and AC.
   - *Reward*: The reward will +1 when it reaches the desired one. 

## Excercise 3.3
The place to draw the line between the agent and the environment is by choosing the action $A_1$ to be acceleration, steering wheel and the break. In this case, the agent is the human body, where the environment is the vehicle and its surrondings.

The basis to choose the line should based on what state parameters are easily to be measurable. For example, for the action $A_1$, the state $S_1$ will be vehicle's speed, heading. In another hand, if the action $A_t$ were chosen to be the tire torque, the environment will be the ground and the surronding vehicles, and the agent will be the vehicle and the human body. Thus state $S_t$ will be 