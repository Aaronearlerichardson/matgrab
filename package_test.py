#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.matgrab import mat2df
import os


def test1():
    data_dir = os.listdir("tests/data")
    vars = ["Subject", "Trial", "Rec", "Day", "FilenamePrefix", "Start",
            "Auditory", "Go", "StartCode", "AuditoryCode", "GoCode", "Noisy", "NoResponse",
            "ResponseStart", "ResponseEnd", "cue", "sound", "go", "cueTime", "block", "cueStart",
            "Trigger", "cueEnd", "audioStart", "audioAlignedTrigger", "delStart", "delEnd",
            "goStart", "goEnd", "respStart", "respEnd", "isiStart", "isiEnd", "tCaptureStart"]
    return mat2df(data_dir, vars)


def test2():
    data_dir = os.listdir("tests/data")
    vars = ["channels.name", "recording.sample_rate"]
    return mat2df(data_dir, vars)


def test3():
    return mat2df("tests/data/D52_experiment.mat")
