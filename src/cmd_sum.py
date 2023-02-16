import argparse

from tools import sumar


def run(**kwargs):
    a = kwargs['val1']
    b = kwargs['val2']
    result = sumar(a, b)
    print(f'El resultado es {result}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='')

    parser.add_argument(
        '--val1', type=str,
        help='Primer elemento a sumar ',
        required=True
    )

    parser.add_argument(
        '--val2', type=str,
        help='Segundo elemento a sumar ',
        required=True
    )

    args = parser.parse_args()

    print("=== Received args: ")
    print(args.__dict__)

    run(**args.__dict__)
