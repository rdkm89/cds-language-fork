import argparse

def input_parse():
    # initialize the parser
    parser = argparse.ArgumentParser()
    # add arguments
    parser.add_argument("--name", type=str, default="Kevin")
    parser.add_argument("--age", type=int, required=True)
    # parse the arguments from command line
    args = parser.parse_args()
    return args

def hello(name, age):
    print("Hello, my name is " + name + "!")
    print("I am " + str(age) + " years old!")

def main():
    # run input parse to get name
    args = input_parse()
    # pass name to hello()
    hello(args.name, args.age)

if __name__=="__main__":
    main()