"""
    **과제 내용:**
1. **`Member`** 클래스와 **`Post`** 클래스를 정의하세요.
2. **`Member`** 클래스에는 다음과 같은 속성을 가지고 있어야 합니다.
    - 회원 이름 (**`name`**)
    - 회원 아이디 (**`username`**)
    - 회원 비밀번호 (**`password`**)
3. **`Member`** 클래스에는 다음과 같은 메소드를 가지고 있어야 합니다.
    - 회원 정보를 print 해주는 `display` (회원이름과 아이디만 보여주고 비밀번호는 보여줘서는 안됩니다!)
4. **`Post`** 클래스에는 다음과 같은 속성을 가지고 있어야 합니다.
    - 게시물 제목 (**`title`**)
    - 게시물 내용 (**`content`**)
    - 작성자 (**`author`**) : 회원의 `username` 이 저장되어야 함!
5. 회원 인스턴스를 세개 이상 만들고 `members` 라는 빈리스트에 append를 써서 저장해주세요
    1. members 리스트를 돌면서 회원들의 이름을 모두 프린트 해주세요
6. 각각의 회원이 게시글을 세개 이상 작성하는 코드를 만들어주세요.(회원이 세명이명 총 9개 이상의 post 인스턴스가 만들어져야 합니다). 만들어진 게시글 인스턴스들은 posts 빈리스트에 append를 써서 저장해주세요
    1. for 문을 돌면서 특정유저가 작성한 게시글의 제목을 모두 프린트 해주세요
    2. for문을 돌면서 ‘특정 단어’가 content에 포함된 게시글의 제목을 모두 프린트 해주세요
    """
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


class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def display(self):
        print(f"회원이름: {self.name}")
        print(f"아이디: {self.username}")


class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def display(self):
        print(f"제목: {self.title}")
        print(f"내용: {self.content}")


def main():
    members = []
    posts = []
    print("\n_________스파르타 커뮤니티___________")
    while True:
        print("")
        print("_________메뉴__________")
        print("1. 멤버추가\n2.멤버 이름 출력\n3.포스트 추가  \n4.멤버가 작성한 게시글 제목 출력 \n5.특정 단어 입력하면 게시글 제목과 주인 출력\n")
        num = int(input("숫자를 입력하시오  :"))
        print("")
        if num == 1:
            add_mem(members)
        elif num == 2:
            print_mem(members)
        elif num == 3:
            write_post(members, posts)
        elif num == 4:
            get_title(posts)
        elif num == 5:
            get_content(posts)
        else:
            print("1~5까지만 입력하시오")


def add_mem(members):
    name = input("유저 이름을 입력하세요: ")
    id = input("아이디를 입력하세요: ")
    password = input("비밀번호를 입력하세요: ")
    member = Member(name, id, password)
    members.append(member)


def print_mem(members):

    print("_________멤버목록___________")   # 멤버이름 출력
    for i in members:
        print(i.name)


def write_post(members, posts):

    while True:
        y_n = input(" 멤버의 포스트를 작성하시겠습니까 (Y/N) : ")
        y_n = y_n.lower()

        if y_n == "y":
            members_name = input(
                "포스트 작성할 멤버의 이름을 입력해주세요:  ")  # 입력 받은 이름이있는지 확인

            name_exits = any(i.name == members_name for i in members)

            if not name_exits:  # 같은 이름이 없을때
                print("그런 이름은 없습니다 ")
                continue

            else:  # 같은 이름이있을때  =>>해당 회원의 포스트를 입력
                title = input("제목을 입력하세요: ")
                content = input("내용을 입력하세요: ")
                post = Post(title, content, members_name)
                posts.append(post)

        elif y_n == "n":
            break
        else:
            print("y/n  로만 입력해주세요 ")
            continue


def get_title(post):  # 멤버의 게시글 제목 추력

    mem = input("어떤 멤버의 게시글 제목을 보겠습니까: ")

    for i in post:
        if i.author == mem:
            print("-{}".format(i.title))


def get_content(post):   # 특정 단어를 검색하면 단어가 포함된 게시글의 제목과 주인이 출력됩니다

    word = input("특정 단어를 검색하면 단어가 포함된 게시글의 제목과 주인이 출력됩니다")

    for i in post:
        if word in i.content:
            print("{}단어가 포함된 게시글 제목 : {}   게시글 주인 : {} " .format(
                word, i.title, i.author))


# 프로그램을 시작합니다.
if __name__ == "__main__":
    main()
