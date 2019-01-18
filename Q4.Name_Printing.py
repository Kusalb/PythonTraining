"""Get the first name and last name from a user and use different string
formatting techniques that we learnt in class to get a formatted string.
For example: If user’s first name is Ram and last name is Bahadur, the output
should be: Hello! Ram Bahadur."""

_first_name = input ("First Name: ")
_last_name = input ("Last Name: ")

print("Hello! " + _first_name + " " + _last_name )
print("Hello! {} {}".format(_first_name, _last_name))
print(f"Hello! {_first_name} {_last_name}")
print("Hello! {f_name} {l_name}".format( f_name= _first_name ,  l_name =_last_name ))
