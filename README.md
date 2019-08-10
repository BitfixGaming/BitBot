
# BitBot

A bot for the [Bitfix Gaming discord](http://discord.gg/jCXTBn9), [based on DMG-Bot](https://github.com/RGameBoy/DMG-Bot)

* Dice roller
* Currency converter (using http://currencyconverterapi.com)
* Game of the day from https://en.wikipedia.org/wiki/List_of_video_games_considered_the_best
* Echoing messages to channels
* Reaction based rank assignment

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Things you need and how to install them

* Python 3.6 or above

### Installing


First, clone this project.

```
$ git clone https://github.com/MrHDR/BitBot.git

```
Install the required python packages with pip.
```
$ pip install -r requirements.txt
```
Rename `config.example.yaml` and add your discord bot key (and optionally your CSE keys) to it.
```
$ mv config.example.yaml config.yaml
$ nano config.yaml

BOT_KEY="YOUR BOT KEY"
```
Finally, start the bot:
```
$ python3 BitBot.py
```

## Adding new extensions

Simply create a new python module inside the `cogs` folder, the bot will automatically attempt to load it on startup. For an example, check out the dice rolling extension `cogs/dice.py` and the [discord.py documention](https://discordpy.readthedocs.io/en/rewrite/index.html).

Please be aware that this project is using the `rewrite` branch of discord.py, keep that in mind when browsing the documentation.

## TODO

* Add role management for ingnoring channels based on clickable reaction emoji's
* Write documentation
* Add tools for moderation
* Add easy introduction for new members