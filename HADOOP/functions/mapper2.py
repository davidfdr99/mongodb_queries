#!/usr/bin/env python 
import sys 
for line in sys.stdin: 
	data = line.strip().split('\t')
	if len(data) == 48: 
		Date, Date_Type, Age, Sex, Race, Ethnicity, Residence_City, Residence_County, Residence_State, Injury_City, Injury_County, Injury_State, Injury_Place, Description_of_Injury, Death_City, Death_County, Death_State, Location, Location_if_Other, Cause_of_Death, Manner_of_Death, Other_Significant_Conditions, Heroin, Heroin_DC, Cocaine, Fentanyl, Fentanyl_Analogue, Oxycodone, Oxymorphone, Ethanol, Hydrocodone, Benzodiazepine, Methadone, Meth_Amphetamine, Amphet, Tramad, Hydromorphone, Morphine_Not_Heroin, Xylazine, Gabapentin, Opiate_NOS, Heroin_Morph_Codeine, Other_Opioid, Any_Opioid, Other, ResidenceCityGeo, InjuryCityGeo, DeathCityGeo = data 
		print("{0}".format(Race)) 
