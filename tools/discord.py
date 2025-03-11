from collections.abc import Generator
from typing import Any
import requests
import html
import re
import xml.etree.ElementTree as ET
from datetime import datetime
from urllib.parse import urljoin, quote, urlencode

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

class DiscordTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        # 获取参数
        route_type = tool_parameters.get("route_type", "channel")
        base_url = tool_parameters.get("base_url", "https://rsshub.app")
        channel_id = tool_parameters.get("channel_id", "")
        guild_id = tool_parameters.get("guild_id", "")
        search_params = tool_parameters.get("search_params", "")
        discord_authorization = tool_parameters.get("discord_authorization", "")
        limit = int(tool_parameters.get("limit", 10))
        
        # 验证必要参数
        if route_type == "channel" and not channel_id:
            yield self.create_text_message("频道ID不能为空")
            return
        
        if route_type == "search" and not guild_id:
            yield self.create_text_message("服务器ID不能为空")
            return
            
        if not discord_authorization:
            yield self.create_text_message("Discord授权令牌不能为空")
            return
            
        # 确保base_url以/结尾
        if not base_url.endswith("/"):
            base_url = base_url + "/"
            
        # 构建路由和查询参数
        route = ""
        query_params = {}
        
        if route_type == "channel":
            route = f"/discord/channel/{channel_id}"
        elif route_type == "search":
            if search_params:
                route = f"/discord/search/{guild_id}/{search_params}"
            else:
                route = f"/discord/search/{guild_id}"
        else:
            yield self.create_text_message(f"不支持的路由类型: {route_type}")
            return
            
        # 构建最终URL
        url = urljoin(base_url, route)
        if query_params:
            url = f"{url}?{urlencode(query_params)}"
            
        try:
            # 设置请求头
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                "X-DISCORD-AUTHORIZATION": discord_authorization
            }
            
            # 获取RSS源
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            
            # 解析XML
            root = ET.fromstring(response.content)
            
            # 获取命名空间
            namespaces = {'': root.tag.split('}')[0].strip('{')} if '}' in root.tag else {}
            
            # 提取标题和描述
            channel = root.find('.//channel', namespaces)
            if channel is None:
                channel = root
                
            title = channel.findtext('./title', 'Discord RSS', namespaces)
            description = channel.findtext('./description', 'Discord RSS Feed', namespaces)
            
            # 提取条目
            entries = []
            items = channel.findall('./item', namespaces)
            
            for item in items[:limit]:
                item_title = item.findtext('./title', '无标题', namespaces)
                item_link = item.findtext('./link', '', namespaces)
                item_pubDate = item.findtext('./pubDate', '', namespaces)
                item_description = item.findtext('./description', '', namespaces)
                item_author = item.findtext('./author', '', namespaces)
                
                # 清理HTML标签
                clean_content = re.sub(r'<.*?>', '', item_description)
                clean_content = html.unescape(clean_content)
                
                # 格式化日期
                published = item_pubDate
                try:
                    if published:
                        dt = datetime.strptime(published, '%a, %d %b %Y %H:%M:%S %Z')
                        published = dt.strftime('%Y-%m-%d %H:%M:%S')
                except:
                    # 如果日期解析失败，保持原样
                    pass
                
                entries.append({
                    'title': item_title,
                    'link': item_link,
                    'published': published,
                    'content': clean_content[:500] + ('...' if len(clean_content) > 500 else ''),
                    'author': item_author
                })
            
            # 返回结果
            route_info = {
                "route_type": route_type,
                "channel_id": channel_id if route_type == "channel" else None,
                "guild_id": guild_id if route_type == "search" else None,
                "search_params": search_params if route_type == "search" else None
            }
            
            result = {
                "title": title,
                "description": description,
                "url": url,
                "entries": entries,
                "route_info": route_info
            }
            
            yield self.create_json_message(result)
            
        except Exception as e:
            error_message = f"获取Discord RSS源失败: {str(e)}"
            yield self.create_text_message(error_message) 