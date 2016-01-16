import argparse
import requests
import twitch_urls as urls
import user
import error

def topgames(limit=10, offset=0):
    args = urls.formatargs({"limit": limit, "offset": offset})
    url = urls.topgames() + args
    response = requests.get(url)
    if (response.status_code == 200):
        return response.json()
    else:
        error.failfast(response)


def printtopgames(limit=10, offset=0):
    toplist = [formattopgame(json) for json in topgames(limit, offset)["top"]]
    header = "{: <40}".format("GAME") + "VIEWERS"
    games = "\n".join(toplist)
    out = header + "\n\n" + games
    print(out)


def formattopgame(json):
    game = json["game"]
    viewers = json["viewers"]
    return "{: <40}".format(game["name"]) + str(viewers)


printtopgames()

