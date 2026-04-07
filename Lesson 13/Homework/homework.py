import pandas as pd
import numpy as np
from scipy.stats import zscore
from sklearn.preprocessing import MinMaxScaler

#Dataset yaradiriq
data = [
    [1, 20, 'M', 'Azerbaijan', 85, 8, 10, 25, '2024-01-10', '2024-05-01', 'Basic'],
    [2, 22, 'F', 'Turkey', 92, 9, 10, 30, '2024-02-15', '2024-05-03', 'Premium'],
    [3, 19, 'M', 'Azerbaijan', 105, 7, 10, 15, '2024-01-20', '2024-04-25', 'Basic'],   # course_score > 100
    [4, 25, 'F', 'Georgia', -5, 6, 10, 18, '2024-03-01', '2024-04-28', 'Standard'],    # course_score < 0
    [5, 21, 'M', 'Azerbaijan', 76, 11, 10, 22, '2024-01-05', '2024-05-02', 'Premium'],  # completed > total
    [6, 23, 'F', 'Turkey', 88, 8, 10, 27, '2024-02-01', '2024-05-01', 'Basic'],
    [7, np.nan, 'M', 'Azerbaijan', 67, 5, 10, 12, '2024-01-12', '2024-04-20', 'Standard'],
    [8, 24, 'F', np.nan, 95, 10, 10, 35, '2024-01-18', '2024-05-04', 'Premium'],
    [9, 20, 'M', 'Georgia', 55, 4, 10, 9, '2024-03-10', '2024-04-15', np.nan],
    [10, 26, 'F', 'Azerbaijan', 81, 7, 10, 20, '2024-02-20', '2024-04-29', 'Basic'],
    [11, 22, 'M', 'Turkey', 73, 6, 10, 19, '2024-01-25', '2024-04-30', 'Standard'],
    [12, 21, 'F', 'Azerbaijan', 64, 5, 10, 14, '2024-02-11', '2024-04-26', 'Basic'],
    [13, 27, 'M', 'Georgia', 90, 9, 10, 40, '2024-01-08', '2024-05-05', 'Premium'],
    [14, 20, 'F', 'Turkey', 58, 3, 10, 8, '2024-03-05', '2024-04-18', 'Basic'],
    [15, 23, 'M', 'Azerbaijan', 77, 8, 10, 24, '2024-02-14', '2024-05-01', 'Standard'],
    [16, 24, 'F', 'Georgia', 69, 6, 10, 16, '2024-01-30', '2024-04-27', 'Premium'],
    [17, 22, 'M', 'Turkey', 83, 7, 10, 21, '2024-02-08', '2024-05-02', 'Basic'],
    [18, 21, 'F', 'Azerbaijan', np.nan, 8, 10, 26, '2024-01-16', '2024-04-30', 'Premium'],
    [19, 28, 'M', 'Georgia', 91, np.nan, 10, 33, '2024-01-07', '2024-05-03', 'Standard'],
    [20, 20, 'F', 'Turkey', 62, 4, 10, 11, '2024-03-12', '2024-04-19', 'Basic'],
    [21, 25, 'M', 'Azerbaijan', 79, 8, 10, 500, '2024-01-03', '2024-05-05', 'Premium'],  # outlier login_count
    [22, 23, 'F', 'Georgia', 84, 7, 10, 23, '2024-02-17', '2024-05-01', 'Standard'],
    [23, 19, 'M', 'Turkey', 71, 6, 10, 17, '2024-01-21', '2024-04-24', 'Basic'],
    [24, 24, 'F', 'Azerbaijan', 66, 5, 10, 13, '2024-03-02', '2024-04-21', 'Premium'],
    [25, 22, 'M', 'Georgia', 87, 9, 10, 29, '2024-01-11', '2024-05-04', 'Standard'],
    [26, 21, 'F', 'Turkey', 93, 10, 10, 36, '2024-01-09', '2024-05-05', 'Premium'],
    [27, 20, 'M', 'Azerbaijan', 59, 4, 10, 10, '2024-02-25', '2024-04-17', 'Basic'],
    [28, 26, 'F', 'Georgia', 74, 6, 10, 18, '2024-02-05', '2024-04-28', 'Standard'],
    [29, 23, 'M', 'Turkey', 82, 7, 10, 22, '2024-01-28', '2024-05-02', np.nan],
    [30, 22, 'F', 'Azerbaijan', 999, 8, 10, 1000, '2024-01-01', '2024-05-06', 'Premium'] # extreme outlier
]

columns = [
    'student_id', 'age', 'gender', 'country', 'course_score',
    'assignments_completed', 'total_assignments', 'login_count',
    'enroll_date', 'last_login_date', 'subscription_type'
]

df = pd.DataFrame(data, columns=columns)

df.to_csv("students.csv", index=False)
print("students.csv yaradıldı.\n")


df = pd.read_csv("students.csv")

print("INFO:")
print(df.info())
print("\nDESCRIBE:")
print(df.describe(include='all'))
print("\nBOŞ DƏYƏRLƏR:")
print(df.isnull().sum())

invalid_rows = df[
    (df['course_score'] > 100) |
    (df['course_score'] < 0) |
    (df['assignments_completed'] > df['total_assignments'])
]

print("\nSilinəcək qeyri-real sətirlər:")
print(invalid_rows)

df = df[
    (df['course_score'] <= 100) &
    (df['course_score'] >= 0) &
    (df['assignments_completed'] <= df['total_assignments'])
]

numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
categorical_mode_cols = ['subscription_type', 'country']

for col in numeric_cols:
    df[col].fillna(df[col].median(), inplace=True)

for col in categorical_mode_cols:
    df[col].fillna(df[col].mode()[0], inplace=True)


z_login = zscore(df['login_count'])
z_score = zscore(df['course_score'])

df['z_login_count'] = z_login
df['z_course_score'] = z_score

df = df[(df['z_login_count'].abs() <= 3) & (df['z_course_score'].abs() <= 3)]

df.drop(columns=['z_login_count', 'z_course_score'], inplace=True)


df['enroll_date'] = pd.to_datetime(df['enroll_date'])
df['last_login_date'] = pd.to_datetime(df['last_login_date'])

df['days_since_enroll'] = (df['last_login_date'] - df['enroll_date']).dt.days


df['completion_rate'] = df['assignments_completed'] / df['total_assignments']
df['engagement_score'] = df['login_count'] * 0.4 + df['completion_rate'] * 0.6


scaler = MinMaxScaler()

numeric_cols_to_scale = [
    'age', 'course_score', 'assignments_completed', 'total_assignments',
    'login_count', 'days_since_enroll', 'completion_rate', 'engagement_score'
]

df[numeric_cols_to_scale] = scaler.fit_transform(df[numeric_cols_to_scale])


df.to_csv("clean_students.csv", index=False)
print("\nclean_students.csv faylı yaradıldı.")


grouped = df.groupby('subscription_type')[['engagement_score', 'course_score']].mean()

print("\nSubscription type üzrə orta engagement_score və course_score:")
print(grouped)