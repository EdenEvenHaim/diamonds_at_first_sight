# Read CSV data into a list
def load_csv_data(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    # Split the header and data
    header = lines[0].strip().split(',')
    data = [line.strip().split(',') for line in lines[1:]]
    return header, data