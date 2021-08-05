def fizzBuzz():
    '''
    FizzBuzz is a children’s game where
    you count from 1 to 20. Easy, right?

    Here’s the catch: instead of saying
    numbers divisible by 3, say “Fizz”.
    And instead of saying numbers
    divisible by 5, say “Buzz”. For
    numbers divisible by both 3 and 5, say
    “FizzBuzz”.
    '''
    for i in range(1,100):
        if i%3==0 and i%5==0:
            print("FizzBuzz")
        elif i%5==0:
            print("Buzz")
        elif i%3==0:
            print("Fizz")
        else:
            print(i)

fizzBuzz()
