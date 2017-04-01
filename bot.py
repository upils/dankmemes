#!/usr/bin/env python3

import json
import discord
import asyncio
from discord.ext import commands

client = discord.Client()

# Récupération d'un meme par son nom
def getMemeByName(memeName):
  with open('memes.json') as file:
    data = json.load(file)
  link = "no link know for this meme."
  for meme in data["memes"]:
    if meme["name"] == memeName:
      link = meme["url"]
  print(link)
  return link

# Liste des memes actuels
def getMemeList():
  with open('memes.json') as file:
    data = json.load(file)
  liste = ""
  for meme in data["memes"]:
    liste = liste + "{}\t <{}>\n".format(meme["name"], meme["url"])
  print("A list have been asked.")
  return liste

# Ajout d'un meme
def addMeme(name, url):
  with open('memes.json') as file:
    data = json.load(file)
  entry = {"name":name, "url":url}
  with open('memes.json','w') as file:
    json.dump(data, file)
  return data

# Suppression d'un meme
def delMeme(name):
  with open('memes.json') as file:
    data = json.load(file)
  dico = {}
  for meme in data["memes"]:
    dico[meme["name"]] = meme["url"]
  dico.pop(name)
  vieilleliste = {'memes':[ {"name":k,"url":dico.get(k)} for k in dico ]}
  with open('memes.json','w') as file:
    json.dump(vieilleliste, file)
  print("The meme {} has been added.".format(name))
  return data


@client.event
async def on_ready():
  print('Logged in as')
  print(client.user.name)
  print(client.user.id)
  #await client.send_message(message.channel, "I'm here to send memes. Type !help to get some help to get the list \
  #                                            of currently available commands.")

@client.event
async def on_message(message):
  if message.content.startswith('! '):

    tmp = await client.send_message(message.channel, 'Meme INCOMING...')
    memeName = message.content[len('! '):].strip()
    meme = getMemeByName(memeName)
    await client.edit_message(tmp, meme)

  elif message.content.startswith('!list'):

    tmp = await client.send_message(message.channel, 'List INCOMING...')
    liste = getMemeList()
    await client.edit_message(tmp, liste)

  elif message.content.startswith('!add '):

    tmp = await client.send_message(message.channel, 'Adding a meme...')
    memeName = message.content[len('!add '):].split()[0]
    print(memeName)
    memeURL = message.content[len('!add '):].split()[1]
    print(memeURL)
    addMeme(memeName, memeURL)
    await client.edit_message(tmp,'Meme has been added !')

  elif message.content.startswith('!del '):

    tmp = await client.send_message(message.channel, 'Deleting a meme...')
    memeName = message.content[len('!del '):].split()[0]
    delMeme(memeName)
    await client.edit_message(tmp,'The meme has been deleted !')

  elif message.content.startswith('!help'):

    await client.send_message(message.channel, "Commands: \n \
    ! <meme> to send a meme on the channel \n \
    !list to list the available memes \n \
    !add <name> <url> to add a new meme \n \
    !del <name> to delete a meme \n")



client.run('Mjk2MzMyNjkzMTUzNzc1NjE2.C7xdNw.2L3Wk4NtAzD5zu5ZRg24spbpggw')
