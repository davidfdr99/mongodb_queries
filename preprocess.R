library(dplyr)
library(lubridate)
library(data.table)

df <- read.csv('./data/Accidental_Drug_Related_Deaths_2012-2021.csv', header = TRUE, check.names=FALSE, na.strings=c("", "NaN", "na"))
                     
df$Date = format_ISO8601(as.POSIXlt.character(df$Date, tryFormats = "%m/%d/%Y"))

df[, 23:44][is.na(df[, 23:44])] <- 0
df[, 23:44][df[, 23:44] == "Y"] <- 1

write_csv(df, './data/data2.csv')
