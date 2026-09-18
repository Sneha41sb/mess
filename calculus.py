def f(x):
    return x**2

def gradient(x):
    return 2*x        # derivative of x^2 is 2x

x = 10.0
lr = 0.1
for step in range(20):
    x = x - lr * gradient(x)

print(x)   # converges toward 0 — the minimum of x^2