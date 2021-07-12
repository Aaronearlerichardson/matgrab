# matgrab
Search and extract field names or variables from MATLAB .mat files and return a pandas Dataframe

# installation

## PYPI
```
pip install matgrab
```

# usage

## python
```
import matgrab
df = matgrab.mat2df("PATH","VARS")
```
PATH may be a file path, directory path, or list of either
VARS may be a string or list of strings that correspond to field names of desired matlab variables

if your desired data is nested within another named data structure or array, that structure name must proceed the desired variable separated by a "."
```
EEG.mat
├── dataset_description {string}
└── sub-D0048 {struct}
    ├── anat {struct}
    │   ├── T1w {string}
    │   └── CT {float}
    └── ieeg {array}
        ├── channels {column}
        └── values {column}
```
To retrieve the values from the above mat file, the command would be:
```
matgrab.mat2df("EEG.mat",["sub-D0048.anat.T1w","sub-D0048.anat.CT","sub-D0048.ieeg.channels","sub-D0048.ieeg.values"])
```

