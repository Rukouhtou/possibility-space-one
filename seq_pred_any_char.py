import torch
import numpy as np

sample = ' life is short deal with it.'

char_set = list(set(sample))
char_dict = {c:i for i, c in enumerate(char_set)}

sample_idx = [char_dict[c] for c in sample]
x_data = [sample_idx[:-1]]

# hyper parameters
input_size = len(char_dict)
hidden_size = len(char_dict)
learning_rate = 8e-3

x_one_hot = [np.eye(input_size)[x] for x in x_data]
y_data = [sample_idx[1:]]

X = torch.FloatTensor(x_one_hot)
Y = torch.LongTensor(y_data)

print(X)
print(X.size())

rnn = torch.nn.RNN(input_size, hidden_size, batch_first=True)

criterion = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(rnn.parameters(), learning_rate)

for i in range(1000):
    optimizer.zero_grad()
    outputs, status = rnn(X)
    loss = criterion(outputs.view(-1, input_size), Y.view(-1))
    loss.backward()
    optimizer.step()
    result = outputs.data.numpy().argmax(axis=2)
    result_str = ''.join([char_set[c] for c in np.squeeze(result)])
    print(f'i loss: {loss.item()}, \nprediction: \n{result}, \ntrue Y: \n{np.array(y_data)}, \npredicted str: {result_str}')