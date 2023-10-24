import discord

def parse(msg : discord.message.Message) -> None:
    preparedMessage = prepareMessage(msg.content)
    isInTrustedList(msg.author)
    return preparedMessage

def prepareMessage(msg : str) -> str:
    msg = msg[1:].strip().lower()
    msg = ' '.join(msg.split())
    return msg

# тут у нас будут команды
# пока что сделал просто заглушки (почти все)

# Проверяем, что пользователь находится в доверенном списке
def isInTrustedList(member: discord.Member) -> bool:
    if not(trustedList):
        return True
    return True if member.name in trustedList else False

# Лист доверенных юзеров
trustedList : list[str]

with open("trusted_list.txt", 'r') as file:
    trustedList = [i.replace('\n', '') for i in file.readlines()]
    print("Доверенный список юзеров:")
    for i in range(len(trustedList)):
        print(f"{i + 1} - {trustedList[i]}")
   