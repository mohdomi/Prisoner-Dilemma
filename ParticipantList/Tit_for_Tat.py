# Always gives Defect for first move and the copy the previous move of the opponent
def titfortat(decision):
   if decision == None:
      return "defect"  
   else:
      return decision 


if __name__ == "__main__":
   decision = None
   print(titfortat(decision))

