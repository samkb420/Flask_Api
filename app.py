from flask import Flask,request
import descrption
# importing Required Modules

from flask_restplus import Api,Resource,fields
import requests
'''
This is a simple api made with Flask and flask_restplus

'''

app = Flask(__name__)
api = Api(app, version=descrption.app_version,title='Inspire App Api Backend',
            description=descrption.banner
            )
ns_home = api.namespace('Home', description="Get Request for Home")
ns_blog = api.namespace('Blog', description="Post Request for Blogs")
ns_app = api.namespace('App', description="App Statistic")


test = api.model('User',{
    "Name":fields.String,
    "Title":fields.String,
    "Blog-body":fields.String,
    "Username":fields.String,
    "password":fields.String
   
})

# test1 = api.model('App',{
#     "Date":fields.String,
#     "Visits":fields.Integer,
#     "likes":fields.Integer,
#     "Accounts":fields.Integer
# })

@ns_home.route('/')
class Hellow(Resource):
    def get(self):
        return {'name':'Samuel Kago'}
    def post(Resource):
        hello= request.get_json()

        return {'Helloow':hello}
    def put(self):
        return {'Author':'John Doe'}
@ns_blog.route('/')
class  Blog(Resource):
    def put(self):
        return {'Author':'John Doe'}
    
    def get(self):
        return {'Author':'John Doe'}
    @api.expect(test)
    def post(Resource):

        data=api.payload

        data1 = { 
            
            "Name":data['Name'],
            "Title":data['Title'],
            "Blog-body":data['Blog-body'],
            "Username":data['Username']
        }

        requestt = request.get_json(data1)
            
        

        return {"Post":requestt}
ns_app = api.namespace('App', description="App Statistic")
@ns_app.route('/')
class Sam(Resource):
    
    def get(self):
        
        datt ={'Date':'Monday','Visits':200, "likes":900,"Accounts":1000 }

        # App_analytics = request.get_json(datt)
        return {"Stats":datt}





if __name__ == "__main__":
    app.run(debug=True)



