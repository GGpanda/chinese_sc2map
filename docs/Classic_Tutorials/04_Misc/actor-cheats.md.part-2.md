迄今为止最常用的演员作弊，也是开发人员（内部或外部）与演员互动的主要方式之一。

#### 语法：

```ActorSend message```

#### 示例：

```ActorSend Destroy ActorSend SetTintColor {255,255,0}```

#### ActorSendTo

向系统演员引用发送消息，使用::User演员来帮助解析系统演员引用。换句话说，这个例程向分支引用名称发送消息（尽管也适用于::Main引用名称）。

此作弊可以是向分支演员发送消息的简便方式；用户无需首先使用ActorFromActor作弊将它们设置为::User引用。

语法：
ActorSendTo refName message

示例：
ActorSendTo ::Host SetOpacity 0.5 ActorSendTo ::Main SetTintColor {255,0,0}

#### ActorScopeDumpLive

在整个地图上列出存活范围的列表。

这个作弊可用于查找消耗资源但不再有（有用的）演员的演员范围。

语法：
ActorScopeDumpLive

**ActorScopeFrom**

这个作弊对于将游戏世界中的各个范围设置为::User范围引用至关重要，从而使用户可以轻松找到并向该范围内的任何演员发送消息。

语法：
ActorScopeFrom scopeName

示例：
ActorScopeFrom ::PortraitGame ActorScopeFrom ::Selection

杀死当前设置的::User演员和::User范围。此命令无法杀死用于防止意外结果的活单位或效果的范围。

这个作弊是一种有效的方式来杀死用户一直在尝试的一个或多个演员，只需杀死它们所在的范围即可（因为这将杀死范围内的所有演员）。

语法：
ActorScopeKill

**ActorScopeOrphan**

这个作弊可用于测试ActorOrphan消息对::User范围内的演员的影响。

语法：
ActorScopeOrphan

**ActorScopeSend**

在用户想要向范围内所有演员发送消息的罕见情况下非常有用。

（另外，虽然这个作弊看起来似乎是将范围内所有模型染成红色（例如），但通常最好让子演员从::Main演员托管，并继承tintColor属性。然后用户仅向范围的::Main演员发送SetTintColor消息，并依赖于托管道具的继承来传播颜色更改。当一个范围中可能包含不应该被染成红色的演员（如敌人影响火花）以及打算染成红色的演员时，后一种方法通常更佳。广播tintColor消息会使范围内的所有模型变红。）

语法：
ActorScopeSend message

示例：
ActorScopeSend Destroy

**ActorUsersDump**

如果用户忘记了这些引用当前设置为什么，这个命令是有用的。

语法：
ActorUsersDump

**ActorUsersFromHoverTarget**

非常有用，可以检查和操作游戏世界中不属于可选对象的任何演员。

语法：
ActorUsersFromHoverTarget

**ActorUsersFromPortraitGame**

可用于检查和操作图像窗口中包含的演员。

语法：
ActorUsersFromPortraitGame

**ActorUsersFromSelection**

非常有用，可以检查和操作游戏世界中属于可选对象的任何演员。

语法：
ActorUsersFromSelection

**ActorWorldParticleFXDestroy**

可用于立即清除世界中模糊的粒子和带状FX（通常在游戏暂停时），以便仔细检查模型或其他一些视觉FX的部分。

语法：
ActorWorldParticleFXDestroy

## 

演员转储消息

用户可以向演员发送演员转储消息，以从中获取有用的与调试相关的信息。

**AliasDump**

打印出当前与演员关联的所有演员别名。

**AnimDumpDB**

打印出与演员关联的模型可用的所有动画。为每个动画打印出持续时间，以及它是否是循环动画。

**AttachDump**

打印出与演员关联的模型上存在的所有附加点。还打印出用户指定的附加键和与每个附加点相关联的目标附加体积。

**HostedPropDump**

如果存在指定的托管道具，则打印出与其关联的所有信息。如果IncludeChildren参数为1，则打印出目标演员的所有子项的道具信息。

示例：
HostedPropDump 0 TintColor HostedPropDump 1 TeamColor

语法：
HostedPropDumpAll IncludeChildren

打印出与演员上存在的所有托管道具相关的所有信息。如果IncludeChildren参数为1，则对所有目标演员的子项执行相同操作。

**RefDump**

打印出由refName指定的演员的调试信息。目前，这仅适用于系统ref表中的演员引用，即格式为::actor.someUserRef、::scope.someUserRef和::global.someUserRef的引用。

示例：
RefDump ::actor.someUserRef

**RefTableDump**

打印出给定Ref表中所有演员引用的调试信息。RefTableType参数区分大小写，期望的标记为Actor、Scope或Global。

示例：
RefDumpAll Actor

**TextureDump**

打印出目标演员关联模型当前使用的所有纹理。指示哪些纹理与纹理槽相关联，以及它们是否已被其他动态纹理替换和替换。

**TextureDumpDB**

打印出与目标演员关联的模型上可供动态纹理替换使用的所有纹理。