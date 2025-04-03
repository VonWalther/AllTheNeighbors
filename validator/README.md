# AllTheNeighbors Validator

This tool validates a submission and grades it compared to expected output.

## Usage

To use this tool, run `python3 validator.py` from `<project_root>/validator`.

```
python3 validator.py '<submission_filename>.json' '<answer_filename>.json' <stretch> <points>
```

### CL arguments

All arguments are positional, so you cannot specify `points` without `stretch`.

* `<submission_filename>.json` (**REQUIRED**) - name of / path to student submission file to compare
* `<answer_filename>.json` (**REQUIRED**) - name of / path to answer key file to compare
* `stretch` - `True` if evaluating stretch goal, default `False`
* `points` - Sets maximum points, default 80

### Output

The program outputs a whole number of points out of the total available points (default 80) to award based on the comparison.