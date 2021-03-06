#!/usr/bin/python3
#-*- coding: utf-8 -*-
import requests
import twitch_urls as urls
import user
import error
import args
import subprocess
import getpass

def clientid():
    return "l9sezw9vvl2azkde7hxf9yu31yyaxjs"


def getrequest(url, params):
    headers = {"accept": "application/vnd.twitchtv.v3+json"}
    return requests.get(url, params=params, headers=headers)


def topgames(limit, offset=0):
    url = urls.topgames()
    args = {"limit": limit, "offset": offset}
    response = getrequest(url, args)
    if urls.valid(response):
        return response.json()
    else:
        error.failfast(response)


def printtopgames(limit, offset=0):
    toplist = [formattopgame(json) for json in topgames(limit, offset)["top"]]
    header = "{: <40}".format("GAME") + "VIEWERS"
    games = "\n".join(toplist)
    out = header + "\n\n" + games
    print(out)


def formattopgame(json):
    game = json["game"]
    viewers = json["viewers"]
    return "{: <40}".format(game["name"]) + str(viewers)


def gamestreams(name, limit=10, offset=0):
    url = urls.game()
    args = {"game": name, "limit": limit, "offset": offset}
    response = getrequest(url, args)
    if urls.valid(response):
        return response.json()
    else:
        error.failfast(response)


def printgamestreams(name, limit=10, offset=0):
    gamelist = [formatgame(json) for json in gamestreams(name, limit, offset)["streams"]]
    header = "{: <20}".format("STREAMER") + "{: <80}".format("TITLE") + "VIEWERS"
    streams = "\n".join(gamelist)
    out = header + "\n\n" + streams
    print(out)


def formatgame(json):
    viewers = json["viewers"]
    streamer = json["channel"]["name"]
    title = json["channel"]["status"]
    return "{: <20}".format(streamer) + "{: <80}".format(title) + str(viewers)


def openlivestreamer(name):
    cmd = "livestreamer twitch.tv/" + name + " best"
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    status = proc.wait()
    if status != 0:
        print(proc.stdout.read().decode("ascii").strip().split("\n")[-1])


def login(username):
    password = getpass.getpass()
    url = urls.auth()
    args = {"response_type": "token", "client_id": clientid(), "redirect_uri": "http://localhost", "scope": "user_read"}
    response = requests.get(url, params=args)
    print(response.status_code)
    print(response.headers)
    print(response.text)


parser = args.get_parser()
args = parser.parse_args()
print(args)
if args.top:
    printtopgames(args.top)
elif args.game:
    printgamestreams(args.game)
elif args.stream:
    openlivestreamer(args.stream)
elif args.follows:
    print(args.follows)
elif args.user:
    login(args.user)
else:
    parser.print_usage()

