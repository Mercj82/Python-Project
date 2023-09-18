import pandas as pd

# Load your data into a DataFrame (replace 'data.csv' with your data file)
df = pd.read_csv('C:/Users/merce/Downloads/insurance.csv')
#import file
print(df.head())
print(df.tail())
#see first few columns
missing_values = df.isnull().sum()
print(missing_values)
#missing values
df['bmi'] = df['bmi'].round(2)
print(df)
#round bmi first two decimals 
df = df.drop_duplicates()
#remove duplicates
df = df.rename(columns={'age': 'Age', 'sex': 'Sex', 'bmi': 'BMI', 'children': 'Children', 'smoker': 'Smoker', 'region': 'Region', 'charges': 'Charges'})
#change columns names
print(df.dtypes)
#data types
df = pd.get_dummies(df, columns=['Sex', 'Smoker'], prefix=['sex', 'smoker'], drop_first=True)
#encoding categorical
avg_charges_by_region = df.groupby('Region')['Charges'].mean()
print(avg_charges_by_region)
#show avg by region
# Display the column names in your DataFrame
print(df.columns)
#columns name
average_charges_smokers = df[df['smoker_yes'] == 1]['Charges'].mean()
print(average_charges_smokers)
average_charges_non_smokers = df[df['smoker_yes'] == 0]['Charges'].mean()
print(average_charges_non_smokers)
#avg medical charges for smokers vs. non smokers
from scipy import stats
p_value = stats.ttest_ind(df[df['smoker_yes'] == 1]['Charges'], df[df['smoker_yes'] == 0]['Charges']).pvalue
print(p_value)
#perform a statistical test
if p_value < 0.05:
    print("The difference in charges between smokers and non-smokers is statistically significant.")
else:
    print("There is no significant difference in charges between smokers and non-smokers.")
#interpret results
correlation = df['BMI'].corr(df['Charges'])
print(correlation)
#correlation between bmi and charges
import statsmodels.api as sm
X = sm.add_constant(df['BMI'])
model = sm.OLS(df['Charges'], X).fit()
coeff_bmi = model.params['BMI']
# Perform regression analysis to model the relationship
print(f"Correlation between BMI and charges: {correlation:.2f}")
print(f"Regression coefficient for BMI: {coeff_bmi:.2f}")
# Interpret the results
import statsmodels.api as sm

X = df[['Age', 'sex_male', 'Children']]
X = sm.add_constant(X)
model = sm.OLS(df['Charges'], X).fit()
# Explore the impact of age, sex, and number of children on charges using regression analysis
print(model.summary())
#model results
average_charges_by_region = df.groupby('Region')['Charges'].mean()
#avg charge by region
from scipy.stats import f_oneway
f_statistic, p_value = f_oneway(
    df[df['Region'] == 'southwest']['Charges'],
    df[df['Region'] == 'southeast']['Charges'],
    df[df['Region'] == 'northwest']['Charges'],
    df[df['Region'] == 'northeast']['Charges']
)
# Perform statistical tests
if p_value < 0.05:
    print("There are significant regional variations in charges.")
else:
    print("There are no significant regional variations in charges.")
# Interpret the results or regional evaluations


