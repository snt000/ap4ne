import inspect

def demo_func(a, b, c=3, d=4, *args, e, f=6, **kwargs):
    pass

sig = inspect.signature(demo_func)

for name, param in sig.parameters.items():
    print(name, param.kind, param.default)
