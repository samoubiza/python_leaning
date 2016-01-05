def spiral_matrix(n):
    shift_x,shift_y = 1,0
    x,y = 0,0
    my_array = [[0]* n for j in range(n)]
    for i in range(1,n**2+1):
        my_array[x][y] = i
        next_x,next_y = x+shift_x, y+shift_y
        if 0<=next_x<n and 0<=next_y<n and my_array[next_x][next_y] == 0:
            x,y = next_x,next_y
        else:
            shift_x,shift_y = -shift_y,shift_x
            x,y = x+shift_x, y+shift_y
    return my_array

def print_spiral(my_array):
    n = range(len(my_array))
    for y in n:
        for x in n:
            print(my_array[x][y], end='')
        print()

print_spiral(spiral_matrix(5))
