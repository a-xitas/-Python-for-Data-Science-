## 1. Reading the MoMA Dataset ##

from csv import reader

# Read the `artworks_clean.csv` file
opened_file = open('artworks_clean.csv')
read_file = reader(opened_file)
moma = list(read_file)
moma = moma[1:]

# Convert the birthdate values
for row in moma:
    birth_date = row[3]
    if birth_date != "":
        birth_date = int(birth_date)
    row[3] = birth_date
    
# Convert the death date values
for row in moma:
    death_date = row[4]
    if death_date != "":
        death_date = int(death_date)
    row[4] = death_date

# Write your code below

for row in moma:
    date = row[6]
    if date != '':
        date = int(date)
    row[6] = date 
   
print(moma[1:][6])
    

## 2. Calculating Artist Ages ##

ages = []

for row in moma:
    date = row[-2]
    birth = row[3]
    if birth != '':
        age = date - birth
    else:
        age = 0
    ages.append(age)

#print(ages)


final_ages = []


for age in ages:
    if age > 20:
        final_age = age
    else:
        final_age = 'Unknown'
    final_ages.append(final_age)
    
#print(final_ages)

    

## 3. Converting Ages to Decades ##

# The ages variable is available
# from the previous screen

decades = []
for age in ages:
    if age == 'Unknown':
        decade = age
    else:
        decade = str(age)
        decade = decade[:-1]
        decade = decade + '0s'
        
    decades.append(decade)
        

    
    

## 4. Summarizing the Decade Data ##

# The decades variable is available
# from the previous screen

decade_frequency = {}

for decade in decades:
    if decade not in decade_frequency:
        decade_frequency[decade] = 1
    else:
        decade_frequency[decade] += 1

## 5. Inserting Variables into Strings ##

artist = "Pablo Picasso"
birth_year = 1881

template_string = "{name}'s birth year is {year}."
output = "{name}'s birth year is {year}.".format(name = artist, year = birth_year)

print(output)

## 6. Creating an Artist Frequency Table ##

#a crir um dicionário vazio para acomodar a N/FT relacionada c o nmr de obras de arte q cada artista prod na sua vida e q s encontram no MOMA
artist_freq = {}

#iterar pela lista de listas moma. Atribuimos o nome do artista à variavel artist e apontamos para a 2º coluna ([1]) em todas as linhas. Depois vemos se a Key artista já pertence ao dicionário artist_fre, se n pertencer criamos uma Key c o nome desse artista e atribuimos o nmr 1, se já existir essa Key, acrescentamos o nmr 1 a esse mesma Key. 
for row in moma:
    artist = row[1]
    if artist not in artist_freq:
        artist_freq[artist] = 1
    else: 
        artist_freq[artist] += 1

    
    

## 7. Creating an Artist Summary Function ##


def artist_summary (nome_artista):
    n_obras_de_arte = artist_freq[nome_artista]
    output = 'There are {n_obras} artworks by {nome} in the data set'.format(n_obras = n_obras_de_arte, nome = nome_artista) 
    print (output)

artist_summary("Henri Matisse")
               
    

## 8. Formatting Numbers Inside Strings ##

pop_millions = [
    ["China", 1379.302771],
    ["India", 1281.935991],
    ["USA",  326.625791],
    ["Indonesia",  260.580739],
    ["Brazil",  207.353391],
]

template = 'The population of {country} is {pop_n:,.2f} million'

for row in pop_millions:
    Country = row[0]
    Pop_n = row[1]
    print(template.format(country = Country, pop_n = Pop_n))
    

## 9. Challenge: Summarizing Artwork Gender Data ##


gender_freq = {}

for row in moma:
    Gender = row[5]
    if Gender not in gender_freq:
        gender_freq[Gender] = 1
    else:
        gender_freq[Gender] += 1
        
for Gender, N in gender_freq.items():
    output = 'There are {n:,} artworks by {G} artists'
    print(output.format(G=Gender, n=N))

print('\n')

for Gender, N in gender_freq.items():
    output = 'There are {0:,} artworks by {1} artists--V2'
    print(output.format(N, Gender))