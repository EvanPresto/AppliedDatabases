import pymysql

import pymongo

myclient = None 


def display():
    print("Movies DB")
    print("------------")
    print("")
    print("MENU")
    print("======")
    print("1 --View Films")
    print("2 - View Actors by Year of Birth & Gender")
    print("3 - View Studios")
    print("4 - Add New Country")
    print("5 - View Movie With Subtitles")
    print("6 - Add New MovieScript")
    print("x = Exit application")
    

def main():
    print(display())
    Choice = str(input("Choice: "))
    while Choice != 'x':
     if Choice == '1':
          ViewFilms()
          break
     elif Choice == '2':
          ViewActors()
          break
     elif Choice == '3':
          ViewStudios()
          break
     elif Choice == '4':
         CountryID = int(input('Please Enter Country ID:'))
         Country = str(input("Enter Country"))
         print(CountryID,Country)
         AddCountry(CountryID,Country)
         display()
     elif Choice == '5':
         ConnectMongo()
         FindSubtitleMovie()
     elif Choice == '6':
         AddMovieScript()
         
     

def ViewFilms():
    conn = pymysql.connect(user = "root", cursorclass = pymysql.cursors.DictCursor, password ="Presto12345",host = "localhost",db = "MoviesDB", port =3306)

    query = "select FilmName from Film"

    with conn:
        cursor = conn.cursor()
        cursor.execute(query)
        print(query)


    

def ViewActors():
    print("loading....")
   

def ViewStudios():
    conn = pymysql.connect(user = "root", cursorclass = pymysql.cursors.DictCursor, password ="Presto12345",host = "localhost",db = "MoviesDB", port =3306)

    query = "select StudioID,StudioName from Studio order by StudioID asc"
    with conn:
        cursor = conn.cursor()
        cursor.execute(query)
        Studios = cursor.fetchall()
        print(Studios)

def AddCountry(CountryID,Country):
    db = pymysql.connect(user = "root", cursorclass = pymysql.cursors.DictCursor, password ="Presto12345",host = "localhost",db = "MoviesDB", port =3306)

    sql = "INSERT INTO Country VALUES (%s,%s)"

    with db:
        cursor = db.cursor()
        cursor.execute(sql, (CountryID,Country))
        db.commit

def ConnectMongo():
    global myclient
    myclient = pymongo.MongoClient()
    myclient.admin.command('ismaster')  

def FindSubtitleMovie():
    mydb = myclient["movieScriptsDB"]
    print(mydb)
    docs = mydb["movieScripts"]
    #Language = int(input("Please Enter Language"))
    #query = ["subtitles":str(Language)]
    #Selection = docs.find(query)
    #print(Selection)
    x = str(input("Enter country"))
    myquery = {"subitles":x}
    selection = docs.find(myquery)
    print(selection)


def AddMovieScript():
    ConnectMongo()
    print('Add New Movie Script')
    print('---------------------')
    NewID = int(input('ID:'))
    while NewID != '-1':
        NewKeyword = str(input('Enter Keyword'))
    




if __name__ == "__main__":
    main()