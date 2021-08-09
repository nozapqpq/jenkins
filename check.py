import sys
import csv


def main():
    target_lst = []
    ok_flg = True
    args = sys.argv
    txtname = args[1]
    with open(txtname) as f:
        for line in f:
            target_lst.append(line[0:-1])

    for l in target_lst:
        if not check_expected(l):
            ok_flg = False

    with open("result.txt", 'w') as f:
        if ok_flg:
            print("OK")
            f.write('OK')
        else:
            print("NG")
            f.write('NG')

def check_expected(s):
    return s == "ABCDEFG"

if __name__ == "__main__":
    main()
