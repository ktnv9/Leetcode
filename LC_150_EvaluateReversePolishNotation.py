def evaluateRPN(tokens):
	
	# use stack to efficiently keep track of numbers and operators.
	stack = []
	
	for token in tokens:
		if token == "+":

			stack.append(stack.pop() + stack.pop())

		elif token == "-":

			# note the order of pops.
			b, a = stack.pop(), stack.pop()
			stack.append(a-b)

		elif token == "*":

			stack.append(stack.pop() * stack.pop())

		elif token == "/":

			# note the order of pops.
			b, a = stack.pop(), stack.pop()
			stack.append(int(a/b))
			
		else:

			# important to convert the input token to int.
			stack.append(int(token))

	return stack[0]

tokens = ["2","1","+","3","*"]
print(evaluateRPN(tokens))

tokens = ["4","13","5","/","+"]
print(evaluateRPN(tokens))

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(evaluateRPN(tokens))

