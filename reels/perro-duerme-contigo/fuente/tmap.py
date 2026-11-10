"""Map a time in the original voiceover to the compacted voiceover timeline."""
import json, os
_M = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'timemap.json')))

def tmap(t):
    acc = 0.0
    for i, (a, b) in enumerate(_M['keep']):
        xf = _M['fade'] if i else 0.0
        if t < a:              # inside a removed gap -> the cut point
            return (acc) / _M['tempo']
        if t <= b:
            return (acc + (t - a)) / _M['tempo']
        acc += (b - a) - (_M['fade'] if i + 1 < len(_M['keep']) else 0)
    return acc / _M['tempo'] + (t - _M['keep'][-1][1]) / _M['tempo']
