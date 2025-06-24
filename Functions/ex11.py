def local_greet(locale):
    language = extract_language(locale)
    region = extract_region(locale)

    if language == 'en':
        match region:
            case 'US':
                return 'Hey!'
            case 'GB':
                return 'Hello!'
            case 'AU':
                return 'Howdy'
    else:
        greet(language)

def extract_language(locale):
    return locale.split('_')[0]

def extract_region(locale):
    return locale.split('_')[1].split('.')[0]

def greet(string):
    match string:
        case 'fr':
            return 'Salut!'
        case 'pt':
            return 'Ola!'
        case 'de':
            return 'Hallo!'
        case 'sv':
            return 'Hej!'
        case 'af':
            return 'Haai!'
        case _:
            return 'N/A'