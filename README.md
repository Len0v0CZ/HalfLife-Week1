# Macro Keyboard

A compact macro keyboard featuring 3 keys and 1 rotary encoder for task automation.
## Components
- Raspberry Pi Pico
- 3x Mechanical Switches
- 1x KY-040 Rotary Encoder
- Custom PCB
- 3D-printed case (base and lid)

![Case](https://halflife.hackclub-assets.com/hackclub-half-life/sessions/kH6ziJEaMe9t9W8X0J1zLBPEueoZX2RM/ebee5b7a31c7b85fe8f497933886ca6db6aebc852d3f4755699ab61d480d59c7.png)
![PCB](https://halflife.hackclub-assets.com/hackclub-half-life/sessions/kH6ziJEaMe9t9W8X0J1zLBPEueoZX2RM/15623268d085ac0246efcaabf5fc8caf50ff0bf703609071a75f22913d1ad481.png)

## Hardware Assembly
1. Solder the Pico, switches, and encoder to the PCB.
2. Mount the assembled PCB into the 3D-printed base using the M3 sized studs.
3. Attach the lid.

## Software Setup
1. Install CircuitPython on the Raspberry Pi Pico, more precisely it uses `adafruit_hid` library.
2. Save the Python script as `code.py` in the root directory.

## Usage
The rotary encoder adjusts the system volume and its button toggles mute. The three mechanical switches can be bound in `code.py`.