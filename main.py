#Author: Daniel Dean dpd@psu.edu
#Collaborator: Yash Patni  yjp5077@psu.edu
#Collaborator: Cameron Ezeiraku cke5142@psu.edu
#Collaborator: Stephanie Huang ssh5302@psu.edu
#Section: 2
#Breakout: 7

def getLetterGrade(grade):
  if __name__ == '__main__':
    grade = float(input("Enter your CMPSC 131 grade: "))
  if grade >= 93.0:
    if __name__ != '__main__':
      return('A')
    else:
      print("Your letter grade for CMPSC 131 is A.")
  elif grade >= 90.0:
    if __name__ != '__main__':
      return('A-')
    else:
      print("Your letter grade for CMPSC 131 is A-.")
  elif grade >= 87.0:
    if __name__ != '__main__':
      return('B+')
    else:
      print("Your letter grade for CMPSC 131 is B+.")
  elif grade >= 83.0:
    if __name__ != '__main__':
      return('B')
    else:
      print("Your letter grade for CMPSC 131 is B.")
  elif grade >= 80.0:
    if __name__ != '__main__':
      return('B-')
    else:
      print("Your letter grade for CMPSC 131 is B-.")
  elif grade >= 77.0:
    if __name__ != '__main__':
      return('C+')
    else:
      print("Your letter grade for CMPSC 131 is C+.")
  elif grade >= 70.0:
    if __name__ != '__main__':
      return('C')
    else:
      print("Your letter grade for CMPSC 131 is C.")
  elif grade >= 60: 
    if __name__ != '__main__':
      return('D')
    else:
      print("Your letter grade for CMPSC 131 is D.")
  else:
    if __name__ != '__main__':
      return('F')
    else:
      print("Your letter grade for CMPSC 131 is F.")

if __name__ == '__main__':
  getLetterGrade(input)
