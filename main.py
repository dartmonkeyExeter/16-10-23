import pandas as pd

df = pd.read_csv('WHR2023.csv')

df_subset = df[['Healthy life expectancy', 'Social support']]
print('there is a strong correlation between healthy life expectancy and '
      f'social support: \n{df_subset.corr()}')

df_subset = df[['Generosity', 'Perceptions of corruption']]
print(f'there is a weak correlation between generosity and '
      f'perceptions of corruption: \n{df_subset.corr()}')

df_subset = df[['Freedom to make life choices', 'Social support']]
print(f'there is a correlation between freedom to make life choices and '
      f'social support: \n{df_subset.corr()}')

df_subset = df[['Generosity', 'Logged GDP per capita']]
print(f'there is a weak negative correlation between generosity and '
      f'logged gdp per capita: \n{df_subset.corr()}')

df_subset = df[['Ladder score', 'Perceptions of corruption']]
print(f'there is a negative correlation between ladder score and '
      f'perceptions of corruption: \n{df_subset.corr()}')
# im so tired
