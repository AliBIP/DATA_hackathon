import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder


data = {
    'Anomaly Scores': [28.67, 51.5, 87.42, 15.79, 0.52, 5.76, 31.55, 54.05, 56.34, 16.51,
                       24.91, 86.07, 74.2, 62.14, 72.65, 91.56, 43.83, 40.46, 44.75, 13.19,
                       89.99, 86.91, 72.25, 96.27, 67.43, 89.86, 87.23, 44.4, 45.42, 25.7,
                       69.2, 77.06],
    'Attack Type': ['Malware', 'Malware', 'DDoS', 'Malware', 'DDoS', 'Malware', 'DDoS', 'Intrusion', 'Intrusion', 'Malware',
                    'Malware', 'Malware', 'Intrusion', 'Malware', 'Malware', 'Intrusion', 'DDoS', 'DDoS', 'DDoS', 'DDoS',
                    'Malware', 'Malware', 'DDoS', 'Malware', 'DDoS', 'Intrusion', 'Malware', 'DDoS', 'Intrusion', 'Intrusion',
                    'DDoS', 'DDoS']
}



df = pd.DataFrame(data)


le = LabelEncoder()
df['Attack Type Encoded'] = le.fit_transform(df['Attack Type'])


plt.figure(figsize=(8, 6))
sns.heatmap(df[['Anomaly Scores', 'Attack Type Encoded']].corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation between Anomalies and Attack Types')
plt.show()