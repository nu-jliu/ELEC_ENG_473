---
geometry: margin=2cm
---
# EE473 Deep Reinforcement Learning Homework 3

## Excercise 3.26
For all $s \in {\cal S}$ and $a \in {\cal A(s)}$, for a state-action pair $\left(s, a\right)$, we can find the expected return for taking action $a$ in state $s$ as $q \left(s, a\right)$ that
$$
\begin{aligned}
    q_* \left(s, a \right) &= \mathbb{E} \left[ R_{t+1} + \gamma v_* \left(S_{t+1}\right) \vert S_t=s, A_t=a \right] \\
    &= \sum_{s', r} p\left(s', r\right \vert s, a) \left[ r + \gamma v_*(s')\right]
\end{aligned}
$$

## Excercise 3.27

$$
\begin{aligned}
    a_* &= \text{arg} \max_a q_*\left(s, a\right) \\
    \pi_*(s) &= \pi(a_* \vert s) \\
    &= \pi\left(\text{arg} \max_a q_* \left( s, a\right) \Bigm\vert s\right)
\end{aligned}
$$

## Excercise 3.29
$$
\begin{aligned}
    v_\pi(s) &= \mathbb{E} \left[ G_t | S_t=s\right] \\
    &= \sum_a \left[r(s, a) + \gamma \sum_{s'} p\left(s' \vert s, a \right) v_\pi\left(s'\right) \right]\pi(s, a)
\end{aligned}
$$

$$
\begin{aligned}
    v_*(s) &= \max_\pi v_\pi(s)\\
    &= \sum_a \left[r(s, a) + \gamma \sum_{s'} p\left(s' \vert s, a \right) v_*\left(s'\right) \right]\pi_*(s, a)
\end{aligned}
$$

$$
\begin{aligned}
    q_\pi(s, a) &= \mathbb{E}_\pi \left[G_t \Bigm\vert S_t=s, A_t=a \right] \\
    &= \mathbb{E}_\pi \left[ R_{t+1} + \gamma G_{t+1} \Bigm\vert S_{t+1} = s', A_t=a\right] \\
    &= r(s, a) + \gamma \sum_{s'} p\left( s' \vert s, a\right)\sum_{a'}q_\pi(a', s') \pi(s' \vert a')
\end{aligned}
$$

$$
\begin{aligned}
    q_*(s, a) &= \max_\pi q_\pi(s, a) \\
    &= \max_\pi \mathbb{E}_\pi \left[ R_{t+1} + \gamma G_{t+1} \Bigm\vert S_{t+1} = s', A_t=a\right] \\
    &= \mathbb{E}_{\pi_*} \left[ R_{t+1} + \gamma G_{t+1} \Bigm\vert S_{t+1} = s', A_t=a\right] \\
    &= r(s, a) + \gamma \sum_{s'} p\left( s' \vert s, a\right)\sum_{a'}q_*(a', s') \pi_*(s' \vert a')
\end{aligned}
$$

## Excercise 4.1
Let state $T$ denote the ternimal state

$$
\begin{aligned}
    q_\pi \left( 11, {\tt down}\right) &= r \left(11, {\tt down}\right) + v_\pi(T) \\
    &= -1 + 0 \\
    &= -1
\end{aligned}
$$

$$
\begin{aligned}
    q_\pi \left( 7, {\tt down}\right) &= r \left(7, {\tt down}\right) + v_\pi(11) \\
    &= -1 + (-14) \\
    &= -15
\end{aligned}
$$

## Policy Iteration vs Value Iteration
Policy iteration requires a explicit representation of the policy $\pi$ while the value representation does not so that it is simplier to solve using value iteration. But the policy iteration requires less steps to converge so that it is more effective. Even though the value iteration is simplier to implement, it is more effective using policy iteration. Hence I favor policy iteration rather than value iteration.