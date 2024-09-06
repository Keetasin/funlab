# from . import funlab
# from pymongo import MongoClient, errors

# def main():
#     options = funlab.get_program_options()
#     app = funlab.create_app()

#     app.run(debug=options.debug, host=options.host,port=int(options.port))

from funlab import web
from pymongo import MongoClient, errors
def main():
    options = web.get_program_options()
    app = web.create_app()
    app.run(debug=options.debug, host=options.host,port=int(options.port))