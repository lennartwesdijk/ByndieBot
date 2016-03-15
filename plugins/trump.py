import requests

from will.plugin import WillPlugin
from will.decorators import respond_to

class TrumpPlugin(TrumpPlugin):
    @respond_to("trump")
    def get_trump(self, message):
        """
        trump: I bring you things Trump said.
        """
        self.reply(message,
                   requests.get("http://looq.nl/trump/index.php").content)
