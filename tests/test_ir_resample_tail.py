import pytest
import media.ir_resample_tail as mod

CASES = [
    ("ir_resample", (48000, 44100)),
    ("tail_length", (1, 2)),
    ("normalize_once", (1, 2)),
    ("comb_check", (1, 2)),
    ("ir_window", (1, 2)),
    ("gain_compensate", (0.5, 0.2)),
    ("sample_align", (1, 2)),
    ("channel_map", (1, 2)),
    ("latency_offset", (1, 2)),
    ("tail_truncate", (1, 2)),
    ("double_normalize_guard", (1, 2)),
    ("precompute", (1, 2)),
    ("convolve_validate", (1, 2)),
    ("metallic_score", (1.0, 2.0)),
    ("bus_gain", (1, 2)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
