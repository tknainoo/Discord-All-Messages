import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@bot.command()
@commands.has_permissions(administrator=True)  # Only admins
async def delusermsg(ctx, member: discord.Member):
    """Delete all messages from a user across all channels"""
    deleted_count = 0

    await ctx.send(f"🧹 Starting to delete messages from {member.mention}...")

    for channel in ctx.guild.text_channels:
        try:
            async for msg in channel.history(limit=None):
                if msg.author == member:
                    try:
                        await msg.delete()
                        deleted_count += 1
                    except Exception as e:
                        print(f"Could not delete message in {channel.name}: {e}")
        except Exception as e:
            print(f"Could not fetch history in {channel.name}: {e}")

    await ctx.send(f"✅ Finished. Deleted {deleted_count} messages from {member.mention}.")

bot.run("YOUR_BOT_TOKEN")
