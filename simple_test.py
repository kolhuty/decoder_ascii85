import base64

original_data = "Hello world!"

# Кодирование
encoded = base64.a85encode(original_data)
print("Закодировано:", encoded)

# Декодирование
decoded = base64.a85decode(encoded)
print("Декодировано:", decoded)

# Проверка
assert original_data == decoded, "Данные не совпадают!"