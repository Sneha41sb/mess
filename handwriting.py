from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

digits=load_digits()
x,y=digits.data,digits.target

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
model=LogisticRegression(max_iter=10000)
model.fit(x_train,y_train)

accuracy=model.score(x_test,y_test)
model.fit(x_train,y_train)
fig,axes=plt.subplots(2,5,figsize=(10,5))
for i,ax in enumerate(axes.flat):
    ax.imshow(digits.images[i], cmap='gray')
    ax.set_title(f"Label: {digits.target[i]}")
    ax.axis('off')
plt.tight_layout()
plt.savefig("handwriting.png")