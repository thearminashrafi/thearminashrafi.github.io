In this entry, we are interested in deriving mutual information, from a set of principles, and then *derive* the definition from them, to clarify the structure of the concept. 


Let's setup the necessary background:

1. A Probability Distribution
2. A random variable 
3. The Kullback-Leibler divergence


A random variable, is a mapping between the sample space $\Omega$, and a set of values $X$, normally the real numbers $\mathbb{R}$.

When one talks about the expectation of a random variable, it is implicitly assumed that one is talking about the expected value defined on the specific distribution. Same is the case for when we are talking about the entropy of a variable, what we mean is the entropy of the underlying distribution over the variable. 

It's important to know that when we are talking about a random variable $V$, it is implied that a probability distribution is defined over the sample space $\Omega$, which is then transffered to the value space $V$. This is not the only possible distribution over the random variable.

## What we would like to achieve

We are interested in finding out a quantity that tells about the information gained about a random variable, when the value of another is known. Here are some useful observations: 

1. Independence: If the random variables $X$ and $Y$ are independent, then we cannot in any way, have any information be gained from $X$, if we know $Y$. 
2. The KL Divergence can be a way for us to measure the surprise of believing in one distribution, over another. A Kind of distance. 
3. We would like to measure how "independent" two variables are from each other, using this distance. 

In order to do this, we need to study the following object: $P(X,Y)$, i.e. the joint distribution over the two variables, which encodes all the joint possibilities for the pair $(X,Y)$, and their probabilities. 

In order to gauge how independent $P(X,Y)$ is, we need to find its distance from a distribution in which $X$ and $Y$ would be independent. This is because whether or not $X$ and $Y$ are indpendent or not, rests solely on how their joint distribution is structured, and not the content of the mappings they represent. One can distribute probability mass in $P(X, Y)$ in such a way that $P(X,Y) = P(X)P(Y)$, where $P(X)$ and $P(Y)$ are some well-defined probability distributions. 

Let $R(X,Y)$ be such a distribution, where $R(X,Y) = R(x)R(Y)$. Now, we would like to measure: 

$$D_{KL}(P(X,Y)||R(X,Y))$$

What does $R(X,Y)$ look like? Let's see if we can learn anything about $R(X,Y)$. 

We know that, one such $R(X,Y)$ is $R(X,Y) = P(X)P(Y)$, as we can prove it is a probability distribution over $X$ and $Y$. Let's expand the definition of KL-divergence, in the discrete case: 

$$D_{KL}(P(X,Y)||R(X,Y)) = \sum_{x \in \mathcal{X}} \sum_{y \in \mathcal{Y}} P(x,y)\log \frac{P(x,y)}{R(x,y)}$$

Now let's multiply and divide this by $P(x)P(y)$:

$$\sum_{x \in \mathcal{X}} \sum_{y \in \mathcal{Y}} P(x,y)\log \frac{P(x,y)(P(x)P(y))}{R(x,y)(P(x)P(y))}$$

with some algebraic manipulation, we get:


$$\sum_{x \in \mathcal{X}} \sum_{y \in \mathcal{Y}} P(x,y)\log \frac{P(x,y)}{P(x)P(y))} + \sum_{x \in \mathcal{X}} \sum_{y \in \mathcal{Y}} P(x,y)\log \frac{P(x)}{R(x,y)}$$

Which after further simplifications, gives us: 

$$D_{KL}(P(X,Y)||R(X,Y)) = D_{KL}(P(X,Y)||P(X)P(Y)) + D_{KL}(P(X)||R(X) + D_{KL}(P(Y)||R(Y)$$

In English, this means any distance between a distribution that is independent over $X$ and $Y$, will be composed of its distance from $P(X)P(Y)$, and the distance between marginals, and the marginals of the original distribution.


Of course, we would like our measure of independence, to be equal to zero, if the random variables are independent form each other. Putting this together, gives us this definition for Mutual Information: 

$$I(X;Y) = D_{KL}(P(X,Y)||P(X)P(Y))$$