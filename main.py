import sys
import base64

data = sys.stdin.buffer.read()

encoded_data = base64.a85encode(data)

sys.stdout.buffer.write(encoded_data)