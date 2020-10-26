#   LEAP PAIRS GENERATOR - THREE ROWS  - variable number COLUMNS
#        P. Gitschner   October 2020

#--------------------------------------------------------------------------

# make Leap Pairs for  -  w  x 3 tall matrix
# starting at   -   a  ,total nodes z = w  x 3
# zone of interference 1  r  (wip)


# PROJECT NOTES:     Name     EXAM ROOM
# Classroom once had 30 students  at 6 x 5 desk arrangement
# To social distance first created an ailse down the middle. Gives 3 x 5 a side
# but want to eliminate adjacencies within each group of 15 desks
#      fixed commas error


####### Enter Number of Columns here ####                      ***
w = 5

#################


pairs = 0
z = w * 3 
a = 1
i = a
#adding variable spacing  (wip)
r = 1

#TopRow -----------------------------------


myString = "(["


while i <= w-r:
  j = str(i)
  #adding variable spacing  (wip)
  k = str(i+r)
  
  myString = myString +"("+ j + ", " + k +" )"
  pairs = pairs + 1
  i += 1
  # comma between pairs
  myString = myString + "," 
  

#last pair of row

# Second row ----------------------------------

i += 1


while i < w+w:
  j = str(i)
  #adding variable spacing
  k = str(i+r)
  
  myString = myString +"("+ j + ", " + k +" )"
  pairs = pairs + 1
  i += 1
  # comma between pairs
  myString = myString + ","


#--below------------------------------
i = a
while i <= w:
  j = str(i)
  #adding variable spacing
  k = str(i+r+w-1)
  
  myString = myString +"("+ j + ", " + k +" )"
  pairs = pairs + 1
  i += 1
  # comma between pairs
  myString = myString + ","

  


#--slant right-------------------------  
i = 1
while i < w:
  j = str(i)
  #adding variable spacing
  k = str(i+r+w)
  
  myString = myString +"("+ j + ", " + k +" )"
  pairs = pairs + 1
  i += 1
  # comma between pairs
  myString = myString + ","
  
 #--slant left-------------------------
 

i = 2
while i <= w:
  j = str(i)
  #adding variable spacing
  k = str(i+r+w-1-1)
  
  myString = myString +"("+ j + ", " + k +" )"
  pairs = pairs + 1
  i += 1
  # comma between pairs
  myString = myString + ","
  
 
#--------------------------------------------------------------L3

# -----bottom row-----------------------------------------------
#myString = myString + "bottom row row 2  h" 
i = 1+ w +w


while i < w+w+ w:
  j = str(i)
  #adding variable spacing
  k = str(i+r)
  
  myString = myString +"("+ j + ", " + k +" )"
  pairs = pairs + 1
  i += 1
  # comma between pairs
  myString = myString + ","


#--below------------------------------
i = a+w
while i <= w +w:
  j = str(i)
  #adding variable spacing
  k = str(i+r+w-1)
  
  myString = myString +"("+ j + ", " + k +" )"
  pairs = pairs + 1
  i += 1
  # comma between pairs
  myString = myString + ","

  


#--slant right-------------------------  
i = 1+w
while i < w +w:
  j = str(i)
  #adding variable spacing
  k = str(i+r+w)
  
  myString = myString +"("+ j + ", " + k +" )"
  pairs = pairs + 1
  i += 1
  # comma between pairs
  myString = myString + ","
  
 #--slant left-------------------------

i = 2 +w
while i <= w +w:
  j = str(i)
  #adding variable spacing
  k = str(i+r+w-1-1)
  
  myString = myString +"("+ j + ", " + k +" )"
  pairs = pairs + 1
  
  i += 1
  # comma between pairs
  if i <= w +w:
    myString = myString + ","
  
  
 
 # endcap ---------------------------------

myString = myString + "])"



#--------------------------------------------------------------Report
print("-----------------------------------------------------------------")
print(" ")
print("   LEAP PAIRS GENERATOR - THREE ROWS  - variable number COLUMNS")
print("-----------------------------------------------------------------")
print(" ")
print("Start             ", a)
print("Number of Columns ", w)
print ("Number of rows     3")
print ("Shape              Rectangular Grid")
print("Spacing  1 for now,wip   ", r)
print ("Number of Nodes   ",z)
print("Total Edges, Pairs Generated   ",  pairs)

print("-------------------------------------------------------------------")

print("Copy AND PASTE THIS  into VGA cartridge appropriate line and spot")
print("")
print (myString)
print("-----------------------------------------------------------------------------")
print("-----------------------------------------------------------------------------")

