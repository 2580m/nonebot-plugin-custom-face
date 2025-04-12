<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot-plugin-custom-face

_✨ QQ 自定义表情相关 API  ✨_

<div align="left">

## 📖 介绍

提供了刷新自定义表情列表，发送自定义表情等 API

## 💿 安装

<details open>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

    pip install nonebot-plugin-custom-face
</details>

打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分追加写入

    plugins = ["nonebot_plugin_custom_face"]

</details>

## 用法

```python
from nonebot import require, on_startswith
from nonebot.adapters.onebot.v11 import Bot, MessageEvent

require("nonebot_plugin_custom_face")

from nonebot_plugin_custom_face import send_custom_face, update_custom_face_list

@on_startswith("test").handle()
async def handle(bot: Bot, event: MessageEvent):
    #刷新一下表情列表
    await update_custom_face_list(bot)
    #<face_1>是本地的表情列表中的表情id，按添加的时间从小到大排序，对于手机版QQ来说，自定义表情中的最旧一个(也就是列表最下边的一个)的本地表情列表中的id为 face_1
    send_face_id = 'face_1'
    await send_custom_face(bot, event, send_face_id)
```

