import sys
import base64

def encode_data(data: bytes):
    """Кодирует данные в ASCII85"""
    return base64.a85encode(data)

def decode_data(data: bytes):
    """Декодирует данные из ASCII85"""
    return base64.a85decode(data, adobe=False)

def read_input():
    """Читает данные из stdin"""
    return sys.stdin.buffer.read()

def write_output(data: bytes, add_newline: bool = True):
    """Записывает результат в stdout."""
    sys.stdout.buffer.write(data + (b'\n' if add_newline else b''))

def handle_encoding():
    """Обрабатывает режим кодирования."""
    data = read_input()
    encoded = encode_data(data)
    write_output(encoded)

def handle_decoding():
    """Обрабатывает режим декодирования."""
    data = read_input()
    try:
        decoded = decode_data(data)
        write_output(decoded)
    except ValueError:
        sys.stderr.write("Error: Invalid ASCII85 input\n")
        sys.exit(3)

def parse_arguments(args: list[str]):
    """Парсит аргументы командной строки."""
    result = {
        'encode': False,
        'decode': False,
        'help': False,
        'error': None
    }

    valid_args = {"-e", "-d", "--help"}
    unknown = [a for a in args if a not in valid_args]

    if unknown:
        result['error'] = f"Unknown options: {', '.join(unknown)}"
        return result

    if "--help" in args:
        result['help'] = True
        return result

    if "-e" in args and "-d" in args:
        result['error'] = "Cannot use both -e and -d"
        return result

    result['encode'] = "-e" in args
    result['decode'] = "-d" in args
    return result

def show_help():
    """Показывает справку."""
    with open("help.txt", "rb") as f:
        sys.stdout.buffer.write(f.read())

def main():
    """Основная логика программы."""
    args = parse_arguments(sys.argv[1:])

    if args['error']:
        sys.stderr.write(f"Error: {args['error']}\n")
        sys.exit(1)

    if args['help']:
        show_help()
        sys.exit(0)

    try:
        if args['decode']:
            handle_decoding()
        else:
            handle_encoding()
    except KeyboardInterrupt:
        sys.stderr.write("\nOperation cancelled\n")
        sys.exit(4)

if __name__ == '__main__':
    main()