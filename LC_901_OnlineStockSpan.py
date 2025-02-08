

class StockSpanner:
	
	def __init__(self):
		self.stack = []

	# monotonic stack solution | O(n) | O(n)
	def next(self, price):
		span = 1
		while self.stack and self.stack[-1][0] <= price:
			span += self.stack.pop()[1]
			
		self.stack.append((price, span))

		return span

	'''	
	# optimized brute force | O(n^2) | O(n)
	def next(self, price):
		
		self.prices.append(price)
		
		span = 1
		indx = len(self.prices)-2

		while indx >= 0 and self.prices[indx] <= price:
			span += self.spans[indx]
			indx -= self.spans[indx]
		
		self.spans.append(span)
		return span
	
	# brute force approach | O(n^2) | O(n)
	def next(self, price):

		self.prices.append(price)
		span = 0
		for index in range(len(self.prices)-1,-1,-1):
			
			if self.prices[index] <= price:
				span += 1
			else:
				break
			
		return span
	'''

prices = [100, 80, 60, 70, 60, 75, 85]

stock_spanner = StockSpanner()

spans = []
for price in prices:
	span = stock_spanner.next(price)
	spans.append(span)

print(spans)
	