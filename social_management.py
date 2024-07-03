class member():

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def display(self):
        print(self.name, self.username)

class post():

    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author 

m1 = member('김아무개', 'kim', '123') 

m2 = member('박아무개', 'park', '1234') 

m3 = member('최아무개', 'choi', '12345') 

members = []

posts = []

members.append(m1)
members.append(m2)
members.append(m3)

for element in members:
    print(element.name)

for element in range(3):
    personal_post = post(f'김타이틀{element+1}', f'김내용{element+1}', m1.name)
    posts.append(personal_post)

for element in range(3):
    personal_post = post(f'박타이틀{element+1}', f'박내용{element+1}', m2.name)
    posts.append(personal_post)

for element in range(3):
    personal_post = post(f'최타이틀{element+1}', f'최내용{element+1}', m3.name)
    posts.append(personal_post)

for element in posts:
    if element.author == '김아무개':
        print(element.title)

for element in posts:
    if '박' in element.content:
        print(element.title)