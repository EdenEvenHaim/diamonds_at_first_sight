def find_highest_price(data):
    prices = [float(row[6]) for row in data]  # Price is in the 7th column
    return max(prices)

def find_average_price(data):
    prices = [float(row[6]) for row in data]  # Price is in the 7th column
    return sum(prices) / len(prices)

def count_ideal_diamonds(data):
    ideal_count = sum(1 for row in data if row[1].lower() == 'ideal')  # Cut is in the 2nd column
    return ideal_count

def find_unique_colors(data):
    colors = set(row[2].upper() for row in data)  # Color is in the 3rd column
    return len(colors), list(colors)

def find_median_carat_premium(data):
    premium_carat = sorted(float(row[0]) for row in data if row[1].lower() == 'premium')  # Carat is in the 1st column, Cut is in the 2nd column
    mid = len(premium_carat) // 2
    if len(premium_carat) % 2 == 0:
        return (premium_carat[mid - 1] + premium_carat[mid]) / 2
    else:
        return premium_carat[mid]

def find_carat_avg_by_cut(data):
    cuts = {}
    for row in data:
        cut = row[1].lower()  # Cut is in the 2nd column
        carat = float(row[0])  # Carat is in the 1st column
        if cut in cuts:
            cuts[cut].append(carat)
        else:
            cuts[cut] = [carat]
    return {cut: sum(carat_list) / len(carat_list) for cut, carat_list in cuts.items()}

def find_price_avg_by_color(data):
    colors = {}
    for row in data:
        color = row[2].upper()  # Color is in the 3rd column
        price = float(row[6]) 
        if color in colors:
            colors[color].append(price)
        else:
            colors[color] = [price]
    return {color: sum(price_list) / len(price_list) for color, price_list in colors.items()}
