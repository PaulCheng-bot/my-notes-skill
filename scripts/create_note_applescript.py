#!/usr/bin/env python3
"""
My Notes Skill - Create notes in Apple Notes
使用 AppleScript 在 Mac 的 Apple Notes 中创建笔记
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

def create_note_applescript(content, folder=None):
    """
    使用 AppleScript 创建笔记
    
    Args:
        content (str): 笔记内容
        folder (str): 文件夹名称
    
    Returns:
        dict: 创建结果
    """
    config = load_config()
    
    if folder is None:
        folder = config.get("defaultFolder", "Notes")
    
    # 格式化内容
    formatted_content = content
    if config.get("addTimestamp", True):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        formatted_content = f"[{timestamp}] {content}"
    
    # 转义双引号
    escaped_content = formatted_content.replace('"', '\\"')
    
    # AppleScript 创建笔记
    applescript = f'''
    tell application "Notes"
        if not (exists folder "{folder}") then
            make new folder with properties {{name:"{folder}"}}
        end if
        make new note at folder "{folder}" with properties {{body:"{escaped_content}"}}
    end tell
    '''
    
    try:
        result = subprocess.run(
            ["osascript", "-e", applescript],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        if result.returncode == 0:
            return {
                "success": True,
                "content": content,
                "formatted_content": formatted_content,
                "folder": folder,
                "timestamp": datetime.now().isoformat()
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
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "content": content
        }

def format_response(result):
    """格式化响应消息"""
    if not result.get("success", False):
        return f"❌ 操作失败：{result.get('error', '未知错误')}"
    
    response = []
    response.append("✅ 已创建笔记")
    response.append(f"📝 内容：\"{result.get('content', '')}\"")
    response.append(f"📁 位置：Apple Notes ({result.get('folder', 'Notes')})")
    response.append(f"🕐 时间：{datetime.now().strftime('%Y-%m-%d %H:%M')}")
    
    return "\n".join(response)

def main():
    """主函数"""
    if len(sys.argv) < 2:
        print("用法：python create_note_applescript.py <笔记内容>")
        print("示例：python create_note_applescript.py \"今天天气很好\"")
        sys.exit(1)
    
    content = sys.argv[1]
    folder = sys.argv[2] if len(sys.argv) > 2 else None
    
    # 创建笔记
    result = create_note_applescript(content, folder)
    
    # 输出结果
    print(format_response(result))
    
    if not result["success"]:
        sys.exit(1)

if __name__ == "__main__":
    main()
