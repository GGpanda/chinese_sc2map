## 详细介绍投掷驱动器

使导弹沿着任意线性路径移动。虽然看似用途有限，但实际上这是从视觉冲击力角度而言最灵活且强大的驱动器。将其与混合物相结合，并在同时发射的导弹组中进行变化，投掷驱动器可以创造出令人惊叹的独特视觉图案。

**投掷旋转类型**

- *无。* 默认值。如果是第一阶段，导弹沿投掷方向前进，但在其他情况下将继续沿当前方向前进，因为投掷可以改变导弹的方向而不影响其旋转。

- *发射器正向* 。使导弹在本阶段开始时朝向发射单元或发射单元的炮塔（如果有）。仅在第一阶段有用。
- *瞄准目标* 。导臹始终直接对准其撞击点。

- *瞄准目标2D* 。类似于瞄准目标，但导弹始终与地面平行。

- *向前投掷* 。导弹面向投掷方向。

- *向量化* 。允许用户在本地坐标中配置任意面朝方向。用于导臹从发射单元以一种夸张的“休眠”姿势抛出，然后激活（在此情况下，导弹指向其他地方是传达视觉信息的原因）。例如，投掷可用于像投放炸弹一样释放导弹，而向量值可用于使导弹在下落到点火高度时始终指向正前方。

**投掷向量**

投掷的本地坐标。它们不需要被规范化。

**投掷波段偏航**

允许用户在偏航平面上配置投掷方差，作为相对于核心投掷轴的偏差。

- *正向最大* 。控制偏航方差在正向（顺时针）方向的外部偏航限制。实际上可以是负值，用于非对称方差。
- *负向最大* 。可选。控制偏航方差在负向（逆时针）方向的外部偏航限制。实际上可以是正值，用于非对称方差。

- *正向最小* 。可选，但如果使用需要配置负向最大和负向最小。可用于打开偏航带中的间隙，以便导弹指挥左右两侧飞行，而不是在中间飞行。

- *负向最小* 。可选，但如果使用需要配置负向最大和正向最小。类似于正向最小，但是在负方向。

换句话说，用户可以指定一段投掷弧，或者在弧度偏向右侧或左侧，他可以防止导弹从弧中的间隙中发射出去，从而不会穿过袭击飞船的机身。这些数字还使得更容易创建：A）海星式的突发图案和B）夸张的“鞭击”式攻击，导臹在击中目标之前朝特定方向突出。

**投掷波段俯仰**

类似于投掷波段偏航，但用于俯仰。当使用了所有四个偏航和俯仰最小值时，这意味着导弹会在正方形环中脱颖而出，而不是横跨整个正方形区域。正如上文所述，这对于创建某些喷射导弹图案是有用的。

**向前投掷**

在使用向量旋转类型时，本地坐标空间中配置任意面向的向量。



## 详细介绍叠加

与阶段不同，叠加应用于导弹的整个飞行路径。用户可以在给定导弹上有最多两个同时叠加，并且每个叠加对最终导弹位置有相等的贡献。

叠加具有一个规模概念，即它们从核心驱动器飞行路径偏离的距离。规模在飞行路径的两端都为零，但可以在飞行中间每个阶段基础上变化。叠加系统自动使用三次样条曲线平滑地混合规模值，导弹在移动时在其中点实现给定阶段的规模。

由于叠加导致导弹额外飞行的距离不影响阶段结束；这完全受核心驱动器运动的控制（这种额外距离很难准确预测，并且实际上显着改变了导弹阶段更替的方式，这是过于变化的）。

**类型**

叠加的类型，是Wave、Orbit还是Revolver。

**极性**

允许用户控制叠加运动的方向。对于Wave叠加，这控制第一个“隆起”的方向，是正方向还是负方向。对于Orbit叠加，它控制轨道是顺时针运动（正方向）还是逆时针运动（负方向）。当尝试协调一对导弹的组合外观时，控制这些是有用的。极性支持多个值：

- *正向*。叠加向正方向移动。
- *负向*。叠加向负方向移动。

- 随机。叠加有50%的机会朝着正方向或负方向移动。

- *交替*。叠加根据不断前进的滚动指数决定方向。指数每当攻击单元执行攻击或操作时递增，因此可用于定期变化，形成条纹状模式。

**极性驱动器**

指定正在使用的滚动指数或执行指数，以驱动交替类型的极性。字符串“::RollingIndex”指定叠加的极性由滚动指数交替，而相关效果ID指定它由在给定效果树中连续执行的每次效果交替。指定效果交替极性在给定攻击中交替极性。

**轴**

本地坐标中控制叠加运动应用的轴线。对于Wave叠加，这控制正弦波的方向。对于Orbit和Revolver叠加，它控制旋转轴。在大多数情况下，这将是0,-1,0（向前）或0,1,0（向后）。但是，通过变化可以创建不寻常和倾斜的叠加（例如，为轨道创建横向旋转轴会形成垂直环面飞行图案）。

**波长**

指定Wave叠加完成整个360度正弦波的距离，或者指定Orbit叠加完成整个旋转的距离。

基础。控制最小波长距离。

范围。将添加到基础距离的随机值的外部边界。这导致正弦波和轨道明显变化，通常会产生更接近真实世界外观的效果。

**波长更改概率**

在每一半波（即在每个波“隆起”后）或一半轨道之后重新计算波长的百分比机会。


## 详细介绍Revolver叠加

Revolver类似于Orbit，但不总是朝着相同方向移动。它们意在模拟罗宇星飞行模式中的“醉醺醺导弹”，其导弹以懒散的、缓慢变化方向和速度的旋转轨道运动。