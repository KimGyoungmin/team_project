import hashlib

class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        hash_object = hashlib.sha256(password.encode())
        hashed_password = hash_object.hexdigest()
        self.password = hashed_password

    def display(self):
        return f'이름: {self.name}, 닉네임: {self.username}'

class Post:
    def __init__(self, title, content, Member):
        self.title = title
        self.content = content
        self.author = Member.username

members = []

member_1 = Member('김철수', 'IronWater', '철수9999')
member_2 = Member('김영희', 'ZeroH', '영희8888')
member_3 = Member('바둑이', 'Chess', '바둑7777')

member_4_name = input('이름을 입력하세요.')
member_4_username = input('닉네임을 입력하세요.')
member_4_password = input('비밀번호를 입력하세요.')

member_4 = Member(member_4_name, member_4_username, member_4_password)

members.append(member_1)
members.append(member_2)
members.append(member_3)
members.append(member_4)

for member in members:
    print(member.password)

for member in members:
    print(member.name)

posts = []

post_1 = Post('안녕하세요.', '가입했습니다. 잘부탁드립니다.', member_1)
post_2 = Post('처음 뵙겠습니다.', '첫 가입입니다.', member_2)
post_3 = Post('멍멍멍멍', '왈왈왈', member_3)
post_4 = Post('등산을 갔다왔습니다.', '경치가 좋네요.', member_1)
post_5 = Post('등산 부럽네요.', '저는 야근중입니다.', member_2)
post_6 = Post('멍멍멍', '으르렁', member_3)
post_7 = Post('잘 지내고 계신가요.', '처음 가입했을때가 엊그제같군요.', member_1)
post_8 = Post('안녕하세요.', '오래간만입니다.', member_2)
post_9 = Post('야옹야옹', '야옹', member_3)

post_0_title = input('제목을 입력하세요.')
post_0_content = input('내용을 입력하세요.')

post_0 = Post(post_0_title, post_0_content, member_4)

posts.append(post_1)
posts.append(post_2)
posts.append(post_3)
posts.append(post_4)
posts.append(post_5)
posts.append(post_6)
posts.append(post_7)
posts.append(post_8)
posts.append(post_9)
posts.append(post_0)

for post in posts:
    if post.author == member_3.username:
        print(post.title)
        
for post in posts:
    if '가입' in post.content:
        print(post.title)