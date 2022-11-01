def show_magicians(list_of_magicians):
    for magician in list_of_magicians:
        print(magician)

def make_great(list_of_magicians):
    for i in range(len(list_of_magicians)):
        list_of_magicians[i] = 'the Great '+list_of_magicians[i]
    return list_of_magicians


magicians = ['Alice',"Bob",'Charles']
show_magicians(magicians)
b = make_great(magicians[:])
show_magicians(magicians)
show_magicians(b)
