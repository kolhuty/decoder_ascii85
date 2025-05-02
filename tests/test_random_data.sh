#!/bin/bash

# Это эталонная реализация теста с рандомизацией. Можете использовать её или её фрагменты.
# Она гораздо проще, чем написали многие, можете прямо её использовать, но корректно в
# CI интегрировать, и вам зачтётся.

# Делаем случайный файл random.bin из 2048 байтиков
dd if=/dev/random bs=2K count=1 status=none of=random.bin

# При помощи эталонной питоновской реализации делаем random.a85 -- те же случайные байтики,
# но закодированные в ASCII85
python3 -c 'import sys
import base64
sys.stdout.buffer.write(base64.a85encode(sys.stdin.buffer.read()))
' <random.bin >random.a85

# Кодируем и декодируем случайные байтики и случайные ASCII85
# кодером и декодером соответственно
python3 ../ascii85.py -e <random.bin >random.a85.test
python3 ../ascii85.py -d <random.a85 >random.bin.test

# Тестирование кодера
if ! cmp -s random.a85 random.a85.test; then
  echo Encoder failed on random data >&2
  exit 1
fi

# Тестирование декодера
if ! cmp -s random.bin random.bin.test; then
  echo Decoder failed on random data >&2
  exit 1
fi

# Если дошли до сюда, всё хорошо
echo Ok! >&2
exit 0