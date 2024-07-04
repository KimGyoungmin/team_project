
import hashlib

class Member:
    def __init__(self, name, userid, password):
        self.name = name
        self.userid = userid
        self.password = password


    def display(self):
        print(f"멤버 이름: {self.name}")


class Post:
    def __init__(self, title, content, author, members_id):
        self.title = title
        self.content = content
        self.author = author  # 멤버 이름
        self.members_id = members_id  # 멤버 id

    def display(self):
        print(f"제목: {self.title}")
        print(f"내용: {self.content}")
        print(f"저자: {self.author}")


def main():
    members = []
    posts = []
    print("\n_________스파르타 커뮤니티___________")
    while True:
        print("")
        print("_________메뉴__________")
        print("1.멤버추가\n2.멤버 이름 출력\n3.포스트 추가 (로그인 해야함) \n4.멤버가 작성한 게시글 제목 출력 \n5.특정 단어 입력하면 게시글 제목과 주인 출력\n")
        num = input("숫자를 입력하시오  :")
        print("")
        if num == "1":
            add_mem(members)
        elif num == "2":
            print_mem(members)
        elif num == "3":
            write_post(members, posts)
        elif num == "4":
            get_title(posts)
        elif num == "5":
            get_content(posts)
        else:
            print("1~5까지만 입력하시오")


def hash_password(password):
    # 비밀번호를 해싱합니다.
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password


def add_mem(members):
    name = input("유저 이름을 입력하세요: ")

    while True:
        id = input("아이디를 입력하세요: ")
        # Id 가 중복되는 값이 있으면 check_duplicate 가 True값 리턴
        if not check_duplicate(members, id):
            break

    unhassed_password = input("비밀번호를 입력하세요: ")
    hashed_password = hash_password(unhassed_password)
    member = Member(name, id, hashed_password)
    members.append(member)


def check_duplicate(members, id):
    for i in members:
        if id == i.userid:
            print("중복되는 아이디가 있습니다 다시입력하세요 ")
            return True


def print_mem(members):

    print("_________멤버목록___________")   # 멤버이름 출력
    for i in members:
        i.display()


def login(members, login_id):  # 맴버객체 배열과 로그인 아이디 받아옴

    unhassed_password = input("비밀번호를 입력하세요: ")  # 해싱전비번
    hashed_password = hash_password(unhassed_password)  # 해싱후비번

    for i in members:

        if i.userid == login_id:  # 로그인 아이디와 같은 아이디 가진 객체찾기
            if i.userid == login_id and i.password == hashed_password:  # 아이디와 비밀번호가 둘다 맞을떄
                return True
            else:
                print(" 아이디나 비밀번호가 틀렸습니다!! ")  # 아이디와 비밀번호 둘중 하나라도 틀렸을떄
                return False


def write_post(members, posts):

    while True:
        y_n = input("포스트를 작성하시겠습니까 (Y/N) : ")
        y_n = y_n.lower()
        exist = False
        if y_n == "y":
            members_id = input(
                "포스트 작성할 아이디를 입력해주세요:  ")

            for i in members:
                if i.userid == members_id:  # 같은 아이디있을때 그아이디로  로그인하러감

                    exist = True
                    if not login(members, members_id):  # 로그인 실패
                        break

                    title = input("\n제목을 입력하세요: ")  # 로그인 성공했을시   포스트입력

                    # 제목 ,내용 ,로그인한사람이름 , 로그인한 사람 아이디  저장
                    content = input("내용을 입력하세요: ")

                    post = Post(title, content, i.name, members_id)
                    posts.append(post)
                    continue

            if not exist:

                print("해당 아이디가 존재하지 않습니다.")  # 같은 아이디가 없을 때 메시지 출력

        elif y_n == "n":
            break
        else:
            print(" y/n  로만 입력해주세요 ")
            continue


def get_title(post):  # 멤버의 게시글 제목 추력

    mem = input("어떤 멤버의 게시글 제목을 보겠습니까: ")

    for i in post:
        if i.author == mem:
            print("-{}".format(i.title))


def get_content(post):   # 특정 단어를 검색하면 단어가 포함된 게시글의 제목과 주인이 출력됩니다

    word = input("특정 단어를 검색하면 단어가 포함된 게시글의 제목과 주인이 출력됩니다: ")
    exist = True
    for i in post:
        if word in i.content:
            exist = False
            print("{}단어가 포함된 게시글 제목 : {}   게시글 주인 : {} " .format(
                word, i.title, i.author))
    if exist:
        print("\n그런 단어를 포함한 게시물은 없습니다")


# 프로그램을 시작합니다.
if __name__ == "__main__":
    main()
