import discord
import time

def parse(msg : discord.message.Message) -> (str, int):
    preparedMessage = prepareMessage(msg.content)
    isInTrustedList(msg.author)

    # Тут будет ответ, который мы отправим юзеру
    ans : str
    # Здесь будет храниться статус выполнения
    # 0 - всё гуд. 1 - что-то пошло не так. 2 - команда не найдена.  -1 - закрываемся
    backCode : int
    
    try:
        match preparedMessage[0]:
            case "whoami":
                ans = whoAmI()
                backCode = 0
            case "shutdown":
                ans = shutdown(msg.author)
                backCode = -1
            case _:
                ans = "Моя твоя не понимать"
                backCode = 2
    except:
        ans = ""
        backCode = 1

    return ans, backCode

def prepareMessage(msg : str) -> list[str]:
    msg = msg[1:].strip().lower().split()
    return msg

# тут у нас будут команды
# пока что сделал просто заглушки (почти все)

# /whoami - выводит информацию о боте
def whoAmI() -> str:
    return "Даров посаны! Я Билли Херрингтон!\n Я здесь, чтобы помочь напоминать вам, кто тут босс качалки. Кстати, fisting is 300 bucks)"

def shutdown(author : discord.Member) -> str:
    if not(isInTrustedList(author)):
        return "Ты бесправное чмо не имеешь право меня выключить!"
    else:
        return "Да мой повелитель! Я сейчас же пойду спать!"
        


# Проверяем, что пользователь находится в доверенном списке
def isInTrustedList(member: discord.Member) -> bool:
    if not(trustedList):
        return True
    return True if member.name in trustedList else False

# Лист доверенных юзеров
trustedList : list[str]

# Читаем лист доверенных юзеров
with open("trusted_list.txt", 'r') as file:
    trustedList = [i.replace('\n', '') for i in file.readlines()]
    print("Доверенный список юзеров:")
    for i in range(len(trustedList)):
        print(f"{i + 1} - {trustedList[i]}")
   