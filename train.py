import numpy as np # libreria per il calcolo scientifico in Python.
import random
import json

#importo la libreria PyTorch, che è una libreria per il deep learning, e le sue sottolibrerie nn e DataLoader per la creazione e il caricamento dei dati.
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

from nltk_utils import bag_of_words, tokenize, stem
from model import NeuralNet

with open('intents.json', 'r') as f:
    intents = json.load(f)

all_words = []
tags = []
xy = [] #lista che conterrá i patterns col testo

"""
Questo ciclo annidato estrae i tag e i modelli di frasi dall'oggetto intents e li utilizza per popolare le liste tags, all_words e xy. 
Il primo ciclo scorre ogni intenzione nella lista intents['intents'] e estrae il tag associato a ogni intenzione. 
Il tag viene quindi aggiunto alla lista tags. Il secondo ciclo all'interno scorre ogni modello di frase per ogni intenzione e utilizza la funzione
 tokenize per suddividere la frase in parole
"""
# loop through each sentence in our intents patterns
for intent in intents['intents']:
    tag = intent['tag'] #recupera tutti i tag
    # add to tag list
    tags.append(tag)
    for pattern in intent['patterns']: #loop su tutti i patterns e li tokenizziamo
        # tokenize each word in the sentence
        w = tokenize(pattern)
        # add to our words list
        all_words.extend(w) #uso extend poiché w é un array
        # add to xy pair
        xy.append((w, tag)) #ho una coppia pattern - tag

# stem and lower each word
ignore_words = ['?', '.', '!',',']
all_words = [stem(w) for w in all_words if w not in ignore_words] #stem ogni parola ignorando la punteggiatura
# remove duplicates and sort
all_words = sorted(set(all_words))


print(len(xy), "patterns")
print(len(tags), "tags:", tags)
print(len(all_words), "unique stemmed words:", all_words)

# create training data
X_train = []  #contiene la bag of words per ogni frase del modello
y_train = []  #contiene l'indice del tag di intenzione
for (pattern_sentence, tag) in xy:
    # X: bag of words for each pattern_sentence
    bag = bag_of_words(pattern_sentence, all_words)
    X_train.append(bag)
    # y: PyTorch CrossEntropyLoss needs only class labels, not one-hot
    label = tags.index(tag)
    y_train.append(label)

#conversione in numpy array
X_train = np.array(X_train)
y_train = np.array(y_train)

# Hyper-parameters 
num_epochs = 1000 #quando il training set é sottoposto al modello si ha una epoch. Il training set potrebbe essere troppo grande per essere elaborato tutti in una volta quindi lo dividiamo in sottogruppi chiamati batch. Il numero di esempi contenuti in ogni batch é detto batch size. se ho 2k esempi posos dividere il set in batch con 500 esempi ciascuni e quindi 1 epoch ha 4 interazioni. Il numero di epoch ed il batch size influiscono sulla velocità di addestramento di un modello, ma anche sul suo modo di perfezionarsi
batch_size = 8
learning_rate = 0.001
input_size = len(X_train[0])
hidden_size = 8  #La dimensione nascosta è il numero di caratteristiche dello stato nascosto per RNN. Quindi, se aumenti la dimensione nascosta, calcoli la funzionalità più grande come output dello stato nascosto.
output_size = len(tags)
print(input_size, output_size)

class ChatDataset(Dataset):

    def __init__(self):
        self.n_samples = len(X_train)
        self.x_data = X_train
        self.y_data = y_train

    # support indexing such that dataset[i] can be used to get i-th sample
    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]

    # we can call len(dataset) to return the size
    def __len__(self):
        return self.n_samples

dataset = ChatDataset()
train_loader = DataLoader(dataset=dataset,batch_size=batch_size, shuffle=True,  num_workers=0)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

model = NeuralNet(input_size, hidden_size, output_size).to(device)

# Loss and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

# Train the model
"""
Addestrare il modello sui dati di addestramento utilizzando un ciclo di epoche. 
In ogni epoca, il modello viene eseguito su ogni batch di parole e etichette e la perdita viene calcolata utilizzando la funzione di perdita.
 La perdita viene utilizzata per calcolare il grado di ottimizzazione utilizzando l'ottimizzatore definito in precedenza.
"""
for epoch in range(num_epochs):
    for (words, labels) in train_loader:
        words = words.to(device)
        labels = labels.to(dtype=torch.long).to(device)
        
        # Forward pass
        outputs = model(words)
        # if y would be one-hot, we must apply
        # labels = torch.max(labels, 1)[1]
        loss = criterion(outputs, labels)
        
        # Backward and optimize
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
    if (epoch+1) % 100 == 0:
        print (f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')


print(f'final loss: {loss.item():.4f}')
"""
Salva il modello addestrato, il suo stato, la dimensione di input, hidden size, output size,
tutte le parole e i tag in un file chiamato training.pth utilizzando la funzione torch.save().
"""
data = {
"model_state": model.state_dict(),
"input_size": input_size,
"hidden_size": hidden_size,
"output_size": output_size,
"all_words": all_words,
"tags": tags
}

FILE = "training.pth"
torch.save(data, FILE)

print(f'training completato. File saved to {FILE}')
