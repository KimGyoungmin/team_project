# ----- 코드 정의 ------
class Member:
    def __init__(self, name,username,password):
        self.name = name
        self.username = username
        self.password = password

    def display(self):
        print(f"회원 이름: {self.name},아이디:{self.username}")

m1 = Member(name="John", username="John", password="<PASSWORD>")
m2 = Member(name="Jack", username="Jack", password="<PASSWORD>")
m3 = Member(name="Jak", username="Jak", password="<PASSWORD>")

members =[]

members.append(m1)
members.append(m2)
members.append(m3)

for member in members:
    member.display()




# class Post:
#     # TODO : 코드 구현이 필요합니다.
#     pass

# # ----- 코드 실행 ------
# members = []
# posts = []

# # TODO : 코드 구현이 필요합니다.pyth