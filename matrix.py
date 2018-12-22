# Python is sequential


#Class
class Matrix:
  def __init__(self, rows=1, cols=1, default_value=0):
    self.rows = rows
    self.cols = cols
    self.default_value = default_value
    self.matrix = [0] * rows 
    # initialize the matrix with default value
    for i in range(rows):
      self.matrix[i] = [0] * cols

  def __add__(self, other):
    # initialize and declare a return matrix

    # Check to see if the size of the matrices are equal. 
    if  (self.rows == other.rows) & (self.cols == other.cols):
      # return matrix declared only if the addition is valid
      returnMatrix = Matrix(self.rows,self.cols)
      # add the matrices together
      for i in range(len(self.rows)):
        for j in range(len(self.cols)):
          returnMatrix[i][j] = self.matrix[i][j] + other.matrix[i][j]        
    else:
      # report invalid addition 
      print("invalid addition")

  def print(self):
    for i in range(self.rows):
      for j in range(self.cols):
        print(self.matrix[i][j],end=' ')
      print('\n')
   

# test  main
def main():
  m = Matrix(5,5,0) 
  m.print()


if __name__ == "__main__":
  main()
