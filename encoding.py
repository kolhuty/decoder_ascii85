def encode(data: bytes):
    """Кодирует данные в ASCII85"""

    chars = b"!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstu"
    encoded = bytearray()
    padding = 0

    #Разбиваем по 4 байта
    for i in range(0, len(data), 4):
        block = data[i:i + 4]

        if len(block) < 4:
            padding = 4 - len(block)
            block += b'\x00' * padding

        #Преобразуем 4 байта в 32-битное число, используем big-endian
        n = int.from_bytes(block, byteorder='big')

        #Если в байте все нули
        if n == 0 and padding == 0:
            encoded.append(ord('z'))
            continue

        #Переводим в символы
        parts = []
        for _ in range(5):
            n, remainder = divmod(n, 85)
            parts.append(remainder)

        parts = parts[::-1]

        for p in parts:
            encoded.append(chars[p])

        #Удаляем лишние символы
        if padding:
            encoded = encoded[:-padding]

    return bytes(encoded)