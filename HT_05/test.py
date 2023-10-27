while True:
    try:
        input_val = int(input('Enter an integer value:  '))
        break
    except ValueError as error:
        print(type(error))
    except KeyboardInterrupt:
        print("A-aaa! We will continue untill I decide to finish!")
