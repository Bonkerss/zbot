import discord, asyncio, functions

token = ""
bot_name = ""
client = discord.Client()


@client.event
@asyncio.coroutine
def on_ready():
    print("+===========+")
    print("+ {} Is Ready +".format(bot_name))
    print("+===========+")

@client.event
@asyncio.coroutine
def on_message(message):
    content = message.content
    author = message.author
    mention_author = author.mention
    func = functions
    func.check_status(author)

    if message.startswith("!help"):
        print("Yeah")


if __name__ == "__main__":
    client.run(token)
