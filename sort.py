import sys
import csv


def main():
    result_arr = []
    input_arr = []
    args = sys.argv
    use_func = args[1]
    csvname = args[2]
    with open(csvname) as file:
        input_arr = list(csv.reader(file))

    if use_func == "correct_sort":
        for lst in input_arr:
            result_arr.append(correct_sort(lst))
    elif use_func == "incorrect_sort":
        for lst in input_arr:
            result_arr.append(incorrect_sort(lst))

    with open("result_"+csvname, 'w') as file:
        writer = csv.writer(file, lineterminator='\n')
        writer.writerows(result_arr)

def correct_sort(lst):
    return sorted(lst)

def incorrect_sort(lst):
    return lst

if __name__ == "__main__":
    main()
