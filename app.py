import hashlib

password = "Hello World!"
hash_object = hashlib.sha256(password.encode())

# 해시 값을 16진수 문자열로 변환
hashed_password = hash_object.hexdigest()

print(f"원본 비밀번호: {password}")
print(f"해시된 비밀번호: {hashed_password}")