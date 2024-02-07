# StarCraft II 编辑器指南

这个库存储了由暴雪娱乐为星际争霸2编辑器提供的教程。

现在由 SC2Mapster 社区进行维护和改进。

## 部署

https://s2editor-guides.readthedocs.io/

![](https://readthedocs.org/projects/s2editor-guides/badge/?version=latest)

## 站点生成器

我们正在使用 [mkdocs.org](https://www.mkdocs.org)。

### 命令

* `mkdocs new [dir-name]` - 创建一个新项目。
* `mkdocs serve` - 启动实时重新加载的文档服务器。
* `mkdocs build` - 构建文档站点。
* `mkdocs help` - 打印这个帮助信息。

### 项目布局

    mkdocs.yml    # 配置文件。
    docs/
        index.md  # 文档首页。
        ...       # 其他 Markdown 页面、图片和其他文件。