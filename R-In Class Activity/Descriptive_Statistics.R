# read csv file

af <- datasets::airquality
View(af)

# Top 10 rows and last 10 rows

head(af)       # top 6 Elements

head(af,15)    # mentioned number of elements will be displayed

tail(af)       # lower 6 elements will be displayed
tail(af,7)

# Extract records from 5 to 25 and from 1 to 5 columns

View(af[5:25,1:5])

# Extract 10,24 record and 1 column

af[c(10,24),1]

# Extract from 15, 24, 30 record from 1 and 5 column

af[c(15,24,30),c(1,5)]     


####Summary of Data####

summary(af)   #Summary of the data set

af$Month      #value of particular column

summary(af$Ozone)   #summary of column     

attach(af)     #attach function is used to attach the mostly used variables with the file
Month

## detach() function is used to detach the attached data

## Data Visualization

#  1. Scatter Plot

plot(x=Ozone, y= Temp, xlab = "Ozone Levels", ylab = "Temprature",main = "Scatter Plot",
     pch=19)
plot(Temp, Wind,col="blue",pch=19)

#  2. Line Plot
plot(Ozone, type = 'l', col="green")

# Plotting the complete the Data set

plot(af)

# 3. Horizontal Bar Plot

unique(Month)    # Unique function is used to find out the unique values in column

barplot(Month)   # Function used to plot the bar graph



table(Month)     # This will give table with the value and the number of time it occurs 
freq <- c(31,30,31,31,30)

barplot(freq,names.arg = c(5,6,7,8,9))   # Type 1 
barplot(freq,names.arg = unique(Month), col='green')  # Type 2

# 4. Histogram

hist(Ozone)     # Function for finding the Histogram
plot(density(Temp))

# -1 to 1 high skewness, -0.5 to 0.5 moderate skewness, 0 = normal

# 5. Single box plot and stats

boxplot(Ozone)

boxplot(Ozone)$stats  # $ function will generate statistics of column like upper, lower extreme etc

boxplot(Ozone)$out    # $out is used to find out the outliers values

# Multiple Box Plots

boxplot(af)     # Box plot for complete data 

boxplot(af, col = c("green","red","yellow","orange","black","brown"))

# Multiple graphs in one canvas

par(mfrow = c(2,2), mar = c(2,2,2,2))  
# par function used to split canvas into required rows and column
# mfrow function is used to specify the rows and columns
# mar is used to specify the margin starting from bottom

plot(Ozone, Temp)
hist(Temp,col="blue")
boxplot(Ozone, col="red")
plot(Ozone, type ='l', col="green")

# Standard Deviation, Mean, Median, Variance, Min, Max

sd(Temp)    # Standard Deviation

mean(Temp)   # Mean

median(Temp)  # Median

var(Temp)    # Variance

min(Temp)   # Minimum

max(Temp)   # Maximum

install.packages('moments')    # installing the packages
library(moments)       # Importing the Packeges

skewness(Temp)    # Skewness
skewness(Ozone,na.rm=T)   # na.rm is used to remove the missing values

kurtosis(Temp)
