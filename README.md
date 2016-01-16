# Twitch CLI

## About

Command-line interface for accessing a limited number of twitch features from the command-line.
Created for the lulz.

## Dependencies

* Python 3.4.3+
* livestreamer
* vlc

## Usage

* twitch *username*

Watch *username's* stream with vlc in best available quality.

* twitch -u *username*

Login to *username's* account. Will prompt for password.

* twitch -f

List streamers you are following.

* twitch

List games by number of viewers

* twitch -g *game*

List top streamers for *game*

