
def base():
    return "https://api.twitch.tv/kraken"

def topgames():
    return base() + "/games/top"

def formatargs(args):
    return "?" + "&".join([key + "=" + str(value) for key, value in args.items()])

