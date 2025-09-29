import addition #as both the files are within the same folder else I had to put folder name at first
print(addition.add())



from addition import add # other way to do the same thing
print(add())

from addition import * # to import all the methods at once , but is generally avoided