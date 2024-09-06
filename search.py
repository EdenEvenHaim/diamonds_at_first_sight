def search_data(data, term, search_choice):
    if search_choice == '1':  # Search by Price
        return [row for row in data if term.lower() in row[6].lower()]  
    elif search_choice == '2':  # Search by Cut
        return [row for row in data if term.lower() in row[1].lower()] 
    elif search_choice == '3':  # Search by Color
        return [row for row in data if term.lower() in row[2].lower()]  
    else:
        return []
