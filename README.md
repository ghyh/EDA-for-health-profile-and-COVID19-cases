# EDA-for-health-profile-and-COVID19-cases
<h1>Purpose</h1>
This study is trying to visit the situation of COVID-19 from a bottom-up perspective by investigating the relationship between the local “health indicators” (or health profiles)[4] and the COVID-19 stats, including testing[5] and mortality rate[6]*, in each city/community** in Los Angeles county, California.  
  
   
*: the data was collected till 11/9/2020. Data from City of Pasadena and Long Beach are not included.  
**: Unincorporated areas are not included in the discussion in this study.  

<h1>Results and Analysis</h1>
It is well-known that COVID-19 is especially lethal to elder people and people with underlying medical condition [13]. Therefore, I also examined the correlation between the health indicators that accounts for underlying medical conditions, like cancer and diabetes, and the COVID-19-related metrics. It’s also surprising that there is no significant correlation (the correlation coefficients are between 0.3 to -0.6) between them, as shown in the figure below, when it comes to the discussion of collective outcome. More data and scientific evidences, such as public health, will be needed to understand this result.

![image](https://user-images.githubusercontent.com/30448897/115976058-116f2d00-a51f-11eb-9fd6-f0d8756e471c.png)

It would be natural to dig into the health indicators with large correlation coefficient associated with COVID-related metrics to  further understand which indicator characterizes the situation of each city/community during pandemic. I picked the top 10 cities in each indicator for analysis (some of them overlap among different indicators), and the result can be found in the figure below. One can see that even when a city has many indicators that rank high among the selected cities (bottom panel), it doesn’t necessary mean it results in high rate of positive cases or high mortality rate (top panel).

![image](https://user-images.githubusercontent.com/30448897/115976059-17650e00-a51f-11eb-8bfa-51eb1d85310a.png)

Although the mortality rate or positive rate of COVID-19 of a city/community cannot attribute to one or a few health indicators, one can still find that most of the health indicators can be linked to two main categories, race and financial status. For example, Prop_FPL1, Prop_FPL2, Prop_foin, Prop_uinA, and Prop_trua fall into the later category. This result is not only consistent with the current situation in LA county that Latino communities have been hit hard by this pandemic [3], [14], [15], but also resonant with the beginning of this report that lower-income families[3], [16] have been impacted the most. The analysis also show that the population/group without college degree, which has the largest correlation coefficient for COVID-19 mortality rate, is the most representative indicator to account for the fact: people without college degree form the majority of essential and front-line workers[17], [18], who have no choice to work from home (WFH) and therefore become the most vulnerable group during pandemic.

<h1>Conclusion</h1>
	Thru the discussion and analysis above, it’s almost certain that under-privilege communities are vulnerable in this pandemic, and we can also predict that this type of communities could be impacted a lot during the next pandemic. While we all took Bill Gate’s warning[23], [24] about this pandemic lightly, we have to be more prepared for the surely-to-come next one[25], [26].  


<h2>Reference</h2>
[1]	“We looked at coronavirus in 8,500 ZIP codes across America. Here’s what we found.” https://www.usatoday.com/in-depth/graphics/2020/06/30/maps-covid-19-rich-and-poor-neighborhoods-show-big-disparities/3257615001/ .
[2]	“New COVID-19 Data: How Low-Income & Minority Americans Are Coping,” Ad Council Org, May 18, 2020. https://www.adcouncil.org/all-articles/new-data-how-low-income-minority-americans-are-coping-with-covid-19 .
[3]	A. Goldstein, “Income emerges as a major predictor of coronavirus infections, along with race,” Washington Post.
[4]	“Los Angeles County City and Community Health Profiles 2018 | LAC Open Data.” https://data.lacounty.gov/Health/Los-Angeles-County-City-and-Community-Health-Profi/capb-kusk .
[5]	“COVID-19 Los Angeles County Persons Tested and Positive Persons Tested by City/Community,” Covid-19 Dashboard. https://lacdph.shinyapps.io/covid19_surveillance_dashboard/_w_a060f0ca/#shiny-tab-city_test_table.
[6]	“COVID-19 Los Angeles County Cases and Deaths by City/Community,” Covid-19 Dashboard. https://lacdph.shinyapps.io/covid19_surveillance_dashboard/_w_a060f0ca/#shiny-tab-city_case_table.
[7]	“pandas - Python Data Analysis Library.” https://pandas.pydata.org/ .
[8]	“seaborn: statistical data visualization — seaborn 0.11.0 documentation.” https://seaborn.pydata.org/ .
[9]	“Matplotlib: Python plotting — Matplotlib 3.3.3 documentation.” https://matplotlib.org/ .
[10]	“NumPy.” https://numpy.org/ .
[11]	Omar Hany, “Gradient Boosting - House Prices.” https://kaggle.com/omarhanyy/gradient-boosting-house-prices .
[12]	“Correlation and dependence,” Wikipedia. Oct. 27, 2020. [Online]. Available: https://en.wikipedia.org/w/index.php?title=Correlation_and_dependence&oldid=985669192.
[13]	“CDC: 94% of Covid-19 deaths had underlying medical conditions,” MSN. https://www.msn.com/en-us/health/medical/cdc-94percent-of-covid-19-deaths-had-underlying-medical-conditions/ar-BB18wrA7 .
[14]	“UCLA researchers find higher COVID positivity rates in Los Angeles County communities with high Latino populations, low incomes.” https://www.newswise.com/coronavirus/ucla-researchers-find-higher-covid-positivity-rates-in-communities-with-high-latino-populations-low-incomes .
[15]	“San Fernando Valley’s Latino neighborhoods hit hard by L.A. County’s COVID-19 outbreak,” KTLA, Dec. 01, 2020. https://ktla.com/news/local-news/san-fernando-valleys-latino-neighborhoods-hit-hard-by-l-a-countys-covid-19-outbreak/ .
[16]	K. Parker, R. Minkin, and J. Bennett, “Economic Fallout From COVID-19 Continues To Hit Lower-Income Americans the Hardest,” Pew Research Center’s Social & Demographic Trends Project, Sep. 24, 2020. https://www.pewsocialtrends.org/2020/09/24/economic-fallout-from-covid-19-continues-to-hit-lower-income-americans-the-hardest/ .
[17]	Adie Tomer and Joseph Kane, “To protect frontline workers during and after COVID-19, we must define who they are,” Brookings, Jun. 10, 2020. https://www.brookings.edu/research/to-protect-frontline-workers-during-and-after-covid-19-we-must-define-who-they-are/ .
[18]	Francine D. Blau, Josefine Koebe and Pamela A. Meyerhofer, Josefine Koebe, and FraPamela A. Meyerhofer, “Essential and Frontline Workers in the COVID-19 Crisis | Econofact,” May 01, 2020. https://econofact.org/essential-and-frontline-workers-in-the-covid-19-crisis .
[19]	N. Scheiber, N. D. Schwartz, and T. Hsu, “‘White-Collar Quarantine’ Over Virus Spotlights Class Divide,” The New York Times, Mar. 27, 2020.
[20]	J. DeParle, “The Coronavirus Class Divide: Space and Privacy,” The New York Times, Apr. 12, 2020.
[21]	“Coronavirus and the widening educational digital divide: The perfect storm for inequalities?,” California Management Review. https://cmr.berkeley.edu/2020/07/covid-education/ .
[22]	“The pandemic could widen the achievement gap. A generation of students is at risk.,” POLITICO. https://www.politico.com/news/2020/09/23/how-the-coronavirus-is-making-school-segregation-worse-420839 .
[23]	“Bill Gates warned of a deadly pandemic for years — and said we wouldn’t be ready to handle it.” https://www.cbsnews.com/news/coronavirus-bill-gates-epidemic-warning-readiness/ .
[24]	“Coronavirus: Bill Gates predicted pandemic in 2015,” The Mercury News, Mar. 25, 2020. https://www.mercurynews.com/2020/03/25/coronavirus-bill-gates-predicted-pandemic-in-2015 .
[25]	“As COVID-19 continues, experts warn of next pandemic likely to come from animals,” MSN. https://www.msn.com/en-us/health/medical/as-covid-19-continues-experts-warn-of-next-pandemic-likely-to-come-from-animals/ar-BB18FURO (accessed Dec. 02, 2020).
[26]	“Amazon could be the origin of the next global pandemic, scientist warns | Fox News.” https://www.foxnews.com/science/amazon-source-next-global-pandemic-scientist-warns .
