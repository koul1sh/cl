import pandas as pd

def map_reduce_with_pandas(input_file):
    df = pd.read_csv(input_file)
    deceased_males = df[(df['survived'] == 0) & (df['sex'] == 'male')]
    average_age_deceased_males = deceased_males['age'].mean()
    deceased_females_by_class = df[(df['survived'] == 0) & (df['sex'] == 'female')]
    count_deceased_females_by_class = deceased_females_by_class['pclass'].value_counts()
    return average_age_deceased_males, count_deceased_females_by_class

input_file = 'titanic.csv'
average_age, female_class_count = map_reduce_with_pandas(input_file)

print(f"Average age of males who died: {average_age:.2f}")
print("Number of deceased females in each class:")
print(female_class_count)
