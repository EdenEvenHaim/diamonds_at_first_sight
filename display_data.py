def display_data(header, data):
    print("\n".join(header))
    print("-" * 70)
    for row in data:
        print("\t".join(row))
