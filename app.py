import os
from load_data import load_csv_data
from display_data import display_data
from search import search_data
from cart_operations import add_to_cart, delete_from_cart
from cart_display import show_cart_items
from analysis import (find_highest_price, find_average_price, count_ideal_diamonds,
                      find_unique_colors, find_median_carat_premium, find_carat_avg_by_cut,
                      find_price_avg_by_color)

# clear:
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# main function:
def main():
    file_path = 'diamonds.csv'
    header, data = load_csv_data(file_path)
    cart = []

    while True:
        # Display the menu
        print("\nMenu:")
        print("1. Add to Cart")
        print("2. Search from Catalog")
        print("3. Delete from Cart")
        print("4. Show Items in Cart")
        print("5. Exit")
        print("6. Clear")
        print("7. Analyze Data")  # New option for analysis

        choice = input("\nEnter your choice (1-7): ")

        if choice == '1':
            item_id = input("Enter the ID of the item to add to the cart: ")
            add_to_cart(data, cart, item_id)

        elif choice == '2':
            print("\nSearch Options:")
            print("1. Search by Price")
            print("2. Search by Cut")
            print("3. Search by Color")
            search_choice = input("Choose a search option (1-3): ")

            if search_choice in ['1', '2', '3']:
                search_term = input("Enter the search term: ")
                search_results = search_data(data, search_term, search_choice)
                if search_results:
                    display_data(header, search_results)
                else:
                    print("No results found.")
            else:
                print("Invalid search option. Please choose 1, 2, or 3.")

        elif choice == '3':
            item_id = input("Enter the ID of the item to delete from the cart: ")
            delete_from_cart(cart, item_id)

        elif choice == '4':
            show_cart_items(header, cart)
        
        elif choice == '5': # Exit
            print("Exiting the program...")
            break

        elif choice == '6': 
            clear()  # Clear  

        elif choice == '7':  # Analyze Data
            print("\nData Analysis Options:")
            print("1. Find the highest diamond price")
            print("2. Find the average price of a diamond")
            print("3. Count the number of ideal type diamonds")
            print("4. Find the unique colors of diamonds")
            print("5. Find the median carat of premium diamonds")
            print("6. Find the carat average for each cut type")
            print("7. Find the price average for each color type")
            
            analysis_choice = input("Choose an analysis option (1-7): ")
            
            if analysis_choice == '1':
                print("Highest Diamond Price:", find_highest_price(data))
            elif analysis_choice == '2':
                print("Average Price of a Diamond:", find_average_price(data))
            elif analysis_choice == '3':
                print("Number of Ideal Type Diamonds:", count_ideal_diamonds(data))
            elif analysis_choice == '4':
                num_colors, colors = find_unique_colors(data)
                print("Number of Unique Colors:", num_colors)
                print("Colors:", ', '.join(colors))
            elif analysis_choice == '5':
                print("Median Carat of Premium Diamonds:", find_median_carat_premium(data))
            elif analysis_choice == '6':
                carat_avg_by_cut = find_carat_avg_by_cut(data)
                print("Carat Average for Each Cut Type:")
                for cut, avg in carat_avg_by_cut.items():
                    print(f"{cut.title()}: {avg:.2f}")
            elif analysis_choice == '7':
                price_avg_by_color = find_price_avg_by_color(data)
                print("Price Average for Each Color Type:")
                for color, avg in price_avg_by_color.items():
                    print(f"{color.title()}: {avg:.2f}")
            else:
                print("Invalid analysis option. Please choose 1-7.")
        
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
