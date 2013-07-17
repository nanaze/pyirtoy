

"""Python IR Toy util

Usage: pyirtoy.py /dev/ttyACM0
"""

import serial
import sys

def RunDevice(device):
  ir = serial.Serial(device, 9600)
  print 1
  # Set to initial mode
  for i in range(5):
    ir.write(chr(0x00))
  print 2
  # Enter sampling mode
  ir.write('S')

  response = ir.read(3)
  assert response == 'S01', 'Expected reply of "S01" from USB toy'





def main():
  if len(sys.argv) != 2:
    sys.exit(__doc__)

  device_path = sys.argv[1]
  RunDevice(device_path)


if __name__ == "__main__":
  main();

