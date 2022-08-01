#!/usr/bin/python3

def lookup(obj):
    methods = []
    for dirs in dir(obj):
        methods.append(dirs)
    return (methods)
