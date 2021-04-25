#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 14:06:19 2020

@author: yhhong
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1 import host_subplot

rootPath = ""
healthProfileFile = "Los_Angeles_County_City_and_Community_Health_Profiles_2018.csv"
covidDeathFile = "LA_County_Covid19_CSA_case_death_table.csv"
covidTestFile = "LA_County_Covid19_CSA_testing_table.csv"

# reading data
healthProfile = pd.read_csv(rootPath + healthProfileFile)
covidDeath = pd.read_csv(rootPath + covidDeathFile)
covidTest = pd.read_csv(rootPath + covidTestFile)

##########################################
### Data Cleaning
##########################################
del covidDeath["Unnamed: 0"] # remove the redundant index col
del covidTest["Unnamed: 0"] # remove the redundant index col

# remove row that is missing from covidDeath
covidDeath = covidDeath.drop(covidDeath[covidDeath["geo_merge"].isin(covidTest["geo_merge"]) == False].index)

# Verify that the rows of Los Angeles doesn't contain null value
print(covidDeath[covidDeath.geo_merge.str.contains("Los Angeles - ")].isnull().sum())
#combine data in City of Los Angeles
cityLosAngelesDeath = covidDeath[covidDeath.geo_merge.str.contains("Los Angeles - ")].sum()
cityLosAngelesDeath['geo_merge'] = 'Los Angeles, City of'
cityLosAngelesDeath['case_rate_final'] = int(cityLosAngelesDeath.cases_final/cityLosAngelesDeath.population*(10**5))
cityLosAngelesDeath['adj_case_rate_final'] = cityLosAngelesDeath['case_rate_final']
cityLosAngelesDeath['death_rate_final'] = int(cityLosAngelesDeath.deaths_final/cityLosAngelesDeath.population*(10**5))
cityLosAngelesDeath['adj_death_rate_final'] = cityLosAngelesDeath['death_rate_final']
covidDeathLA = covidDeath.append(cityLosAngelesDeath,ignore_index=True)

cityLosAngelesTest = covidTest[covidTest.geo_merge.str.contains("Los Angeles -")].sum()
cityLosAngelesTest['geo_merge'] = 'Los Angeles, City of'
cityLosAngelesTest['testing_rate_final'] = int(cityLosAngelesTest.testing_rate_final/cityLosAngelesTest.population*(10**5))
cityLosAngelesTest['adj_testing_rate_final'] = cityLosAngelesTest['testing_rate_final']
cityLosAngelesTest['pos_testing_rate_final'] = int(cityLosAngelesTest.pos_testing_rate_final/cityLosAngelesTest.population*(10**5))
cityLosAngelesTest['adj_pos_testing_rate_final'] = cityLosAngelesTest['pos_testing_rate_final']
covidTestLA = covidTest.append(cityLosAngelesTest,ignore_index=True)

# Rename some of the cities with the format "City of "
covidDeathLA.loc[covidDeathLA.geo_merge.str.contains('City of '),'geo_merge'] = covidDeathLA.geo_merge.str.replace("City of ","")
covidTestLA.loc[covidTestLA.geo_merge.str.contains('City of '),'geo_merge'] = covidTestLA.geo_merge.str.replace("City of ","")

# examing whether there are null/NA cells in the data frame
print(covidDeathLA.isnull().sum())
# there are 4 null values in "population" column, but those are in unincorporated area, not included in the file "Los_Angeles_County_City_and_Community_Health_Profiles_2018.csv"
print(covidTestLA.isnull().sum())
# column 'No_libr' contains nan value, which is from the row 'Los Angeles County', the sum of all column
# Remove the row later
print(healthProfile.isnull().sum().sort_values())
healthProfile = healthProfile.drop(healthProfile.loc[healthProfile['GEONAME'] == 'Los Angeles County'].index)

## convert numeric columns from text (object) to numbers
## columns with wrong dtype ['Prop_grad','Propt_HPI','Rte_hiv','Rte_syin','No_gasw','Propt_envi','Rte_CalF','No_CalF','No_EBT','No_farm','Prop_Eng','Prop_foin','Prop_obse','Prop_DM','Rte_coin','Rte_brin','Rte_luca','Rte_COPD','Prop_asth','Rte_hom','Rte_te17','Rte_te19','Rte_IMR','Rte_suic','Rte_UOD','Prop_duinC','Rte_mein','Rte_cein','Rte_luin','Prop_HI']
## Column 'No_CalF' has comma among numerical digits
healthProfile['No_CalF'] = healthProfile['No_CalF'].str.replace(",","")
colToFixNames = ['Prop_grad','Propt_HPI','Rte_hiv','Rte_syin','No_gasw','Propt_envi','No_CalF','Rte_CalF','No_EBT','No_farm','Prop_Eng','Prop_foin','Prop_obse','Prop_DM','Rte_coin','Rte_brin','Rte_luca','Rte_COPD','Prop_asth','Rte_hom','Rte_te17','Rte_te19','Rte_IMR','Rte_suic','Rte_UOD','Prop_duinC','Rte_mein','Rte_cein','Rte_luin','Prop_HI']
for c in colToFixNames:
    healthProfile[c] = pd.to_numeric(healthProfile[c],errors="coerce")

##############################################
## Consolidate three dataframes into one for further analysis
##############################################
covidTestRateLA = covidTestLA[covidTestLA['geo_merge'].isin(healthProfile['GEONAME']) == True][['testing_rate_final','pos_testing_rate_final']].reset_index(drop=True)
covidDeathRateLA = covidDeathLA[covidDeathLA['geo_merge'].isin(healthProfile['GEONAME']) == True][['case_rate_final','death_rate_final']].reset_index(drop=True)
healthProfileSelected = healthProfile[healthProfile.GEONAME.isin(covidTestLA['geo_merge'])].reset_index(drop=True)
consolidatedData = pd.concat([healthProfileSelected,covidTestRateLA,covidDeathRateLA],axis=1)
print(consolidatedData.head(5))

colMean = consolidatedData.mean(axis=0,numeric_only=True)
colStd = consolidatedData.std(axis=0,numeric_only=True)

# Ref: https://stackoverflow.com/questions/25039626/how-do-i-find-numeric-columns-in-pandas#28155580
# Ref: https://www.kaggle.com/omarhanyy/gradient-boosting-house-prices
numericalTypes = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
for col in consolidatedData:
    currentCol = consolidatedData[col]
    tempCol = consolidatedData[col]
    noNullVal = tempCol.isnull().sum()
	
    if noNullVal > 0 and (tempCol.dtype in numericalTypes):        
        randomValueList = np.random.uniform(colMean[col] - colStd[col] if colMean[col] - colStd[col] >= 0 else 0, colMean[col] + colStd[col], size=noNullVal)
        consolidatedData[col][tempCol.isna()] = randomValueList

#############################################
## Analysis
#############################################
# Calculating heat map of correlation
correlationMatrix = consolidatedData.corr()
sns.heatmap(consolidatedData.corr(), cmap = 'coolwarm')
healthRelatedCols = ['Prop_65y+','Prop_DM','Rte_coin','Rte_brin','Rte_COPD','Rte_CVD','Rte_cein','Rte_luin','Rte_mein','testing_rate_final','pos_testing_rate_final','case_rate_final','death_rate_final']
healthRelatedCorrelation = consolidatedData[healthRelatedCols]
sns.heatmap(healthRelatedCorrelation.corr(),cmap = 'coolwarm')

## Calculation of correation
correlationTestingRate = correlationMatrix['testing_rate_final'].sort_values(ascending=False)
print(correlationTestingRate.head(15))
correlationPosTestingRate = correlationMatrix['pos_testing_rate_final'].sort_values(ascending=False)
print(correlationPosTestingRate.head(15))
correlationCaseRate = correlationMatrix['case_rate_final'].sort_values(ascending=False)
print(correlationCaseRate.head(15))
correlationDeathRate = correlationMatrix['death_rate_final'].sort_values(ascending=False)
print(correlationDeathRate.head(15))
# print(correlationTestingRate.tail(15))
# print(correlationPosTestingRate.tail(15))
# print(correlationCaseRate.tail(15))
# print(correlationDeathRate.tail(15))

# Communities that rank high in the following health profiles
latinoPopTopCommunity = consolidatedData.sort_values(by=['Prop_Lat'],ascending=False).head(10)
truaRateTopcommunity = consolidatedData.sort_values(by=['Prop_trua'],ascending=False).head(10)
sugarTopCommunity = consolidatedData.sort_values(by=['Prop_bev'],ascending=False).head(10)
prop17yTopCommunity = consolidatedData.sort_values(by=['Prop_18y'],ascending=False).head(10)
lessThanhighSchollTopCommunity = consolidatedData.sort_values(by=['Prop_edLH'],ascending=False).head(10)
fpl2TopCommunity = consolidatedData.sort_values(by=['Prop_FPL2'],ascending=False).head(10)
fpl1TopCommunity = consolidatedData.sort_values(by=['Prop_FPL1'],ascending=False).head(10)
uninsuredAdultsTopCommunity = consolidatedData.sort_values(by=['Prop_uinA'],ascending=False).head(10)
newCervicalCancerFemaleTopCommunity = consolidatedData.sort_values(by=['Rte_cein'],ascending=False).head(10)

## merge all data frames above for further analysis
#print(list(latinoPopTopCommunity))
allColName = list(latinoPopTopCommunity)
selectedCommunities = pd.merge(latinoPopTopCommunity,truaRateTopcommunity, on=allColName, how='outer')
selectedCommunities = pd.merge(selectedCommunities, sugarTopCommunity, on=allColName, how='outer')
selectedCommunities = pd.merge(selectedCommunities, prop17yTopCommunity, on=allColName, how='outer')
selectedCommunities = pd.merge(selectedCommunities, lessThanhighSchollTopCommunity, on=allColName, how='outer')
selectedCommunities = pd.merge(selectedCommunities, fpl2TopCommunity, on=allColName, how='outer')
selectedCommunities = pd.merge(selectedCommunities, fpl1TopCommunity, on=allColName, how='outer')
selectedCommunities = pd.merge(selectedCommunities, uninsuredAdultsTopCommunity, on=allColName, how='outer')
selectedCommunities = pd.merge(selectedCommunities, newCervicalCancerFemaleTopCommunity, on=allColName, how='outer')
selectedCommunities = selectedCommunities.sort_values(by='pos_testing_rate_final', ascending = False)

## Using matplotlib to draw bar chart for visualization
posTestingRateData = selectedCommunities['pos_testing_rate_final'].values
caseRateFinalData = selectedCommunities['case_rate_final'].values
deathRateFinalData = selectedCommunities['death_rate_final'].values
latinoPopTopCommunityData = selectedCommunities['Prop_Lat'].values
truaRateTopcommunityData = selectedCommunities['Prop_trua'].values
sugarTopCommunityData = selectedCommunities['Prop_bev'].values
prop18yTopCommunityData = selectedCommunities['Prop_18y'].values
lessThanhighSchollTopCommunityData = selectedCommunities['Prop_edLH'].values
fpl2TopCommunityData = selectedCommunities['Prop_FPL2'].values
fpl1TopCommunityData = selectedCommunities['Prop_FPL1'].values
uninsuredAdultsTopCommunityData = selectedCommunities['Prop_uinA'].values
foodInsecurityTopCommunityData = selectedCommunities['Prop_foin'].values
cityLabels = selectedCommunities.GEONAME.tolist()

x = np.arange(len(cityLabels))
x = x*12
width = 1
shift = 8

fig, ax = plt.subplots(2)

rects1 = ax[0].bar(x - 1/3*shift, posTestingRateData, width, label='Postive Testing Rate')
rects2 = ax[0].bar(x, caseRateFinalData, width, label='Case Rate')
rects3 = ax[0].bar(x + 1/3*shift, 10*deathRateFinalData, width, label='Death Rate')
rects4 = ax[1].bar(x - 4/8*shift, latinoPopTopCommunityData, width, label='Latino residents')
rects5 = ax[1].bar(x - 3/8*shift, truaRateTopcommunityData, width, label='Truant public school students')
rects6 = ax[1].bar(x - 2/8*shift, sugarTopCommunityData, width, label='Consumption of sugar sweetened beverages')
rects7 = ax[1].bar(x, -1/8*prop18yTopCommunityData, width, label='Minor household member')
rects8 = ax[1].bar(x, lessThanhighSchollTopCommunityData, width, label='Less than HS education')
rects9 = ax[1].bar(x + 1/8*shift, fpl2TopCommunityData, width, label='Below 200% Federal Poverty Level')
rects10 = ax[1].bar(x + 2/8*shift, fpl1TopCommunityData, width, label='Below 100% Federal Poverty Level')
rects11 = ax[1].bar(x + 3/8*shift, uninsuredAdultsTopCommunityData, width, label='Underinsured Adults')
rects12 = ax[1].bar(x + 4/8*shift, uninsuredAdultsTopCommunityData, width, label='Food Insecurity among households')

ax[0].set_ylabel("rate\n(per 10k popuplation)")
ax[0].set_xticks(x)
ax[0].xaxis.set_tick_params(which='both', labelbottom=False)
ax[0].legend(loc="center", bbox_to_anchor=(0.5,1.4))
ax[1].set_ylabel("Proportion in city")
ax[1].set_xticks(x)
ax[1].set_xticklabels(cityLabels, rotation = -90)
ax[1].legend()
ax[1].legend(loc="center",bbox_to_anchor=(0.5,-1.7))

plt.show()
