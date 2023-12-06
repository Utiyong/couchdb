import couchdb
server = couchdb.Server('http://utibe:uticul203@localhost:5984/') 
#CREATE A DATABASE
db_name = 'mydatabase'
try:
    db = server.create(db_name)
except couchdb.http.PreconditionFailed as e:
    db = server[db_name] 

data = {
    'firstname': 'utibe',
    'email': 'utibe@gmail.com'
}

doc_id, doc_rev = db.save(data)
#READ DATA
doc = db.get(doc_id)
print(doc)

#UPDATE DATA
doc = db.get(doc_id)
doc['program'] = 'computer_engineering'
db.save(doc)

#MODIFY DATA
def modify_data(doc_id, new_data):
    doc = db.get(doc_id)
    doc.update(new_data)
    db.save(doc)

new_data = {'level': '500level'}
modify_data(doc_id, new_data)

#DELETE A DOCUMENT
#doc = db.get(doc_id)
#db.delete(doc)


