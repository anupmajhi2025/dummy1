import pandas as pd

data = pd.read_csv("titanic.csv")

#dataset overriew
# print(data.shape)
# print(data.info)
# print(data.describe)

new_order = ["Name", "Age", "Sex", "Survived", "Fare"]
redorder = data[data['Age'] > 18]
b = redorder[new_order]
print(redorder[new_order])


print(redorder.isnull().sum())

a = redorder["Age"].apply(lambda age : "young" if age < 30 else "senior")
print(a.head(10))
c = b.drop(columns="Fare")
print(b.tail())
print(c.tail())