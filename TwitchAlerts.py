# These are the required libraries to run the bot
import pyttsx3
from twitchio.ext import commands

# This is the code to setup the text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 175)


# This is the code that will run when the bot is started
class Bot(commands.Bot):

  # Initial Bot Setup
  def __init__(self):
    # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
    # prefix can be a callable, which returns a list of strings or a string...
    # initial_channels can also be a callable which returns a list of strings...
    super().__init__(token = '694pw970wlgxijwsxpydbk5u2osd6n', prefix = '!', initial_channels = ['thecapish'])

  # This function will run when the bot is ready
  async def event_ready(self):
        # Notify us when everything is ready!
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

  # This function will run when a user joins the stream
  async def event_join(self, channel, user):
    # This line sends a welcome message in chat
    # await channel.send(f"Welcome to the stream {user.name}")
    await channel.send("Thanks for watching MIT admission officers")
    
    # These lines say the welcome messagte
    # engine.say(f"Welcome to the stream {user.name}")
    engine.say("Thanks for watching MIT admission officers")
    engine.runAndWait()

# These lines run the bot
bot = Bot()
bot.run()