# -*- coding: utf-8 -*-

def valid(response):
    return response.status_code == 200

def base():
    return "https://api.twitch.tv/kraken"

def topgames():
    return base() + "/games/top"

def formatargs(args):
    return "?" + "&".join([key + "=" + str(value) for key, value in args.items()])

