library(dplyr)
library(ggplot2)
library(kableExtra)

df = read_csv('./plt/population.csv')

ggplot(df, aes(x = Age, fill = Gender,
                 y = ifelse(test = Gender == "Male",
                            yes = -Count, no = Count))) + 
  geom_bar(stat = "identity") +
  scale_y_continuous(labels = abs, limits = max(df$Count) * c(-1,1)) +
  labs(title = "Population Pyramid", x = "Age", y = "Number of death") +
  scale_colour_manual(values = c("pink", "steelblue"),
                      aesthetics = c("colour", "fill")) +
  coord_flip()

df2 = read_csv('./plt/races.csv')
df2[, 1] <- NULL

df2 %>%
  kbl() %>%
  kable_styling(bootstrap_options = "striped", full_width = F, position = "center")