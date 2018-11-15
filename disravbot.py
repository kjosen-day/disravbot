#!/usr/bin/python
import discord
from auth_my import *
from ravelry import *

TOKEN = 'NTEwNTU3MzQ1NTEyNjg1NTgz.DseKEw.PmpTDiAi6JlKS0Ezomd4UXzDl-0'

client = discord.Client()
ravelry = Ravelry(ravelry_accesskey, ravelry_personalkey);

def uniq (input):
    output = []
    for x in input:
            if x not in output:
                    output.append(x)
    return output

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # reasonably copied from linkrav_bot.py:process_comment_subreddit
    comment_reply = ''
    matches = re.findall(RAV_MATCH, message.content, re.IGNORECASE)

    if matches is not None:
        matches = uniq(matches)

        # append to comments
        for match in matches:
            match_string = ravelry.url_to_string(match)
            if match_string is not None:
                comment_reply += match_string

    # generate comment
    if comment_reply != '':
        logger.debug("\n\n-----%s-----\n\n", comment_reply)
        await client.send_message(message.channel, comment_reply)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)