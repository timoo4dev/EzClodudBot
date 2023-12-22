import discord
import ezcloud
import random

from discord import slash_command

class CreateTickets(ezcloud.View):
    def __init__(self):
        super().__init__(timeout=None)
        
    @discord.ui.Button(
        label="Support",
        style=discord.ButtonStyle.blurple,
        emoji="❗"
    )
    
    @discord.ui.Button(
        label="Team Bewerbungen",
        style=discord.ButtonStyle.blurple,
        emoji="👥"
    )
    
    @discord.ui.Button(
        label="EzCloud/bot",
        style=discord.ButtonStyle.blurple,
        emoji="🤖"
    )
    async def ezcloudbot(self, Button: discord.Button, interaction: discord.Interaction):
        
        

class Ticket(ezcloud.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.persistent_views_added = False
    
    @ezcloud.Cog.listener()
    async def on_ready(self):
        if not self.persistent_views_added:
            self.add_item(CreateTickets())
            self.persistent_views_added = True
    
    @slash_command()
    @discord.default_permissions(administartor=True)
    async def ticket(self, ctx):
        await ctx.respond("Bevor du unten ein Ticket öffnest, lies kurz die dazugehörigen Beschreibungen. Es werden sich die geeigneten Teamler dann bei dir im Ticket melden.\n\n")