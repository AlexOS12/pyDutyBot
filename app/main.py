import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print(f"Logged in as {self.user} (ID: {self.user.id})")
        print('-'*10)  
        pass

    async def on_message(self, message: discord.message.Message):
        if message.author.id == self.user.id:
            pass

        if message.content.startswith('/whoami'):
            print(message.author.name)
            await message.reply("I am an idiot bot! XD", mention_author=True)

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

token : str

with open('token.txt', 'r') as file:
    token = file.read().replace('\n', '')

client = MyClient(intents=intents)
client.run(token)