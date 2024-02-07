* **ModelLink** - 要用于解密的模型数据条目的名称。

## 演员作弊用法

用户可以在从编辑器中运行地图时将演员作弊输入到聊天栏中。

输出内容将进入 Alert.txt 日志，该日志可在用户的“StarCraft II/GameLogs”目录中找到。Alert.txt 日志的文件名前面附加有日期和时间戳，因此实际示例的名称如下：“2011-08-08 10.30.05 Alerts.txt”。

目前不支持快捷方式，但以后可能会添加快捷方式。



### 演员作弊清单

在每个命令的给定语法中，由花括号{}括起的参数表示可选参数。对于某些作弊成功执行时，将设置两个全局变量，“::User actor” 和 “::User scope” 值，其他作弊可以基于这些值进行操作。杀死演员和范围的作弊不包括那些可能破坏当前活跃单位和效果的演员和范围。

#### ActorCreateAt

在指定位置创建一个演员。将“::User actor” 设置为此演员，并将“::User scope” 设置为其范围。

此作弊对于直接在测试地图上创建一个演员，以便观察其属性并与之交互，而无需等待地图遇到通常会创建演员的情况非常有用。坐标使用户能够精确放置演员用于战斗测试等场合。

##### 语法

```ActorCreateAt x,y actorName {contentName} {content2Name} {content3Name}```

##### 示例

```ActorCreateAt 50,50 Model Drone ```<br/>
```ActorCreateAt 50,50 NexusSplat```

#### ActorCreateAtCursor

在鼠标光标位置创建一个演员（以及包含它的演员范围）。将“::User actor” 设置为此演员，并将“::User scope” 设置为其范围。

此作弊对于直接在测试地图上创建一个演员，以便观察其属性并与之交互，而无需等待地图遇到通常会创建演员的情况非常有用。它将演员放置在光标位置，因此用户无需担心获取特定坐标以将演员定位在易于看到的位置。

##### 语法

```ActorCreateAtCursor actorName {contentName} {content2Name} {content3Name}```

##### 示例

```ActorCreateAtCursor Model Drone ```<br/>
```ActorCreateAtCursor NexusSplat```

#### ActorDumpAutoCreates

转储所有像这样创建的所有演员的列表：

```xml
<On Terms="UnitBirth.Marine" Send="Create"/>
```

这种演员创建模式称为“自动创建”，因为演员会自动响应消息而创建自身。这与以下创建模式不同：

```xml
<On Terms="ActorCreation" Send="Create SomeActor"/>
```

因为这里的“Create”消息明确指定要创建的演员。

ActorDumpAutoCreates可用于追踪某些事件无意间创建的演员。

##### 语法

```ActorDumpAutoCreates```

#### ActorDumpEvents

转储“::User actor”看到的所有演员事件列表，不包括自动创建事件。

此作弊可用于在地图上执行各种文本搜索，例如，如果用户想要查看响应给定信号事件的所有演员，不管它们位于哪个依赖关系中。

##### 语法

```ActorDumpEvents```

#### ActorDumpLeakRisks

转储比特定年龄大的演员列表，这些演员可能泄露。用户可以检查闪光模型是否超过一分钟，例如，因为闪光通常不持续那么长时间。某些类型的演员永远不会出现在泄漏风险列表中，因为它们由系统自动清理，因此通常不会受到不良数据的泄露。

如果地图随着时间的推移变得逐渐变慢，此作弊可以确定是否泄漏演员为原因。

##### 语法

```ActorDumpLeakRisks age```



#### ActorDumpLive

转储整个地图上存活的演员列表，由包含的范围排序。

此作弊有助于确定演员是否存在，尽管它们未出现在游戏世界中预期的位置。错误出现在0,0 的演员仍将显示在活动演员列表中。

##### 语法

```ActorDumpLive```



#### ActorFrom

从一个活动的演员中根据引用名称设置一个新的“::User actor”。

此作弊对于将游戏世界中的各种演员设置到“::User ref”，以便用户可以向其发送作弊命令非常重要。

##### 语法

```ActorFrom RefName```

##### 示例

```ActorFrom ::HoverTarget```<br/>
```ActorFrom ::Selection```

#### ActorFromActor

将“::User actor”设置为通过另一个演员和分支引用名称引用的演员。

此作弊对于将游戏世界中的各种父级和子级演员设置到“::User ref”，以便用户可以向其发送作弊命令非常有用。通常用于对演员的“::Host ref”执行操作。

##### 语法 

```ActorFromActor refName```

##### 示例

```ActorFromActor ::Host```

将“::User actor”设置为托管它的演员。

```ActorFromActor ::Creator```

将“::User actor”设置为创建它的演员。

#### ActorKillAll

杀死所有演员，除了那些属于活动单位和效果树的演员。

有助于清除测试地图中的演员，以便随后可以隔离地测试单个演员。

#### 语法: 

```ActorKillAll```

#### ActorKillClass

杀死鼠标光标范围内指定类别的所有演员。如果未指定范围，则为无限。

如果某些类型的演员让用户难以专注于解决方案，用户可以使用该命令清除区域（或整个地图）中的特定类型演员。例如，可能需要杀死所有地形演员以确认它们是否导致性能问题。

#### 语法: 

```ActorKillClass class {range}```


示例:

```ActorKillClass Model 15 ActorKillClass Sound```

#### ActorKillLink 

杀死鼠标光标范围内具有指定演员链接的所有演员。如果未指定范围，则为无限。

可以用于清除区域（或整个地图）中特定演员条目的所有实例，如果它们让用户难以专注于解决方案。例如，如果创建了太多模型并掩盖了用户正在调试的攻击的某个其他部分的图形 FX，则可能需要杀死特定名称的所有模型。或者，用户可能会杀死带有给定名称的所有声音，以查看是否可以听到与特效相关联的其他声音。

#### 语法: 

```ActorKillLink link {range}```



##### ActorSend

向当前活动的“::User actor”发送一个有效的用户消息。