#!/usr/bin/env python
# coding: utf-8

# # Macroeconomic Indicators
# The process of conducting macroeconomic policy often starts with studying and projecting the behavior of a variety of indicators that provide some information about the economy's current or expected future performance. While there are many different variables one could look to depending on the interests and goals of the individual(s) or institution(s) involved, in this chapter we will focus specifically on four main indicators that tend to play a critical role in many policy decisions.
# 

# ## GDP ($Y$)
# Earlier, when studying Production, we introduced the concept of GDP briefly. To recap, we looked at how GDP aims to capture a country's overall production over a given period of time. In theory it can then be used as a way to measure a country's economic performance in a given quarter or year; the higher its GDP, the more that it's produced, the better it's doing economically, and vice versa. In this chapter, we'll go into more detail on its significance and how it's measured. By definition, GDP, often denoted as $Y$, is measured as the:
# 1. **market value** of 
# 2. **final** goods and services
# 3. **newly produced**
# 4. in the **domestic economy**
# 5. over a **specified period of time**
# 
# Let's dive into each of these individually:
# 
# First, the **market value** refers to the market price of price goods and services, which sets a standard for how we value goods and services. This is especially useful when we are trying to add together products that may be quite different from one another.
# 
# Second, **final goods and services** refers to those which *are not* used up in the production process. We only consider these in our calculation of GDP, because we don't want to end up overrepresenting the overall level of production. Intermediate goods, which *are* used up in the production process, inherently add some value to the final product, and therefore if we were to consider these in our calculation, we would end up overstating the level of production.
# 
# Third, **newly produced** tells us that we are only interested in goods and services that were made during the time period we are looking at. Since we are using GDP as a way to measure the level of production in the economy, it wouldn't really make a whole lot of sense to include products that were produced outside the time period that we are looking at in our calculation.
# 
# Fourth, **in the domestic economy** refers to the fact that in our calculation of GDP we only include goods and services that were produced within the geographical area of the country that we are looking at. Given that we are trying to measure the  level of production of a certain country, it makes sense that we wouldn't want to consider products or services that are produced outside of the country in our calculation.
# 
# Lastly, **over a specified period of time** simply points out that GDP is measured as a unit of time. This is important to consider when comparing countries based on their GDP, as we would want to make sure to consider the same time period for all of them.
# 
# The above definition and approach to calculating GDP considers the production of goods and services in the economy. However, it's important to note that GDP can also be calculated by looking at the total spending on those goods and services or total income earned from producing those goods and services. You may recall that in our discussion on Production, we often referred to output and income synonomously. This is because in theory, each of these approaches to calculating GDP (production, expenditure, and income) should all yield the same result, and indeed we find that for the most part they do. While we won't go into detail on the income approach to calculating GDP, we will take a look at the expenditure approach later on in this chapter.
# 

# ## Unemployment Rate ($U$)
# The unemployment rate is also an important measure of a country's economic performance, as it gives us some insight on the supply and demand of labor in the economy. By definition, the unemployment rate measures the percentage of the labor force &ndash; the sum of all employed and unemployed people &ndash; that is not currently employed, but is willing, able, and looking for work. Mathematically, this can be expressed by the following equation:
# 
# $$Unemployment Rate = \frac{Unemployed}{Labor Force}$$
# 
# As stated before, the labor force is just the sum of all employed and unemployed persons in the population, so we can simplify the equation above to be
# 
# $$Unemployment Rate = \frac{Unemployed}{Employed + Unemployed}$$
# 
# An important thing to remember, is that in order to be considered unemployed, a person must be able, willing, and currently looking for work. This means that anyone who is unable to work or has stopped looking for a job is no longer considered part of the labor force and is therefore not included in the unemployment rate. Intuitively this makes sense for the most part, as it probably wouldn't be very helpful to include retirees or stay-at-home parents or even students for that matter when calculating the unemployment rate. It's worth considering, however, that this also means that people who have been unable to find any work and therefore stopped looking &ndash; often referred to as discouraged workers &ndash; would not be represented in the unemployment rate either.
# 
# 

# ## Inflation Rate ($\pi$)
# Generally speaking, the inflation rate in an economy measures the percent change in prices over a specified period of time, and it is usually calculated using a price index. While there are many different price indices that can be used to calculate inflation, one of the more common ones is the Consumer Price Index (CPI). The CPI measures the average price for a basket of goods and services relative to some defined base year, and is calculated by taking the value of said basket in any given year, dividing it by its value in the base year, and multiplying that by 100. Mathematically, this can be expressed as
# 
# $$ CPI_t = \frac{Price~of~Goods_t}{Price~of~Goods_0} * 100$$   
# 
# where t = 0 refers to the base year.
# 
# We can then calculate the inflation rate for a given year as
# 
# $$ \pi_t = \frac{CPI_t - CPI_{t-1}}{CPI_{t-1}} * 100$$     
# 
# The inflation rate is yet another key indicator that macroeconomists look at, as it also tends to be a representation of a country's overall economic performance. A small, positive inflation rate is considered a good thing, as it's usually an indication of a growing economy. However, inflation rates that are negative or too high can create a lot of problems, and as such the inflation rate tends to play an important role in guiding monetary policy decisions &ndash; something we will discuss more later in this chapter.
# 
# 

# ## Real Interest Rate ($r$)
# If you have a bank account or own a credit card or have ever taken a loan, chances are that you've come across an interest rate at some point. In general, interest rates represent the cost of borrowing or on the flip side the return on saving or lending. There are many different interest rates that can be found in the economy from interest rates for savings accounts to interest rates charged for mortgages to interest rates set by the Central Bank. All of the interest rates that we observe in the economy are known as nominal interest rates &ndash; interest rates that are not adjusted for inflation.
# 
# As discussed earlier, inflation measures the change in prices over a given time and can be used in some sense to measure the relative value of a dollar (or other unit of currency) over time. It makes sense then, that we might want to take into inflation into account, when deciding what interest rate would make sense to lend/borrow at. To do this, we use real interest rates, which are calculated by taking nominal interest rates and subtracting inflation. This relationship between inflation, nominal interest rates, and real interest rates is captured by what is known as the Fisher Equation
# 
# $$ r_t = i_t - \pi_t $$   
# where $r_t$ refers to the real interest rate, $i_t$ refers to the nominal interest rate, and $\pi_t$ refers to the inflation rate, all in a given time period.
# 
# As a final note, we find that generally speaking all of the nominal interest rates present in the economy tend to be pretty strongly correlated with each other. Therefore, for purposes of simplification, macroeconomists will often refer to these rates in singular form in their models as simply the nominal interest rate or the real interest rate. As seen in the Fisher equation above, we use $i$ to denote the nominal interest rate, and $r$ to denote the real interest rate.

# In[ ]:




