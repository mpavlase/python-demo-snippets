# `__getattr__` vs `__getattribute__`

**__getattr__** - is called for **non-existing** attribute access\
**__getattribute__** - is called for **existing** attribute access
 

```python
class A:
    name = 'name of class A'

    def __getattr__(self, key):
        print(f'... called __getattr__ to retrieve {key=}')
        return '__getattr__ result'

    def __getattribute__(self, key):
        print(f'... called __getattribute__ to retrieve {key=}')
        return super().__getattribute__(key)

a = A()
print(f'{a.name=}')
print(f'{a.age=}')
```

Result:
```
... called __getattribute__ to retrieve key='name'
a.name='name of class A'
... called __getattribute__ to retrieve key='age'
... called __getattr__ to retrieve key='age'
a.age='__getattr__ result'
```

# Reference
- https://stackoverflow.com/questions/4295678/understanding-the-difference-between-getattr-and-getattribute
