import base64

data = b"Hello world!"

#Кодирование
encoded = base64.a85encode(data)
print("Закодировано:", encoded)

#Декодирование
decoded = base64.a85decode(encoded)
print("Декодировано:", decoded)
