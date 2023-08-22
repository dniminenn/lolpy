# LolPy

A Python-based clone of the lolcat command that generates rainbow-colored text.

Tested on your favourite Linux distribution. Ensure Python is installed on the system before continuing.

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
    sunset: With reds, oranges, and purples.
    forest: Evoking feelings of deep woods with greens and browns.
    winter: Shades of blue and white to represent cold and snowy scenes.
    candy: Pinks, purples, and light blues.
    tropical: Vibrant blues, greens, and yellows.

To use a gradient, specify it with the -g option:

```echo "Hello World" | lolpy -g ocean```

```lolcat -g tropical /proc/cpuinfo```

## License

LolPy is licensed under the MIT License. Refer to the LICENSE file for more details.
