$$
\nabla\times\mathbf{H}={\frac{\partial\mathbf{D}}{\partial t}}\\
\nabla\times\mathbf{E}=-{\frac{\partial\mathbf{B}}{\partial t}}
\\\nabla\cdot\mathbf{B} = 0
\\\nabla\cdot\mathbf{D}=0.
$$

### 电磁场的量子化

一维空腔中的电场 $x $ 分量做傅里叶展开：

$E_{x}(z,t)=\sum_{j}A_{j}q_{j}(t)\sin(k_{j}z)$

$k_{j} = j\pi/L, j =1,2,3..$，$A_{j}=\left(\frac{2\nu_{j}^{2}m_{j}}{V\epsilon_{0}}\right)^{1/2}$，$\nu_{j}=j\pi c/L$

由$\nabla\times\mathbf{H}={\frac{\partial\mathbf{D}}{\partial t}}$得到$H_{y}=\sum_{j}A_{j}\left({\frac{\dot{q}_{j}\epsilon_{0}}{k_{j}}}\right)\cos(k_{j}z)$

The classical Hamiltonian for the field is

$$
{\mathcal H}=\frac{1}{2}\int_{V}d\tau(\epsilon_{0}E_{x}^{2}+\mu_{0}H_{y}^{2})\\=\frac{1}{2}\sum_{j}(m_{j}\nu_{j}^{2}q_{j}^{2}+m_{j}\dot{q}_{j}^{2})=
\\{\frac{1}{2}}\sum_{j}\left(m_{j}v_{j}^{2}q_{j}^{2}+{\frac{p_{j}^{2}}{m_{j}}}\right)
$$
引入对易关系：

$$
\begin{array}{l}{{[q_{j},\,p_{j}]=i\hbar\delta_{j j^{\prime}},}}\\ {{[q_{j},\,q_{j^{\prime}}]=[p_{j},\,p_{j}]=0.}}\end{array}
$$


升降算符：
$$
a_{j}e^{-i\nu_{j}t}=\frac{1}{\sqrt{2m_{j}\hbar\nu_{j}}}(m_{j}\nu_{j}q_{j}+i p_{j})
\\a_{j}^{\dagger}e^{i v_{j}t}=\frac{1}{\sqrt{2m_{j}\hbar v_{j}}}(m_{j}\nu_{j}q_{j}-i p_{j})
$$
得到哈密顿量写法：

$$
\mathcal{H}=\hbar\sum_{j}\nu_{j}\left(a_{j}^{\dagger}a_{j}+\frac{1}{2}\right)
$$

其中升降算符满足：
$$
[a_{j},a_{j^{\prime}}{]}=\delta_{j j^{\prime}}
\\ {{{}[a_{j},a_{j^{\prime}}{]}={[a_{j}^{\dagger},a_{j^{\prime}}{]}}=0.}}
$$
则电场和磁场算符写为：
$$
E_{x}(z,t)=\sum_{j}\mathscr{E}_{j}(a_{j}e^{-i\nu_{j}t}+a_{j}^{\dagger}e^{i\nu_{j}t})\sin k_{j}z
\\
H_{y}(z,t)=-i\epsilon_{0}c\sum_{j}\mathscr{E}_{j}(a_{j}e^{-i\nu_{j}t}-a_{j}^{\dagger}e^{i\nu_{j}t})\cos k_{j}z
$$
where the quantity $\mathscr{E}_{j}=\left(\frac{\hbar\nu_{j}}{\epsilon_{0}V}\right)^{1/2}$，自由空间，k可以任意，且可以视作是空腔的箱极限：

$$
\mathbf{E}(\mathbf{r},t)=\sum_{\mathbf{k}}{\hat{\epsilon}}_{\mathbf{k}}{\mathscr{E}}_{\mathbf{k}}{\alpha}_{\mathbf{k}}{e^{-i\nu_{k}t+i\mathbf{k}\cdot\mathbf{r}}}+{\mathsf{c.c.}}
\\\mathrm{H}({\bf r},t)=\frac{1}{\mu_{0}}\sum_{\bf k}\frac{\bf k\times\hat{\epsilon_{k}}}{v_{k}}\mathscr{E}_{{\bf k}}{\bf x_{k}}e^{-i v_{k}t+i{\bf k\cdot r}}+\mathrm{c.c.},
$$
其中：$\mathscr{E}_{\mathrm{k}}=\left(\frac{\hbar\nu_{k}}{2\epsilon_{0}V}\right)^{1/2}$.其中 ${\mathbf{k}}\cdot{\hat{{\epsilon}}}_{{k}}=0$，易得模密度的表达式：
$$
D(\nu)d\nu=\frac{L^{3}\nu^{2}}{\pi^{2}c^{3}}d\nu,
$$
电场与磁场的对易关系，将电场磁场写为：
$$
{E}(\mathbf{r},t)=\sum_{\mathbf{k},\lambda}\hat{\epsilon}_{\mathbf{k}}^{(\lambda)}{\mathcal{E}}_{\mathbf{k}}a_{\mathbf{k},\lambda}e^{-i\nu_{k}t+i\mathbf{k}\cdot\mathbf{r}}+{H.c.},
\\
\mathrm{H}({\bf r},t)=\frac{1}{\mu_{0}}\sum_{{\bf k}\lambda}\frac{\mathrm{k}\times\hat{\epsilon}_{{\bf k}}^{(\lambda)}}{\nu_{k}}{\mathcal{E}_{{\bf k}}a_{{\bf k},\lambda}e^{-i\nu_{k}t+i k\cdot{\bf r}}+H.c.}
$$


其中 $\hat{\epsilon}_{\mathbf{k}}^{(\lambda)}$ 是偏振的方向，$\lambda$ 是两个偏振的序号。将其与对应方向点乘得到：
$$
[{E}_{x}({\bf r},t),{ H}_{y}({\bf r^{\prime}},t)]=\frac{\hbar c^{2}}{2V}\sum_{{\bf k},\lambda}\epsilon_{{\bf k}x}^{(\lambda)}\left[\epsilon_{{\bf k}x}^{(\lambda)}k_{z}-\epsilon_{{\bf k}z}^{(\lambda)}k_{x}\right]
\\\times\left[e^{i{\bf k}\cdot\left({\bf r-r^{\prime}}\right)}-e^{-i{\bf k}\cdot({\bf r-r^{\prime}})}\right],
$$
由偏振方向和波传播方向相互正交有：
$$
\hat{\epsilon}_{\bf k}^{(1)}\hat{\epsilon}_{\bf k}^{(1)}+\hat{\epsilon}_{\bf k}^{(2)}\hat{\epsilon}_{\bf k}^{(2)}+\frac{\bf k\bf k}{k^{2}}=1,
$$
进而：
$$
\epsilon_{\mathrm{ki}}^{(1)}\epsilon_{\mathrm{k}j}^{(1)}+\epsilon_{\mathrm{ki}}^{(2)}\epsilon_{\mathrm{kj}}^{(2)}=\delta_{i j}-\frac{k_{i}k_{j}}{k^{2}}
$$
$ij$ 为 $x,y,z$，于是对易关系进一步化简为：
$$
[{E}_{x}({\bf r},t),{ H}_{y}({\bf r^{\prime}},t)]=\frac{\hbar c^{2}}{2V}\sum_{{\bf k},\lambda}\epsilon_{{\bf k}x}^{(\lambda)}\left[\epsilon_{{\bf k}x}^{(\lambda)}k_{z}-\epsilon_{{\bf k}z}^{(\lambda)}k_{x}\right]
\\\times\left[e^{i{\bf k}\cdot\left({\bf r-r^{\prime}}\right)}-e^{-i{\bf k}\cdot({\bf r-r^{\prime}})}\right]
\\
=\frac{\hbar c^{2}}{2V}\sum_{\bf k}k_{z}\left[e^{i{\bf k}\cdot({\bf r}-{\bf r}^{\prime})}-e^{-i{\bf k}\cdot({\bf r}-{\bf r}^{\prime})}\right]
\\ =-i\hbar c^{2}\frac{\partial}{\partial z}\delta^{(3)}({\bf r}-\bf r^{\prime})
$$
 第四行来源于将离散求和极限化为积分：$\sum_{\bf k} \rightarrow\frac{V}{(2\pi)^{3}}\int d^{3}k.$

更广泛的：
$$
[E_{j}({\bf r},t),{ H}_{j}({\bf r^{\prime}},t)]=0\quad(j=x,y,z),
\\
[{ E}_{j}({\bf r},t),{ H}_{k}({\bf r}^{\prime},t)]=-i\hbar c^{2}\frac{\hat{\varrho}}{\partial\ell}\delta^{(3)}({\bf r}-{\bf r}^{\prime}),
$$
where $j, k$, and $l$ form a cyclic permutation of  $x,y,z$

### 兰姆位移

According to Dirac theory, the $2S_{1/2}$ and $2P_{1/2}$ levels should have equal energies. However, radiative corrections due to the interaction between the atomic electron and the vacuum, shift the  $2S_{1/2}$ level higher in energy by around 1057 MHz relative to the $2P_{1/2}$ level.

具体的计算很复杂，这里给了一种启发式的计算：

The effect of the fluctuations in the electric and magnetic fields associated with the vacuum is a perturbation of the electron in a hydrogen atom from the standard orbits of the Coulomb potential $-e^2/4\pi\epsilon_0r$ due to the proton; so the electron radius $r→r + \delta r$, where $\delta r$ is the fluctuation in the position of the electron due to the fluctuating fields. The change in potential energy,and thus the associated level shift, is given by 

$$
\begin{array}{l}{{\Delta V=\Delta x\frac{\partial V}{\partial x}+\Delta y\frac{\partial V}{\partial y}+\Delta z\frac{\partial V}{\partial z}}}\\ {{\qquad+\frac{1}{2}\,(\Delta x)^{2}\,\frac{\partial^{2}V}{\partial x^{2}}+\frac{1}{2}\,(\Delta y)^{2}\,\frac{\partial^{2}V}{\partial y^{2}}+\frac{1}{2}\,(\Delta z)^{2}\,\frac{\partial^{2}V}{\partial z^{2}}+\cdots}}\end{array}
$$

Since the fluctuations are isotropic  $$\langle\Delta x\rangle=\langle\Delta y\rangle=\langle\Delta z\rangle=0$$  and $$((\Delta x)^{2})=\langle(\Delta y)^{2}\rangle=\langle(\Delta z)^{2}\rangle=\langle(\Delta r)^{2}\rangle/3$$ . Then
$$
\langle\Delta{ V}\rangle={\frac{1}{6}}\langle(\delta r)^{2}\rangle\nabla^{2}{ V}
$$


For the 2S state of hydrogen

$$
\begin{array}{l l}{{\left<\nabla^{2}\left({\frac{-e^{2}}{4\pi\epsilon_{0}r}}\right)\right>_{\mathrm{at}}={\frac{-e^{2}}{4\pi\epsilon_{0}}}\int d{\bf r}\psi_{2s}^{*}({\bf r})\nabla^{2}\left({\frac{1}{r}}\right)\psi_{2s}({\bf r})}}\\ {{={\frac{e^{2}}{\epsilon_{0}}}|\psi_{2s}(0)|^{2}}} {{={\frac{e^{2}}{8\pi\epsilon_{0}a_{0}^{3}}}}}\end{array}
$$
而P轨道在0处波函数为0，所以没有能级偏移。

空气中的${\left|0\right>,k}$ 波模与电子发生相互作用，假设其振动速度远远大于电子的波尔转动速度的话可以简单描述以相同的频率发生振动：$\delta r(t)\cong\delta r(0)e^{-i v t}+c.c.$ 带入牛顿运动定律，We thus have: $(\delta r)_{\mathrm{k}}\cong\frac{e}{m c^{2}k^{2}}E_{\mathrm{k}},$ 
$$
\begin{array}{r l}{\langle(\delta {r})^{2}\rangle_{\mathrm{vac}}=\sum_{\mathbf{k}}\left({\frac{e}{m c^{2}k^{2}}}\right)^{2}\langle0|(E_{\mathbf{k}})^{2}|0\rangle}\\ {=\sum_{\mathbf{k}}\left({\frac{e}{m c^{2}k^{2}}}\right)^{2}\left({\frac{\hbar c k}{2\epsilon_{0}V}}\right),}\end{array}
$$
这种近似在$k>\pi/a_0$时有效，这时振动比绕核旋转快，同时也要在相对论极限下，$k<mc/\hbar$，这样才能让最后结果收敛（反正是估算），最后得到lamb位移表达式：
$$
\langle\Delta V\rangle=\frac{4}{3}\frac{e^{2}}{4\pi\epsilon_{0}}\frac{e^{2}}{4\pi\epsilon_{0}\hbar c}\left(\frac{\hbar}{m c}\right)^{2}\frac{1}{8\pi a_{0}^{3}}\ln\left(\frac{4\epsilon_{0}\hbar c}{e^{2}}\right)
$$






