if __name__ == '__main__':
    message = input()
    message = message.replace('мяу', '.')
    message = message.replace('мрр', '-')
    message = message.replace('.', 'мяу')
    message = message.replace('-', 'мрр')
    print(message)
    input()



