
# Web Scraper of COVID-19 data for Czechia

Python package [covid19czechia](https://pypi.org/project/covid19czechia/) provides access to COVID-19 data of Czechia.

The data is scraped from

* Ministry of Health, Czech Republic
* Czech Statistical Office

## Setup and usage

Install from [pip](https://pypi.org/project/covid19czechia/) with

```python
pip install covid19czechia
```

Importing module is done such as

```python
import covid19czechia as CZ

x = CZ.covid_deaths()
```

Package is regularly updated. Update with

```bash
pip install --upgrade covid19czechia
```

## COVID-19 Cases

Get Covid-19 cases in Czechia.

```python
x = CZ.covid_confirmed_cases()
```

Aggregated dataframe countrywise / regionwise / districtwise can be fetched using

```python
x1 = CZ.covid_confirmed(level = 1) # country
x2 = CZ.covid_confirmed(level = 2) # region
x3 = CZ.covid_confirmed(level = 3) # district
```

The data contains counts by age, age group and sex and information of week. To aggregate results only over some of the groups (example - per day)

```python
x = x\
    .groupby(['date','week'])\
    .aggregate({'confirmed': 'sum'})\
    .reset_index()
```

Result of the example contains columns day, week and confirmed.

## COVID-19 Tests

Get Covid-19 tests in Czechia.

```python
x1 = CZ.covid_tests(level = 1) # country
x2 = CZ.covid_tests(level = 2) # region
x3 = CZ.covid_tests(level = 3) # district
```

## COVID-19 Deaths

Get Covid-19 deaths in Czechia (weekly counts, by gender and age group)

```python
x = CZ.covid_deaths()
```

The function returns Pandas dataframe. It can be stored to csv file with

```python
x.to_csv("filename.csv", header = True, index = False)
```

### Administrative unit setting

Optional parameter `level` sets granularity of administrative units
the deaths are computed in.

Defaultly (`level = 1`) the deaths are taken from the whole Czechia.

```python
x = CZ.covid_deaths(level = 1) # same as no argument given (above)
```

Settings `level = 2` corresponds with deaths in regions (*kraje*, NUTS 3).

```python
x = CZ.covid_deaths(level = 2)
```

Setting `level = 3` means deaths per district (*okresy*, LAU 1).

```python
x = CZ.covid_deaths(level = 3)
```

Read more about administrative units of Czech Republic
[here](https://en.wikipedia.org/wiki/NUTS_statistical_regions_of_the_Czech_Republic).

## Total weekly deaths

For total deaths check my another package [eurostat_deaths](https://github.com/martinbenes1996/eurostat_deaths).


