library(dplyr)
library(lubridate)
library(data.table)

df <- read.csv('./data/Accidental_Drug_Related_Deaths_2012-2021.csv',
header = TRUE, check.names=FALSE, na.strings=c("", "NaN", "na"))
                     
df$Date <- format_ISO8601(as.POSIXlt.character(df$Date, tryFormats = "%m/%d/%Y"))

# df[, 23:44][is.na(df[, 23:44])] <- ""
df[, 23:44][df[, 23:44] == "Y"] <- 1

drugs_col_names = colnames(df[23:43])

add_drugs_doc <- function(x){
  res = paste('drugs', x, sep=".")
  return(res)
}
new_cols <- lapply(drugs_col_names, add_drugs_doc)
colnames <- names(df)
colnames[23:43] <- paste(new_cols)
colnames(df) <- colnames

write_csv(df, './data/data2.csv')