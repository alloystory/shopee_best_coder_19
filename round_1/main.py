import csv
from pathlib import Path

if __name__ == "__main__":
    filepath = Path("./spam_cleaned.csv")
    output = Path("./output.csv")
    with filepath.open('r') as input_file:
        with output.open("w") as output_file:
            input_list = list()
            reader = csv.reader(input_file)
            for idx, row in enumerate(reader):
                if idx == 0:
                    continue
                print(tylistpe(row[3]))
                for word in row[3]:
                    input_list.append([idx, word])
                    print([idx, word])
                    break
                break