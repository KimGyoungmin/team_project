"""
    **과제 내용:**

1. **`Member`** 클래스와 **`Post`** 클래스를 정의하세요.
2. **`Member`** 클래스에는 다음과 같은 속성을 가지고 있어야 합니다.
    - 회원 이름 (**`name`**)
    - 회원 아이디 (**`username`**)
    - 회원 비밀번호 (**`password`**)
3. **`Member`** 클래스에는 다음과 같은 메소드를 가지고 있어야 합니다.
    - 회원 정보를 print해주는 `display` (회원이름과 아이디만 보여주고 비밀번호는 보여줘서는 안됩니다!)
4. **`Post`** 클래스에는 다음과 같은 속성을 가지고 있어야 합니다.
    - 게시물 제목 (**`title`**)
    - 게시물 내용 (**`content`**)
    - 작성자 (**`author`**) : 회원의 `username` 이 저장되어야 함!d
5. 회원 인스턴스를 세개 이상 만들고 `members` 라는 빈리스트에 append를 써서 저장해주세요
    1. members 리스트를 돌면서 회원들의 이름을 모두 프린트 해주세요
6. 각각의 회원이 게시글을 세개 이상 작성하는 코드를 만들어주세요.(회원이 세명이명 총 9개 이상의 post 인스턴스가 만들어져야 합니다). 만들어진 게시글 인스턴스들은 posts 빈리스트에 append를 써서 저장해주세요
    1. for 문을 돌면서 특정유저가 작성한 게시글의 제목을 모두 프린트 해주세요
    2. for문을 돌면서 ‘특정 단어’가 content에 포함된 게시글의 제목을 모두 프린트 해주세요
"""

# ----- 코드 정의 ------
from pprint import pprint


class Member:
    key = 0  # 고유값 설정

    # 생성자 지정
    def __init__(self, name="", username="", password=""):  # name, username, password 생성
        self.name = name
        self.username = username
        self.password = password
        self.members = []  # 회원 목록 저장할 리스트

    # 회원정보 출력
    def display(self):  # 회원정보 출력(비밀번호는 보여주면 안된다)
        if not self.members:  # 회원 목록이 null 값일때
            print()
            print("------회원이 아무도 없습니다------")
            print()
        else:
            print()
            print("------전체 회원 목록------")
            for member in self.members:  # 각각의 회원을 출력
                name, username, password, key = member
                pprint(f"회원이름:{name}    회원아이디:{username}    회원 비밀번호:{
                    '*'*len(password)}    primarykey:{key}")
            print()
    # 회원정보 생성

    def create_member(self, new_name, new_username, new_password):
        if self.check_member(new_username):  # 아이디 중복 확인
            Member.key += 1  # 고유키 값 1증가
            new_member = [new_name, new_username, new_password, Member.key]
            self.members.append(new_member)
            print()
            print("------아이디 생성완료------")
            print()
            return True
        return False

    # username 유효성 검사

    def check_member(self, username):
        if not self.members:
            return True
        for member in self.members:
            if username == member[1]:
                print()
                print("------아이디가 중복되었습니다------")
                print()
                return False
        return True

    # 저장된 회원 목록들을 쉽게 접근하기 위해서 return
    def get_members(self):
        return self.members


class Post():
    post_key = 0

    def __init__(self, title="", content="", author=""):
        self.title = title
        self.content = content
        self.author = author
        self.contents = []

    def check(self, author, password, members):
        for member in members:
            if author == member[1]:
                if password == member[2]:
                    print()
                    print("------게시글을 작성해주세요------")
                    print()
                    return True
        print()
        print("------회원 정보를 다시 확인해주세요------")
        print()
        return False

    def post_display(self):
        if not self.contents:
            print()
            print("------게시글이 없습니다------")
            print()
        else:
            print()
            print("------전체 게시글------")
            for post in self.contents:
                title, content, author, post_key = post
                pprint(f"순번:{post_key} 제목:{title} 작성자:{author} 내용:{content}")
                print()

    def write(self, new_title, new_content, new_author):
        Post.post_key += 1
        new_post = [new_title, new_content, new_author, Post.post_key]
        self.contents.append(new_post)
        self.title = new_title
        self.content = new_content
        self.author = new_author
        return True

    def get_posts(self):
        return self.contents


member_chk = Member()
post_chk = Post()

# member_chk.create_member('파이썬', 'python', '1234')
# member_chk.create_member('자바', 'java', '1234')

# member_chk.display()


"""
result
'회원이름:파이썬    회원아이디:python    회원 비밀번호:****    primarykey:1'
'회원이름:자바    회원아이디:java    회원 비밀번호:****    primarykey:2'
"""


# post_chk.write("첫번째 글", "안녕하세요!", "python")
# post_chk.write("두번째 글", "반갑습니다!", "python")

# post_chk.write("첫번째 글", "안녕하세요!", "java")
# post_chk.write("두번째 글", "반갑습니다!", "java")

# post_chk.post_display()
"""
result
'순번:1 제목:첫번째 글 작성자:python 내용:안녕하세요!'
'순번:2 제목:두번째 글 작성자:python 내용:반갑습니다!'
'순번:4 제목:첫번째 글 작성자:java 내용:안녕하세요!'
'순번:5 제목:두번째 글 작성자:java 내용:반갑습니다!'

"""

post_exit = True
while post_exit:
    print("""------원하는 프로그램실행 번호를 입력하세요------

회원등록/1    회원리스트/2     게시글작성/3      게시글목록/4        종료/5""")
    select_num = int(input("번호입력 : "))
    if select_num == 1:  # 회원등록
        while True:
            print("------회원 정보를 입력해주세요------")
            new_name = input("회원 이름 : ")
            new_username = input("회원 아이디 :")
            new_password = input("비밀번호 :")
            # member_chk.create_member(new_name, new_username, new_password)
            if member_chk.create_member(new_name, new_username, new_password) == True:
                break
            else:
                print("회원등록/1     메인으로 돌아가기/2")
                chk_create = int(input("번호입력 : "))
                if chk_create == 1:
                    continue
                elif chk_create == 2:
                    break

    elif select_num == 2:  # 회원리스트
        member_chk.display()

    elif select_num == 3:  # 게시글작성
        while True:
            print("------게시글 입력 권한을 확인하겠습니다------")
            new_author = input("회원 아이디 :")
            password = input("회원 비밀번호 :")
            if post_chk.check(new_author, password, member_chk.get_members()) == True:
                new_title = input("제목 입력 : ")
                new_content = input("내용 입력 : ")
                post_chk.write(new_title, new_content, new_author)
                print("------게시글 작성완료------")
                break
            else:
                print("회원 정보 다시 입력하기/1     메인으로 돌아가기/2")
                chk_create = int(input("번호입력 : "))
                if chk_create == 1:
                    continue
                elif chk_create == 2:
                    break

    elif select_num == 4:  # 게시글목록
        post_chk.post_display()
        print()

    elif select_num == 5:  # 터미널종료
        print("------게시글 프로그램 종료------")
        post_exit = False

"""
    **추가 도전 과제:**
1. input을 이용하여 Member 인스턴스 만드는것을 사용자가 터미널에서 할 수 있게 해주세요.
2. post도 터미널에서 생성할 수 있게 해주세요.
3. (심화)비밀번호 해싱이 무엇인지 공부한 후 hashlib 라이브러리를 써서 회원 비밀번호를 해시화하여 저장하게 해주세요.
"""

"""
 **평가**

- 클래스와 인스턴스 개념을 설명할 수 있는가?
- 메소드와 어트리뷰트(속성)을 설명할 수 있는가?
- 클래스를 정의할 수 있는가?
- 인스턴스를 생성할 수 있는가?
"""
