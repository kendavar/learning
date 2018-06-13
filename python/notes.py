def new_decorator(func):
	def wrap_func():
		print("CODE HERE BEFORE EXECUTTING FUNC")
		func()
		print("FUNC() has been called")

	return wrap_func

@new_decorator
def func_needs_decorator():
	print("This function is in need of a decorator!")


func_needs_decorator = new_decorator(func_needs_decorator)

func_needs_decorator()
