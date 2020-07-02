import pkg_resources
# my_data = pkg_resources.resource_string("Cards_gif", "C2.gif")
# print ("C2.gif bytes", my_data)

# exist_flag = pkg_resources.resource_exists(__name__, "C2.gif")
# print ("C2.gif exists", exist_flag)
#
# my_stream = pkg_resources.resource_stream(__name__, "C2.gif")
# print ("C2.gif stream", my_stream)
#
# my_string = pkg_resources.resource_string(__name__, "C2.gif")
# print ("C2.gif string", my_string)
#
isdir_flag = pkg_resources.resource_isdir(__name__, "Cards_gif")
print ("Cards_gif isdir", isdir_flag)

# print (dir(pkg_resources))

# print (pkg_resources.__name__)
#
# x = 10
# print (x)
# print (dir(x))