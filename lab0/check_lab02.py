try: 
    input()
    input()
    if input() == 'Jag har druckit 3 koppar kaffe idag.':
        print('CG> success true')
    else:
        print('CG> success false')
except EOFError: 
    print('CG> success false')
