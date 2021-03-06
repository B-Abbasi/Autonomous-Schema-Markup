import torch
import torch.nn as nn

class clsLSTM(nn.Module):
    def __init__(self, input_size, embed_size, hidden_size, num_layers,num_classes):
        super(clsLSTM, self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers

        self.embedding = nn.Embedding(input_size, embed_size)
        self.rnn = nn.LSTM(embed_size, hidden_size, num_layers)
        # self.fc_out = nn.Linear(hidden_size, 1)
        self.fc_out = nn.Linear(hidden_size, num_classes)

    def forward(self, x):
        # Set initial hidden and cell states
        h0 = torch.zeros(self.num_layers, x.size(1), self.hidden_size).to(device)
        c0 = torch.zeros(self.num_layers, x.size(1), self.hidden_size).to(device)

        embedded = self.embedding(x)
        outputs, _ = self.rnn(embedded, (h0, c0))
        prediction = self.fc_out(outputs[-1, :, :])

        return prediction