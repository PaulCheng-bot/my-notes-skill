#!/usr/bin/env python3
"""
My Notes Skill - Create notes in Apple Notes
使用 memo CLI 在 Mac 的 Apple Notes 中创建笔记
"""

import subprocess
import sys
import json
from datetime import datetime
from pathlib import Path

def load_config():
    """加载配置文件"""
    config_path = Path(__file__).parent / "config.json"
    if config_path.exists():
        with open(config_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {
        "defaultFolder": "Notes",
        "addTimestamp": True,
        "addTags": True,
        "defaultTags": ["openclaw"]
    }

def check_memo_installed():
    """检查 memo CLI 是否已安装"""
    try:
        result = subprocess.run(
            ["which", "memo"],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            return True
        return False
    except Exception:
        return False

def create_note(content, tags=None):
    """
    创建笔记
    
    Args:
        content (str): 笔记内容
        tags (list): 标签列表
    
    Returns:
        dict: 创建结果
    """
    config = load_config()
    
    # 检查 memo 是否安装
    if not check_memo_installed():
        return {
            "success": False,
            "error": "memo CLI 未安装，请运行：brew install memo",
            "command": "brew install memo"
        }
    
    # 处理标签
    if tags is None:
        tags = []
    
    # 添加默认标签
    if config.get("addTags", True):
        default_tags = config.get("defaultTags", ["openclaw"])
        tags = list(set(tags + default_tags))
    
    # 格式化内容
    formatted_content = content
    if config.get("addTimestamp", True):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        formatted_content = f"[{timestamp}] {content}"
    
    # 添加标签到内容
    if tags:
        tag_str = " ".join([f"#{tag}" for tag in tags])
        formatted_content = f"{formatted_content} {tag_str}"
    
    try:
        # 使用 memo CLI 创建笔记（交互式，使用 -a 参数）
        # memo notes -a 会打开编辑器，所以我们需要通过 stdin 输入内容
        folder = config.get("defaultFolder", "Notes")
        result = subprocess.run(
            ["memo", "notes", "-a", "-f", folder],
            input=formatted_content,
            capture_output=True,
            text=True,
            timeout=10
        )
        
        if result.returncode == 0:
            return {
                "success": True,
                "content": content,
                "formatted_content": formatted_content,
                "tags": tags,
                "timestamp": datetime.now().isoformat(),
                "folder": folder
            }
        else:
            return {
                "success": False,
                "error": result.stderr or "创建笔记失败",
                "content": content
            }
            
    except subprocess.TimeoutExpired:
        return {
            "success": False,
            "error": "命令执行超时",
            "content": content
        }
    except FileNotFoundError:
        return {
            "success": False,
            "error": "memo CLI 未找到，请确保已安装",
            "command": "brew install memo",
            "content": content
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "content": content
        }

def list_notes(limit=10):
    """列出最近的笔记"""
    if not check_memo_installed():
        return {"success": False, "error": "memo CLI 未安装"}
    
    try:
        result = subprocess.run(
            ["memo", "list", "-n", str(limit)],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        if result.returncode == 0:
            notes = result.stdout.strip().split("\n")
            return {
                "success": True,
                "notes": notes,
                "count": len(notes)
            }
        else:
            return {
                "success": False,
                "error": result.stderr or "列出笔记失败"
            }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

def search_notes(query):
    """搜索笔记"""
    if not check_memo_installed():
        return {"success": False, "error": "memo CLI 未安装"}
    
    try:
        result = subprocess.run(
            ["memo", "search", query],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        if result.returncode == 0:
            notes = result.stdout.strip().split("\n")
            return {
                "success": True,
                "notes": notes,
                "query": query,
                "count": len(notes)
            }
        else:
            return {
                "success": False,
                "error": result.stderr or "搜索失败",
                "query": query
            }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "query": query
        }

def format_response(result, action="create"):
    """
    格式化响应消息
    
    Args:
        result (dict): 操作结果
        action (str): 操作类型 (create/list/search)
    
    Returns:
        str: 格式化的响应消息
    """
    if not result.get("success", False):
        return f"❌ 操作失败：{result.get('error', '未知错误')}\n\n💡 提示：{result.get('command', '请检查配置')}"
    
    if action == "create":
        response = []
        response.append("✅ 已创建笔记")
        response.append(f"📝 内容：\"{result.get('content', '')}\"")
        response.append(f"📁 位置：Apple Notes ({result.get('folder', 'Notes')})")
        response.append(f"🕐 时间：{datetime.now().strftime('%Y-%m-%d %H:%M')}")
        
        if result.get("tags"):
            tags_str = " ".join([f"#{tag}" for tag in result["tags"]])
            response.append(f"🏷️ 标签：{tags_str}")
        
        return "\n".join(response)
    
    elif action == "list":
        notes = result.get("notes", [])
        if not notes:
            return "📭 暂无笔记"
        
        response = [f"📋 最近的笔记 ({result.get('count', 0)} 条):", ""]
        for i, note in enumerate(notes, 1):
            response.append(f"{i}. {note}")
        
        return "\n".join(response)
    
    elif action == "search":
        notes = result.get("notes", [])
        if not notes:
            return f"🔍 未找到包含 \"{result.get('query', '')}\" 的笔记"
        
        response = [f"🔍 搜索结果 ({result.get('count', 0)} 条):", ""]
        for i, note in enumerate(notes, 1):
            response.append(f"{i}. {note}")
        
        return "\n".join(response)
    
    return str(result)

def main():
    """主函数 - 从命令行参数读取"""
    if len(sys.argv) < 2:
        print("用法：python create_note.py <笔记内容> [--tags tag1,tag2]")
        print("示例：python create_note.py \"今天天气很好\" --tags 生活，心情")
        sys.exit(1)
    
    content = sys.argv[1]
    tags = []
    
    # 解析标签参数
    if "--tags" in sys.argv:
        tags_index = sys.argv.index("--tags")
        if tags_index + 1 < len(sys.argv):
            tags = sys.argv[tags_index + 1].split(",")
    
    # 创建笔记
    result = create_note(content, tags)
    
    # 输出结果
    if result["success"]:
        print(format_response(result, "create"))
    else:
        print(f"❌ 失败：{result.get('error', '未知错误')}")
        sys.exit(1)

if __name__ == "__main__":
    main()
