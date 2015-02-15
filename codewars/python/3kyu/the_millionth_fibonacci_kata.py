# http://www.codewars.com/kata/53d40c1e2f13e331fc000c26/train/python
# n where 1000000 <= n <= 1500000

def fib(n):
  if n == 0 or n == 1: return n
  elif n < 0:
    return (-1)**(n % 2 + 1) * fib(-n)
  else: return fib_iter(1, 0, 0, 1, n)


def fib_iter(a, b, p, q, count, factor = 1):

  if count == 0: return b
  elif count % 2 == 0:
    if p == 0:
      new_p = 1
      new_q = 1
    else:
      new_p = p * factor - 1
      new_q = q * factor

    if factor == 1: factor = 3
    else: factor = factor ** 2 - 2
    return fib_iter(a, b, new_p, new_q, count / 2, factor)
  else:
    return fib_iter(
      b * q + a * q + a * p,
      b * p + a * q,
      p,
      q,
      count - 1,
      factor
    )

