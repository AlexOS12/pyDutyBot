import discord
from colorama import init, Fore
import dbworker.dbworker as db

init()

class MyClient(discord.Client):
    async def on_ready(self):
        print(f"Logged in as {self.user} (ID: {self.user.id})")
        print('-'*10)  
        pass

    async def on_message(self, message: discord.message.Message):
        if message.author.id == self.user.id:
            pass

        if message.content.startswith('/whoami'):
            print(Fore.GREEN + message.author.name, Fore.YELLOW + "wrote:", Fore.WHITE + f'"{message.content}"')
            await message.reply("I am an idiot bot! XD", mention_author=True)
        elif message.content.startswith('/dosomeshit'):
            print(Fore.GREEN + message.author.name, Fore.YELLOW + "wrote:", Fore.WHITE + f'"{message.content}"')
            try:
                num = int(message.content.split()[1])
                print(num)
                ans = db.sql_executor(f"insert into test values ({num})")
                # ans = db.sql_executor("insert into test values (1)")
                if ans == False:
                    await message.reply("You did some shit! XD", mention_author=True)
                else:
                    await message.reply("All's good!", mention_author=True)
            except:
                await message.reply("Something went wrong XD", mention_author=True)
        elif message.content.startswith('/shutdown'):
            await message.channel.send("@everyone, WeeWee! XD")
            db.shutdown()
            exit()
                



intents = discord.Intents.default()
intents.members = True
intents.message_content = True

token : str

with open('token.txt', 'r') as file:
# with open('C:\\Users\\mayor\\Documents\\GitHub\\pyDutyBot\\app\\token.txt', 'r') as file:
    token = file.read().replace('\n', '')

client = MyClient(intents=intents)
client.run(token)