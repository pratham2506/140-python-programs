import zlib
string = "hello world!hello world!hello world!hello world!"
compressed_string = zlib.compress(string.encode())
decompressed_string = zlib.decompress(compressed_string).decode()
print("Original String : ",string)
print("Compressed String : ",compressed_string)
print("Decompressed String : ",decompressed_string)

