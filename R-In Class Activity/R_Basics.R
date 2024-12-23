a = 5
a
A <- 50+50
A
class(A)

T
class(T)
f <- TRUE
class(f)
x <- a+A
x


marks <- c(10,20,30)
marks
names <- c("Riddhesh","Samiksha")
names
info <- c("abhi",0,1.1)
info

info[1]



# Accessing Elements

info[1:2]
info[c(1,3)]

#Function in R
match(0,info)

# Assigning or replacing values in Vector.

names[1] <- "Riddhu Dalring"
names
marks[1:3] <- c(55,60,80)
marks

#List Creation

lst <- list(50L,"Abhi",68.56,FALSE)
lst
#Accessing the elements of list
lst[2]
lst[2:4]
lst[1] <- 700
lst[1]

#Data Frame Creation

ID <- c(1,2,3,4,5,6)
Names <- c("Abhi","Rushi","Athu","Kunu","Suru","Riddhu")
Age <- c(22,23,22,21,22,20)
Dept <- c("Scientist","Analayst","Developer","HR","Finance","Accounts")

df <- data.frame(ID,Names,Age,Dept)
df
View(df)

#Accessing elements from Data Frame

df[5,4]
df[1,1:3]
df[1,c(2,4)]
df[c(1,2),c(1:4)]

#Replacing the elements from data frame

df[2,4] <- "Clerk"
df[4:5,4] <- c("Chef","Maid")
View(df)
