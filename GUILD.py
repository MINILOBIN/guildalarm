import asyncio
import discord
from datetime import datetime
client = discord.Client()

token = "NjY4MDUxNTUyNDM0NjUxMTY2.XiMNBg.r0NGqSyYWUmg5uRgLQGULJIHCxQ"
@client.event
async def on_ready():
    print("다음으로 로그인합니다")
    print(client.user.name)
    print(client.user.id)
    print("================")

# 봇이 특정 메세지를 받고 인식하는 코드
@client.event
async def on_message(message):
    # 메세지를 보낸 사람이 봇일 경우 무시한다
    if message.content.startswith('!작동'):
        channel = message.channel
        await channel.send('길드 알람 작동을 시작합니다')
        flag1 = 0
        flag2 = 0
        flag3 = 0
        boss = 0
        while 1:
            now = datetime.now()
            if now.minute == 50:
                if now.hour == 11 and flag1 == 0:
                    await channel.send('모두 플래그 하러 갑시다!!')
                    flag1 = 1
                    flag2 = 0
                    flag3 = 0
                    boss = 0
                if now.hour == 18 and flag2 == 0:
                    await channel.send('모두 플래그 하러 갑시다!!')
                    flag1 = 0
                    flag2 = 1
                    flag3 = 0
                    boss = 0
                if now.hour == 20 and flag3 == 0:
                    await channel.send('모두 플래그 하러 갑시다!!')
                    flag1 = 0
                    flag2 = 0
                    flag3 = 1
                    boss = 0
            if now.minute == 30:
                if now.hour == 23 and boss == 0:
                    await channel.send('다들 오늘 길보 빼먹지 않고 돌았죠?! :)')
                    boss = 1
                    flag1 = 0
                    flag2 = 0
                    flag3 = 0
client.run(token)
