def going_through_file (day, doc_name):
    print("Day ", day)
    the_file = open(doc_name)
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        # melon = words[0]
        # count = words[1]
        # amount = words[2]
        melon, count, amount = words(0, 1, 2)

        print(f"Delivered {count} {melon}s for total of ${amount}")
    the_file.close()


going_through_file (1,"um-deliveries-day-1.txt")
going_through_file (2,"um-deliveries-day-2.txt")
going_through_file (3,"um-deliveries-day-3.txt")



