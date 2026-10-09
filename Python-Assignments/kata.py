class Kata:
<<<<<<< HEAD
 
    def isEven(integer):
=======

 
    def isEven(self, integer):
>>>>>>> 5d65ad1 (Update Python assignments)
        if integer % 2 == 0:
            return True
        else:
            return False


<<<<<<< HEAD
    def isPrimeNumber(integer):
=======
    def isPrimeNumber(self, integer):
>>>>>>> 5d65ad1 (Update Python assignments)
        if integer < 2:
            return False

        for number in range(2, integer):
            if integer % number == 0:
                return False

        return True



<<<<<<< HEAD
    def subtract(integer1, integer2):
=======
    def subtract(self, integer1, integer2):
>>>>>>> 5d65ad1 (Update Python assignments)
        if integer1 > integer2:
            return integer1 - integer2
        else:
            return integer2 - integer1



<<<<<<< HEAD
    def divide(integer1, integer2):
=======
    def divide(self, integer1, integer2):
>>>>>>> 5d65ad1 (Update Python assignments)
        if integer2 == 0:
            return 0

        return integer1 / integer2


  
<<<<<<< HEAD
    def factorOf(integer):
=======
    def factorOf(self, integer):
>>>>>>> 5d65ad1 (Update Python assignments)
        count = 0

        for factor in range(1, integer + 1):
            if integer % factor == 0:
                count = count + 1

        return count


  
<<<<<<< HEAD
    def isSquare(integer):
=======
    def isSquare(self, integer):
>>>>>>> 5d65ad1 (Update Python assignments)
        number = 0

        while number * number <= integer:
            if number * number == integer:
                return True

            number = number + 1

        return False


  
<<<<<<< HEAD
    def isPalindrome( integer):
=======
    def isPalindrome(self, integer):
>>>>>>> 5d65ad1 (Update Python assignments)
        originalNumber = integer
        reversedNumber = 0

        while integer > 0:
            digit = integer % 10
            reversedNumber = reversedNumber * 10 + digit
            integer = integer // 10

        return originalNumber == reversedNumber



<<<<<<< HEAD
    def factorialOf( integer):
=======
    def factorialOf(self, integer):
>>>>>>> 5d65ad1 (Update Python assignments)
        factorial = 1

        for number in range(1, integer + 1):
            factorial = factorial * number

        return factorial



<<<<<<< HEAD
    def squareOf(integer):
=======
    def squareOf(self, integer):
>>>>>>> 5d65ad1 (Update Python assignments)
        return integer * integer