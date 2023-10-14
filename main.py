import discord
from discord.ext import tasks, commands

import urllib.request

import asyncio

client=commands.Bot()


class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.command_prefix = "!"
        self.token = "MTE2MjQwNTUzMjI5NzA4MDk5Mg.G0moVd.Y8ohKeHCd6pIFfYXoPs5DtDNVV5hAPtQP28NYA"

    def run(self):
        super().run(self.token)

    async def on_ready(self):
        print("DaHobbys bot is ready!")              
                    

                   
bot = Bot()

client = Bot()

intents = discord.Intents.default()
intents.members = True



@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')


@client.event
async def on_member_join(member):
    channel_id = 1162660076574757005
    channel = bot.get_channel(channel_id)
    if channel:
        await channel.send(f'{member.mention} joined us!')


@client.event
async def on_member_leave(member):
    channel_id = 1162660076574757005
    channel = bot.get_channel(channel_id)
    if channel:
        await channel.send(f'{member.display_name} left us!')


@bot.slash_command(
    name="text",
    description="Convert your text to a minecraft chat log!"
)
async def text(ctx, text, rainbow:discord.Option(str, "LGBTQ Text?!?!", choices = ["GayText", "HetroText"])):
    await ctx.defer()
    url = f"https://skyblock.noms.tech/render/bridge/{urllib.request.quote(text)}.gif"
    if rainbow == "GayText":
        url += "?rainbow"
    
    await ctx.respond(url)
    
    
@bot.event
async def on_voice_state_update(member, before, after):
    channel_id = 1162660076574757005
    channel = bot.get_channel(channel_id)

    if channel:
        if before.channel is None and after.channel is not None:
            join_time = after.channel.created_at.strftime('%Y-%m-%d %H:%M:%S')

            embed = discord.Embed(
                title=f'{member.display_name} joined {after.channel.name}',
                description=f'Join Time: {join_time}',
                color=discord.Color.green()
            )

            await channel.send(embed=embed)
            

@bot.slash_command(name='timeout', description='Timeout a member', guild_ids=[1060480506002690068])
async def timeout_member(ctx, member: discord.Member, duration: int, description: str):
    if ctx.author.guild_permissions.administrator:
        await member.add_roles(discord.utils.get(ctx.guild.roles, name='Muted'))

        await ctx.respond(f'{member.mention} has been timed out for {duration} minutes. Reason: {description}')

        await asyncio.sleep(duration * 60)
        await member.remove_roles(discord.utils.get(ctx.guild.roles, name='Muted'))
        await ctx.send(f'{member.mention} has been unmuted.')

    else:
        await ctx.send("You're not allowed to run this :D")
        
@bot.slash_command(name='qt', description='Timeout a member', guild_ids=[1060480506002690068])
async def timeout_member(ctx, member: discord.Member, duration: int, description: str):
    if ctx.author.guild_permissions.administrator:
        await member.add_roles(discord.utils.get(ctx.guild.roles, name='Muted'))

        await ctx.respond(f'{member.mention} has been timed out for {duration} minutes. Reason: {description}')

        await asyncio.sleep(duration * 60)
        await member.remove_roles(discord.utils.get(ctx.guild.roles, name='Muted'))
        await ctx.send(f'{member.mention} has been unmuted.')

    else:
        await ctx.send("You're not allowed to run this :D")
        


      

    
    
    
    
bot.run()
