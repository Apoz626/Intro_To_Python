import traceback

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('"Symbol" needs to be a string of length 1.')
    if (width < 2) or (height < 2):
        raise Exception('"Width" and "Height" must be greater than 1.')
    
    print(symbol * width)
    
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
        
    print(symbol * width)

boxPrint('$', 5, 5)

## using error formatting with custom message
try:
    raise Exception('This is the traceback error message.')
except:
    errorFile = open('error_lot.txt', 'a')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written to error_log.txt')
