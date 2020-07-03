import os
print ("first way")
data_dir = os.path.join(os.path.dirname(__file__), 'data')
data_path = os.path.join(data_dir, 'message.eml')
print ("getcwd",os.getcwd())
print ("data_path",data_path)
with open(data_path, encoding='utf-8') as fp:
    eml = fp.read()
print ("first way",eml)

# print ("second way")
# # In Python 3, resource_string() actually returns bytes!
# import email_test.tests.data
# from pkg_resources import resource_string
# eml = resource_string('email_test.tests.data', 'message.eml').decode('utf-8')
# print ("second way",eml)

# print ("second way")
# # In Python 3, resource_string() actually returns bytes!
# from pkg_resources import resource_string
# eml = resource_string(__name__, 'message.eml').decode('utf-8')
# print ("second way",eml)

# print ("third way")
from importlib_resources import files
# # Reads contents with UTF-8 encoding and returns str.
# eml = files('email_test.tests.data').joinpath('message.eml').read_text()
# print ("third way",eml)

# print ("fourth way")
# import email_test.tests.data
# eml = files(email_test.tests.data).joinpath('message.eml').read_text()