library(dplyr)
library(lubridate)

df <- read.csv('./data/Accidental_Drug_Related_Deaths_2012-2021.csv', header = TRUE, check.names=FALSE)
                     
df$Date = format_ISO8601(as.POSIXlt.character(df$Date, tryFormats = "%m/%d/%Y"))

head(df)

write_csv(df, './data/dataFinal.csv')
