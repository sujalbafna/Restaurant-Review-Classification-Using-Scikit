# Restaurant Review Classification Using Scikit 🍴📊

This project uses machine learning techniques to classify restaurant reviews as either positive or negative. It employs Scikit-learn for model training, testing, and evaluation. 

## Prerequisites 📋

Before using this repository, ensure you have the following:

- Python 3.x 🐍
- Scikit-learn 📚
- Pandas 🍑
- Numpy ➗
- Matplotlib 📈

## Installation ⚙️

1. Clone this repository:

   ```bash
   git clone https://github.com/sujalbafna/Restaurant-Review-Classification-Using-Scikit.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Restaurant-Review-Classification-Using-Scikit
   ```

3. Install the necessary dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   Or manually install the dependencies:

   ```bash
   pip install scikit-learn pandas numpy matplotlib
   ```

## Usage 🚀

### Step 1: Prepare the Data 📂

- The dataset is located in the `data/` folder. You can modify the dataset or replace it with your own if necessary.

### Step 2: Train the Model 🧑‍🏫

1. Open the `train_model.py` file.
2. The script will load the dataset, preprocess the reviews, and train a classifier.
3. You can choose the classifier you want to use (e.g., Naive Bayes, SVM, etc.) in the script.

To run the model training:

```bash
python train_model.py
```

This will train the classifier and save the trained model to a file.

### Step 3: Test the Model ✅

1. Open the `test_model.py` file to test the classifier with new restaurant reviews.
2. Replace `new_reviews` with your own set of restaurant reviews for prediction.

To test the model:

```bash
python test_model.py
```

This will print out whether the review is positive or negative.

### Step 4: Evaluate the Model 📊

The model’s performance is evaluated using various metrics such as accuracy, precision, recall, and F1-score, which are printed after training.

## Example Usage 💡

```python
# Example of classifying a review
review = "The food was amazing and the service was excellent!"
prediction = classifier.predict([review])
print(prediction)  # Output: Positive
```

## Folder Structure 📂

- `data/` – Contains the dataset for training and testing.
- `train_model.py` – Script for training the model.
- `test_model.py` – Script for testing the model.
- `requirements.txt` – List of required libraries.

## License 📝

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments 🙏

- Scikit-learn documentation for the machine learning models and tools.
- [Other resources you used].
```
