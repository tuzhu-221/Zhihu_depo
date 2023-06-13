
<img src="https://www.zhihu.com/equation?tex=\nabla\times\mathbf{H}={\frac{\partial\mathbf{D}}{\partial t}}\\
\nabla\times\mathbf{E}=-{\frac{\partial\mathbf{B}}{\partial t}}
\\\nabla\cdot\mathbf{B} = 0
\\\nabla\cdot\mathbf{D}=0.
" alt="\nabla\times\mathbf{H}={\frac{\partial\mathbf{D}}{\partial t}}\\
\nabla\times\mathbf{E}=-{\frac{\partial\mathbf{B}}{\partial t}}
\\\nabla\cdot\mathbf{B} = 0
\\\nabla\cdot\mathbf{D}=0.
" class="ee_img tr_noresize" eeimg="1">

### 电磁场的量子化

一维空腔中的电场  <img src="https://www.zhihu.com/equation?tex=x " alt="x " class="ee_img tr_noresize" eeimg="1">  分量做傅里叶展开：

 <img src="https://www.zhihu.com/equation?tex=E_{x}(z,t)=\sum_{j}A_{j}q_{j}(t)\sin(k_{j}z)" alt="E_{x}(z,t)=\sum_{j}A_{j}q_{j}(t)\sin(k_{j}z)" class="ee_img tr_noresize" eeimg="1"> 

 <img src="https://www.zhihu.com/equation?tex=k_{j} = j\pi/L, j =1,2,3.." alt="k_{j} = j\pi/L, j =1,2,3.." class="ee_img tr_noresize" eeimg="1"> ， <img src="https://www.zhihu.com/equation?tex=A_{j}=\left(\frac{2\nu_{j}^{2}m_{j}}{V\epsilon_{0}}\right)^{1/2}" alt="A_{j}=\left(\frac{2\nu_{j}^{2}m_{j}}{V\epsilon_{0}}\right)^{1/2}" class="ee_img tr_noresize" eeimg="1"> ， <img src="https://www.zhihu.com/equation?tex=\nu_{j}=j\pi c/L" alt="\nu_{j}=j\pi c/L" class="ee_img tr_noresize" eeimg="1"> 

由 <img src="https://www.zhihu.com/equation?tex=\nabla\times\mathbf{H}={\frac{\partial\mathbf{D}}{\partial t}}" alt="\nabla\times\mathbf{H}={\frac{\partial\mathbf{D}}{\partial t}}" class="ee_img tr_noresize" eeimg="1"> 得到 <img src="https://www.zhihu.com/equation?tex=H_{y}=\sum_{j}A_{j}\left({\frac{\dot{q}_{j}\epsilon_{0}}{k_{j}}}\right)\cos(k_{j}z)" alt="H_{y}=\sum_{j}A_{j}\left({\frac{\dot{q}_{j}\epsilon_{0}}{k_{j}}}\right)\cos(k_{j}z)" class="ee_img tr_noresize" eeimg="1"> 

The classical Hamiltonian for the field is


<img src="https://www.zhihu.com/equation?tex={\mathcal H}=\frac{1}{2}\int_{V}d\tau(\epsilon_{0}E_{x}^{2}+\mu_{0}H_{y}^{2})\\=\frac{1}{2}\sum_{j}(m_{j}\nu_{j}^{2}q_{j}^{2}+m_{j}\dot{q}_{j}^{2})=
\\{\frac{1}{2}}\sum_{j}\left(m_{j}v_{j}^{2}q_{j}^{2}+{\frac{p_{j}^{2}}{m_{j}}}\right)
" alt="{\mathcal H}=\frac{1}{2}\int_{V}d\tau(\epsilon_{0}E_{x}^{2}+\mu_{0}H_{y}^{2})\\=\frac{1}{2}\sum_{j}(m_{j}\nu_{j}^{2}q_{j}^{2}+m_{j}\dot{q}_{j}^{2})=
\\{\frac{1}{2}}\sum_{j}\left(m_{j}v_{j}^{2}q_{j}^{2}+{\frac{p_{j}^{2}}{m_{j}}}\right)
" class="ee_img tr_noresize" eeimg="1">
引入对易关系：


<img src="https://www.zhihu.com/equation?tex=\begin{array}{l}{{[q_{j},\,p_{j}]=i\hbar\delta_{j j^{\prime}},}}\\ {{[q_{j},\,q_{j^{\prime}}]=[p_{j},\,p_{j}]=0.}}\end{array}
" alt="\begin{array}{l}{{[q_{j},\,p_{j}]=i\hbar\delta_{j j^{\prime}},}}\\ {{[q_{j},\,q_{j^{\prime}}]=[p_{j},\,p_{j}]=0.}}\end{array}
" class="ee_img tr_noresize" eeimg="1">


升降算符：

<img src="https://www.zhihu.com/equation?tex=a_{j}e^{-i\nu_{j}t}=\frac{1}{\sqrt{2m_{j}\hbar\nu_{j}}}(m_{j}\nu_{j}q_{j}+i p_{j})
\\a_{j}^{\dagger}e^{i v_{j}t}=\frac{1}{\sqrt{2m_{j}\hbar v_{j}}}(m_{j}\nu_{j}q_{j}-i p_{j})
" alt="a_{j}e^{-i\nu_{j}t}=\frac{1}{\sqrt{2m_{j}\hbar\nu_{j}}}(m_{j}\nu_{j}q_{j}+i p_{j})
\\a_{j}^{\dagger}e^{i v_{j}t}=\frac{1}{\sqrt{2m_{j}\hbar v_{j}}}(m_{j}\nu_{j}q_{j}-i p_{j})
" class="ee_img tr_noresize" eeimg="1">
得到哈密顿量写法：


<img src="https://www.zhihu.com/equation?tex=\mathcal{H}=\hbar\sum_{j}\nu_{j}\left(a_{j}^{\dagger}a_{j}+\frac{1}{2}\right)
" alt="\mathcal{H}=\hbar\sum_{j}\nu_{j}\left(a_{j}^{\dagger}a_{j}+\frac{1}{2}\right)
" class="ee_img tr_noresize" eeimg="1">

其中升降算符满足：

<img src="https://www.zhihu.com/equation?tex=[a_{j},a_{j^{\prime}}{]}=\delta_{j j^{\prime}}
\\ {{{}[a_{j},a_{j^{\prime}}{]}={[a_{j}^{\dagger},a_{j^{\prime}}{]}}=0.}}
" alt="[a_{j},a_{j^{\prime}}{]}=\delta_{j j^{\prime}}
\\ {{{}[a_{j},a_{j^{\prime}}{]}={[a_{j}^{\dagger},a_{j^{\prime}}{]}}=0.}}
" class="ee_img tr_noresize" eeimg="1">
则电场和磁场算符写为：

<img src="https://www.zhihu.com/equation?tex=E_{x}(z,t)=\sum_{j}\mathscr{E}_{j}(a_{j}e^{-i\nu_{j}t}+a_{j}^{\dagger}e^{i\nu_{j}t})\sin k_{j}z
\\
H_{y}(z,t)=-i\epsilon_{0}c\sum_{j}\mathscr{E}_{j}(a_{j}e^{-i\nu_{j}t}-a_{j}^{\dagger}e^{i\nu_{j}t})\cos k_{j}z
" alt="E_{x}(z,t)=\sum_{j}\mathscr{E}_{j}(a_{j}e^{-i\nu_{j}t}+a_{j}^{\dagger}e^{i\nu_{j}t})\sin k_{j}z
\\
H_{y}(z,t)=-i\epsilon_{0}c\sum_{j}\mathscr{E}_{j}(a_{j}e^{-i\nu_{j}t}-a_{j}^{\dagger}e^{i\nu_{j}t})\cos k_{j}z
" class="ee_img tr_noresize" eeimg="1">
where the quantity  <img src="https://www.zhihu.com/equation?tex=\mathscr{E}_{j}=\left(\frac{\hbar\nu_{j}}{\epsilon_{0}V}\right)^{1/2}" alt="\mathscr{E}_{j}=\left(\frac{\hbar\nu_{j}}{\epsilon_{0}V}\right)^{1/2}" class="ee_img tr_noresize" eeimg="1"> ，自由空间，k可以任意，且可以视作是空腔的箱极限：


<img src="https://www.zhihu.com/equation?tex=\mathbf{E}(\mathbf{r},t)=\sum_{\mathbf{k}}{\hat{\epsilon}}_{\mathbf{k}}{\mathscr{E}}_{\mathbf{k}}{\alpha}_{\mathbf{k}}{e^{-i\nu_{k}t+i\mathbf{k}\cdot\mathbf{r}}}+{\mathsf{c.c.}}
\\\mathrm{H}({\bf r},t)=\frac{1}{\mu_{0}}\sum_{\bf k}\frac{\bf k\times\hat{\epsilon_{k}}}{v_{k}}\mathscr{E}_{{\bf k}}{\bf x_{k}}e^{-i v_{k}t+i{\bf k\cdot r}}+\mathrm{c.c.},
" alt="\mathbf{E}(\mathbf{r},t)=\sum_{\mathbf{k}}{\hat{\epsilon}}_{\mathbf{k}}{\mathscr{E}}_{\mathbf{k}}{\alpha}_{\mathbf{k}}{e^{-i\nu_{k}t+i\mathbf{k}\cdot\mathbf{r}}}+{\mathsf{c.c.}}
\\\mathrm{H}({\bf r},t)=\frac{1}{\mu_{0}}\sum_{\bf k}\frac{\bf k\times\hat{\epsilon_{k}}}{v_{k}}\mathscr{E}_{{\bf k}}{\bf x_{k}}e^{-i v_{k}t+i{\bf k\cdot r}}+\mathrm{c.c.},
" class="ee_img tr_noresize" eeimg="1">
其中： <img src="https://www.zhihu.com/equation?tex=\mathscr{E}_{\mathrm{k}}=\left(\frac{\hbar\nu_{k}}{2\epsilon_{0}V}\right)^{1/2}" alt="\mathscr{E}_{\mathrm{k}}=\left(\frac{\hbar\nu_{k}}{2\epsilon_{0}V}\right)^{1/2}" class="ee_img tr_noresize" eeimg="1"> .其中  <img src="https://www.zhihu.com/equation?tex={\mathbf{k}}\cdot{\hat{{\epsilon}}}_{{k}}=0" alt="{\mathbf{k}}\cdot{\hat{{\epsilon}}}_{{k}}=0" class="ee_img tr_noresize" eeimg="1"> ，易得模密度的表达式：

<img src="https://www.zhihu.com/equation?tex=D(\nu)d\nu=\frac{L^{3}\nu^{2}}{\pi^{2}c^{3}}d\nu,
" alt="D(\nu)d\nu=\frac{L^{3}\nu^{2}}{\pi^{2}c^{3}}d\nu,
" class="ee_img tr_noresize" eeimg="1">
电场与磁场的对易关系，将电场磁场写为：

<img src="https://www.zhihu.com/equation?tex={E}(\mathbf{r},t)=\sum_{\mathbf{k},\lambda}\hat{\epsilon}_{\mathbf{k}}^{(\lambda)}{\mathcal{E}}_{\mathbf{k}}a_{\mathbf{k},\lambda}e^{-i\nu_{k}t+i\mathbf{k}\cdot\mathbf{r}}+{H.c.},
\\
\mathrm{H}({\bf r},t)=\frac{1}{\mu_{0}}\sum_{{\bf k}\lambda}\frac{\mathrm{k}\times\hat{\epsilon}_{{\bf k}}^{(\lambda)}}{\nu_{k}}{\mathcal{E}_{{\bf k}}a_{{\bf k},\lambda}e^{-i\nu_{k}t+i k\cdot{\bf r}}+H.c.}
" alt="{E}(\mathbf{r},t)=\sum_{\mathbf{k},\lambda}\hat{\epsilon}_{\mathbf{k}}^{(\lambda)}{\mathcal{E}}_{\mathbf{k}}a_{\mathbf{k},\lambda}e^{-i\nu_{k}t+i\mathbf{k}\cdot\mathbf{r}}+{H.c.},
\\
\mathrm{H}({\bf r},t)=\frac{1}{\mu_{0}}\sum_{{\bf k}\lambda}\frac{\mathrm{k}\times\hat{\epsilon}_{{\bf k}}^{(\lambda)}}{\nu_{k}}{\mathcal{E}_{{\bf k}}a_{{\bf k},\lambda}e^{-i\nu_{k}t+i k\cdot{\bf r}}+H.c.}
" class="ee_img tr_noresize" eeimg="1">


其中  <img src="https://www.zhihu.com/equation?tex=\hat{\epsilon}_{\mathbf{k}}^{(\lambda)}" alt="\hat{\epsilon}_{\mathbf{k}}^{(\lambda)}" class="ee_img tr_noresize" eeimg="1">  是偏振的方向， <img src="https://www.zhihu.com/equation?tex=\lambda" alt="\lambda" class="ee_img tr_noresize" eeimg="1">  是两个偏振的序号。将其与对应方向点乘得到：

<img src="https://www.zhihu.com/equation?tex=[{E}_{x}({\bf r},t),{ H}_{y}({\bf r^{\prime}},t)]=\frac{\hbar c^{2}}{2V}\sum_{{\bf k},\lambda}\epsilon_{{\bf k}x}^{(\lambda)}\left[\epsilon_{{\bf k}x}^{(\lambda)}k_{z}-\epsilon_{{\bf k}z}^{(\lambda)}k_{x}\right]
\\\times\left[e^{i{\bf k}\cdot\left({\bf r-r^{\prime}}\right)}-e^{-i{\bf k}\cdot({\bf r-r^{\prime}})}\right],
" alt="[{E}_{x}({\bf r},t),{ H}_{y}({\bf r^{\prime}},t)]=\frac{\hbar c^{2}}{2V}\sum_{{\bf k},\lambda}\epsilon_{{\bf k}x}^{(\lambda)}\left[\epsilon_{{\bf k}x}^{(\lambda)}k_{z}-\epsilon_{{\bf k}z}^{(\lambda)}k_{x}\right]
\\\times\left[e^{i{\bf k}\cdot\left({\bf r-r^{\prime}}\right)}-e^{-i{\bf k}\cdot({\bf r-r^{\prime}})}\right],
" class="ee_img tr_noresize" eeimg="1">
由偏振方向和波传播方向相互正交有：

<img src="https://www.zhihu.com/equation?tex=\hat{\epsilon}_{\bf k}^{(1)}\hat{\epsilon}_{\bf k}^{(1)}+\hat{\epsilon}_{\bf k}^{(2)}\hat{\epsilon}_{\bf k}^{(2)}+\frac{\bf k\bf k}{k^{2}}=1,
" alt="\hat{\epsilon}_{\bf k}^{(1)}\hat{\epsilon}_{\bf k}^{(1)}+\hat{\epsilon}_{\bf k}^{(2)}\hat{\epsilon}_{\bf k}^{(2)}+\frac{\bf k\bf k}{k^{2}}=1,
" class="ee_img tr_noresize" eeimg="1">
进而：

<img src="https://www.zhihu.com/equation?tex=\epsilon_{\mathrm{ki}}^{(1)}\epsilon_{\mathrm{k}j}^{(1)}+\epsilon_{\mathrm{ki}}^{(2)}\epsilon_{\mathrm{kj}}^{(2)}=\delta_{i j}-\frac{k_{i}k_{j}}{k^{2}}
" alt="\epsilon_{\mathrm{ki}}^{(1)}\epsilon_{\mathrm{k}j}^{(1)}+\epsilon_{\mathrm{ki}}^{(2)}\epsilon_{\mathrm{kj}}^{(2)}=\delta_{i j}-\frac{k_{i}k_{j}}{k^{2}}
" class="ee_img tr_noresize" eeimg="1">
 <img src="https://www.zhihu.com/equation?tex=ij" alt="ij" class="ee_img tr_noresize" eeimg="1">  为  <img src="https://www.zhihu.com/equation?tex=x,y,z" alt="x,y,z" class="ee_img tr_noresize" eeimg="1"> ，于是对易关系进一步化简为：

<img src="https://www.zhihu.com/equation?tex=[{E}_{x}({\bf r},t),{ H}_{y}({\bf r^{\prime}},t)]=\frac{\hbar c^{2}}{2V}\sum_{{\bf k},\lambda}\epsilon_{{\bf k}x}^{(\lambda)}\left[\epsilon_{{\bf k}x}^{(\lambda)}k_{z}-\epsilon_{{\bf k}z}^{(\lambda)}k_{x}\right]
\\\times\left[e^{i{\bf k}\cdot\left({\bf r-r^{\prime}}\right)}-e^{-i{\bf k}\cdot({\bf r-r^{\prime}})}\right]
\\
=\frac{\hbar c^{2}}{2V}\sum_{\bf k}k_{z}\left[e^{i{\bf k}\cdot({\bf r}-{\bf r}^{\prime})}-e^{-i{\bf k}\cdot({\bf r}-{\bf r}^{\prime})}\right]
\\ =-i\hbar c^{2}\frac{\partial}{\partial z}\delta^{(3)}({\bf r}-\bf r^{\prime})
" alt="[{E}_{x}({\bf r},t),{ H}_{y}({\bf r^{\prime}},t)]=\frac{\hbar c^{2}}{2V}\sum_{{\bf k},\lambda}\epsilon_{{\bf k}x}^{(\lambda)}\left[\epsilon_{{\bf k}x}^{(\lambda)}k_{z}-\epsilon_{{\bf k}z}^{(\lambda)}k_{x}\right]
\\\times\left[e^{i{\bf k}\cdot\left({\bf r-r^{\prime}}\right)}-e^{-i{\bf k}\cdot({\bf r-r^{\prime}})}\right]
\\
=\frac{\hbar c^{2}}{2V}\sum_{\bf k}k_{z}\left[e^{i{\bf k}\cdot({\bf r}-{\bf r}^{\prime})}-e^{-i{\bf k}\cdot({\bf r}-{\bf r}^{\prime})}\right]
\\ =-i\hbar c^{2}\frac{\partial}{\partial z}\delta^{(3)}({\bf r}-\bf r^{\prime})
" class="ee_img tr_noresize" eeimg="1">
 第四行来源于将离散求和极限化为积分： <img src="https://www.zhihu.com/equation?tex=\sum_{\bf k} \rightarrow\frac{V}{(2\pi)^{3}}\int d^{3}k." alt="\sum_{\bf k} \rightarrow\frac{V}{(2\pi)^{3}}\int d^{3}k." class="ee_img tr_noresize" eeimg="1"> 

更广泛的：

<img src="https://www.zhihu.com/equation?tex=[E_{j}({\bf r},t),{ H}_{j}({\bf r^{\prime}},t)]=0\quad(j=x,y,z),
\\
[{ E}_{j}({\bf r},t),{ H}_{k}({\bf r}^{\prime},t)]=-i\hbar c^{2}\frac{\hat{\varrho}}{\partial\ell}\delta^{(3)}({\bf r}-{\bf r}^{\prime}),
" alt="[E_{j}({\bf r},t),{ H}_{j}({\bf r^{\prime}},t)]=0\quad(j=x,y,z),
\\
[{ E}_{j}({\bf r},t),{ H}_{k}({\bf r}^{\prime},t)]=-i\hbar c^{2}\frac{\hat{\varrho}}{\partial\ell}\delta^{(3)}({\bf r}-{\bf r}^{\prime}),
" class="ee_img tr_noresize" eeimg="1">
where  <img src="https://www.zhihu.com/equation?tex=j, k" alt="j, k" class="ee_img tr_noresize" eeimg="1"> , and  <img src="https://www.zhihu.com/equation?tex=l" alt="l" class="ee_img tr_noresize" eeimg="1">  form a cyclic permutation of   <img src="https://www.zhihu.com/equation?tex=x,y,z" alt="x,y,z" class="ee_img tr_noresize" eeimg="1"> 

### 兰姆位移

According to Dirac theory, the  <img src="https://www.zhihu.com/equation?tex=2S_{1/2}" alt="2S_{1/2}" class="ee_img tr_noresize" eeimg="1">  and  <img src="https://www.zhihu.com/equation?tex=2P_{1/2}" alt="2P_{1/2}" class="ee_img tr_noresize" eeimg="1">  levels should have equal energies. However, radiative corrections due to the interaction between the atomic electron and the vacuum, shift the   <img src="https://www.zhihu.com/equation?tex=2S_{1/2}" alt="2S_{1/2}" class="ee_img tr_noresize" eeimg="1">  level higher in energy by around 1057 MHz relative to the  <img src="https://www.zhihu.com/equation?tex=2P_{1/2}" alt="2P_{1/2}" class="ee_img tr_noresize" eeimg="1">  level.

具体的计算很复杂，这里给了一种启发式的计算：

The effect of the fluctuations in the electric and magnetic fields associated with the vacuum is a perturbation of the electron in a hydrogen atom from the standard orbits of the Coulomb potential  <img src="https://www.zhihu.com/equation?tex=-e^2/4\pi\epsilon_0r" alt="-e^2/4\pi\epsilon_0r" class="ee_img tr_noresize" eeimg="1">  due to the proton; so the electron radius  <img src="https://www.zhihu.com/equation?tex=r→r + \delta r" alt="r→r + \delta r" class="ee_img tr_noresize" eeimg="1"> , where  <img src="https://www.zhihu.com/equation?tex=\delta r" alt="\delta r" class="ee_img tr_noresize" eeimg="1">  is the fluctuation in the position of the electron due to the fluctuating fields. The change in potential energy,and thus the associated level shift, is given by 


<img src="https://www.zhihu.com/equation?tex=\begin{array}{l}{{\Delta V=\Delta x\frac{\partial V}{\partial x}+\Delta y\frac{\partial V}{\partial y}+\Delta z\frac{\partial V}{\partial z}}}\\ {{\qquad+\frac{1}{2}\,(\Delta x)^{2}\,\frac{\partial^{2}V}{\partial x^{2}}+\frac{1}{2}\,(\Delta y)^{2}\,\frac{\partial^{2}V}{\partial y^{2}}+\frac{1}{2}\,(\Delta z)^{2}\,\frac{\partial^{2}V}{\partial z^{2}}+\cdots}}\end{array}
" alt="\begin{array}{l}{{\Delta V=\Delta x\frac{\partial V}{\partial x}+\Delta y\frac{\partial V}{\partial y}+\Delta z\frac{\partial V}{\partial z}}}\\ {{\qquad+\frac{1}{2}\,(\Delta x)^{2}\,\frac{\partial^{2}V}{\partial x^{2}}+\frac{1}{2}\,(\Delta y)^{2}\,\frac{\partial^{2}V}{\partial y^{2}}+\frac{1}{2}\,(\Delta z)^{2}\,\frac{\partial^{2}V}{\partial z^{2}}+\cdots}}\end{array}
" class="ee_img tr_noresize" eeimg="1">


<img src="https://www.zhihu.com/equation?tex=\langle\Delta x\rangle=\langle\Delta y\rangle=\langle\Delta z\rangle=0$ <img src="https://www.zhihu.com/equation?tex=  and " alt="  and " class="ee_img tr_noresize" eeimg="1">  <img src="https://www.zhihu.com/equation?tex=((\Delta x)^{2})=\langle(\Delta y)^{2}\rangle=\langle(\Delta z)^{2}\rangle=\langle(\Delta r)^{2}\rangle/3" alt="((\Delta x)^{2})=\langle(\Delta y)^{2}\rangle=\langle(\Delta z)^{2}\rangle=\langle(\Delta r)^{2}\rangle/3" class="ee_img tr_noresize" eeimg="1"> $ . Then
" alt="\langle\Delta x\rangle=\langle\Delta y\rangle=\langle\Delta z\rangle=0$ <img src="https://www.zhihu.com/equation?tex=  and " alt="  and " class="ee_img tr_noresize" eeimg="1">  <img src="https://www.zhihu.com/equation?tex=((\Delta x)^{2})=\langle(\Delta y)^{2}\rangle=\langle(\Delta z)^{2}\rangle=\langle(\Delta r)^{2}\rangle/3" alt="((\Delta x)^{2})=\langle(\Delta y)^{2}\rangle=\langle(\Delta z)^{2}\rangle=\langle(\Delta r)^{2}\rangle/3" class="ee_img tr_noresize" eeimg="1"> $ . Then
" class="ee_img tr_noresize" eeimg="1">
\langle\Delta{ V}\rangle={\frac{1}{6}}\langle(\delta r)^{2}\rangle\nabla^{2}{ V}

<img src="https://www.zhihu.com/equation?tex=For the 2S state of hydrogen

" alt="For the 2S state of hydrogen

" class="ee_img tr_noresize" eeimg="1">
\begin{array}{l l}{{\left<\nabla^{2}\left({\frac{-e^{2}}{4\pi\epsilon_{0}r}}\right)\right>_{\mathrm{at}}={\frac{-e^{2}}{4\pi\epsilon_{0}}}\int d{\bf r}\psi_{2s}^{*}({\bf r})\nabla^{2}\left({\frac{1}{r}}\right)\psi_{2s}({\bf r})}}\\ {{={\frac{e^{2}}{\epsilon_{0}}}|\psi_{2s}(0)|^{2}}} {{={\frac{e^{2}}{8\pi\epsilon_{0}a_{0}^{3}}}}}\end{array}

<img src="https://www.zhihu.com/equation?tex=而P轨道在0处波函数为0，所以没有能级偏移。

空气中的 <img src="https://www.zhihu.com/equation?tex={\left|0\right>,k}" alt="{\left|0\right>,k}" class="ee_img tr_noresize" eeimg="1">  波模与电子发生相互作用，假设其振动速度远远大于电子的波尔转动速度的话可以简单描述以相同的频率发生振动： <img src="https://www.zhihu.com/equation?tex=\delta r(t)\cong\delta r(0)e^{-i v t}+c.c." alt="\delta r(t)\cong\delta r(0)e^{-i v t}+c.c." class="ee_img tr_noresize" eeimg="1">  带入牛顿运动定律，We thus have:  <img src="https://www.zhihu.com/equation?tex=(\delta r)_{\mathrm{k}}\cong\frac{e}{m c^{2}k^{2}}E_{\mathrm{k}}," alt="(\delta r)_{\mathrm{k}}\cong\frac{e}{m c^{2}k^{2}}E_{\mathrm{k}}," class="ee_img tr_noresize" eeimg="1">  
" alt="而P轨道在0处波函数为0，所以没有能级偏移。

空气中的 <img src="https://www.zhihu.com/equation?tex={\left|0\right>,k}" alt="{\left|0\right>,k}" class="ee_img tr_noresize" eeimg="1">  波模与电子发生相互作用，假设其振动速度远远大于电子的波尔转动速度的话可以简单描述以相同的频率发生振动： <img src="https://www.zhihu.com/equation?tex=\delta r(t)\cong\delta r(0)e^{-i v t}+c.c." alt="\delta r(t)\cong\delta r(0)e^{-i v t}+c.c." class="ee_img tr_noresize" eeimg="1">  带入牛顿运动定律，We thus have:  <img src="https://www.zhihu.com/equation?tex=(\delta r)_{\mathrm{k}}\cong\frac{e}{m c^{2}k^{2}}E_{\mathrm{k}}," alt="(\delta r)_{\mathrm{k}}\cong\frac{e}{m c^{2}k^{2}}E_{\mathrm{k}}," class="ee_img tr_noresize" eeimg="1">  
" class="ee_img tr_noresize" eeimg="1">
\begin{array}{r l}{\langle(\delta {r})^{2}\rangle_{\mathrm{vac}}=\sum_{\mathbf{k}}\left({\frac{e}{m c^{2}k^{2}}}\right)^{2}\langle0|(E_{\mathbf{k}})^{2}|0\rangle}\\ {=\sum_{\mathbf{k}}\left({\frac{e}{m c^{2}k^{2}}}\right)^{2}\left({\frac{\hbar c k}{2\epsilon_{0}V}}\right),}\end{array}

<img src="https://www.zhihu.com/equation?tex=这种近似在 <img src="https://www.zhihu.com/equation?tex=k>\pi/a_0" alt="k>\pi/a_0" class="ee_img tr_noresize" eeimg="1"> 时有效，这时振动比绕核旋转快，同时也要在相对论极限下， <img src="https://www.zhihu.com/equation?tex=k<mc/\hbar" alt="k<mc/\hbar" class="ee_img tr_noresize" eeimg="1"> ，这样才能让最后结果收敛（反正是估算），最后得到lamb位移表达式：
" alt="这种近似在 <img src="https://www.zhihu.com/equation?tex=k>\pi/a_0" alt="k>\pi/a_0" class="ee_img tr_noresize" eeimg="1"> 时有效，这时振动比绕核旋转快，同时也要在相对论极限下， <img src="https://www.zhihu.com/equation?tex=k<mc/\hbar" alt="k<mc/\hbar" class="ee_img tr_noresize" eeimg="1"> ，这样才能让最后结果收敛（反正是估算），最后得到lamb位移表达式：
" class="ee_img tr_noresize" eeimg="1">
\langle\Delta V\rangle=\frac{4}{3}\frac{e^{2}}{4\pi\epsilon_{0}}\frac{e^{2}}{4\pi\epsilon_{0}\hbar c}\left(\frac{\hbar}{m c}\right)^{2}\frac{1}{8\pi a_{0}^{3}}\ln\left(\frac{4\epsilon_{0}\hbar c}{e^{2}}\right)
$$






