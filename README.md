# Bayesian Network

Public library for a Bayesian Network in python. This library uses only `re` as dependency. It works as a standalone library and can be used in any python project.

It is defined as a class `BayesNetwork` which has the following methods:

* `add_node` : Adds a node to the network
* `edit_node` : Edits a node in the network
* `compact` : Shows a compact representation of the network
* `defined` : Checks if every node is defined
* `query` : Queries the network for a given node

## Installation
```bash
pip install memebayes
```
## Usage
### Importing the library
```python
from memebayes import BayesNetwork
```
### Creating a network
```python
network = BayesNetwork(nodes:list)
```
- `nodes` is a list of strings, with the names of the nodes in the network.
### Adding a node
```python
network.add_node(node:str, parents:list, probabilities:dict)
```
- `node` is the name of the node to be added.
- `parents` is a list of strings, with the names of the parents of the node.
- `probabilities` is a dictionary with the probabilities of the node. The keys are the possible values of the node, and the values are the probabilities of the node given the parents. If the node has no parents, the keys are the possible values of the node, and the values are the probabilities of the node.
### Editing a node
```python
network.edit_node(node:str, parents:list, probabilities:dict)
```
### Compacting the network
```python
network.compact() # Returns a string Ej.P(C)P(B|C)P(A|B,C)
```
### Checking if the network is defined
```python
network.defined() # Returns a boolean
```
### Querying the network
```python
network.query(query:str) # Returns the probabilities of the node given the evidence
```
- `query` is a string with the query to be made. The format is `node|evidence`, where `node` is the name of the node to be queried, and `evidence` is a list of strings with the evidence of the query. The format of the evidence is `node=value`, where `node` is the name of the node, and `value` is the value of the node. If there is no evidence, the format is `node`.

## Examples

```python
from memebayes import BayesNetwork

net = BayesNetwork(["B","E","A","J","M"]) # Create a network with the nodes B, E, A, J and M

net.edit_node("B",pt={"B":0.001}) # Edit the node B with the probability of being true
net.edit_node("E",pt={"E":0.002}) # Edit the node E with the probability of being true

net.edit_node("A",parents=["B","E"], pt = {"A|BE":0.95,"A|B-E":0.94,"A|-BE":0.29,"A|-B-E":0.001}) # Edit the node A with all the possible probabilities of being true given the parents B and E

net.edit_node("J", parents = ["A"], pt = {"J|A": 0.9, "J|-A": 0.5}) # Edit the node J with the probability of being true given that A is true
net.edit_node("M", parents=["A"], pt={"M|A": 0.7, "M|-A": 0.01}) # Edit the node M with the probability of being true given that A is true

print(net.compact()) # Print the compact representation of the network (Ej.P(B)P(E)P(A|B,E)P(J|A)P(M|A))
print(net.defined()) # Check if the network is defined (True)
print(net.query("B")) # Query the network for the node B (0.001)
 
print(net.query("B|JM")) # Query the network for the node B given that J and M are true (0.0007)
```
### Graph image
![imagen](https://user-images.githubusercontent.com/64183934/220893461-12586da5-ab6d-4c4c-a483-0020eb5ecbd4.png)



## References

This library is based on the following references:

* https://en.wikipedia.org/wiki/Bayesian_network
* http://courses.csail.mit.edu/6.034s/handouts/spring12/bayesnets-pseudocode.pdf
* https://www.cs.cmu.edu/~awm/15781/slides/bayesinf05a.pdf
