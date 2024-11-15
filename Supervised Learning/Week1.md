# Week 1
## Basics
- **Supervised Learning**:
    - It is machine learning techinique where a supervisor teaches machine by giving examples.
    - It learns from input(X) to output(Y) mappings.
    $$X \implies Y$$
- **Regression Model**: 
    - Any machine learning model that predicts number as output is called a regression model.
    - Infinite no of possible outputs.
- **Classification model**: 
    - Any ML model that predicts category as output is called a Classification model.
    - Finite no of possible outputs 
## Terminologies
<img src="Images1/Screenshot 2024-08-13 140052.png" width="" height=""> 

- The training set has two arrays X which is known as input variable or **feature** and Y which is known as output variable or **target**.
- $(x^{(i)},y^{(i)})$ reprsents the i th training example from training set.
<img src="Images1/Screenshot 2024-08-13 142841.png" width="" height="">

- $f$ reffers to the model , $\hat y$ reffers to the value estimated by the model by taking the input $x$. $y$ refers to the target value or right answer.
$$f(x)=\hat y$$
- We represent univariant/single featured linear regression model as 
$$f_{w,b}(x)=wx+b=\hat y$$
## Cost Function/Squared Error Cost function
- We use this function to check how close is the estimated value $\hat y$ to target value $y$.
- The cost function is:
$$J(w,b)=\frac{1}{2m}\sum_{i=1}^{m} (\hat y^{(i)}-y^{(i)})^2$$
$$\implies J(w,b)=\frac{1}{2m}\sum_{i=1}^{m} (f (x^{(i)})-y^{(i)})^2 $$
- Squared error cost function is the most commonly used cost function.

**Univariant Linear Regression model details**:
<img src="Images1/Screenshot 2024-08-14 155732.png" width="" height="">

- The goal of machine learning algorithms is to get a minimised cost function.

**Soup bowl shaped model of cost function**:

<img src="Images1/Screenshot 2024-08-14 160831.png" width="" height="">

- The global minima of the cost fuction is the optimal solution.

**Gradient Descent**
---

<img src="Images1/Screenshot 2024-10-09 102714.png" width="" height="">

<img src="Images1/Screenshot 2024-10-09 105228.png" width="" height="">

<img src="Images1/Screenshot 2024-10-09 105634.png" width="" height="">

<img src="Images1/Screenshot 2024-10-09 105845.png" width="" height="">

<img src="Images1/Screenshot 2024-10-09 110016.png" width="" height="">

<img src="Images1/Screenshot 2024-10-09 110324.png" width="" height="">

<img src="Images1/Screenshot 2024-10-09 111655.png" width="" height="">

<img src="Images1/Screenshot 2024-10-09 112439.png" width="" height="">

- The gradient descent algorithm results in local minimum instead of global minimum.
- But in squared error cost function it results global minimum, since there is one minima.
- This is how the value move down step by step in gradient descent algorithm

<img src="Images1/Screenshot 2024-10-09 175008.png" width="" height="">

- Batch refers to set of all training examples
- Hence in batch gradient descent at each step of gradient descent the whole training example changes.

<img src="Images1/Screenshot 2024-10-09 174823.png" width="" height="">


















