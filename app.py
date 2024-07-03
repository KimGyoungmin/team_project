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


class Member:

    def __init__(self, name="", username="", password=""):  # name, username, password 생성
        self.name = name
        self.username = username
        self.password = password
        self.members = []


    def display(self):  # 회원정보 출력(비밀번호는 보여주면 안된다)
        if not self.members:
            return print("회원이 아무도 없습니다.")
        else:         
            for i in range(len(self.members)):
                name = self.members[i][0]
                username = self.members[i][1]
                password = self.members[i][2]
                id = self.members[i][3]
                print(f"회원이름 : {name} 회원아이디 : {username} 회원 비밀번호 : {"*"*len(password)}  primarykey : {id}")
                

    def create_member(self, new_name, new_username, new_password):  # 회원정보 생성
        new_member = [new_name, new_username, new_password]
        self.members.append(new_member)
        self.members[-1].append(len(self.members))
        self.name = new_name
        self.username = new_username
        self.password = new_password
        
        


member_chk = Member()
member_chk.create_member('파이썬', 'python', '1234')
member_chk.create_member('자바', 'java', '1234')
member_chk.create_member('씨에스에스', 'css', '1234')
member_chk.display()


class Post(Member):
    def __init__(self,title="", content="",author = Member().username):
        self.title = title
        self.content = content
        self.author = author
        
        
        
        
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
