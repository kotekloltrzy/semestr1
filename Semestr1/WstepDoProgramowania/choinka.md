```python
ch = int(input(f'Podaj wysokosc choinki: '))
s = ' '


def choinka(h):
    w = 1
    for i in range(h):
        print((h-1)*s, "*"*w)
        h -= 1
        w += 2

choinka(ch)
```
