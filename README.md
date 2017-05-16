# DankMemes bot

This is a very simple bot to allow users to easily post memes on the channel.

Memes are stored in the memes.txt file.

The bot uses [discord.py](https://github.com/Rapptz/discord.py).

To build the image :

```
docker build -t dankmeme .
```

To run the script :

```
docker run -d --rm --name dankmeme -e "DISCORD_KEY=API_KEY_TO_REPLACE" -v $PWD/memes.txt:/opt/app/memes.txt dankmeme:latest
```

With docker-compose, you will have to create a `.env` file with the line :

```
DISCORD_KEY=API_KEY_TO_REPLACE
```

Then, you can launch with :

```
docker-compose up -d
```
