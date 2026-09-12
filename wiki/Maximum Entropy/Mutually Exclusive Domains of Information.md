Imagine we would like to update our [[Belief|belief]] $Q$, given some incoming information, formulated as a constraint set $\mathcal{C}$, over the possible posterior probability distributions $P$.


We would like to determine a numerical functional $S[P,Q]$ or $S_Q[P]$, which tells us how preferable a posterior $P$ is, compared to other possible posteriors $P'$. This means that if 

$$
S_Q[P] \ge S_Q[P'] 
$$
means that $P$ is preferred to $P'$. 

We use the [[The Principle of Minimal Updating]], as our basis for preference. One specific application of this, is to apply it to partial constraints. Hence, $S_Q$ is supposed to measure the amount of preference for a particular new belief $P$, given how small it has changed from $Q$. The bigger the change, the less it is preferred. 

### Mutually Exclusive Domains

Let $g_{\tilde{D}}$ note a constraint over the space of posteriors $P$, localized to a subspace $\tilde{D} \subset \Omega$ of the sample space. In this particular scenario, we would like the investigate the consequences of the principle of updating, and the structural constraints it imposes on $S$. 

Let us now formalize the belief update procedure: 

$$
\begin{aligned}
\underset{p \in \mathcal{P}}{\operatorname{argmax}} S[P,Q]\\
\text{Subject to} \quad & P \in \mathcal{C}
\end{aligned}
$$
where $\mathcal{C}$ is the constraint set, defined by $g_{\tilde{D}}$.

We would like the principle to apply universally, meaning for any type of constraint. This means, that it should also apply to the case where: 

$$
g_{\tilde{D}}: \sum_{i\in \tilde{D}}p_ia_i = c
$$
This means, that we would like the above rule, to apply to the case where we have the constraint of the above form, where we have a partial expectation, defined on $\tilde{D}$. Let's investigate the structural consequences of having the principle of minimal updating, in the case of mutually exclusive domains. 





