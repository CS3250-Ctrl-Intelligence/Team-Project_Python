import discord
import os
from discord.ext import commands

from chat import chat

import mysql.connector as mc

def recommendation(email):
    # searchDate = '2022-01-01'
    mydb = mc.connect(
        host= os.getenv('DATABASE_SERVER'),
        user= os.getenv('DATABASE_USERNAME'),
        password=os.getenv('DATABASE_PASSWORD'),
        database=os.getenv('DATABASE_NAME'),
        port= os.getenv('DATABASE_PORT')
    )

    cur = mydb.cursor()
    query = "SELECT DISTINCT inventory.Supplier_ID from orders INNER JOIN inventory ON orders.Product_ID = inventory.Product_ID WHERE Cust_Email="+ "'" + email + "'" + "LIMIT 5;"
    cur.execute(query)


    mostProduct = [i[0] for i in cur.fetchall()]
    query="SELECT Sale_Price, Product_ID FROM inventory WHERE Supplier_ID IN (" + "'" + mostProduct[0]+"','"+ mostProduct[1]+"','"+ mostProduct[2]+"','" +mostProduct[3]+"','" + mostProduct[4]+ "') ORDER BY RAND() LIMIT 10 ;"
    cur.execute(query)
    recommendations = cur.fetchall()
    # for i in recommendation:
    #     print (i)
    return recommendations

def hist(email):
    
    mydb = mc.connect(
        host= os.getenv('DATABASE_SERVER'),
        user= os.getenv('DATABASE_USERNAME'),
        password=os.getenv('DATABASE_PASSWORD'),
        database=os.getenv('DATABASE_NAME'),
        port= os.getenv('DATABASE_PORT')
    )

    cur = mydb.cursor()
    query = "SELECT Cust_Email, orders.Date, orders.Quantity, FORMAT((orders.Quantity* inventory.Sale_Price), 2), orders.Product_ID from orders INNER JOIN inventory ON orders.Product_ID = inventory.Product_ID WHERE Cust_Email="+ "'" + email + "'" + ";"
    
    cur.execute(query)


    purchaseHistory = cur.fetchall()
    mydb.close()
    return purchaseHistory

def filter_below(price):

    mydb = mc.connect(
        host= os.getenv('DATABASE_SERVER'),
        user= os.getenv('DATABASE_USERNAME'),
        password=os.getenv('DATABASE_PASSWORD'),
        database=os.getenv('DATABASE_NAME'),
        port= os.getenv('DATABASE_PORT')
    )

    cur = mydb.cursor()
    query = "SELECT Sale_Price, Product_ID FROM inventory WHERE Sale_Price <"+ price +" ORDER BY RAND() LIMIT 10;"
    
    cur.execute(query)
    budget = cur.fetchall()
    mydb.close()
    return budget

def filter_above(price):

    mydb = mc.connect(
        host= os.getenv('DATABASE_SERVER'),
        user= os.getenv('DATABASE_USERNAME'),
        password=os.getenv('DATABASE_PASSWORD'),
        database=os.getenv('DATABASE_NAME'),
        port= os.getenv('DATABASE_PORT')
    )

    cur = mydb.cursor()
    query = "SELECT Sale_Price, Product_ID FROM inventory WHERE Sale_Price >"+ price +" ORDER BY RAND() LIMIT 10;"
    
    cur.execute(query)
    deluxe = cur.fetchall()
    mydb.close()
    return deluxe

def filter_between(price_above,price_below):

    mydb = mc.connect(
        host= os.getenv('DATABASE_SERVER'),
        user= os.getenv('DATABASE_USERNAME'),
        password=os.getenv('DATABASE_PASSWORD'),
        database=os.getenv('DATABASE_NAME'),
        port= os.getenv('DATABASE_PORT')
    )

    cur = mydb.cursor()
    query = "SELECT Sale_Price, Product_ID FROM inventory WHERE Sale_Price >"+ price_above +" AND Sale_Price <"+ price_below + " ORDER BY RAND() LIMIT 10;"
    
    cur.execute(query)
    moderate = cur.fetchall()
    mydb.close()
    return moderate

client = commands.Bot(command_prefix="!")
client.remove_command('help')
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if str(message.content)[0] != '!':
        msg=chat(message.content)
        await message.channel.send(msg)
        
    await client.process_commands(message)

# This command requires an argument(email) to find a recommendation based on that user history
@client.command()
async def recommend(ctx, arg):
    transac = ""

    for tups in recommendation(str(arg)):
        for tup in tups:
            transac += str(tup) + "\t\t\t"
        transac += "\n"

    await ctx.send("Price\t\t\t\t\tProduct ID")
    await ctx.send(transac)

# Handle error
@recommend.error
async def recommend_error(ctx,error):
    if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
        await ctx.send("Please input your email after !recommend")

# This command requires an argument(email) to find the purchase history of that user
@client.command()
async def history(ctx, arg):
    transac = ""

    for tups in hist(str(arg)):
        for tup in tups:
            transac += str(tup) + "\t\t\t"
        transac += "\n"

    await ctx.send("Email\t\t\t\t\t\t\t\t\t\tDate\t\t\tQuantity\t\t\tPrice\t\t\t\t\tProduct ID")
    await ctx.send(transac)

# Handle error
@history.error
async def history_error(ctx,error):
    if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
        await ctx.send("Please input your email after !history")

# This command will give a list of 10 products with the sale price below arg
@client.command()
async def below(ctx,arg):
    transac = ""

    for tups in filter_below(str(arg)):
        for tup in tups:
            transac += str(tup) + "\t\t\t"
        transac += "\n"

    await ctx.send("Price\t\t\tProduct ID")
    await ctx.send(transac)

# Handle error
@below.error
async def below_error(ctx,error):
    if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
        await ctx.send("Please input a number after !below")

# This command will give a list of 10 products with the sale price above arg
@client.command()
async def above(ctx,arg):
    transac = ""

    for tups in filter_below(str(arg)):
        for tup in tups:
            transac += str(tup) + "\t\t\t"
        transac += "\n"

    await ctx.send("Price\t\t\tProduct ID")
    await ctx.send(transac)

# Handle error
@above.error
async def above_error(ctx,error):
    if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
        await ctx.send("Please input a number after !above")

# This command will give a list of 10 products with the sale price above arg1 and below arg2
@client.command()
async def between(ctx, arg1,arg2):
    transac = ""

    for tups in filter_between(str(arg1), str(arg2)):
        for tup in tups:
            transac += str(tup) + "\t\t\t"
        transac += "\n"

    await ctx.send("Price\t\t\t\tProduct ID")
    await ctx.send(transac)

# Handle error
@between.error
async def between_error(ctx,error):
    if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
        await ctx.send("Please input a range after !between")

@client.command()
async def help(ctx):
    embed = discord.Embed(
        title='Commands',
        description="All bot command"
    )
    embed.add_field(name="!help", value="List all bot commands",inline=False)
    await ctx.send(embed=embed)

client.run(os.getenv('DISCORD_TOKEN'))