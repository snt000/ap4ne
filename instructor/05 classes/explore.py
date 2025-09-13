def explore(obj, name="object"):
    """Print attributes (with values) and methods of a Python object (excluding __dunder__ stuff)."""
    attrs = []
    methods = []
    for n in dir(obj):
        if n.startswith("__"):
            continue  # skip dunder methods
        val = getattr(obj, n)
        if callable(val):
            methods.append(n)
        else:
            attrs.append((n, val))

    print(f"\n=== Exploration of {name} ({type(obj)}) ===")
    print("Attributes:")
    for a, v in attrs:
        # Trim long values for readability
        v_str = str(v)
        if len(v_str) > 60:
            v_str = v_str[:57] + "..."
        print(f"  - {a}: {v_str}")
    print("Methods:")
    for m in methods:
        print(f"  - {m}()")