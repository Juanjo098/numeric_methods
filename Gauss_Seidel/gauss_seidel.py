array_size = 0
array = []
xs = []
errors = []

def input_int(promt):
    try:
        return int(input(promt))
    except ValueError:
        print("ERROR. Ingrese un valor numérico.\n")
        return input_int(promt)
    
def input_float(promt):
    try:
        return float(input(promt))
    except ValueError:
        print("ERROR. Ingrese un valor numérico.\n")
        return input_float(promt)
 
def define_array_size():
    global array_size
    while True:
        array_size = input_int("Ingresa el tamaño de la matriz: ")
        if array_size > 1:
            break
        else:
            print("El tamaño de la matriz no puede ser menor a 2.\n")
            
def define_results_array():
    global xs
    global errors
    for elements in range(array_size):
        xs.append(0)
        errors.append(0)
            
def insert_array_values():
    global array
    for row in range(array_size):
        tmp = []
        for column in range(array_size):
            tmp.append(input_float(f"Ecuación {row + 1}, x{column}: "))
        tmp.append(input_float(f"Resultado de la ecuación {row + 1}: "))
        array.append(tmp)
        
def show_2d_array(array):
    for row in array:
        for column in row:
            print(f"{column},", end=" ")
        print("")
    print("")
            
def show_1d_array(array):
    for element in array:
        print(f"{element},", end=" ")
    print("")        
        
def process():
    global array
    global xs
    global errors
    for row in range(array_size):
        result = 0
        for column in range(len(array[row])):
            if column != row:
                if column < len(array[row]) - 1:
                    result -= array[row][column] * xs[column]
                else:
                    result += array[row][column]
        xs[row] = result / array[row][row]
        
    
define_array_size()
define_results_array()
insert_array_values()
process()
print(array)
print(xs)
print(errors)
