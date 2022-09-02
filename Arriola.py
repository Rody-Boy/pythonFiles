from pyDatalog import pyDatalog
#given terms
pyDatalog.create_terms("Y","Bear","Elephant","Cat","Black","Gray","Brown","Big","Small","size","Color","X","Z")
+size("Bear","Big")
+size("Elephant","Big")
+size("Cat","Small")
+Color("Bear","Brown")
+Color("Elephant","Gray")
+Color("Cat","Black")

#search bar/query
print(size(X,Y))
print(Color(X,Y))
print(size(X,"Big"))
print(Color(X,"Black"))