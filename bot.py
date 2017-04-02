#!/usr/bin/env python3
# Author : upils

import json
import discord
import asyncio
from discord.ext import commands

client = discord.Client()

# Charger le fichier de memes
def loadFile():
  data = {}
  with open('memes.txt') as file:
    for line in file:
      name = line.split('\t')[0]
      url = line.split('\t')[1].strip()
      data[name] = url
  return data

# Récupération d'un meme par son nom
def getMemeByName(memeName):
  memesDict = loadFile()
  if memeName in memesDict:
    link = memesDict[memeName]
  else:
    link = "no link know for this meme."
  return link

# Liste des memes actuels
def getMemeList():
  memesDict = loadFile()
  list = ['','']
  i = 0
  for k in memesDict:
    if list[i].count('\n') > 41:
      i = i + 1
    list[i] = list[i] + "{}\t <{}>\n".format(k, memesDict.get(k))
  print("A list have been asked.")
  return list

# Ajout d'un meme
def addMeme(name, url):
  with open('memes.txt', 'a') as file:
    file.write('{}\t{}\n'.format(name, url))

# Suppression d'un meme
def delMeme(name):
 # with open('memes.json') as file:
 #   data = json.load(file)
 # dico = {}
 # for meme in data["memes"]:
 #   dico[meme["name"]] = meme["url"]
 # dico.pop(name)
 # memesDict = {'memes':[ {"name":k,"url":dico.get(k)} for k in dico ]}
 # with open('memes.json','w') as file:
 #   json.dump(memesDict, file)
 # print("The meme {} has been added.".format(name))
 # return data
  with open('memes.txt', 'r') as file:
    lines = file.readlines()
  with open('memes.txt', 'w') as file:
    for line in lines:
        if line.split('\t')[0] != name:
          print(line)
          file.write(line)


@client.event
async def on_ready():
  print('Logged in as')
  print(client.user.name)
  print(client.user.id)
  #await client.send_message(message.channel, "I'm here to send memes. \
#Type !help to get some help to get the list \
#of currently available commands.")

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
    for chunk in liste:
     await client.send_message(message.channel, chunk)

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

#Load API key
with open('api.key') as file:
    APIKEY = file.read().strip()

#Run the bot
client.run(APIKEY)
