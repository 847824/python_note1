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


product = '''
<h1>{productName}</h1>
p{productContent}</p>
'''


productsList = ''


proList = [
    {
        'name':'苹果',
        'content':'红红的苹果'
    },
    {
        'name':'雪梨',
        'content':'红红的雪梨'
    },
    {
        'name':'香蕉',
        'content':'红红的香蕉'
    },
]

for item in proList:
    productsList = productsList + product.format(productName=item['name'],productContent=item['content'])
# print(productsList)



@app.route('/')
def index():
    title = '淘宝首页'

    return page.format(title=title,content=productsList)



app.run(debug=True)