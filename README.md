# Twitch CLI

## About

Command-line interface for accessing a limited number of twitch features from the command-line.
Created for the lulz.

## Dependencies

 Python 3.4.3+
 livestreamer
 vlc

## Usage

```bash
$ twitch username
```

Watch username's stream with vlc in best available quality.

```bash
$ twitch -u username
```

Login to username's account. Will prompt for password.

```bash
$ twitch -f
```

List streamers you are following.

```bash
$ twitch
```

List games by number of viewers

```bash
$ twitch -g game
```

List top streamers for game

