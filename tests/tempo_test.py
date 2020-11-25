# Copyright 2020 The TEMPO Collaboration
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Tests for the time_evovling_mpo.tempo module.
"""

import pytest
import numpy as np

import time_evolving_mpo as tempo


def test_guess_tempo_parameters():
    system = tempo.System(0.5 * tempo.operators.sigma("x"))
    correlation_function = lambda t: (np.cos(t)+1j*np.sin(6.0*t)) * np.exp(-2.0*t)
    correlations = tempo.CustomCorrelations(correlation_function,
                                            max_correlation_time=10.0)
    bath = tempo.Bath(0.5 * tempo.operators.sigma("z"), correlations)
    with pytest.warns(UserWarning):
        param = tempo.guess_tempo_parameters(system=system,
                                             bath=bath,
                                             start_time=0.0,
                                             end_time=15.0)
