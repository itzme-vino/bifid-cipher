
def getInput(lines = []):
  """ 
    Gets input from file input. Returns list of lines from input file
  """
  import fileinput
  return [ line.strip('\n') for line in fileinput.input() ]

class BifidCipher:
  searchInTableau = lambda self, letter : next( (col, row.index(letter)) for col, row in enumerate(self.tableau) if letter in row )
  getLetter = lambda self, x, y : self.tableau[x][y]

  def __init__(self, tableau):
    self.tableau = tableau

  def encrypt(self, message):
    message = message.replace(" ", "")

    # searches letter in matrix
    tuples = [ self.searchInTableau(letter) for letter in message ]

    # Order new pairs in two lists, list of rows & list of cols
    x_coordinates = [ coordinate[0] for coordinate in tuples ]
    y_coordinates = [ coordinate[1] for coordinate in tuples ]
    
    numbers = x_coordinates + y_coordinates # concatenate lists
      
    # map numbers to new letter and append to cypherText
    cypherText = [ self.getLetter(numbers[i], numbers[i + 1]) for i in range(0, len(numbers) - 1, 2) ]

    return ''.join(cypherText)

  def decrypt(self, cypherText):
    flatten = lambda l: [ item for sublist in l for item in sublist ]

    # searches letter in matrix
    tuples = flatten( [ list(self.searchInTableau(letter)) for letter in cypherText ] )

    half = len(tuples)//2
    x_coordinates, y_coordinates = tuples[:half], tuples[half:]

    message = [ self.getLetter(x_coordinates[i], y_coordinates[i]) for i in range(half) ]
    
    return ''.join(message)

def main():

  TABLEAU = [
    ['E', 'N', 'C', 'R', 'Y'],
    ['P', 'T', 'A', 'B', 'D'],
    ['F', 'G', 'H', 'I', 'K'],
    ['L', 'M', 'O', 'Q', 'S'],
    ['U', 'V', 'W', 'X', 'Z'],
  ]

  bifid = BifidCipher(TABLEAU)

  inputLines = getInput()

  if inputLines[0] == 'ENCRYPT':
    res = bifid.encrypt(inputLines[1])

  elif inputLines[0] == 'DECRYPT':
    res = bifid.decrypt(inputLines[1])
    
  else:
    print('COMMAND ERROR')

  print(res)
  return 

if __name__ == "__main__":
  main()
