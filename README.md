# 2026

## Preliminaries and environments

For access to the data files we need to be in the `epp` group.
Type the following to see if `epp` appears in the list. If not we need to contact the system admins (via a bugzilla) to change this.

```bash
groups
```

The event data from the LHCb experiments is in ROOT tree formats. This is a highly optimised binary form of colum data
(rows are "events" and columns are variables, e.g. the mass of a particle).
In this project we have a simple `run` script to give the correct environment.

The rule is that every command that you do should be prefixed by `./run`. E.g.

```bash
./run echo hello world
```

## Example data analysis with ROOT

Try this and see what it does
```bash
./run ./scripts/examples/example.py
```

Then look at the script

## Uproot analysis

[Uproot](https://uproot.readthedocs.io/en/latest/) is a very nice standalone project that allows you to extract ROOT TTree data directly
into, e.g., numpy arrays or pandas dataframes.



