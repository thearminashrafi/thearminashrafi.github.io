We can look at the concept of relative entropy, as a way to establish a way to update probabilities.

Imagine we have an discrete outcome space $\Omega = \{0, 1, \cdots, n\}$. Let a proposition $D$ be a subset of this space. A Belief $Q$, is simply a probability distribution, defined over this outcome space. 

This means: 

1. $Q_i \ge 0$
2. $Q(\Omega) = 1$ 

Now, imagine we receive information, in the form of a constraint, on the possible probability distributions to believe in. How can we update our belief? There could be many possible posterior distributions to believe in. We would like to find a way to prefer one over the other, with reference to our prior belief $Q$. 

In principle, $Q$ contains our current belief about the situation, and we would like to incorporate it in choosing our next belief $P$. We would like to prefer distributions, that do no diverge from our prior belief.  This is called the Principle of Parsimony, or [[The Principle of Minimal Updating]]: 

> **Principle of Minimal Updating (PMU)**: *Beliefs should be updated only to the minimal extent required by the new information.*


Now, there are various ways that we can express this same principle. 

1. [[Mutually Exclusive Domains of Information]]
2. [[Subsystem Independence]]

