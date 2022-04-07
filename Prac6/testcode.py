def csv_reader(animals.csv):
    file = open(animals.csv)
    result = file.read().split("\n")
    return result
