#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import scipy.io as sio
import pandas as pd
import os


def mat2df(mat_file, var=None, filepath=None):
    var_in = var
    if isinstance(var, str):
        var = [var]
    elif var is None:
        if isinstance(mat_file, dict):
            var = mat_file.keys()

    v_names = []
    # mat_file is a file path and var_list is a list of strings corresponding to structure field names
    if isinstance(mat_file, str):
        if os.path.isfile(mat_file):
            return mat2df(sio.loadmat(mat_file, simplify_cells=True), var, filepath=mat_file)
        elif os.path.isdir(mat_file):
            df_list = []
            for file in os.listdir(mat_file):
                df_list.append(mat2df(file, var))
            return pd.concat(df_list, axis=1).squeeze()
        else:
            print(mat_file + "is not a valid file path")
            return
    elif isinstance(mat_file, dict):
        mat = mat_file
        if any("__" in i for i in list(mat)) or any("readme" in i for i in list(mat)):
            for i in list(mat):
                if "__" not in i and "readme" not in i:
                    return mat2df(mat[i], var_in, filepath)
            raise ValueError("no variable stored in {file}".format(file=filepath))
        elif any(i in mat.keys() for i in var) or any("." in i for i in var):
            df_list = []
            for i in var:
                if "." in i:
                    (left, right) = i.split(".", 1)
                    if left in mat.keys():
                        df_list.append(mat2df(mat[left], right, filepath))
                elif i in mat.keys():
                    for v_name in list(set(var).intersection(mat.keys())):
                        v_names.append(v_name)
                    try:
                        df_list.append(pd.DataFrame(mat).filter(v_names).reset_index(drop=True))  # end
                    except ValueError as e:
                        print("warning:", e)
                        for cols in [mat[v_name] for v_name in v_names]:
                            if isinstance(cols,
                                          dict):  # if all values of dict are scalar, then an index must be provided
                                if all(np.isscalar(i) for i in cols.values()):
                                    df_list.append(pd.DataFrame(cols, index=[0]))
                                else:
                                    df_list.append(pd.DataFrame(cols).reset_index(drop=True))
                            else:
                                df_list.append(pd.DataFrame(cols).reset_index(drop=True))
            return pd.concat(df_list, axis=1).squeeze()
        else:
            raise ValueError("None of the vars {vars} were found in {file}".format(vars=var, file=filepath))
    elif isinstance(mat_file, list):
        if isinstance(mat_file[0], str):
            if os.path.isfile(mat_file[0]):
                return pd.concat([mat2df(mat, var_in) for mat in mat_file], axis=1).squeeze()
        else:
            mat = pd.DataFrame(mat_file)
            if var is None:
                return mat.reset_index(drop=True).squeeze()
            else:
                return mat.filter(list(set(var).intersection(mat.columns.tolist()))).reset_index(drop=True).squeeze()
    elif isinstance(mat_file, np.ndarray):
        return pd.DataFrame(mat_file).squeeze()
