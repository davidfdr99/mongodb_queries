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
  kbl(caption = "Drug-related Deaths per Race in CT (2012-2021)") %>%
  kable_classic("striped", full_width=F, html_font = "Cambria")

df3 <- data.frame("Task" = c("Pipeline 1", "Pipeline 2", "Pipeline 3", "Pipeline 4", "Pipeline 5","Pipeline 6", "Pipeline 7", "Pipeline 8"),
        "Hadoop" = c("23s", "", "", "24s", "", "", "", ""),
        "PyMongo Aggregate Pipeline" = c("0.084974s", "0.0708818s", "0.086834s", "0.072529s",
          "0.069751s", "0.067856s", "0.086834s", "0.395058s")
        )

df3 %>%
  kbl(caption = "Execution Time Comparison", 
      col.names = c("Task", "Hadoop", "PyMongo Aggregate Pipeline"),
      align = c("lcc")) %>%
  kable_classic("striped", full_width=F, html_font = "Cambria") 

