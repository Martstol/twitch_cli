# -*- coding: utf-8 -*-
import requests
import twitch_urls as urls
import user
import error
import args


def getrequest(url, params):
    headers = {"accept": "application/vnd.twitchtv.v3+json"}
    return requests.get(url, params=params, headers=headers)


def topgames(limit=10, offset=0):
    url = urls.topgames()
    args = {"limit": limit, "offset": offset}
    response = getrequest(url, args)
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


def printgamestreams(game):
    pass


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

