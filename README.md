# LolPy

A Python-based clone of the lolcat command that generates rainbow-colored text.
## Installation

Directly download and install lolpy using the following command:

    curl -o /usr/local/bin/lolpy https://github.com/dniminenn/lolpy/raw/main/lolpy.py
    chmod +x /usr/local/bin/lolpy

## Usage

usage: lolpy [-h] [-f FREQUENCY] [-g {rainbow,ocean}] [-i] [FILE ...]

    -h, --help: Show help message.
    -f, --frequency: Set color frequency. Default is 1.
    -g, --gradient {rainbow,ocean}: Choose a gradient style. Default is rainbow.
    -i, --interactive: Launch in interactive mode. Type and see the rainbow in real time.
    FILE: Files to read. If empty, stdin is used.

For example:

```cat /proc/cpuinfo | lolpy -f 1```
or simply
```lolpy -g ocean /proc/cpuinfo```

## Interactive Mode

To enter the interactive mode, simply use the -i flag:

```lolpy -i```

## Gradients

LolPy supports different gradient styles:

    rainbow: The classic, vibrant spectrum of colors.
    ocean: Cool, blueish tones reminiscent of the sea.

To use a gradient, specify it with the -g option:

```echo "Hello World" | lolpy -g ocean```

## License

LolPy is licensed under the MIT License. Refer to the LICENSE file for more details.
