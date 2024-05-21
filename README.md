## 下面是一个简单的README文件，说明如何使用Python开发一个Telegram机器人：

# Telegram 机器人开发

这是一个用Python编写的Telegram机器人

v1.0：用于回复今天天气情况。
v1.1：回复壁纸可以返回今天的必应壁纸，且加入了gpt3.5接口功能。

## 使用前准备

1. 创建Telegram账号（如果还没有）
2. 在Telegram中搜索并与 [@BotFather](https://telegram.me/BotFather) 对话，创建一个新的机器人并获得API令牌。
3. 安装Python（如果尚未安装），建议使用Python 3.10 版本。
4. 安装 `python-telegram-bot` 库，你可以使用pip进行安装：
   ```
   pip install python-telegram-bot
   ```

## 配置机器人

在 `config.py` 文件中配置你的机器人API令牌：

```python
TOKEN = "YOUR_BOT_TOKEN_HERE"
```

## 运行机器人

运行 `main.py` 文件来启动你的机器人：

```
python main.py
```

## 使用机器人

在Telegram中搜索你创建的机器人，并开始对话。你的机器人将会自动响应你发送的消息，并根据你的命令执行相应的操作。之后将会引入等多的API功能。

## 贡献

如果你发现了bug或者有改进的建议，欢迎提交issue或者pull request。

## 版权

本项目采用 [MIT](LICENSE) 开放源代码许可证。