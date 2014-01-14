#!/usr/bin/env python
from __future__ import print_function
import serial
import sys
import time

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Usage:")
        print("    python %s DEVICE_PORT [BAUD_RATE]")

    port = sys.argv[1]
    baudrate = 9600
    if len(sys.argv) > 2:
        baudrate = int(sys.argv[2])

    with serial.Serial(port=port, baudrate=baudrate, timeout=1) as ser:
        with open(time.strftime("Serial-%y%m%y-%H%M%S.txt"), 'w') as f:
            try:
                while True:
                    line = ser.readline()
                    f.write(line)
            except KeyboardInterrupt:
                pass
