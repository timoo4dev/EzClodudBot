import discord
import datetime
from utils.config.color import errcolor


async def botowner(ctx):
    if not ctx.author.id == 1078242409495932969:
        embed = discord.Embed(
            title="Fehlende Brechtigungen!",
            description="Dir Fehlen folgende Brechtigung ```BOT OWNER```",
            color=errcolor,
            timestamp=datetime.datetime.utcnow(),
        )
        await ctx.respond(embed=embed, ephemeral=True)
        return True


async def admin(ctx):
    if not ctx.author.guild_permissions.administrator:
        embed = discord.Embed(
            title="Fehlende Brechtigungen!",
            description="Dir Fehlen folgende Brechtigung ```ADMINISTRATOR```",
            color=errcolor,
            timestamp=datetime.datetime.utcnow(),
        )
        await ctx.respond(embed=embed, ephemeral=True)
        return True


async def ban_members(ctx):
    if not ctx.author.guild_permissions.ban_members:
        embed = discord.Embed(
            title="Fehlende Brechtigungen!",
            description="Dir Fehlen folgende Brechtigung ```BAN MEMBERS```",
            color=errcolor,
            timestamp=datetime.datetime.utcnow(),
        )
        await ctx.respond(embed=embed, ephemeral=True)
        return True


async def kick_members(ctx):
    if not ctx.author.guild_permissions.ban_members:
        embed = discord.Embed(
            title="Fehlende Brechtigungen!",
            description="Dir Fehlen folgende Brechtigung ```KICK MEMBERS```",
            color=errcolor,
            timestamp=datetime.datetime.utcnow(),
        )
        await ctx.respond(embed=embed, ephemeral=True)
        return True


async def manage_channels(ctx):
    if not ctx.author.guild_permissions.manage_channels:
        embed = discord.Embed(
            title="Fehlende Brechtigungen!",
            description="Dir Fehlen folgende Brechtigung ```MANAGE CHANNELS```",
            color=errcolor,
            timestamp=datetime.datetime.utcnow(),
        )
        await ctx.respond(embed=embed, ephemeral=True)
        return True


async def create_invite(ctx):
    if not ctx.author.guild_permissions.create_instant_invite:
        embed = discord.Embed(
            title="Fehlende Brechtigungen!",
            description="Dir Fehlen folgende Brechtigung ```CREATE INSTANT INVITE```",
            color=errcolor,
            timestamp=datetime.datetime.utcnow(),
        )
        await ctx.respond(embed=embed, ephemeral=True)
        return True


async def manage_guild(ctx):
    if not ctx.author.guild_permissions.manage_guild:
        embed = discord.Embed(
            title="Fehlende Brechtigungen!",
            description="Dir Fehlen folgende Brechtigung ```MANAGE GUILD```",
            color=errcolor,
            timestamp=datetime.datetime.utcnow(),
        )
        await ctx.respond(embed=embed, ephemeral=True)
        return True


async def add_reactions(ctx):
    if not ctx.author.guild_permissions.add_reactions:
        embed = discord.Embed(
            title="Fehlende Brechtigungen!",
            description="Dir Fehlen folgende Brechtigung ```ADD REACTIONS```",
            color=errcolor,
            timestamp=datetime.datetime.utcnow(),
        )
        await ctx.respond(embed=embed, ephemeral=True)
        return True


async def manage_messages(ctx):
    if not ctx.author.guild_permissions.manage_messages:
        embed = discord.Embed(
            title="Fehlende Brechtigungen!",
            description="Dir Fehlen folgende Brechtigung ```MANAGE MESSAGES```",
            color=errcolor,
            timestamp=datetime.datetime.utcnow(),
        )
        await ctx.respond(embed=embed, ephemeral=True)
        return True


async def mute_members(ctx):
    if not ctx.author.guild_permissions.mute_members:
        embed = discord.Embed(
            title="Fehlende Brechtigungen!",
            description="Dir Fehlen folgende Brechtigung ```MUTE MEMBERS```",
            color=errcolor,
            timestamp=datetime.datetime.utcnow(),
        )
        await ctx.respond(embed=embed, ephemeral=True)
        return True


async def change_nickname(ctx):
    if not ctx.author.guild_permissions.change_nickname:
        embed = discord.Embed(
            title="Fehlende Brechtigungen!",
            description="Dir Fehlen folgende Brechtigung ```CHANGE NICKNAME```",
            color=errcolor,
            timestamp=datetime.datetime.utcnow(),
        )
        await ctx.respond(embed=embed, ephemeral=True)
        return True


async def manage_nicknames(ctx):
    if not ctx.author.guild_permissions.manage_nicknames:
        embed = discord.Embed(
            title="Fehlende Brechtigungen!",
            description="Dir Fehlen folgende Brechtigung ```MANAGE NICKNAME```",
            color=errcolor,
            timestamp=datetime.datetime.utcnow(),
        )
        await ctx.respond(embed=embed, ephemeral=True)
        return True


async def manage_roles(ctx):
    if not ctx.author.guild_permissions.manage_roles:
        embed = discord.Embed(
            title="Fehlende Brechtigungen!",
            description="Dir Fehlen folgende Brechtigung ```MANAGE ROLES```",
            color=errcolor,
            timestamp=datetime.datetime.utcnow(),
        )
        await ctx.respond(embed=embed, ephemeral=True)
        return True


async def manage_emojis(ctx):
    if not ctx.author.guild_permissions.manage_emojis:
        embed = discord.Embed(
            title="Fehlende Brechtigungen!",
            description="Dir Fehlen folgende Brechtigung ```MANAGE EMOJIS```",
            color=errcolor,
            timestamp=datetime.datetime.utcnow(),
        )
        await ctx.respond(embed=embed, ephemeral=True)
        return True


async def manage_events(ctx):
    if not ctx.author.guild_permissions.manage_emojis:
        embed = discord.Embed(
            title="Fehlende Brechtigungen!",
            description="Dir Fehlen folgende Brechtigung ```MANAGE EVENTS```",
            color=errcolor,
            timestamp=datetime.datetime.utcnow(),
        )
        await ctx.respond(embed=embed, ephemeral=True)
        return True


async def manage_threads(ctx):
    if not ctx.author.guild_permissions.manage_emojis:
        embed = discord.Embed(
            title="Fehlende Brechtigungen!",
            description="Dir Fehlen folgende Brechtigung ```MANAGE THREADS```",
            color=errcolor,
            timestamp=datetime.datetime.utcnow(),
        )
        await ctx.respond(embed=embed, ephemeral=True)
        return True
