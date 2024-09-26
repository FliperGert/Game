def text_notification(name, *args):
    match name:
        case 'birth':
            return f'{args[0]} was birth'
        case 'birthday':
            return f'{args[0]} is {args[1]}'
        case 'pare':
            return f'{args[0]} love {args[1]}'
