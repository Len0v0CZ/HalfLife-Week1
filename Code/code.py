import time
import board
import digitalio
import rotaryio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

keyb = Keyboard(usb_hid.devices)
cons_control = ConsumerControl(usb_hid.devices)
enc = rotaryio.IncrementalEncoder(board.GP18, board.GP17)
last_p = enc.position
button_pins = {
    "SW1": board.GP16,
    "SW4": board.GP19,
    "SW3": board.GP20,
    "SW2": board.GP21
}

buttons = {}
for name, pin in button_pins.items():
    bt = digitalio.DigitalInOut(pin)
    bt.direction = digitalio.Direction.INPUT
    bt.pull = digitalio.Pull.UP
    buttons[name] = {"GPIO": bt, "Last": True}

macros = {
    "SW4": (Keycode.CONTROL, Keycode.A),
    "SW3": (Keycode.CONTROL, Keycode.C),
    "SW2": (Keycode.CONTROL, Keycode.V),
}

while True:
    current_p = enc.position
    p_delta = current_p - last_p

    if p_delta > 0:
        for i in range(p_delta):
            cons_control.send(ConsumerControlCode.VOLUME_INCREMENT)
    elif p_delta < 0:
        for i in range(abs(p_delta)):
            cons_control.send(ConsumerControlCode.VOLUME_DECREMENT)

    last_p = current_p

    for name, data in buttons.items():
        current_state = data["GPIO"].value
        if not current_state and data["Last"]:
            if name == "SW1":
                cons_control.send(ConsumerControlCode.MUTE)
            else:
                keyb.press(*macros[name])
            data["Last"] = False
        elif current_state and not data["Last"]:
            if name != "SW1":    
                keyb.release_all()
            data["Last"] = True

    time.sleep(0.05)