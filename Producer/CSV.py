import csv
import time

def datafromfile():
    a = []
    with open('Location/file_Name.csv') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        #a = [x.replace("\n", "") for x in a]
        a=csvfile.readlines()
        time.sleep(5)
        return a


if __name__ == '__main__':
    print(datafromfile())
