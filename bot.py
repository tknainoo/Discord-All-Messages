import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

# Load bot token from .env
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.members = True          # Required for managing roles
intents.message_content = True  # Required to read messages
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

# -----------------------------
# DELETE ALL ROLES COMMAND
# -----------------------------
@bot.command()
@commands.has_permissions(administrator=True)
async def delroles(ctx):
    await ctx.send(
        "⚠️ Are you sure you want to delete **ALL roles** in this server?\n"
        "Type `!confirmdel` within 30 seconds to continue."
    )

    def check(m):
        return m.author == ctx.author and m.content.lower() == "!confirmdel"

    try:
        msg = await bot.wait_for("message", timeout=30.0, check=check)
        if msg:
            await delete_all_roles(ctx)
    except:
        await ctx.send("❌ Confirmation timed out. No roles were deleted.")

async def delete_all_roles(ctx):
    guild = ctx.guild
    deleted = 0

    for role in guild.roles:
        try:
            if role.name != "@everyone" and role < guild.me.top_role:
                await role.delete()
                deleted += 1
        except Exception as e:
            print(f"Could not delete {role.name}: {e}")

    await ctx.send(f"✅ Deleted {deleted} roles successfully.")

# -----------------------------
# DELETE ALL MESSAGES FROM A USER
# -----------------------------
@bot.command()
@commands.has_permissions(administrator=True, manage_messages=True)
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

# Run the bot
bot.run(TOKEN)
