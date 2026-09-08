In most definitions of Mutual Information, the definition is given directly. I believe *deriving* the definitions from another set of examples can be really illuminating.

## A Measure of Relationship between Random Variables

We are interested in finding out a quantity that tells about the information gained about a random variable $X$, when the value of another variable $Y$ is known [^1]. We will list a set of design criteria, that we would like our measure relationship to show.

### Design Criteria

1. **Independence**: If the random variables $X$ and $Y$ are independent, then our measure of relationship needs to be 0. 
2. **Non-Negativity**: We are measure how dependent two variables are, which at a minimum, is 0, when they are independent.

Now, some important points to keep in mind in this context: 
### Observations

1. The Joint Distribution $P(X,Y)$ encapsulates all the information between all possibles pairs of values between $X$ and $Y$.
2. In general, $X$ and $Y$ are not independent from each other over $P(X,Y)$. There are a myriad of probability measures $R(X,Y)$ that can be defined in such a way that $X$ and $Y$ are independent from each other.

So here is a question: 

> If $X$ and $Y$ were dependent, how surprised would we be, if we believed they were independent, as characterized by $R(X,Y)$?

A measure of such a surprisal would the [[Kullback-Leibler Divergence]], given as: 

$$
D_{KL}(P(X,Y)||R(X,Y)) = \sum_{(x,y) \in \mathcal{X} \times \mathcal{Y}} P(x,y)\log \frac{P(x,y)}{R(x,y)}
$$


This characterizes the relationship between $P(X,Y)$ and *any probability distribution* $R(X,Y)$, in which: 

$$
R(X,Y) = R_X(X)R_Y(Y)
$$
The space of possible $R(X,Y)$ is large, and depends on the choice $R(X,Y)$. In addition, let's notice that: 

**Lemma 1.** *The probability distribution $R(X,Y) = P(X)P(Y)$*, where $P(X)$ and $P(Y)$ signify the marginal probability distributions derived from $P(X,Y)$.

*Proof.* Left to reader.

**Lemma 2.** *It can be shown that* $D_{\text{KL}}(P(X, Y) \parallel R_X(X) R_Y(Y))$ is equal to: 

$$
 D_{\text{KL}}(P(X, Y) \parallel P_X(X) P_Y(Y)) + D_{\text{KL}}(P_X(X) \parallel R_X(X)) + D_{\text{KL}}(P_Y(Y) \parallel R_Y(Y))
$$*Proof.* Let us start from the original form: 


$$
\sum_{(x,y) \in \mathcal{X} \times \mathcal{Y}} P(x,y)\log \frac{P(x,y)}{R(x,y)}
$$

Now, let's multiply and divide the quotient in the logarithm by $P_X(x)P_Y(y)$:


$$
\sum_{(x,y) \in \mathcal{X} \times \mathcal{Y}} P(x,y)\log \frac{P(x,y)[P_X(x)P_Y(y)]}{R(x,y)[P_X(x)P_Y(y)]}
$$
Let's rewrite this as 2 sums: 

$$
\sum_{x \in \mathcal{X}} \sum_{y \in \mathcal{Y}} P(x,y)\log \frac{P(x,y)[P_X(x)P_Y(y)]}{R(x,y)[P_X(x)P_Y(y)]}
$$

Using logarithmic identity $\log(a \cdot b \cdot c) = \log a + \log b + \log c$, and the fact that $R(X,Y) = R_X(X)R_Y(Y)$:

$$\log \frac{P(x, y)}{R_X(x) R_Y(y)} = \log \frac{P(x, y)}{P_X(x) P_Y(y)} + \log \frac{P_X(x)}{R_X(x)} + \log \frac{P_Y(y)}{R_Y(y)}$$
Substituting this back in, and separating the sums gives us the result. $\blacksquare$ 


We now have a general form for the difference between $P(X,Y)$, and any arbitrary joint distribution $R(X,Y)$ where $X$ and $Y$ are independent. 


### Checking the new formula against the Design Criteria

In order to see if the new formula matches our design criteria, let's check the one by one. 


1. **Independence**: If we assume $X$ and $Y$ are independent over $P(X,Y)$, using the form above, the distance measure would simplify to: 

$$
D_{KL}(P_X(X)\parallel R_X(X)) + D_{KL}(P_Y(Y)\parallel R_Y(Y))
$$

### Observations

1. The measure is only 0, if $R_X(X) = P_X(X)$ and $R_Y(Y) = P_Y(Y)$.
2. This means that $R(X,Y) = P_X(X)P_Y(Y)$. 
3. We now have a measure of the distance between $P(X,Y)$ and a joint distribution $R(X,Y)$ over $X$ and $Y$, where If we want this measure to be 0 when $X$ and $Y$ are independent, $R$ is forced to be the product of the marginals of $P(X,Y)$. 
4. Another interesting observation, is that choosing $R(X,Y) = P_X(X)P_Y(Y)$, is the unique joint distribution over $R(X,Y)$ where: 
	1. $X$ and $Y$ are independent.
	2. It achieves minimum relative entropy or [[Kullback-Leibler Divergence]] from $P(X,Y)$.

Putting all this together, gives us this definition for Mutual Information: 

$$
I(X;Y) = D_{KL}(P(X,Y)||P(X)P(Y))
$$

[^1]: This information regarding (in)dependence is not a standalone property of $X$ and $Y$, but is dictated by a joint probability measure P(X,Y) defined over them.
