def process_data(input_filename, output_filename):
    f1 = open(input_filename, 'r')
    f2 = open(output_filename, 'w')
    while f1:
        data = f1.readline()
        if not data:
            break
        data = float(data)
        data = data ** 2
        f2.write(str(data)+"\n")
    

    f1.close()
    f2.close()

    f = open(output_filename, 'r')
    square = f.read()
    print(square)


process_data("input.txt", "output.txt")