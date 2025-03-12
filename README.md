# RSSHub Dify Plugin

> **Note**: For comprehensive information about available routes and parameters, please refer to the official [RSSHub Documentation](https://docs.rsshub.app/).

This is a RSSHub plugin for Dify that allows you to access RSS feeds from RSSHub through Dify.

# Installation

Read more in [Release](https://github.com/stvlynn/RSSHub-Dify-Plugin/releases)

## Features

- Get RSS feeds from RSSHub
- Support for custom RSSHub instances
- Limit the number of returned items
- Convenient access to specific services (such as X/Twitter, LinkedIn)

## Usage

1. Install this plugin in Dify
2. Use the plugin in your prompts, for example:

```
Use RSSHub to get the latest articles from sspai
```

## Available Tools

### Custom Route

Get RSS feeds from RSSHub using a custom route.

**Parameters:**
- `base_url`: The base URL of the RSSHub instance, default is `https://rsshub.app`
- `route`: The RSSHub route path, e.g. `/zhihu/hot`
- `limit`: Maximum number of items to return, default is 10

### X (Twitter)

Get RSS feeds from X (Twitter) via RSSHub.

![](./_assets/X.png)

**Parameters:**
- `route_type`: Twitter route type, with the following options:
  - User Timeline
  - Keyword Search
  - List Timeline
  - Home Timeline
  - Latest Home Timeline
  - User Likes
  - User Media
- `base_url`: The base URL of the RSSHub instance, default is `https://rsshub.app`
- `username`: Twitter username without @ (e.g., elonmusk). Required for user timeline, user likes, and user media route types
- `keyword`: The keyword to search for. Required for keyword search route type
- `list_id`: Twitter list ID. Required for list timeline route type
- `exclude_replies`: Whether to exclude replies, default is false. Only applies to user timeline route type
- `exclude_rts`: Whether to exclude retweets, default is false. Only applies to user timeline route type
- `limit`: Maximum number of items to return, default is 10

### LinkedIn

Get RSS feeds from LinkedIn via RSSHub.

![](./_assets/linkedin.png)

**Parameters:**
- `route_type`: LinkedIn route type, with the following options:
  - Jobs
- `base_url`: The base URL of the RSSHub instance, default is `https://rsshub.app`
- `keywords`: Job search keywords
- `job_types`: Job types, available options:
  - Full Time
  - Part Time
  - Contractor
  - All
- `exp_levels`: Experience levels, available options:
  - Internship
  - Entry Level
  - Associate
  - Mid-Senior Level
  - Director
  - All
- `work_type`: Work type, available options:
  - Onsite
  - Remote
  - Hybrid
  - Any
- `time_posted`: Filter by when the job was posted, available options:
  - Past 24 hours
  - Past week
  - Past month
  - Any time
- `geo_id`: Geographic location ID (e.g., 91000012 for East Asia)
- `limit`: Maximum number of items to return, default is 10

### Threads

Get RSS feeds from Threads via RSSHub.

![](./_assets/threads.png)

**Parameters:**
- `route_type`: Threads route type, with the following options:
  - User
- `base_url`: The base URL of the RSSHub instance, default is `https://rsshub.app`
- `username`: Threads username without @ symbol
- `show_author_in_title`: Show author name in title, default is true
- `show_author_in_desc`: Show author name in description (RSS body), default is true
- `show_quoted_in_title`: Show quoted thread in title, default is true
- `show_emoji_for_quotes_and_reply`: Use 🔁 instead of QT, ↩️ instead of Re, default is true
- `replies`: Include replies, default is true
- `show_author_avatar_in_desc`: Show author avatar in description, default is false (not recommended if your RSS reader extracts images from description)
- `show_quoted_author_avatar_in_desc`: Show quoted author avatar in description, default is false (not recommended if your RSS reader extracts images from description)
- `limit`: Maximum number of items to return, default is 10

### Discord

Get RSS feeds from Discord via RSSHub.

![](./_assets/discord.png)

**Parameters:**
- `route_type`: Discord route type, with the following options:
  - Channel Messages
  - Guild Search
- `base_url`: The base URL of the RSSHub instance, default is `https://rsshub.app`
- `channel_id`: Discord channel ID, required for Channel Messages route type
- `guild_id`: Discord server ID, required for Guild Search route type
- `search_params`: Search parameters for Guild Search route type (e.g., content=friendly&has=image,video). Supports content, author_id, mentions, has, min_id, max_id, channel_id, pinned, etc.
- `discord_authorization`: Discord authorization header from the browser (required for both route types)
- `limit`: Maximum number of items to return, default is 10

### Google News

Get RSS feeds from Google News via RSSHub.

![](./_assets/google_news.png)

**Parameters:**
- `base_url`: The base URL of the RSSHub instance, default is `https://rsshub.app`
- `category`: Category title of Google News, e.g. 'Top stories', 'World', 'Business'
- `language_code`: Language code for Google News content, e.g. 'en-US', 'zh-CN', 'ja-JP'
- `country_code`: Country or region code for Google News content, e.g. 'US', 'CN', 'JP'
- `country_edition`: Country edition for Google News, usually in format 'COUNTRY:LANGUAGE', e.g. 'US:en', 'CN:zh'
- `limit`: Maximum number of items to return, default is 10

## Supported Routes

RSSHub supports a large number of routes. You can view all supported routes in the [RSSHub Documentation](https://docs.rsshub.app/).

Here are some commonly used route examples:

- `/zhihu/hot` - Zhihu Hot List
- `/sspai/matrix` - Sspai Matrix
- `/36kr/hot-list` - 36Kr Hot List
- `/weibo/search/hot` - Weibo Hot Search

## Developer

- [Steven Lynn](https://github.com/stvlynn)

## License

[MIT](./LICENSE)

## rsshub

**Author:** stvlynn
**Version:** 0.0.1
**Type:** tool

### Description



