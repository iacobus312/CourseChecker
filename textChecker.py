def textChecker(input_file, delimiter = ' '):
    two_d_list = []
    with open(input_file, 'r', encoding = 'utf-8') as file:
        for line in file:
            row = line.strip().split(delimiter)
            two_d_list.append(row)
    return two_d_list

def main():
    returnvalue = textChecker('output.txt')
    for row in returnvalue:
        for i in range(len(row)):
            try:
                row[i] = int(row[i])
            except ValueError:
                pass
                    
        if len(row) == 3 and isinstance(row[0], int) and isinstance(row[1], str) and isinstance(row[2], int):
            print(row)
        else:
            returnvalue.remove(row)
main()
