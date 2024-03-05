def coffee_spec(size, **details):
    print(f"Coffee size: {size}")

    for key, values in details.items():
        print(f"detail: {key}: {values}")

    print(details)

coffee_spec("medium", prize=5.99, temp=90, intensity="strong")