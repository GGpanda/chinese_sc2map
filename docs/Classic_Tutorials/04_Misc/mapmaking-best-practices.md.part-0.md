# 地图制作：艺术和表演中的最佳实践

![地图制作：艺术和表演中的最佳实践](https://web.archive.org/web/20160505140409im_/http://bnetcmsus-a.akamaihd.net/cms/blog_header/b3/B3FQCUUA4HBW1461972169271.jpg)

上周，我们在 Team Liquid 公布了第七届 Team Liquid 地图比赛！我们非常激动地期待社区中富有创造力的大脑为我们开发新颖有趣的地图，供我们在即将到来的梯队赛季中进行游玩。

随着社区中地图制作活动的加剧，我们希望借此机会与您分享一些最佳实践，我们相信这对所有社区地图制作者都是有益的。这些最佳实践完全与地图制作的艺术方面有关，它们的使用不仅可以让地图看起来很棒，而且还可以在我们的玩家在 StarCraft II 上进行游玩时在各种各样的设备上表现良好。因此，废话不多说，让我们开始讨论装饰物：地图制作者可用的各种结构、植被和装饰模型。

## 装饰物

[![img](https://web.archive.org/web/20160505140409im_/https://bnetcmsus-a.akamaihd.net/cms/content_entry_media/AH0O3MMAJ3IP1461966790257.jpg)](https://web.archive.org/web/20160505140409/https://bnetcmsus-a.akamaihd.net/cms/content_entry_media/00354ZPG88NO1461966790159.jpg)

**图片 A：** 在这个场景中有 200 棵树。虽然看起来很漂亮，但这对性能是不必要地苛刻。许多树重叠在一起或被其他树覆盖。

**图片 B：** 在这里，树木数量减少了一半，但每棵树都有更多的空间，重叠更少，且整体外观得到保留。这对于性能有限的玩家是有价值的。

[![img](https://web.archive.org/web/20160505140409im_/https://bnetcmsus-a.akamaihd.net/cms/content_entry_media/3PPAL00W5LLZ1461966790108.jpg)](https://web.archive.org/web/20160505140409/https://bnetcmsus-a.akamaihd.net/cms/content_entry_media/W82EPJAA2T451461966790139.jpg)

**图片 A：** 这些装饰物有隐藏成本......

**图片 B：** 当地形被隐藏时，您可以看到被降低到地形下方的其余装饰物。像这样的大型装饰物仍然*完全渲染*并具有大量的过度绘制。

[![img](https://web.archive.org/web/20160505140409im_/https://bnetcmsus-a.akamaihd.net/cms/content_entry_media/AG4EYN69P72K1461966791686.jpg)](https://web.archive.org/web/20160505140409/https://bnetcmsus-a.akamaihd.net/cms/content_entry_media/EW2138CYW6TU1461966791619.jpg)

**图片 A：** 过度绘制为什么不好？这里是一棵靠近水域的大树（已经昂贵的渲染）。您可以看到水面上的阴影。

**图片 B：** 在这张图片中，您可以看到*即使将摄像机移开*并且树木不再显示在屏幕上，阴影仍然可见，这意味着树木仍然需要被渲染。

[![img](https://web.archive.org/web/20160505140409im_/https://bnetcmsus-a.akamaihd.net/cms/content_entry_media/5RVFS0PEORVY1461966791826.jpg)](https://web.archive.org/web/20160505140409/https://bnetcmsus-a.akamaihd.net/cms/content_entry_media/VEWS0M5K02UC1461966791820.jpg)

**图片 A：** 在区域中均匀放置物体看起来更自然，但这会遮挡单位或为某些单位提供不公平的优势。

**图片 B：** 尽量保持游戏区域畅通无阻，并将大部分装饰物放置在不可玩区域或您不希望玩家去的区域。

------

## 灯光和阴影

[![img](https://web.archive.org/web/20160505140409im_/https://bnetcmsus-a.akamaihd.net/cms/content_entry_media/B0TYOSB0EDAW1461966791343.jpg)](https://web.archive.org/web/20160505140409/https://bnetcmsus-a.akamaihd.net/cms/content_entry_media/BMRCJ4RL5DJJ1461966791301.jpg)

在创建一个级别时，请选择色彩和谐的装饰物、雾和灯光，限制您的调色板。颜色过多会从游戏玩法中分散注意力，使焦点远离单位。

[![img](https://web.archive.org/web/20160505140409im_/https://bnetcmsus-a.akamaihd.net/cms/content_entry_media/QJV4ZFF8RHUV1461966790476.jpg)](https://web.archive.org/web/20160505140409/https://bnetcmsus-a.akamaihd.net/cms/content_entry_media/X73YUFNA4Z9I1461966790408.jpg)

在照明您的级别时，最高优先级应该是**单位的可读性**。在左边，您会看到 MarSara 照明，这是一个不错的起点。从那里开始，尝试调整设置以为您的级别设定基调和氛围。右边的图像具有不错的沉郁照明，而单位仍然保持可读性。 

[![img](https://web.archive.org/web/20160505140409im_/https://bnetcmsus-a.akamaihd.net/cms/content_entry_media/Q9TI74STRWOA1461966791157.jpg)](https://web.archive.org/web/20160505140409/https://bnetcmsus-a.akamaihd.net/cms/content_entry_media/FPJL9G9H56F21461966791161.jpg)

确保在地图上任何装饰物出现的位置绘制通路。这将防止单位进入到网格的几何结构中。这包括填补小单位（如虫族）卡住的地方。按 H 键查看通路菜单。