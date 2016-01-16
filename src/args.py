import argparse

def get_parser():
    parser = argparse.ArgumentParser(description="Command-line interface for accessing twitch streams from the command-line")
    parser.add_argument("-t", "--top", action="store_true", help="List games by number of viewers")
    parser.add_argument("-g", "--game", help="List the top streamers for the given game. Does accept names with spaces", nargs="+")
    parser.add_argument("stream", metavar="username", nargs="?", help="Watch a stream, using vlc with the best available quality")
    parser.add_argument("-u", "--user", help="Login to a twitch account. Will prompt for password")
    parser.add_argument("-f", "--follows", action="store_true", help="List streamers the logged in user is following if they are streaming")
    parser.add_argument("-v", "--version", action="version", version="version 0.0")
    return parser


