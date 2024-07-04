import hashlib


class Member:
    def __init__(self, name,username,password):
        self.name = name
        self.username = username
        self.password = password

    def hash_pw(password):
        hashed_pw = hashlib.SHA-256(password.endode()).hexdigest()
        return (hashed_pw)


    def display(self):
        print(f"회원 이름: {self.name},아이디:{self.username}")



class Post(Member):
    def __init__(self, name , username , password , title , content):
        super().__init__(name, username , password)
        self.title = title
        self.content = content
        self.author = username

    def posts(self):
        print(f"제목: {self.title} 내용: {self.content} 작성자: {self.author}")


m1 = Member(name="John", username="John", password="<PASSWORD>")
m2 = Member(name="Jm", username="Jm", password="<PASSWORD>")
m3 = Member(name="je", username="je", password="<PASSWORD>")

m4_name = input('이름을 입력하세요.')
m4_username = input('닉네임을 입력하세요.')
m4_password = input('비밀번호를 입력하세요.')

m4 = Member(m4_name, m4_username, m4_password)



m1_post_1 = Post("John", "John", "<PASSWORD>", "첫 번째 글", "이것은 첫 번째 게시물입니다.")
m1_post_2 = Post("John", "John", "<PASSWORD>", "첫 번째 글", "이것은 두 번째 게시물입니다.")
m1_post_3 = Post("John", "John", "<PASSWORD>", "첫 번째 글", "이것은 세 번째 게시물입니다.")

m2_post_1 = Post("Jm", "Jm", "<PASSWORD>", "첫 번째 글", "이것은 첫 번째 게시물입니다.")
m2_post_2 = Post("Jm", "Jm", "<PASSWORD>", "첫 번째 글", "이것은 두 번째 게시물입니다.")
m2_post_3 = Post("Jm", "Jm", "<PASSWORD>", "첫 번째 글", "이것은 세 번째 게시물입니다.")

m3_post_1 = Post("je", "je", "<PASSWORD>", "첫 번째 글", "이것은 첫 번째 게시물입니다.")
m3_post_2 = Post("je", "je", "<PASSWORD>", "첫 번째 글", "이것은 두 번째 게시물입니다.")
m3_post_3 = Post("je", "je", "<PASSWORD>", "첫 번째 글", "이것은 세 번째 게시물입니다.")



m4_title_1 = input('제목을 입력하세요.')
m4_content_1 = input('내용을 입력하세요.')

m4_post_1 = Post(m4_name, m4_username , m4_password, m4_title_1, m4_content_1)

members = []

members.append(m1)
members.append(m2)
members.append(m3)
members.append(m4)


posts = []
posts.append(m1_post_1)
posts.append(m1_post_2)
posts.append(m1_post_3)
posts.append(m2_post_1)
posts.append(m2_post_2)
posts.append(m2_post_3)
posts.append(m3_post_1)
posts.append(m3_post_2)
posts.append(m3_post_3)
posts.append(m4_post_1)


for member in members:
    member.display()
    print("작성한 게시물 입니다")
    for post in posts:
        if post.author == member.username:
            post.posts()

            
