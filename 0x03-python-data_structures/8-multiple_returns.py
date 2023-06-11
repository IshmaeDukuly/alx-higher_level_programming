#!/usr/bin/python3
def multiple_returns(sentence):
    s_length = len(sentence)
    char = sentence[0] if s_length > 0 else None
    return (s_length, char)
