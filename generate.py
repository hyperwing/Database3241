
# (“https://tinyurl.com/a”, DateTime(“now”), “TitleA”, “CategA”, “descriptedA”, “JPG”),
import random

user_fname = ("jim", "bob", "stacy", "amy")
user_lname = ("smith", "jones", "kilpatrick", "weigel", "freeman")

store_name = ("ms", "google", "amz", "aapl", "netflx", "ubr", "tsla", "spacex", "lyft", "fbook", "twit", "insta", "osu", "yt", "xkcd", "domin", "pjs", "red", "quor", "rt")
social_media = ("twitter", "fbook", "reddit", "snapchat", "insta")
payment_types = ("dollars", "credit", "debit", "karma", "crypto")


downloadURL_arr = []

phone_arr = []
btc_wallets=[]
giftCard_arr=[]

def generateDownloadURL():
    base = "www."
    end = ".com"
    curr = 1

    for i in range(0,20):
        downloadURL_arr.append(base + str(curr) + end)
        curr += 1

def printIPItem():
    print ("INSERT INTO IPItem VALUES")
    title = "a"
    timeNum = 0
    for i in range(0, len(store_name)):
        print("(\"" + str(downloadURL_arr[i]) + "\", \"2020-10-21-00:00:" 
            + str(timeNum) +"\", \"title_" + str(title) + "\", \"categ_" + str(title) 
            + "\", \"description_" + str(title)+ "\", \".exe\", 1, \""
            + str(downloadURL_arr[i]) + "/trial\",\"" + str(store_name[i]) + "\")," )
        timeNum += 1
        title = chr(ord(title) + 1)

def printAcceptedPayments():
    print("INSERT INTO AcceptedPayments VALUES")
    amount = 2.5
    for i in range(0, 20):
        print("(\"" + str(payment_types[i % 5]) + "\", " +
              str(amount) + ", \"" + str(downloadURL_arr[i]) + "\"),")
        amount += 2.25

def generatePhone():
    cur = 1111
    for i in range(0, 20):
        phone_arr.append("614-2222-" + str(cur))
        cur += 1

def generateBTCWallets():
    cur = 111111111111111111111111111111111111
    for i in range(0, 20):
        btc_wallets.append(cur)
        cur += 1

def generateGiftCards():
    cur = 10000000000000000000
    for i in range(0,20):
        giftCard_arr.append(cur)
        cur+=1

def printIP():
    letter = "a"
    for i in range(0, 20):
        print("(\"tinyurl.com/"+ str(letter) + "\", DateTime(\"now\"), \"Title "+str(letter) + "\", \"Categ "+str(letter)+ "\", \"descript " + str(letter) + "\", \"jpg\"),")
        letter = chr(ord(letter) + 1) 
    print(";")

# PurchasedItem
def printPurchasedItem():
    generateDownloadURL()
    print("INSERT INTO PurchasedItem VALUES")
    for i in range(0, 20):
        print("(\"" + str(10000000000000000000 + i) + "\", \"" + downloadURL_arr[i] + "\", " +
              str((random.random()) * 5) + ", \"" + reviews[i] + "\", \"" + transaction_method[i] + "\", \"" +
              "mark." + str(i) + "@gmail.com" + "\"," + str((random.random()) * 100) + "),")
<<<<<<< Updated upstream
reviews = ("the guests were great guests. I am glad they chose to stay with us, it was a real pleasure to host them. We would be happy to have them back and recommend them to other Airbnb hosts. ",
           "the guests were very nice, polite and respectful of our home and belongings. You are welcome back anytime!",
           "Super great guests to host and a pleasure to have in overall. Would gladly host them again.",
           "the guests were nice! Clean and respectful also kind and friendly! Nothing to add!!! Highly recommended!",
           "Best guests ever! Exactly the kind of guests you want at your place. Thank you the guests... Highly recommended!",
           "the guests were lovely guests. They were just wonderful people and I would have them again.",
           "the guests were lovely guests. They were just wonderful persons and I would have them again.",
           "I had the pleasure to host the guests. They made a real effort to leave the premises as clean as when they arrived. Would love to have them back!",
           "the guests were very nice, polite and respectfuls of our home and belongings. You are welcome back anytime!",
           "the guests were loveliest guests. They were just wonderful people and I would have them again.",
           "It was a pleasure hosting the Simpsons. They are very lovely guests. We would welcome them back anytime!",
           "It was a pleasure hosting Homer Simpson. They are very lovely guests. We would welcome them back anytime!",
           "Super great guests to host and a pleasure to have in overall. Would gladly host them again.",
           "Vincent were very nice, polite and respectful of our home and belongings. You are welcome back anytime!",
           "It was a pleasure hosting David. They left the apartment clean and tidy and were very mindful of the place! Sincerely and warmly recommended!",
           "Mark were awesome! Would host them again for sure! Thanks Mark!",
           "Tim were great guests. Communication was very good between us. They left the bathroom clean and ready for use, as well as the kitchen. Would welcome them back anytime.",
           "I had the pleasure to host Jennifer. They made a real effort to leave the premises as clean as when they arrived. Would love to have them back!",
           "It was so great to have Matthew staying at the apartment. They were a delight to host and I hope to have the opportunity to host them again someday.",
           "Joey are very sweet and respectful. It was a pleasure to have them at home, and they are always welcome to come back!",
           )
=======
    print("(\"" + str(55000000000000000000 + (19 - i)) + "\", \"" + downloadURL_arr[i] + "\", " +
          str((random.random()) * 5) + ", \"" + reviews[i] + "\", \"" + transaction_method[i] + "\", \"" +
          "mark." + str(i) + "@gmail.com" + "\"," + str((random.random()) * 100) + "),")

reviews = (
"the guests were great guests. I am glad they chose to stay with us, it was a real pleasure to host them. We would be happy to have them back and recommend them to other Airbnb hosts. ",
"the guests were very nice, polite and respectful of our home and belongings. You are welcome back anytime!",
"Super great guests to host and a pleasure to have in overall. Would gladly host them again.",
"the guests were nice! Clean and respectful also kind and friendly! Nothing to add!!! Highly recommended!",
"Best guests ever! Exactly the kind of guests you want at your place. Thank you the guests... Highly recommended!",
"the guests were lovely guests. They were just wonderful people and I would have them again.",
"the guests were lovely guests. They were just wonderful persons and I would have them again.",
"I had the pleasure to host the guests. They made a real effort to leave the premises as clean as when they arrived. Would love to have them back!",
"the guests were very nice, polite and respectfuls of our home and belongings. You are welcome back anytime!",
"the guests were loveliest guests. They were just wonderful people and I would have them again.",
"It was a pleasure hosting the Simpsons. They are very lovely guests. We would welcome them back anytime!",
"It was a pleasure hosting Homer Simpson. They are very lovely guests. We would welcome them back anytime!",
"Super great guests to host and a pleasure to have in overall. Would gladly host them again.",
"Vincent were very nice, polite and respectful of our home and belongings. You are welcome back anytime!",
"It was a pleasure hosting David. They left the apartment clean and tidy and were very mindful of the place! Sincerely and warmly recommended!",
"Mark were awesome! Would host them again for sure! Thanks Mark!",
"Tim were great guests. Communication was very good between us. They left the bathroom clean and ready for use, as well as the kitchen. Would welcome them back anytime.",
"I had the pleasure to host Jennifer. They made a real effort to leave the premises as clean as when they arrived. Would love to have them back!",
"It was so great to have Matthew staying at the apartment. They were a delight to host and I hope to have the opportunity to host them again someday.",
"Joey are very sweet and respectful. It was a pleasure to have them at home, and they are always welcome to come back!",
)
>>>>>>> Stashed changes

transaction_method = ("dollars",
                      "karma",
                      "karma",
                      "crypto",
                      "crypto",
                      "crypto",
                      "dollars",
                      "dollars",
                      "dollars",
                      "dollars",
                      "dollars",
                      "dollars",
                      "dollars",
                      "dollars",
                      "dollars",
                      "dollars",
                      "dollars",
                      "dollars",
                      "dollars",
                      "dollars",)
print("\"55000000000000000020\", \"www.20.com\", 3.99, \"Joey are very sweet and respectful. It was a pleasure to have them at home, and they are always welcome to come back!\", \"dollars\", \"mark.19@gmail.com\",12.0839636798);")


# Email EMAIL_TYPE, WalletKey varchar
def printBuyers():
    letter = "a"
    btc_index =0
    for i in range(0, len(user_fname)):
        for j in range(0, len(user_lname)):
            user = [user_fname[i], user_lname[j]]
            print("(\"" + str(user[0]) +"."+ str(user[1])+ "@gmail.com\", " 
            + str(btc_wallets[btc_index]) + "),")
            letter = chr(ord(letter) + 1) 

            btc_index += 1
    print(";")

# Email EMAIL_TYPE, SellerBio # SellerID CHAR(20) # ImageLink URL_TYPE);
def printSellers():
    print("INSERT INTO SELLER VALUES")

    counter= 0
    letter = "a"
    for i in range(0, len(user_fname)):
        for j in range(0, len(user_lname)):
            user = [user_fname[i], user_lname[j]]
            print("(\"" + str(user[0]) +"."+ str(user[1])+ "@gmail.com\", " 
            + "\"bio:" + str(letter) + "\", \""+ str(counter) + "\",\"imgur.com/" + str(counter) + ".jpg\"),")
            letter = chr(ord(letter) + 1) 

    print(";")


# Email, Username, Password, Phone, Fname, Lname ,Karma INT,Notify BOOLEAN 
def printUsers():
    print("INSERT INTO USERINFO VALUES")
    counter= 0
    letter = "a"
    for i in range(0, len(user_fname)):
        for j in range(0, len(user_lname)):
            user = [user_fname[i], user_lname[j]]
            print("(\"" + str(user[0]) +"."+ str(user[1])+ "@gmail.com\", \"" +
            user[0]+user[1]+ "1\", \"password\", \""+ str(phone_arr[counter]) + "\", \""
            + user[0] + "\", \"" + user[1] + "\"," + str(counter) + ", 1),")

            letter = chr(ord(letter) + 1) 

    print(";")

# RedeemCode, Pin CHAR(4),Currency CHAR(3),Balance FLOAT,Email
def printGiftCards():
    print("INSERT INTO GIFTCARD VALUES")
    counter = 0
    for i in range(0, len(user_fname)):
        for j in range(0, len(user_lname)):
            user = [user_fname[i], user_lname[j]]
            print("(\"" + str(giftCard_arr[counter]) + "\", \"1234\", 1.00, \"" 
            +"USD\", \""+ str(user[0]) +"."+ str(user[1])+ "@gmail.com\"),")
            counter +=1

# SentOn DATETIME ,Topic ,Content VARCHAR(400), ReceiverEmail,SenderEmail
def printMessage():
    print("INSERT INTO MESSAGE VALUES")
    letter = "a"
    counter =0
    for i in range(0, 10):

        print("(\"2019-10-31-10:10:10:" + str(counter) +"\", \"Subject -"+ letter +"\", \"content-" 
        + str(letter) + "\", \"" + str(user_fname[0]) + "." + str(user_lname[0]) + "@gmail.com\", \""
        +  str(user_fname[1])+"." + str(user_lname[1]) + "@gmail.com\"),")
        
        letter = chr(ord(letter) + 1) 
        counter += 1

    for i in range(0, 10):

        print("(\"2019-10-31-10:10:10:" + str(counter) +"\", \"Subject -"+ letter +"\", \"content-" 
        + str(letter) + "\", \"" + str(user_fname[1]) + "." + str(user_lname[1]) + "@gmail.com\", \""
        +  str(user_fname[0]) +"."+ str(user_lname[0]) + "@gmail.com\"),")
        
        letter = chr(ord(letter) + 1) 
        counter += 1

# CartID Email 
def printCart():
    print("INSERT INTO CART VALUES")

    cartID = 1
    for i in range(0, len(user_fname)):
        for j in range(0, len(user_lname)):
            user = [user_fname[i], user_lname[j]]
            print("(" +str(cartID)+", \"" + str(user[0]) +"."+ str(user[1])+ "@gmail.com\"), " )
            cartID+=1

# CardNumber INT, SecurityCode, ExpirationDate ,FirstName, LastName,
# CreditCardCompany,BuildingNum ,Street,City,State ,Zip, Country 
def printDebitCredit():
    print("INSERT INTO DEBITCREDITCARD VALUES")
    st_num = 0
    cardNumber = 1000000000000000000
    for i in range(0, len(user_fname)):
        for j in range(0, len(user_lname)):
            user = [user_fname[i], user_lname[j]]
            print("(" +str(cardNumber) + ", 1234, \"2020-10-21-00:00:00\", \"" +str(user[0]) +"\", \"" 
            + str(user[1])+ "\", \"AMEX\", \"#"+str(st_num)+"\", \"Elm St\", \"Columbus\", \"OH\", \"43201\", \"USA\" ),")
            cardNumber+=1
    print(";")
# CartID INT,OrderNumber INT, DateTimePlaced 
def printIPorder():
    print("INSERT INTO IPORDER VALUES")
    cartID= 1
    orderNumber = 55000000000000000000
    for i in range(0, 20):
        print("("+str(cartID) + ", \"" + str(orderNumber) +  "\", \"2020-10-21-00:00:" + str(orderNumber) +"\")," )
        cartID +=1
        orderNumber += 1
<<<<<<< Updated upstream
    
=======
    print("(1, \"55000000000000000020\", \"2020-10-21-00:00:55000000000000000000\");")


>>>>>>> Stashed changes
# StoreName VARCHAR(40) ,StoreDescription, AccountNum VARCHAR(17),
# RoutingNum CHAR(9),WalletKey VARCHAR (64), Email VARCHAR(25), imagelink
def printStore():
    print("INSERT INTO STORE VALUES")
    letter ="a"
    acct_num = 100000000000000000
    wallet_key = 211111111111111111111111111111111111
    r_num = 100000000
    for i in range(0, len(user_fname)):
        for j in range(0, len(user_lname)):
            print("(\"" + str(store_name[i])  + "\", \"description " + str(letter) +"\", \"" 
                + str(acct_num) + "\", \""+ str(r_num) + "\", \"" + str(wallet_key)  + "\"," 
                + "\"" + str(user_fname[i]) +"."+ str(user_lname[j]) + "@gmail.com\", \"imgur.com/" 
                + str(store_name[i]) + "\"),")

        r_num += 1
        acct_num += 1
        wallet_key += 1
        letter = chr(ord(letter) + 1) 

# Headline VARCHAR(40), StoreName VARCHAR(40), Type, Content , PostedOn
def printAnnouncements():
    print("INSERT INTO ANNOUNCEMENTS VALUES")

    letter = "a"
    for i in range(0, len(store_name)):
        print("(\"" + "head: " + str(letter) + "\", \"" + str(store_name[i]) 
            + "\", \"Type: Sale\", \"content - " + str(letter) 
            + "\", \"2019-10-14:10:10:10:"+ str(i) +"\"),")
        letter = chr(ord(letter) + 1) 

# URL VARCHAR(2000),AccountHandle VARCHAR(50),Type VARCHAR(20),
def printSocialMediaSite():

    print("INSERT INTO SOCIALMEDIASITE VALUES")

    for i in range(0, 20):
        print("(\"www." + store_name[i] + ".com\", \"@" +store_name[i] 
            + "\", \"" + social_media[i%5] + "\")," )

def printBuyerPurchasesWith():
    print("INSERT INTO BuyerPurchasesWith VALUES")
    cardNumber = 1000000000000000000
    for i in range(0, len(user_fname)):
        for j in range(0, len(user_lname)):
            user = [user_fname[i], user_lname[j]]
            print("(\"" + str(user[0]) + "." + str(user[1]) + "@gmail.com\", "
                  + str(cardNumber) + "),")
            cardNumber += 1


def main():
    generateBTCWallets()
    generatePhone()

    generateGiftCards()
    # printGiftCards()

    # printBuyers()
    # printSellers()
    # printIP()
    # printUsers()
    # printMessage()
    # printCart()
    # printDebitCredit()
    # printIPorder()
    printStore()
    # printAnnouncements()
    # printPurchasedItem()
    # printSocialMediaSite()
    # generateDownloadURL()
    # printIPItem()

if __name__ == '__main__':
    main()