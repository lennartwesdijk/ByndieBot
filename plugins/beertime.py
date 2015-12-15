import datetime
import random

from will.plugin import WillPlugin
from will.decorators import respond_to, hear

class BeerTimePlugin(WillPlugin):
    @hear("( beer |^beer$| beertime | ^beertime$)")
    @respond_to("beertime")
    def reply_to_beertime(self, message):
        """
        beertime: I tell you how long it is until Jesse brings you beer.
        """
        self.reply(message, get_beer_slogan())


def get_beer_slogan():
    now = datetime.datetime.now()
    today = datetime.date.today()
    todaybeeroclock = now.replace(hour=17, minute=00, second=00)
    todayendbeeroclock = now.replace(hour=18, minute=00, second=00)
    todayend = now.replace(hour=23, minute=59, second=59)
    weekday = today.weekday()

    formatcountdown = todaybeeroclock - now

    if now < todayend and 0 <= weekday <= 4:
        if todaybeeroclock < now <= todayendbeeroclock:
            formatcountdown = todayendbeeroclock - now
        else:
            formatcountdown = todaybeeroclock - now

    beertimeslogans = [
        "It's BEER time! Go on, you know you want one...",
        "I got 99 problems & BEERTIME solves all of 'em",
        "Trust me, you can dance...BEERTIME!",
        "A hard earned thirst needs a big cold beer",
        "Have a BEER, It's the most natural thing in the world",
        "Remember! Beer as food-value, but food does not have beer-value",
        "BEER will save the world! I don't know how, but it will",
        "BEER! I only drink to make YOU more interesting",
        "Hey, looks like its BEERTIME, better grab me a cold one",
        "Drink good BEER, with GOOD friends",
        "The party is not over till the beer is in the belly",
        "All your BEER are belong to us",
        "I need to do something about my Guzzelitis",
        "My idea of a balanced diet is a BEER in each hand",
        "Jesse will come soon, he WILL be the HERO of your day",
        "A beer a day keeps the doctor away. Have one!",
        "Shhh...Yep, I hear a BEER calling me",
        "Friends bring happiness into your life, best friends bring BEER!",
        "It makes you see double...and feel single. Have one!",
        "Beauty lies in the hands of the BEERHOLDER",
        "Wish you were BEER",
        "Life is brewtiful",
        "Unlike BEER, love doesn't taste good when it's cold",
        "BEER doesn't ask silly questions, BEER understands",
        "Everything I needed in life, i learned from BEER"
    ]

    tooearlyslogans = [
        "It's too early for BEER, you could have a problem...",
        "Be smart...Be safe...Be sober...",
        "Addiction is self-destruction...",
        "And they all claim they can stop drinking any time they want to...",
        "Come on man...",
        "Less drinking, more thinking...",
        "Alcohol is a parent to domestic violence...",
        "Drink water...refresh, rehydrate, replenish...",
        "Alcohol is not the answer right now...",
        "You are not working right now...go back to work...",
        "You need much less BEER than you think you need right now...0 to be honest...",
        "Don't rush anything...when the time is right it'll happen",
        "Stay focused, excited and passionate about what you do...",
        "There will be a time when everything will fall into place..."
    ]

    weekendlogans = ["FFS... it's the WEEKEND, go home and relax!"]

    if weekday > 4:
        return "(jesse) {}".format(random.choice(weekendlogans))
    elif todaybeeroclock <= now < todayendbeeroclock:
        return "(jesse) {}".format(random.choice(beertimeslogans))
    else:
        s = formatcountdown.seconds
        h, s = divmod(s, 3600)
        m, s = divmod(s, 60)

        if h > 0:
            hours = '{} hours, '.format(h)
        else:
            hours = ''

        if m > 0:
            minutes = '{} minutes and '.format(m)
        elif h == 0:
            minutes = ''

        seconds = '{} seconds'.format(s)

        return "(jesse) {} Just wait another {}{}{}".format(
            random.choice(tooearlyslogans), hours, minutes, seconds)
