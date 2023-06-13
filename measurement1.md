---
title: 测量理论1
date: 2023-03-27 15:42:23
tags: 量子力学, quantum mechanics, quantum measurement
categories: 量子测量
---

# 经典测量理论

一个物理学量用 $x$ 表示（可以是离散的，也可以是连续的，一维或者多维都行），在测量前并不知道其具体的取值，但是知道其取值范围，并且由于经验或者别的信息，知道他在每个取值上的概率分布 $P(x)$（先验概率分布 或者 state-of-knowledge）。

假设似然函数（likelihood function）已知，其定义为：$P(y|x)$，在 $x$ 给定的条件下，$y$ 被测得的概率。

在单次测量中，我们得到一次测量结果$y_0$，根据测量结果对我们的 state-of-knowledge 进行更新，这个过程叫做完成了一次测量。

由贝叶斯定理：

\begin{equation}
\begin{aligned}
P(x|y_0) = \frac{P(xy_0)}{P(y_0)} = \frac{P(y_0|x)P(x)}{\sum_x P(y_0|x)P(x)}
\end{aligned}
\end{equation}

等式右边 $P(x)$ 代表测量前我们对参量 $x$ 的知识（state-of-knowledge），$P(y_0|x)$则是似然函数，测量发生后，根据测量结果我们将知识更新为 $P(x|y_0)$。

任意 $N$ 次测量，彼此之间都是无关，$x$ 的概率分布可以写为：

\begin{equation}
\begin{aligned}
P(x|y_1,y_2,..y_N) &= \frac{P(y_N|x,y_1,y_2,...y_{N-1})P(x|y_1,y_2,...y_{N-1})}{\mathcal{N_{y_i}}}
\\\\ &=  \frac{P(y_N|x,...)P(y_{N-1}|x,...)...P(y_{1}|x)P(x)}{\Pi_i \mathcal{N}_i }
\end{aligned}
\end{equation}

其中

<div>$\mathcal{N}_{i} = \sum_x P(y_i|x,...)P(x|y_1,y_2,...y_{i-1})$ </div>

原式化简为：

\begin{equation}
\begin{aligned}
P(x|y_1,y_2,..y_N) &= \Pi_i \frac{P(y_i|x,y_1,y_2,...y_{i-1})}{\sum_x P(y_i|x,y_1,y_2,...y_{i-1})P(x|y_1,y_2,...y_{i-1})}
\\\\ & = \Pi_i \frac{P(y_i|x)}{\sum_x P(y_i|x)P(x|y_1,y_2,...y_{i-1})} P(x)
\end{aligned}
\end{equation}

其中，变量相互之间无关，意味着每次测量后似然关系没有改变既$P(y_i|x,y_1,y_2,...y_{i-1}) = P(y_i|x)$，也就是测量并没有改变物理量的大小(当然我觉得弱关联近似成立也是有可能的)。

实际上下方的归一化系数不太重要，重要的是分母上方的乘积，可以直接相乘之后再做归一化。

在实际测量中，往往由于测量误差是由多个相互独立的随机变量造成的影响，所以 $P(y|x)$ 似然函数往往为gauss型函数。同样，在经过多次测量后，任意给定一个物理量的取值$x_0$，想求该物理量取值为$x_0$的概率可以写为：

\begin{equation}
\begin{aligned}
P(x_0|y_1,y_2,..y_N) &= P(y_1|x_0)P(y_2|x_0)P(y_3|x_0)... P(x_0)/N
\\\\ &= \mathscr{F}^{-1}(\tilde P(w_1) * \tilde P(w_2)... \tilde P(w_N)) P(x_0)/N
\end{aligned}
\end{equation}

其中 $\tilde P(w)$ 为概率 $P(y|x_0)$ 关于 $y$ 的傅里叶变换，内部代表对其卷积，<mark>假设 $\tilde P(w)$ 为方差有限且在无穷上可积的函数</mark>，则可以将其归一化后看作是 $w$ 上的一个概率分布，再根据

\begin{equation}
\begin{aligned}
P(x+y) = P(x) *P(y)
\end{aligned}
\end{equation}

可知，$P(x_0|y_1,y_2,..y_N)  =  \mathscr{F}^{-1}(C\tilde P(w_1+w_2+w_3...w_n)) $，再由中心极限定理可知，$C\tilde P(w_1+w_2+w_3...w_n)$ 满足gauss分布，所以其傅里叶变换也是gauss分布。

在绝大多数情况下，对物理量的初始知识并不重要，不会影响到最终结果，但不是绝对的，为了避免 prior states-of-knowledge 对测量产生影响，需要选定特殊的先验知识来表达对物理量 “一无所知”，同时得考虑到测量的鲁棒性，也就是一些outliers不能对测量结果产生巨大的影响，得选用一些特殊的先验知识，具体的参看[书 part2 chapter21](https://www.cambridge.org/cn/academic/subjects/physics/theoretical-physics-and-mathematical-physics/probability-theory-logic-science?format=HB&isbn=9780521592710)



# 一次经典的长度测量

对一把长度为20的尺子进行测量，对恒为正数且完全无知的测量值prior知识的写法最好写为 $p(x) = a/x$，其中 $a$ 为某个任意常数，由于肉眼和仪器导致误差呈现高斯分布，假设其$\sigma = 0.5$，对应的like-hood关系也是高斯的 $\sigma = 0.5$ 的函数。

```python
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig,ax = plt.subplots(figsize=(1*12,1*9),facecolor='white',edgecolor='white')

# 测量的参数
N = 300 #测量的次数
sigma = 0.5 #like-hood 呈高斯型，其方差
x0 = 20 #尺子的长度
errors = np.random.normal(mu, sigma, N)
measures  = x0+errors #测量结果

#作图

x = np.linspace(19,21,20000)
state_of_knowledge = [100/i for i in x] #图像上只呈现19-21的变化
    
def init():
    global state_of_knowledge
    state_of_knowledge = state_of_knowledge/sum(state_of_knowledge)
    ax.axvline(x0, linestyle='--', color='black')
    line, = ax.plot(x,state_of_knowledge)
    return line

def update(measurement_value): #一个frame代表一次测量
    global state_of_knowledge
    ax.clear()
    ax.axvline(x0, linestyle='--', color='black')
    state_of_knowledge = [state_of_knowledge[i]*np.exp(-(x[i]-20)**2/2/sigma**2) for i in range(20000)]
    state_of_knowledge = state_of_knowledge/sum(state_of_knowledge)
    line, = ax.plot(x,state_of_knowledge)
    return line

anim = FuncAnimation(fig,update,frames=measures,interval=30,init_func = init) #每一秒完成30次测量
anim.save("measure.gif")
```

<img src="measure.gif" width="80%">









