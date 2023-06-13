'''This program calculates the square root of an inputted number and the number
of iterations that the algorithm took to reach a degree of accuracy of 1e-14'''
print(__doc__)
print()
import math
EPSILON = 1.0e-14
answer = 'yes'

while answer[0] == 'y' or answer[0] == 'Y':
  input_num = float(input('Enter a number to be square rooted: '))
  approximation = 1
  iteration = 0
  #for positive numbers and 0
  if input_num >= 0:
    while math.fabs((approximation * approximation) - input_num) > EPSILON:
      approximation = 0.5 * (approximation + (input_num / approximation))
      iteration += 1
    print('The square root of', input_num, 'is', approximation)
    print('The number of iterations needed was', iteration)
    answer = input('Do you wish to continue?: ')
  #for negative numbers
  elif input_num < 0:
    while math.fabs((approximation * approximation) - math.fabs(input_num)) > EPSILON:
      approximation = 0.5 * (approximation + (math.fabs(input_num) / approximation))
      iteration += 1
    print('The square root of {} is {}i'.format(input_num, approximation))
    print('The number of iterations needed was', iteration)
    answer = input('Do you wish to continue?: ')
print('Thank you for using my program =)')
