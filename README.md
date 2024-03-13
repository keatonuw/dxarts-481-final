# A Process Piece

"k-fold searchspace" is a video and audio composition created with the code in this repository. The final artifact can be viewed [here](https://youtu.be/3OJW6IgdPpM?si=1GxdfQFCm6pEHftG). 

### A Guide to the Code
- `code/markov/*.py`: Process a corpus, train, and make predictions with a Markov Model.
- `code/ConcatReSynth*.ipynb`: Python `signalflow` patches that perform concatenative resynthesis.
- `code/TextDataSynth.ipynb`: Python `signalflow` patch that granulates an input sound using text to parameterize the synthesis.
- `code/dataset_gen.ipynb`: Creates a dataset for MusicGen.
- `code/DXARTS_Final_MusicGen.ipynb`: Fine-tunes a MusicGen model on a dataset.
- `code/DXARTS_Final_Generation.ipynb`: Runs inference on a MusicGen model.
- `td/*`: TouchDesigner patch.
