weather = 'sunny'

match weather:
    case 'sunny':
        print("It's a beautiful day!")
    case 'rainy':
        print("Grab your umbrella.")
    case 'cloudy':
        print("No need for sunscreen.")
    case 'snowy':
        print("Wear layers!")
    case _:
        print("Good luck.")