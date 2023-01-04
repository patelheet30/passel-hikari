# PASSEL-HIKARI

This is a hikari port of the passel bot. I don't really like discord.py so this is
why this port exists.

## Run Bot Locally (Your own laptop)

1) <u>**Download**</u> the repo from above.
2) Unzip the file and open up `main.py`
3) Insert your bot token between the speech marks in`TOKEN=""`
4) Replace INSERT_HERE with the server id the bot is going to be in as an integer(whole number) in `default_enabled_guilds=INSERT_HERE`
5) Open up terminal/command prompt and navigate to folder where `main.py` is.
6) Run `pip install -r requirements.txt` in terminal/command prompt.
7) Open up `info.py` and do what the file tells you to do
8) Now run this if you're on Windows:

```bash
py main.py
```

8) If on Mac run this:

```bash
python3 main.py
```

9) Make sure you've enabled Message Content Intent in the Bot section of your Application of the Discord Developer Portal

## Run Bot on Fly.io

1) Go to https://github.com/stoir/passel_public/blob/main/HostingViaFlyIo.pdf
2) Follow all the steps. Instead of performing step 3, 4 and 5 like it says in the pdf, follow steps 1 to 7 from the section above.