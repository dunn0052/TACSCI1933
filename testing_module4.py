import javaRunner



def test(file, name, path = None):
    data = []
    test = ['Sieve size must be at least 2.', '', '2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99', '2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97']

    #compile code
    javaRunner.javaC(path, file)

    # get code output
    output = javaRunner.javaR("Driver")
    check = zip(output, test)
    for c in check:
        data.append(c[0] == c[1])
    javaRunner.clear("lab5_to_grade/Driver.class") #checkout to see that it works, but probably just compiles over it
    javaRunner.clear("lab5_to_grade/Sieve.class") 
    print(data)
    return data
