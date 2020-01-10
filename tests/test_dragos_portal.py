#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for `dragos_portal` module."""

import pytest

from dragos_portal import dragos_portal


@pytest.fixture
def response():
    return "foo bar"


def test_dragos_portal_initialization():
    assert 1 == 1
