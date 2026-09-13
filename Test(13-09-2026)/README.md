
## What This Notebook Covers

1. **Neural Networks**
2. **Inference**
3. **Large Language Models (LLMs)**

## 1. 🧠 Neural Networks

### Question 1

A simple neuron is implemented using:

- Inputs
- Weights
- Bias
- Weighted sum
- Sigmoid activation function

The notebook uses NumPy to calculate the neuron's output.

The weighted sum is calculated using the dot product:

weighted sum = xi * wi + bias

After calculating the weighted sum, the **Sigmoid activation function** is applied:

Sigmoid(x) = 1 / (1 + e^(-x))

This gives an output between 0 and 1.

### Question 2 


- Creates a small input tensor.
- Defines a linear layer with 2 inputs and 1 output.
- Includes a bias.
- Calculates the output.
- Prints the weights and bias.

## 2. Inference

### Model Memory Calculation

The notebook considers a llm with billions of parameters stored using FP16 precision.

Since FP16 uses **2 bytes per parameter**, the basic calculation is:

Number of parameters × 2 bytes

During training, a model learns its parameters and updates them. During inference, the trained model uses those existing parameters to produce predictions.

### Text Classification

It tests sentences such as:

- `"I love this"`
- `"This is Terrible"`
- `"It's okay, I guess"`

This demonstrates how a pretrained model can be used directly for classification without building the model from scratch.

## 3. 🤖 Large Language Models (LLMs)


### How Does an LLM Predict the Next Token?

This explains the process using a diagram and breaks it into a few important stages.

#### 1. Tokenization

Text is first splitted into small parts called **tokens**.

These tokens are then represented numerically so that the model can process them.

#### 2. Embeddings

The tokens are converted into numerical representations called **embeddings**.

#### 3. Transformer Layer

The transformer architecture processes these representations and helps the model capture relationships and context within the input.

#### 4. Next-Token Prediction

The model calculates probabilities for possible next tokens and selects a likely token based on those probabilities.

This process is repeated token by token to generate a sequence of text.

## 4. GPT-2 Text Generation 

To make the LLM concept practical, the notebook uses the pretrained **GPT-2** model through Hugging Face.

The experiment:

1. Loads the GPT-2 tokenizer.
2. Loads the GPT-2 causal language model.
3. Uses the prompt:
The Future of AI is
4. Generates tokens.
5. Decodes the generated token IDs back into readable text.

This provides a simple demonstration of **causal language modeling**, where the model generates text by predicting tokens.

