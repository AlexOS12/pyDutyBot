import discord
import parser

class MyClient(discord.Client):
    async def on_ready(self):
        print(f"Logged in as {self.user} (ID: {self.user.id})")
        print("---------\n\n")

    async def on_message(self, msg: discord.message.Message):
        if msg.author.id == self.user.id: pass

        if msg.content.startswith('/'):
            print(f"{msg.id} | {msg.author.name} {'[Trusted]' if parser.isInTrustedList(msg.author) else ''} wrote: {msg.content}")
            ans, code = parser.parse(msg)
            print(f"Reply to {msg.id} | answer: {ans} | code: {code}")
            if code == 1:
                await msg.reply("Извините босс, я не справился(", mention_author=True)
            elif code == -1:
                await msg.reply(ans, mention_author=True)
                await msg.channel.send("everyone! Я иду на покой")
                exit(0) # надо будет придумать более безопасный способ заверешения работы Билли
            else:
                await msg.reply(ans, mention_author=True)

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

token : str

with open('token.txt', 'r') as file:
    token = file.read().replace('\n', '')

client = MyClient(intents=intents)
client.run(token)