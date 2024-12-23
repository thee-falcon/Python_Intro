import csv

# to create a csv file and write some data to it
with open("data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["transaction_id", "product_id", "price"])
    writer.writerow([100, 1, 5])
    writer.writerow([1001, 2, 10])

# to read a csv file
with open("data.csv") as file:
    reader = csv.reader(file)
    print(list(reader))
    # we can iterat to the file using for loop, but before we iterat in that file, we should comment the print function
    # because even we implement the for loop we will see nothing, because this file has a postion or index
    # and when we convert it the index becomes to end of file, so when we try to iterat to it the index is already in the end of file
    # so we gonna see nothing
    # How we can solve this problem: we can comment the print function or
    #                                resetting the read position to the begining of the file using seek() functi
    file.seek(0)
    for read in reader:
        print(read)