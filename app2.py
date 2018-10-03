from flask import Flask

app = Flask(__name__)



page = '''
<html>
	<head>
		<title>{title}</title>
	</head>
	<body>
		{content}
	</body>
</html>
'''



students = [
    {'name':'xiaoming'},
    {'name':'xiaohong'},
    {'name':'xiaohei'}
]

pageList = ''
for i,item in enumerate(students):
    if i%2==0 :
        pageList += '<h1 style="background:skyblue;">{name}</h1>'.format(name=item['name'])
    else:
        pageList += '<h1 style="background:pink;">{name}</h1>'.format(name=item['name'])
    


@app.route('/')
def index():
    title = '首页'
    return page.format(title=title,content=pageList)

app.run(debug=True)