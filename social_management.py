class member():

    def __init__(self):
        self.name = ''
        self.username = ''  
        self.password = ''  

    def display(self):
        print(self.name, self.username)

class post():

    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author 

m1 = member() 
m1.name = '김아무개'
m1.username = 'kim'
m1.password = '123'

m2 = member() 
m2.name = '박아무개'
m2.username = 'park'
m2.password = '1234'

m3 = member() 
m3.name = '최아무개'
m3.username = 'choi'
m3.password = '12345'

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

# sadasdasdsdasd