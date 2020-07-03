import pkg_resources
my_data = pkg_resources.resource_string(__name__, "foo.dat")
print ("foo.dat bytes", my_data)

exist_flag = pkg_resources.resource_exists(__name__, "foo.dat")
print ("foo.dat exists", exist_flag)

my_stream = pkg_resources.resource_stream(__name__, "foo.dat")
print ("foo.dat stream", my_stream)

my_string = pkg_resources.resource_string(__name__, "foo.dat")
print ("foo.dat string", my_string)

isdir_flag = pkg_resources.resource_isdir(__name__, "Cards_gif")
print ("Cards_gif isdir", isdir_flag)

# my_data = pkg_resources.resource_string(__file__, "foo.dat")
# print ("foo.dat bytes", my_data)
#
# exist_flag = pkg_resources.resource_exists(__file__, "foo.dat")
# print ("foo.dat exists", exist_flag)
#
# my_stream = pkg_resources.resource_stream(__file__, "foo.dat")
# print ("foo.dat stream", my_stream)
#
# my_string = pkg_resources.resource_string(__file__, "foo.dat")
# print ("foo.dat string", my_string)
#
# isdir_flag = pkg_resources.resource_isdir(__file__, "foo.dat")
# print ("foo.dat isdir", isdir_flag)