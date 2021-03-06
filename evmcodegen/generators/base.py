#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author : <github.com/tintinweb>


class _BaseCodeGen(object):

    TYPE_OPCODE_ONLY = 1  # generator generates opcodes only, no operands
    TYPE_OPCODE_WITH_OPERAND = 2  # generator generates instructions with operands

    def __init__(self):
        self.type = None  # undefined

    def generate(self, length=None):
        raise NotImplementedError("--not implemented--")

    def __iter__(self):
        return self

    def __next__(self):
        return self.generate()
