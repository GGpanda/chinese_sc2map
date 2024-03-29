**重力** - 导弹所经历的重力。通过调整这个数值，可以使某些类型的导弹看起来“漂浮”（低重力）或在运动中表现得更具侵略性（高重力）。

**清障** - 这是导弹能够接近地面的最短距离。对于可能在从上方或下方攻击目标时可能与悬崖边缘碰撞的导弹类型非常有用。最好避免在弹道导弹中使用此选项。

**清障前瞻** - 此数值决定了在寻找可能与地面碰撞的时候需要前瞻多远。单位前瞻得越远，就能越早开始调整路径，但会增加更多性能开销。

**忽略地形** - 此标记确定导弹是否使用清障和清障前瞻字段，还是直接穿过地形。

**转向类型**

决定导弹朝向目标转向的方式，以及是否关注由人类战斗机飞行员维持的上方概念。可以有三个值：

- *默认*。导弹像战斗机飞行员一样转向，更倾向于使用让其更快抵达目标的转向弧线，偏航或俯仰。这取决于导弹的偏航和俯仰速率，以及目标的相对位置。不同于战斗机飞行员，导弹不会自行调整，开心地保持颠倒状态。
- *恢复至上方*。导弹像真正的战斗机飞行员一样转向，旋转回来以使其上方轴向指向天空当它不在转向时。这种转向类型可能导致导弹执行著名的由著名的德国第一次世界大战王牌飞行员设计的“伊梅尔曼转弯”。

- *最佳*。导弹使用四元数到达最优三维旋转，以尽快到达目标。这可能导致看似不考虑物理规律的反直觉旋转。

**跟踪**

调整导弹在目标移动时的反应方式，可能导致导弹看起来表现异常的方式：

- *无“钩”*。默认设置。导臹角色追踪同步运动，除了在最终同步步骤中发生异步步骤外，该角色始终沿着前一个同步步骤的航线继续。当导弹略微偏离目标位置时，朝向其会使导弹在飞行的最后几秒内发生剧烈旋转。不使用此设置可能导致导弹在击中目标前突然转向，而在错误情况下设置此选项可能导致导弹看似擦肩而过目标。
- *线性*。导弹始终指向最初发射时建立的方向。激光常使用此选项，应该不会旋转。而导致其侧向滑动，就像第一部星际争霸中那样。

- *实际*。导弹在最终同步步骤中保持朝向相同的方向，就像无“钩”一样，但仍可以引导朝向精确的冲击点。

**到达测试类型**

控制导弹测试自身是否足够接近目标来被认为“到达”。可以有三个值：

- *自适应*。默认设置。该测试在目标点使用二维，对目标单位时自动切换到三维。
- *二维*。导弹使用二维测试，这意味着一个电磁脉冲导弹可能在目标上方远距离爆炸，但仍被认为已击中目标。

- *三维*。导弹查看真实的三维距离以确定到达。弹道导弹通常对点目标执行二维测试，但有时需要对急剧弧线进行三维测试。如果没有进行三维测试，弹道导弹会在目标远上方爆炸，因为它在XY平面上几乎正好在目标上方，尽管在三维空间中仍然很远。

- *从不*。导弹永远不会造成影响。这在需要将导弹投向特定方向，且导弹扫描周围目标行为时很有用。

**融合类型**

控制重叠阶段之间融合发生的方式。可以有三个值：

- *线性*。直线融合。
- *对数*。导致融合迅速开始但逐渐减弱。结果看起来曲线非常平滑。

- *指数*。导致融合缓慢开始但指数增长。

**结尾**

一个控制阶段何时以及如何结束的关键字段。它有4个与之关联的不同值：

- *融合位置*。决定给定阶段何时开始融合到下一个阶段。如果该数字等于停止位置，则意味着该阶段有一个硬过渡，没有融合。若该数字为正数，则表示当导弹距离发射导弹的单位已行进了该距离时开始融合。若为负数，则表示当导弹距离目标该距离时开始融合。在第一个阶段，可以为零，表示立即开始融合，或者如果是最后一个阶段的唯一条目，也可以为零。在这种情况下，意味着当导弹击中目标时，阶段结束。总体而言，这是沿着核心运动驱动器（例如，引导驱动器的核心引导路径）的距离，不考虑导弹由于覆盖物而行进的额外距离。
- *停止位置*。控制如果有融合时阶段实际结束。

- *融合范围*。添加到融合位置值的随机值的上限。这会导致导弹飞行路径在每次发射时产生变化。它不会导致融合位置超越停止位置。始终为正数。

- *停止范围*。添加到停止位置的随机值的上限。始终为正数。

**旋转启动角色类型**

配置导弹的视觉部分在发射时的旋转，使其表面旋转无需匹配游戏启动旋转。

- *无*。默认设置。导弹角色的发射旋转匹配导弹的游戏旋转。
- *发射到目标*。导臂在发射时直接面向其冲击点。如果导弹从车辆的侧部发射，可能不是一个很好的选择。

- *发射到目标二维*。类似于“发射到目标”，但导弹保持与地面平行。

- *提供*。表示导弹角色的发射旋转通过游戏代码内部供给给角色。由触手使用。

**旋转角色类型**

配置导弹在飞行时的旋转，使其表面旋转不一定与其实际行进路径相关。

- *无*。默认设置。导弹角色的旋转与导弹的游戏旋转相匹配。
- *对接*。导臂到达位置，并与确定其冲击点的角色的反向旋转位置相匹配。这种类型的角色旋转用于触手回归，以确保触手的“头部”精确匹配其后坐动画。如果导弹的冲击点具有0，-1，0的前向矢量，那么导弹在朝向目标移动时将具有0，1，0的前向矢量。这是因为导弹面对触手的所有者，即使触手似乎仍然面向其目标。