# A Simple Autologin Bot in Python

This is a simple python autologin bot I made because I was annoyed with the internet solution my apartment used, which required me to login on a splash page every day or so to have internet. This doesn't play well with SSH only servers...

The `autologin_bot.py` script is designed to be run as a `systemd` process. It reads a text file (example given by 'example_login.txt`) containing your login info and then proceeds to test your internet periodically. If it can't connect, it uses the credentials from the text file and logs you back in.

**This was designed for Linux. Small tweaks in the `ping` function will be required to use this with Windows.**

## Version

The script was written with Python v3.8.3.

## Dependencies

The script only has one external dependency: `mechanize` (v0.4.5 at the time of writing).

If on Arch Linux:

```
$ sudo pacman -S python-mechanize
```
otherwise `pip` works too:

```
$ pip3 install mechanize
```

## Login Text File

An example file, `example_login.txt`, gives a template for storing your login info to be read by the bot script. *Now, I had a simple login password that was unique and not attached to anything sensitive. I suggest you do the same.*

## Running the Script

Run the script from the command line as such:

```
$ python autologin_bot.py credential_file_path
```

or

```
$ python autologin_bot.py credential_file_path delay_between_pings
```

The first command uses the default delay of 5 minutes between internet pings. Now just use with `systemd` or with whatever you fancy!
