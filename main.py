import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print(f"Logged in as {self.user} (ID: {self.user.id})")
        print('-'*10)  
        pass

    async def on_message(self, message):
        if message.author.id == self.user.id:
            pass

        if message.content.startswith('/whoami'):
            await message.reply("I am an idiot bot! XD", mention_author=True)

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('token')