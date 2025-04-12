import json
from pathlib import Path
from nonebot import logger
from nonebot.plugin import on_command
from nonebot.params import CommandArg
from nonebot.adapters.onebot.v11 import Bot, MessageSegment, Message, GroupMessageEvent  # 添加导入
from nonebot.permission import SUPERUSER

# 定义存储路径
CUSTOM_FACE_FILE = Path("data/sing/custom_face_list.json")
CUSTOM_FACE_FILE.parent.mkdir(parents=True, exist_ok=True)  # 确保目录存在

async def fetch_custom_face_list() -> dict:
    """
    获取自定义表情列表，若不存在则返回空字典
    """
    if not CUSTOM_FACE_FILE.exists():
        logger.error("自定义表情列表不存在，请先获取自定义表情！")
        return {}

    try:
        with open(CUSTOM_FACE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        logger.error(f"加载自定义表情列表失败: {e}")
        return {}

async def save_custom_face_list(custom_face_list: list):
    """
    保存自定义表情列表到 JSON 文件
    """
    renamed_face_list = {f"face_{i+1}": face for i, face in enumerate(reversed(custom_face_list))}
    try:
        with open(CUSTOM_FACE_FILE, "w", encoding="utf-8") as f:
            json.dump(renamed_face_list, f, ensure_ascii=False, indent=4)
        logger.info(f"自定义表情列表已保存至 {CUSTOM_FACE_FILE.resolve()}")
    except Exception as e:
        logger.error(f"保存自定义表情列表失败: {e}")
        raise

async def update_custom_face_list(bot: Bot) -> int:
    """
    更新自定义表情列表并保存到 JSON 文件
    """
    custom_face_list = await bot.fetch_custom_face()
    logger.info(f"获取到 {len(custom_face_list)} 个自定义表情")

    try:
        await save_custom_face_list(custom_face_list)
        return len(custom_face_list)
    except Exception as e:
        logger.error(f"更新自定义表情列表失败: {e}")
        raise

async def send_custom_face(bot: Bot, event: GroupMessageEvent, face_key: str):
    """
    发送自定义表情
    """
    custom_face_list = await fetch_custom_face_list()
    if face_key not in custom_face_list:
        raise ValueError(f"未找到对应的自定义表情：{face_key}")

    face_data = custom_face_list[face_key]
    try:
        await bot.send(event, MessageSegment.image(face_data))
    except Exception as e:
        logger.error(f"发送自定义表情失败: {e}")
        raise
