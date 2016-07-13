# Function Design Recipe
``` python
def convert_to_celsius(fahrenheit):
    ''' (number) -> float
    
    Return the number of Celsius degrees equivalent to fahrenheit degrees.
    
    >>> convert_to_celsius(32)
    0.0
    >>> convert_to_celsius(212)
    100.0
    '''
    return (fahrenheit - 32) * 5 / 9
```
# Function Reuse
``` python
def area(base, height):
    ''' (number, number) -> number
    
    Return the area of a triangle with given base and height.
    
    >>> area(10, 40)
    200.0
    >>> area(3.4, 7.5)
    12.75
    '''
    
    return base * height / 2
```
``` python
def perimeter(side1, side2, side3):
    '''(number, number, number) -> number
    
    Return the perimeter of the triangle with side of length side1, side2 and side3.
    
    >>> perimeter(3, 4, 5)
    12
    >>> perimeter(10.5, 6, 9.3)
    25.8
    '''
      
    return side1 + side2 + side3
```    
### Recipe for Designing Functions:
1. Examples
2. Type Contract
3. Header
4. Description
5. Body
6. Test

``` python
def semiperimeter(side1, side2, side3):
    '''
    (number, number, number) -> float

    Return the semiperimeter of a triangle with sides of length side1, side2 and side3.
    >>> semiperimeter(3, 4, 5)
    6.0
    >>> semiperimeter(10.5, 6, 9.3)
    12.9
    '''
    return primeter(side1, side2, side3) / 2
```
# import
``` python
import math
dir(math)
help(math.sqrt)
```
``` python
import math
def area_hero(side1, side2, side3):
''' (number, number, number) -> float 

Return the area of a triangle with sides of length side1, side2, and side3.

>>> area_hero(3, 4, 5)
6.0
>>> area_hero(10.5, 6, 9.3)
27.731
'''
semi = semiperimeter(side1, side2, side3)
area = math.sqrt(semi * (semi - side1) * (semi - side2) * (semi - side3))
return area
```
# if statements
``` python
def report_status(scheduled_time, estimated_time):
''' (number, number) -> str

Return the flight status (on time, early, delayed) for a flight that was scheduled to arrive at scheduled_timed,
but is now estimated to arrive at estimated_time.

Pre-condition: 0.0 <= scheduled_time < 24 and 0.0 <= estimated_time < 24

>>> report_status(14.3, 14.3)
'on time'
>>> report_status(12.5, 11.5)
'early'
>>> report_status(9.0, 9.5)
'delayed'
'''
if scheduled_time == estimated_time:
    return 'on time'
elif scheduled_time > estimated_time:
    return 'early'
else:
    return 'delayed'
```
# No if required
``` python
def is_even(num):
''' (int) -> bool

Return whether num is even.

>>> is_even(4)
True
>>> is_even(77)
False
'''
return num % 2 == 0
# if num % 2 == 0:
#     return True
# else:
#     return False    