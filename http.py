print (" THIS SCRIPT PROGRAMED BY KAREEM WALID ")

import urllib.request,json#WILL IMPORT URLLIB
def main():#SIMPLE FUNCTION
    website=input("Enter link of your website that you want to read http : ")#ENTER URL OF WEBSITE AS : HTTP://WWW.GOOGLE.COM
    filename=input("Enter name of file : ")#ENTER NAME OF FILE THAT YOUR WAMT CODES SAVE IN IT AS : GOOGLE.TXT OR GOOGLE.HTML
    data=urllib.request.urlopen(website).read()#SAVE INTO DATA THE GIVEN FROM urllib.request.urlopen AND READ IT
#SECOND STAGE !
    new=open(filename,"w")#OPEN FILE AND WRITE CODES INTO IT >>>>>>AUTO ^^
    #STR IS TYPE OF DATA WILL WRITE AS STRING
    new.write(str(data))
    new.close()#CLOSE

if __name__ == '__main__':main()#CALL THE MAIN FUNCTION
#BYE HOPE YOU ENJOY IT
