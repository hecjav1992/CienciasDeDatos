import seaborn as sns

data=sns.load_dataset('tips')
print(data['total_bill'].quantile(0.10))

