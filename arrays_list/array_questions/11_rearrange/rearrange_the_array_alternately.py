# Complex
def rearrange(self, arr, n):
	temp = n // 2
	mx = arr[n - 1] + 1

	for i in range(temp): arr[i] = mx * arr[n - 1 - i] + arr[i]

	lst = n - 1
	if n % 2: arr[lst], lst = arr[temp], lst - 1

	for j in range(temp):
		i = temp - j - 1
		arr[lst], arr[lst - 1] = arr[i] % mx, arr[i] // mx
		lst = lst - 2

	return
