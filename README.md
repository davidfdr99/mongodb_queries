# Queries and data visualisation in MongoDB

This repository inculdes scripts performing queries in a database of drug-related accidental deaths in the State of Connecticut (CT) from 2012-2021.

The dataset can be accessed through [data.gov](https://catalog.data.gov/dataset/accidental-drug-related-deaths-2012-2018). The database was imported locally and accessed through the PyMongo library.

## Queries

`mp_pm_python` contains the functions for map-reduce operations that are deprecated since the release of MongoDB 5.0

`pipelines` contains the aggregations pipelines for the respective queries

## References

"Accidental Drug Related Deaths 2012-2021", https://catalog.data.gov/dataset/accidental-drug-related-deaths-2012-2018, last accessed: 06/12/22, 13:52 MEZ

"Introduction to colour schemes", Paul Tol's Notes, https://personal.sron.nl/~pault/, last accessed: 06/12/22, 13:54