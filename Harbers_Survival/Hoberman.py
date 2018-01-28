# Load libraries
from tkinter import *
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC


def initialize():
    # *** Button Label *** #
    label1 = Label(frame, text='Haberman Survival',bg='#ff99ff', borderwidth=2, relief="solid")
    label1.config(font=('Times New Roman', 24))
    label1.place(x=200, y=50)

    # *** Button 1 *** #
    button1 = Button(frame, text='Predict',width=5, command=prediction,bg='#0066ff', borderwidth=2, relief="solid")
    button1.config(font=('Times New Roman', 16))
    button1.place(x=400, y=400)

    # *** Button 2 *** #
    button2 = Button(frame, text='Plot', width=5, command=plotData,bg='#99c2ff', borderwidth=2, relief="solid")
    button2.config(font=('Times New Roman', 16))
    button2.place(x=200, y=400)

    # *** Button 3 *** #
    button3 = Button(frame, text='Solve', width=5, command=solved_line,bg='#80b3ff', borderwidth=2, relief="solid")
    button3.config(font=('Times New Roman', 16))
    button3.place(x=300, y=400)



def solved_line():
    # Create linear regression object
    Dcc.fit(X_train, Y_train)
    plt.show();

def plotData():
    dataset.plot();
    plt.show();

def prediction():
    a = str(input1.get("1.0", "end-1c"))
    b = str(input11.get("1.0", "end-1c"))
    c = str(input12.get("1.0", "end-1c"))

    X_validation = [[a, b, c]]
    predictions = Dcc.predict(X_validation)
    if predictions ==1 :
        show_output='1. the patient survived 5 years or longer '
    if predictions == 2:
        show_output = '2. the patient died within 5 year'
    lbl = Label(frame, text=show_output, fg='red')
    lbl.config(font=('Times New Roman', 15))
    lbl.place(x=100, y=550)



if __name__ == '__main__':
    # Declare Frame #
    root = Tk()
    frame = Frame(root, width=700, height=650,bg='#b3ffd9')
    root.title("Haberman Survival");
    frame.pack()

    # Text Field #
    Input = Label(frame, text='1. Age of patient at time of operation ')
    Input.config(font=('Times New Roman', 16))
    Input.place(x=100, y=100)

    input1 = Text(frame, height=1, width=45, fg='blue')
    input1.config(font=('Times New Roman', 14))
    input1.place(x=100, y=140)

    Input = Label(frame, text='2. Patient year of operation')
    Input.config(font=('Times New Roman', 16))
    Input.place(x=100, y=200)

    input11 = Text(frame, height=1, width=40, fg='blue')
    input11.config(font=('Times New Roman', 14))
    input11.place(x=100, y=240)

    Input = Label(frame, text='3. Number of positive axillary nodes detected')
    Input.config(font=('Times New Roman', 16))
    Input.place(x=100, y=300)

    input12 = Text(frame, height=1, width=45, fg='blue')
    input12.config(font=('Times New Roman', 14))
    input12.place(x=100, y=340)

    Input = Label(frame, text='Prediction',fg='red', borderwidth=2, relief="groove")
    Input.config(font=('Times New Roman', 14))
    Input.place(x=100, y=480)

    # Load dataset
    url = 'F:\\MachineLearningProject\\datafordeath\\data.csv'
    names = ['Age', 'year','axillary','Survival']
    dataset = pandas.read_csv(url, names=names)

    # To Show Data
    #print(dataset.head(20))


    # Split-out validation dataset
    array = dataset.values
    X = (array[:,:3]) #For input
    Y = (array[:,3])  #For output
    validation_size = 0.20 #for testing
    seed = 8
    X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)


    # Make predictions on validation dataset
    Dcc = SVC()

    #For Checking Accuracy
    Dcc.fit(X_train, Y_train)
    predictions = Dcc.predict(X_validation)
    print(accuracy_score(Y_validation, predictions))

    initialize()
root.mainloop()
