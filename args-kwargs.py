def coffee_spec(size, *additives, **details):
    print(f"Coffee size: {size}")

    for additive in additives:
        print(f"add: {additive}")

    for key, values in details.items():
        print(f"detail: {key}: {values}")


coffee_spec("medium", "milk", "sugar", "caramel", prize=5.99, temp=90, intensity="strong")
