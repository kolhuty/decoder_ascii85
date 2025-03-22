def decode(encoded: bytes) -> bytes:
    """Декодирует данные из ASCII85"""

    chars = b"!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstu"
    char_to_value = {char: i for i, char in enumerate(chars)}
    encoded = encoded.replace(b'\n', b'')

    decoded = bytearray()
    padding = 0
    i = 0

    while i < len(encoded):
        #Обработка 'z'
        if encoded[i] == ord('z'):
            if i + 1 < len(encoded) and encoded[i + 1] != ord('z'):
                decoded += b'\x00\x00\x00\x00'
                continue

        #Обрабатываем по 5 символов
        group = []
        valid_chars = 0
        while len(group) < 5 and i < len(encoded):
            char = encoded[i]
            if char == ord('z'):
                break

            if char not in char_to_value:
                raise ValueError(f"Invalid ASCII85 character: {chr(char)}")

            group.append(char_to_value[char])
            valid_chars += 1
            i += 1

        #Дополняем последнюю группу до 5 символов
        if valid_chars < 5:
            padding = 5 - valid_chars
            group += [84] * padding

        #Преобразуем группу в число
        value = 0
        for j in range(5):
            value = value * 85 + group[j]

        #Число в 4 байта
        decoded_block = value.to_bytes(4, byteorder='big')

        #Удаляем лишние байты
        if padding:
            decoded += decoded_block[:-padding]
        else:
            decoded += decoded_block

    return bytes(decoded)