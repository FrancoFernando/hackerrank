from string import ascii_lowercase

def print_rangoli(size):
    
    if size == 1:
        print('a')
        return
    
    letters = ascii_lowercase[:size]
    rangoli = []
    row_size = 4*size-3
    
    for i in range(size):
        suffix = '-'.join(letters[size-i:])
        prefix = suffix[::-1]
        letter = letters[size-i-1]
        rangoli.append('-'.join([prefix,letter,suffix]).center(row_size,'-'))
    
    rangoli.extend(rangoli[-2::-1])
    print('\n'.join(rangoli))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
