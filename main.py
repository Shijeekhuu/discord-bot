import discord
from discord.ext import commands
import random  # random-оо гадаа импортолсон нь дээр

intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True
intents.members = True  # Гишүүдийн ID авахын тулд

bot = commands.Bot(command_prefix=".", intents=intents)
registered_players = set()  # Оролцогчдын ID-г хадгалах

@bot.event
async def on_ready():
    print(f'Бот {bot.user} нэвтэрлээ!')

@bot.command()
async def hello(ctx):
    await ctx.send("Сайн уу!")

roll_scores = {}


@bot.command()
async def roll(ctx):
    number = random.randint(1, 100)
    roll_scores[ctx.author.name] = number
    await ctx.send(f"🎲 {ctx.author.mention}, чи {number} гэсэн тоо шидлээ!")

@bot.command()
async def showroll(ctx):
    if not roll_scores:
        await ctx.send("Одоогоор хэн ч roll хийгээгүй байна.")
        return

    sorted_scores = sorted(roll_scores.items(), key=lambda x: x[1], reverse=True)

    leaderboard_text = "**🏆 Roll Leaderboard:**\n"
    for i, (user, score) in enumerate(sorted_scores, start=1):
        leaderboard_text += f"{i}. **{user}** — {score} 🎲\n"

    await ctx.send(leaderboard_text)

@bot.command()

async def stoproll(ctx):
    
    roll_scores.clear()  # Оноог бүгдийг арилгана
    await ctx.send("🔁 Roll оноонууд шинэчлэгдлээ. Шинэ раунд эхэлж байна!")
    await ctx.send(leaderboard_text)
    
@bot.event
async def on_message(message):
    global registration_open

    if message.author.bot:
        return

    content = message.content.strip()

    if content.lower() == "bulaa_start":
        registration_open = True
        registered_players.clear()
        await message.channel.send("🟢 Бүртгэл эхэллээ! `+` гэж бичээд оролцоно уу. @everyone")
    elif content.lower() == "bulaa_stop":
        registration_open = False
        await message.channel.send("🔴 Бүртгэл хаагдлаа!")
    elif content == "+":
        if registration_open:
            if message.author.id not in registered_players:
                registered_players.add(message.author.id)
                await message.channel.send(f"✅ {message.author.name} бүртгэгдлээ!")
            else:
                await message.channel.send(f"⚠️ {message.author.name}, та аль хэдийн бүртгэгдсэн байна.")
        else:
            await message.channel.send("🚫 Бүртгэл хаалттай байна.")
    elif content == "-":
        if message.author.id in registered_players:
            registered_players.remove(message.author.id)
            await message.channel.send(f"❌ {message.author.name} бүртгэлээс хасагдлаа.")
        else:
            await message.channel.send(f"⚠️ {message.author.name}, та бүртгэлд байхгүй байна.")

    await bot.process_commands(message)

@bot.command()
async def players(ctx):
    if not registered_players:
        await ctx.send("📭 Одоогоор бүртгэгдсэн хүн алга.")
        return

    players_text = "**🎯 Бүртгэгдсэн оролцогчид:**\n"
    for user_id in registered_players:
        user = await bot.fetch_user(user_id)
        players_text += f"- {user.mention}\n"

    await ctx.send(players_text)

    
import discord
from discord.ext import commands

class HelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="command")
    async def custom_help(self, ctx):
        embed = discord.Embed(
            title="📖 Командуудын жагсаалт",
            description="Эдгээр коммандуудыг ашиглаж болно:",
            color=discord.Color.blue()  # 🟦 Энд өнгө сонгож болно
        )

        embed.add_field(name=".hello", value="Сайн уу! гэж мэндчилнэ", inline=False)
        embed.add_field(name=".roll", value="1-100 хүртэлх тоо шидэж оноо авна", inline=False)
        embed.add_field(name=".showroll", value="Roll leaderboard харуулна", inline=False)
        embed.add_field(name=".stoproll", value="Roll оноог шинэчилнэ", inline=False)
        embed.add_field(name=".players", value="Бүртгэгдсэн оролцогчдыг харуулна", inline=False)
        embed.add_field(name="bulaa_start / bulaa_stop", value="Бүртгэл эхлүүлэх / зогсоох", inline=False)
        embed.add_field(name="+ / -", value="Өөрийгөө бүртгэх / хасах", inline=False)

        embed.set_footer(text="🤖 Шижээгийн бот 2025")

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(HelpCog(bot))

from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)
