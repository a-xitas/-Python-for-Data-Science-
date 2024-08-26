## 1. Introducing Data Cleaning ##

# Read the text on the left, and then scroll to the bottom
# to find the instructions for the coding exercise

# Write your answer to the instructions below -- the list of
# lists is stored using the variable name `moma`

num_rows = len(moma)
print(num_rows)


## 2. Reading our MoMA Dataset ##

# import the reader function from the csv module
from csv import reader

# use the python built-in function open()
# to open the children.csv file
opened_file = open('children.csv')

# use csv.reader() to parse the data from
# the opened file
read_file = reader(opened_file)

# use list() to convert the read file
# into a list of lists format
children = list(read_file)

# remove the first row of the data, which
# contains the column names
children = children[1:]

# Write your code here

from csv import reader

opened_file = open('artworks.csv')
read_file = reader(opened_file)
moma = list(read_file)
moma = moma[1:]
print(moma)



## 3. Replacing Substrings with the Replace Method ##

age1 = "I am thirty-one years old"
age2 = age1.replace('one', 'two')

print(age2)


## 4. Cleaning the Nationality and Gender Columns ##

# Variables you create in previous screens
# are available to you, so you don't need
# to read the CSV again

for row in moma:
    nationality = row[2]
    nationality = nationality.replace('(', '')
    nationality = nationality.replace(')', '')
    row[2] = nationality
    
for row in moma:
    gender = row[5]
    gender = gender.replace('(', '')
    gender = gender.replace(')', '')
    row[5] = gender
    
print(moma[0][2])
print(moma[0][5])
print(moma[2][2])
print(moma[2][5])


## 5. String Capitalization ##

# limpar as incongruências na Data referente ao genero (Gender) do autor:
for row in moma:
    Gender = row[5]
    Gender = Gender.title()
    if not Gender:
        Gender = 'Gender Unknown/Other'
    row[5] = Gender 

# limpar as incongruências na Data referente à Nacionalidade (Nationality) do autor:
for row in moma:
    Nationality = row[2]
    Nationality = Nationality.title()
    if Nationality == '':
        Nationality = 'Nationality Unknown'
    row[2] = Nationality
        
    

## 6. Errors During Data Cleaning ##

def clean_and_convert(date):
    # check that we don't have an empty string
    if date != "":
        # move the rest of the function inside
        # the if statement
        date = date.replace("(", "")
        date = date.replace(")", "")
        date = int(date)
    return date

for row in moma:
    BeginDate = clean_and_convert(row[3])
    EndDate = clean_and_convert(row[4])
    row[3] = BeginDate
    row[4] = EndDate
    
print(moma[1:][4:7])

    

## 7. Parsing Numbers from Complex Strings, Part One ##

test_data = ["1912", "1929", "1913-1923",
             "(1951)", "1994", "1934",
             "c. 1915", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "c. 1955.", "c. 1970's", 
             "C. 1990-1999"]

bad_chars = ["(",")","c","C",".","s","'", " "]

def strip_characters(string):
    for c in bad_chars:
        string = string.replace(c, '')
    return string


stripped_test_data = []

for string in test_data:
    string = strip_characters(string)
    stripped_test_data.append(string)
    
print(stripped_test_data)

## 8. Parsing Numbers from Complex Strings, Part Two ##

test_data = ["1912", "1929", "1913-1923",
             "(1951)", "1994", "1934",
             "c. 1915", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "c. 1955.", "c. 1970's", 
             "C. 1990-1999"]

bad_chars = ["(",")","c","C",".","s","'", " "]

def strip_characters(string):
    for c in bad_chars:
        string = string.replace(c, '')
    return string

stripped_test_data = ['1912', '1929', '1913-1923',
                      '1951', '1994', '1934',
                      '1915', '1995', '1912',
                      '1988', '2002', '1957-1959',
                      '1955', '1970', '1990-1999']

def process_date(string):
    if '-' in string:
        string = string.split('-')
        string_1 = int(string[0])
        string_2 = int(string[1])               
        string = (string_1 + string_2)/2
        string = round(string)
    else:
        string = int(string)
        
    return string

processed_test_data = []

for s in stripped_test_data:
    string = process_date(s)
    processed_test_data.append(string)
    
print(processed_test_data)


for row in moma:
    Date = strip_characters(row[6])
    row[6] = Date
    Date = process_date(row[6])
    row[6] = Date 

print(moma[3][6])


        