---
title: Reinforcement Learning Basics
tags: [rl, notes]
date: 2025-10-15
---

# Reinforcement Learning Basics

Reinforcement learning studies how an agent should act in an environment to maximize cumulative reward.

## The MDP Framework

A **Markov Decision Process** is a tuple $(S, A, P, R, \gamma)$:

- $S$ — state space
- $A$ — action space
- $P(s' \mid s, a)$ — transition dynamics
- $R(s, a)$ — expected reward
- $\gamma \in [0, 1)$ — discount factor

The agent's goal is to find a policy $\pi(a \mid s)$ that maximizes the expected discounted return:

$$G_t = \sum_{k=0}^{\infty} \gamma^k R_{t+k+1}$$

## Value Functions

The **state-value function** under policy $\pi$:

$$V^\pi(s) = \mathbb{E}_\pi \left[ G_t \mid S_t = s \right]$$

The **action-value function** (Q-function):

$$Q^\pi(s, a) = \mathbb{E}_\pi \left[ G_t \mid S_t = s, A_t = a \right]$$

## Bellman Equations

The Bellman expectation equation for $V^\pi$:

$$V^\pi(s) = \sum_a \pi(a \mid s) \sum_{s'} P(s' \mid s, a) \left[ R(s, a) + \gamma V^\pi(s') \right]$$

The **Bellman optimality equation** characterizes $V^*$:

$$V^*(s) = \max_a \sum_{s'} P(s' \mid s, a) \left[ R(s, a) + \gamma V^*(s') \right]$$

> [!NOTE]
> The Bellman equations form a system of $|S|$ equations in $|S|$ unknowns. For tabular MDPs this can be solved exactly; for large state spaces we approximate.

## Takeaways

- The MDP formalism is Markov: future transitions depend only on $(s, a)$, not history.
- $\gamma < 1$ ensures convergence for infinite-horizon problems.
- The Bellman equations underlie virtually all RL algorithms — from dynamic programming to deep Q-networks.
