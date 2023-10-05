def fibonacci(n):
  # if n == 0:
  #   return 0
  # elif n == 1:
  #   return 1
  # else:
  #   return fibonacci(n - 1) + fibonacci(n - 2)

  fib_list = [0, 1]

  if len(fib_list) <= n:
    while len(fib_list) <= n:
      fib_list.append(fib_list[len(fib_list) - 1] + fib_list[len(fib_list) - 2])

  return fib_list[n]

  


