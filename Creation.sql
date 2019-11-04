PRAGMA foreign_keys=ON;  -- for sqlite to enforce foreign key constraints

CREATE TABLE UserInfo( 
Email VARCHAR(25), 
Username VARCHAR(25) UNIQUE NOT NULL,
Password VARCHAR(25) NOT NULL, 
Phone VARCHAR(12) NOT NULL, 
Fname VARCHAR(30) NOT NULL,
Lname VARCHAR(30) NOT NULL,
Karma INT NOT NULL, 
Notify BIT DEFAULT 0,
PRIMARY KEY(Email)
); 
CREATE TABLE Buyer(
Email VARCHAR(25),
WalletKey VARCHAR(32),
PRIMARY KEY (Email),
FOREIGN KEY (Email) REFERENCES UserInfo(Email) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE Seller(
Email VARCHAR(25),
SellerBio VARCHAR(400) NOT NULL,
SellerID CHAR(20) UNIQUE NOT NULL,
PRIMARY KEY (Email),
FOREIGN KEY (Email) REFERENCES UserInfo(Email) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE GiftCard(
RedeemCode CHAR(20),
Pin CHAR(4),
Currency CHAR(3),
Balance FLOAT,
Email VARCHAR(25) NOT NULL,
PRIMARY KEY(RedeemCode, Pin),
FOREIGN KEY (Email) REFERENCES Buyer(Email) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE Message(
SentOn DATETIME NOT NULL,
Topic VARCHAR(20) NOT NULL,
Content VARCHAR(400) NOT NULL,
ReceiverEmail VARCHAR(25),
SenderEmail VARCHAR(25),
PRIMARY KEY (SentOn, ReceiverEmail, SenderEmail),
FOREIGN KEY (ReceiverEmail) REFERENCES UserInfo(Email) ON DELETE CASCADE ON UPDATE CASCADE,
FOREIGN KEY (SenderEmail) REFERENCES UserInfo(Email) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE Cart(
CartID INT,
Email VARCHAR(25) NOT NULL,
PRIMARY KEY (CartID),
FOREIGN KEY (Email) REFERENCES Buyer(Email) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE DebitCreditCard(
CardNumber INT, 
SecurityCode INT NOT NULL, 
ExpirationDate DATE NOT NULL, 
FirstName VARCHAR(30) NOT NULL, 
LastName VARCHAR (30) NOT NULL,
CreditCardCompany VARCHAR(20) NOT NULL,
BuildingNum VARCHAR(6) NOT NULL,
Street VARCHAR(40) NOT NULL,
City VARCHAR(30) NOT NULL,
State VARCHAR(30) NOT NULL,
Zip VARCHAR(9) NOT NULL,
Country VARCHAR(40) NOT NULL,
PRIMARY KEY (CardNumber)
);
CREATE TABLE IPOrder(
CartID INT NOT NULL,
OrderNumber CHAR(20), 
DateTimePlaced DATETIME NOT NULL,
PRIMARY KEY (OrderNumber), 
FOREIGN KEY (CartID) REFERENCES Cart(CartID) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE Store(
StoreName VARCHAR(40) NOT NULL,
StoreDescription VARCHAR(400),
AccountNum VARCHAR(17),
RoutingNum CHAR(9),
WalletKey VARCHAR(32),
Email VARCHAR(25) NOT NULL,
PRIMARY KEY(StoreName),
FOREIGN KEY (Email) REFERENCES Seller(Email) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE SocialMediaSite(
URL VARCHAR(2000),
AccountHandle VARCHAR(50),
Type VARCHAR(20),
PRIMARY KEY(URL)
);
CREATE TABLE IPItem(
DownloadURL VARCHAR(2000), 
ReleaseDate DATETIME NOT NULL, 
Title VARCHAR(40) UNIQUE NOT NULL,
Category VARCHAR(20) NOT NULL, 
Description VARCHAR(400) NOT NULL, 
FileType VARCHAR (8) NOT NULL,
IsForSale BIT NOT NULL,
Trial VARCHAR(2000) NOT NULL,
StoreName VARCHAR(40) NOT NULL,
PRIMARY KEY(DownloadURL),
FOREIGN KEY(StoreName) REFERENCES Store(StoreName) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE Picture(
ImageLink VARCHAR(2000),
Type VARCHAR(30),
AltText VARCHAR(75) NOT NULL,
DownloadURL VARCHAR(2000),
PRIMARY KEY (ImageLink),
FOREIGN KEY (DownloadURL) REFERENCES IPItem(DownloadURL) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE IP_Keywords(
Keyword VARCHAR(15), 
DownloadURL VARCHAR(2000),
PRIMARY KEY(Keyword, DownloadURL),
FOREIGN KEY(DownloadURL) REFERENCES IPItem(DownloadURL) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE Announcements(
Headline VARCHAR(40), 
StoreName VARCHAR(40), 
Type VARCHAR(15) NOT NULL, 
Content VARCHAR(400) NOT NULL, 
PostedOn DATETIME NOT NULL,
PRIMARY KEY(Headline, StoreName),
FOREIGN KEY(StoreName) REFERENCES Store(StoreName) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE PurchasedItem(
OrderNumber CHAR(20), 
DownloadURL VARCHAR(2000), 
Rating FLOAT, 
Review VARCHAR(400), 
TransactionMethod VARCHAR(7) NOT NULL, 
DeliveryEmail VARCHAR(25),
TransactionAmount FLOAT,
PRIMARY KEY(OrderNumber, DownloadURL),
FOREIGN KEY (OrderNumber) REFERENCES IPOrder(OrderNumber) ON DELETE CASCADE ON UPDATE CASCADE,
FOREIGN KEY (DownloadURL) REFERENCES IPItem(DownloadURL) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE AcceptedPayments(
PaymentType VARCHAR(7), 
PaymentAmount FLOAT, 
DownloadURL VARCHAR(2000) NOT NULL,
PRIMARY KEY(PaymentType, PaymentAmount, DownloadURL),
FOREIGN KEY(DownloadURL) REFERENCES IPItem(DownloadURL) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE Contain(
DownloadURL VARCHAR(2000),
CartID INT,
PRIMARY KEY(CartID, DownloadURL),
FOREIGN KEY(CartID) REFERENCES Cart(CartID) ON DELETE CASCADE ON UPDATE CASCADE,
FOREIGN KEY(DownloadURL) REFERENCES IPItem(DownloadURL) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE PostOn(
URL VARCHAR(2000),
StoreName VARCHAR(40),
PRIMARY KEY(URL, StoreName),
FOREIGN KEY(URL) REFERENCES SocialMediaSite(URL) ON DELETE CASCADE ON UPDATE CASCADE,
FOREIGN KEY(StoreName) REFERENCES Store(StoreName) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE BuyerPurchasesWith(
Email VARCHAR(25),
CardNumber INT,
PRIMARY KEY(Email, CardNumber),
FOREIGN KEY(Email) REFERENCES Buyer(Email) ON DELETE CASCADE ON UPDATE CASCADE,
FOREIGN KEY(CardNumber) REFERENCES DebitCreditCard(CardNumber) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE Follow(
Email VARCHAR(25),
StoreName VARCHAR(40),
NOTIFY BIT DEFAULT 0,
PRIMARY KEY(Email, StoreName),
FOREIGN KEY(Email) REFERENCES Buyer(Email) ON DELETE CASCADE ON UPDATE CASCADE,
FOREIGN KEY(StoreName) REFERENCES Store(StoreName) ON DELETE CASCADE ON UPDATE CASCADE
);
ALTER TABLE Store ADD ImageLink VARCHAR(2000) REFERENCES Picture(ImageLink) ON DELETE SET NULL ON UPDATE CASCADE;
ALTER TABLE SELLER ADD ImageLink VARCHAR(2000) REFERENCES Picture(ImageLink) ON DELETE SET NULL ON UPDATE CASCADE;
