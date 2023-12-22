import discord
import ezcloud
import random

class welcome(ezcloud.Cog):
    
    @ezcloud.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel()
        guild = self.bot.get_guild()
        
        welcome_emojis = ["👋", "🙌",  "🖐️", "🤚", "🙋‍♀️", "🙋‍♂️", "💁‍♀️"]

        welcome_messages = [
            f"Willkommen an Bord, {member.mention}! Lass uns zusammen den Server rocken.",
            f"Wir haben schon auf dich gewartet, {member.mention}. Willkommen auf unserem Server!",
            "Du bist hier! Endlich ist unser Server komplett. Herzlich willkommen.",
            "Willkommen auf unserem Server! Wir hoffen, dass du hier eine großartige Zeit haben wirst.",
            f"Hola, {member.mention}! Willkommen auf unserem Server.",]
        
        embed = discord.Embed(title=f"Willkommen auf {guild.name}!", description=f"*{random.choice(welcome_messages)}*", colour=0x5c00c7)
    

        if member.avatar is None:
            ezcloud.random_avatar()
        else:
            url = member.avatar.url
        
        view = discord.ui.View(timeout=None)
        button3 = discord.ui.Button(
            label="Begrüßen",
            style=discord.ButtonStyle.green,
            emoji="🤗"
        )
        async def call1(
            self,
            interaction: discord.Interaction
        ):
            if member == interaction.user:
                return await interaction.response.send_message("Hallo du kannst dich nicht selber begrüßen")
            else:
                button3.disabled = True
                await interaction.response.send_message(f'{interaction.user.mention} heißt **{member.display_name}** Herzlich Willkommen {random.choice(welcome_emojis)}')
                await interaction.message.edit(view=view)
                
            button3.callback = call1
            view.add_item(button3)
            await channel.send(embed=embed, view=view)
                
def setup(bot):
    bot.add_cog(welcome(bot))