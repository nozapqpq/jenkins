import sys
import csv


def main():
    target_lst = []
    ok_flg = True
    args = sys.argv
    csvname = args[1]
    with open(csvname) as file:
        target_lst = list(csv.reader(file))

    for lst in target_lst:
        if not check_sorted(lst):
            ok_flg = False

    with open("result.txt", 'w') as file:
        if ok_flg:
            file.write('OK')
        else:
            file.write('NG')

def check_sorted(lst):
    num = -999
    for l in lst:
        if num <= int(l):
            num = int(l)
        else:
            return False
    return True

if __name__ == "__main__":
    main()
