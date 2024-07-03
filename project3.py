# Member 클래스와 Post 클래스를 정의
class Member:
    def __init__(self,name,username,password):
        self.name = name
        self.username = username
        self.password = password
    
    def display(self):
        return print(f"회원이름 : {self.name}, 회원아이디 : {self.username}")
    
class Post(Member):
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author= author
        
        
members = []
posts = []        
member1 = Member("감자","포카칩","1234")
member2 = Member("바나나","바나나칩","1234")
member3 = Member("초코","초코송이","1234")

members.append(member1)
# members.append(member2)
# members.append(member3)

for member in members :
    print(member.name)
    
    
post1 = Post("포카칩제목1","포카칩내용1",member1.username)
post2 = Post("포카칩제목2","포카칩내용2",member1.username)
post3 = Post("포카칩제목3","포카칩내용3",member1.username)
post4 = Post("바나나칩제목1","바나나칩내용1",member2.username)
post5 = Post("바나나칩제목2","바나나칩내용2",member2.username)
post6 = Post("바나나칩제목3","바나나칩내용3",member2.username)
post7 = Post("초코송이제목1","초코송이내용1",member3.username)
post8 = Post("초코송이제목2","초코송이내용2",member3.username)
post9 = Post("초코송이제목3","초코송이내용3",member3.username)


posts.append(post1)
posts.append(post2)
posts.append(post3)
posts.append(post4)
posts.append(post5)
posts.append(post6)
posts.append(post7)
posts.append(post8)
posts.append(post9)

for post in posts:
    if post.author == member1.username:
        print(post.title)
        
    if "바나나" in post.content:
        print(post.title)