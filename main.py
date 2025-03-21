import sys
import base64

def encode():
    "Переводит байты в ASCII85"
    data = sys.stdin.buffer.read()

    encoded_data = base64.a85encode(data)
    # вывод
    sys.stdout.buffer.write(encoded_data)
    sys.exit(0)

def decode():
    "Переводит символы ASCII85 в байты"
    data = sys.stdin.read()
    # Декодируем ASCII85
    decoded_bytes = base64.a85decode(data, adobe=False)
    # Выводим результат в stdout
    sys.stdout.buffer.write(decoded_bytes)
    sys.exit(0)

def check_arg():
    # Разрешенные аргументы
    valid_args = {"-e", "-d"}
    args = sys.argv[1:]

    #проверка на неизвестные элементы
    unknown_args = [arg for arg in args if arg not in valid_args]

    if unknown_args:
        sys.stderr.write(f"Error: Option does not exist. Call --help {' '.join(unknown_args)}\n")
        sys.exit(1)

    #проверяем конфликт -e и -d
    if "-e" in args and "-d" in args:
        sys.stderr.write("Error: Cannot use options -e и -d at the same time\n")
        sys.exit(2)

    return "-d" in args

if __name__ == '__main__':
    #определяем режим
    if check_arg():
        decode()
    else:
        encode()