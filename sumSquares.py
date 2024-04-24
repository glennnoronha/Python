import multiprocessing

def calculate_sum_squares(start, end, results):
    total = 0
    for x in range(start, end + 1):
        total += x ** 2
    results.put(total)

def main():
    first_num = int(input("Enter first number: "))
    last_num = int(input("Enter last number: ")) 

    cores = multiprocessing.cpu_count()
    print(f"Number of processes: {cores}")

    total_numbers = last_num - first_num + 1
    numbers_per_core = total_numbers // cores
    remaining_numbers = total_numbers % cores

    print(f'Subrange lengths:')
    ranges = []
    start = first_num
    for i in range(cores):
        end = start + numbers_per_core - 1
        if i < remaining_numbers:
            end += 1
        print(f'Core {i + 1}: {start} to {end}')
        ranges.append((start, end))
        start = end + 1

    sq = multiprocessing.Queue()
    processes = []

    for i, (start, end) in enumerate(ranges):
        process = multiprocessing.Process(target=calculate_sum_squares, args=(start, end, sq))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    total_square = 0
    while not sq.empty():
        total_square += sq.get()

    print(f"The total sum of squares from {first_num} to {last_num} is: {total_square}")

if __name__ == "__main__":
    main()
