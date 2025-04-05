from discord.ext import commands

class HelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help")
    async def custom_help(self, ctx):
        help_text = "**📖 Командуудын жагсаалт:**\n\n"

        help_text += "**🔹 .hello** — 'Сайн уу!' гэж мэндчилнэ\n"
        help_text += "**🔹 .roll** — 1-100 хүртэлх санамсаргүй тоо шидэж оноо авна\n"
        help_text += "**🔹 .showroll** — Roll онооны leaderboard харуулна\n"
        help_text += "**🔹 .stoproll** — Roll оноог шинэчилж дахин эхлүүлнэ\n"
        help_text += "**🔹 .players** — Бүртгэгдсэн оролцогчдыг харуулна\n"
        help_text += "**🔹 bulaa_start / bulaa_stop** — Бүртгэлийн системийг эхлүүлж/зогсооно\n"
        help_text += "**🔹 + / -** — Бүртгэлд нэмэх, хасах\n"

        await ctx.send(help_text)

async def setup(bot):
    await bot.add_cog(HelpCog(bot))
