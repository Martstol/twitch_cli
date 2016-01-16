# -*- coding: utf-8 -*-
import requests
import twitch_urls as urls
import user
import error
import args

def topgames(limit=10, offset=0):
    args = urls.formatargs({"limit": limit, "offset": offset})
    url = urls.topgames() + args
    response = requests.get(url)
    if (urls.valid(response)):
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

parser = args.get_parser()
args = parser.parse_args()
if args.top:
    printtopgames()
elif args.game:
    print(" ".join(args.game))
elif args.stream:
    print(args.stream)
elif args.follows:
    print(args.follows)
elif args.user:
    print(args.user)
else:
    parser.print_usage()

