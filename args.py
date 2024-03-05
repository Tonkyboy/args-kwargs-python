def coffee_spec(size, *additives):
    print(f"Coffee size: {size}")

    for additive in additives:
        print(f"add: {additive}")

    print(additives)


coffee_spec("medium", "milk", "sugar", "caramel")
