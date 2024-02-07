# 角色作弊

使用 Patch 1.4.0，modders 现在可以使用角色作弊来在编辑器中运行测试地图时创建和操作角色。这对于快速测试想法而无需设置数据或执行触发器非常有用。

在运行测试地图时，作弊也可以用于修改和检查几乎任何角色，这对于调试运行时角色问题很有帮助。

作弊还可用于发送几个新启用的 dump 消息，如 AnimDumpDB、AttachDump、HostedPropDump、RefDump 和 TextureDump。这些消息使 modders 能够在游戏运行时检查某些角色的内部方面，这对于作为额外调试辅助工具很有帮助。

## 角色作弊概念

### 引用名称

术语 "Ref Name" 是 "Actor Reference Name" 的缩写，它唯一标识称为角色引用 ("actor ref" 或简称 "ref") 的系统变量类型。根据 1) 引用名称的含义和 2) 它所用于的上下文，角色引用可以解析为给定角色。在指定的地方，引用名称可用在许多作弊中。它们的可用性可能会有所不同，取决于它们被使用的上下文：

- D- 在 Actor(D)ata 中
- T- 在 (t)riggers 中的与角色相关的函数内
- C- 通过角色 (c)heats

当前可用的引用名称包括：

| **::HoverTarget**       | C    | 鼠标指针下的角色。                                       |
| ----------------------- | ---- | ------------------------------------------------------ |
| **::LastCreated**       | DTC  | 在触发器中，这将解析为通过触发器函数直接成功创建的最后一个角色（但不会通过任何其他方式创建，比如通过数据中的消息作为触发器调用的结果）。在其他任何地方，它还包括通过 Create 消息明确创建的角色（即 Create SomeActor）。这旨在通过各种不同变体中的 LastCreated() 机制最大化一致性，同时尽量在其他任何地方遵守最少惊讶规则。 |
| **::LastCreatedActual** | DTC  | 用户通过任何方式成功创建的最后一个角色。包括通过 Create 消息创建的角色，角色请求创建，或系统内部创建的角色（例如当 CActorAction 创建散架时）。 |
| **::Main**              | DTC  | ::User 范围内的 "主" 角色。                               |
| Doodad                  |      | CActorDoodad。                                        |
| Unit                    |      | CActorUnit。                                          |
| 其余                    |      | 范围内创建的第一个角色。                                 |
| **::PortraitGame**      | DTC  | 游戏肖像窗口的主要角色，目前，在选择什么都不会改变。     |
| **::PortraitGameSelf**  | DTC  | 该角色范围内主要角色的肖像。用于从单位的范围内的任何角色向其肖像角色发送消息很有用。如果肖像是当前单位以外的其他人，则不返回任何内容。 |
| **::Self**              | D    | 接收事件的角色。                                         |
| **::User**              | TC   | 包含最近一次 ActorFrom 作弊的结果。                           |
| **::global.<RefName>**  | DTC  | 来自全局引用表的角色引用。                                   |
| **::scope.<RefName>**   | DTC  | 来自包含范围引用表的角色引用。                                |
| **::actor.<RefName>**   | DTC  | 来自包含角色引用表的角色引用。                                 |
| **TargetKey**           | TC   | 由 ::User 范围的关键表示的角色。当结果集中有多个命中时，仅返回其中的第一个。 |

### 分支引用名称

|                  |      | 注意                                                     |
| ---------------- | ---- | ------------------------------------------------------ |
| **::Creator**    | DTC  | ::User 角色的创建者。                                      |
| Hosts            |      | 主机角色是从中继承数据的一个角色，例如承受、容纳的道具等。          |
| **::Host**       | DTC  | 主要主机。用于承受和容纳的道具。                                  |
| **::HostImpact** | DTC  | 用于定位光束的影响点。                                          |
| **::HostLaunch** | DTC  | 用于定位光束的发射点。                                          |
| **::HostReturn** | DTC  | 神经丝使用的目标主机作为返回行程的目标。                           |
| **::Supporter**  | DTC  | 用于将一个角色的生存期与 "支持" 角色链接（通常用于设置事件，告诉一个角色当其支持角色死亡时死亡）。 |

### 范围引用名称

| **::Actor**        | TC   | ::User 角色的范围。                                       |
| ------------------ | ---- | ------------------------------------------------------ |
| **::LastCreated**  | TC   | 用户通过作弊或客户端代码成功创建的最后一个范围。在数据内部不相关，因为数据不创建范围。  |
| **::PortraitGame** | TC   | 游戏肖像窗口的范围。                                      |
| **::Selection**    | C    | 所选单位的范围。即使选择了多个单位，也只返回单个范围。             |
| **::User**         | TC   | 包含最近一次 ActorScopeFrom 作弊的结果。当该引用被填充为新的有效角色范围时，自动设置为值 ::LastCreated。 |

### 内容关键

Create 消息可以使用 1 到 3 个内容关键。这些关键使触发器和作弊能够更轻松地使用相同数据输入创建各种角色实例，但具有不同的 "内容" 参数。例如：

`ActorCreateAt Model Hydralisk `

`ActorCreateAt Model Marine`

这两个作弊都创建名为 "Model" 的 CActorModel。第一个使用 "Hydralisk" 资产创建，第二个使用 "Marine" 资产创建。各种类型的角色基于情况支持不同的创建参数样式。以下是支持内容参数的角色类型列表，以及指定顺序。

#### CActorBeam ModelLink RefLaunch RefImpact

* **ModelLink** - 用于光束的 modelData 条目的名称。
* **RefLaunch** - 用于填充光束的 ::HostLaunch 的 ref 名称。
* **RefImpact** - 用于填充光束的 ::HostImpact 的 ref 名称。

#### CActorList RefName

* **RefName** - 用于填充列表的源 ref 名称。

#### CActorModel

* **ModelLink** - 用于该模型的 modelData 条目的名称。
* **Variation** - 模型的特定变体编号，如果需要（否则会随机选择）。

#### CActorSound

* **SoundLink** - 要使用的声音的名称。

#### CActorSplat