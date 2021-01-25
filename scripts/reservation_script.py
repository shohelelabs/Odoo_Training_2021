from xmlrpc import client

url ='https://shohelelabs-odoo-training-2021-odoolibrary-1987828.dev.odoo.com'
db ='shohelelabs-odoo-training-2021-odoolibrary-1987828'
username ='admin'
password ='admin'

common = client.ServerProxy("{}/xmlrpc/2/common".format(url))
print(common.version)

uid = common.authenticate(db,username,password,{})
print(uid)

models = client.ServerProxy("{}/xmlrpc/2/object".format(url))

model_access = models.execute_kw(db, uid, password,
                              'library.reservation','check_access_rights',
                              ['write'],{'raise_exception':False})
print(model_access)


books = models.execute_kw(db, uid, password,
                         'library.book', 'search_read',
                         [[['level','in',['intermediate','beginner']]]])
print(books)

book = models.execute_kw(db, uid, password,
                        'library.book','search',
                        [[['name','=','Accounting 201']]])
print(book)


reservation_fields = models.execute_kw(db, uid, password,
                        'library.reservation','fields_get',
                        [],{'attributes': ['string','type','required']})

print(reservation_fields)

new_reservation =  models.execute_kw(db, uid, password, 'library.reservation', 'create',
                                [
                                    {
                                        'book_id':book[0], 
                                        'duration':5,
                                    }
                                ]
                                )

print(new_reservation)