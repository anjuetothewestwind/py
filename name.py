from name_function import get_formatted_name

print("Enter 'q' at any time you want to quit.")
while True:
    first = input('\nplease give me a first name.')
    if first == 'q':
        break
    last = input('\nplease give me a last name.')
    if last == 'q':
        break
    formatted_name = get_formatted_name(first,last)
    print('\tNeatly formatted name: ' + formatted_name + '.')

