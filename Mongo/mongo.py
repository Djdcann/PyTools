from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['pymongo_test']

posts = db.posts
data = {
    'id': '1',
    'content': 'ayy',
    'author': 'D_rack'
}
result = posts.insert_one(data)
print('One post: {0}'.format(result.inserted_id))