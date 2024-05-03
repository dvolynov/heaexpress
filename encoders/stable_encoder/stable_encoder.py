from chemformula import ChemFormula
from scipy.spatial import Delaunay
from collections import defaultdict
import pandas as pd
import random

from .modules import Atom



class StableEncoder:

    all_elements = ['Ag', 'Al', 'As', 'Au', 'Bi', 'Cd', 'Co', 'Cr', 'Cu', 'Fe', 'Ga', 'Ge', 'Hf', 'Hg', 'In', 'Ir', 'Mg', 'Mn', 'Mo', 'Nb', 'Ni', 'Os', 'Pb', 'Pd', 'Pt', 'Re', 'Rh', 'Ru', 'Sb', 'Sc', 'Si', 'Sn', 'Ta', 'Te', 'Ti', 'V', 'W', 'Y', 'Zn', 'Zr']

    def __init__(self, density: int) -> None:
        self.density = density


    def to_matrix(self, composition: str) -> pd.DataFrame:
        quantity, quality = self._get_composition(composition)

        atoms = self._distribute(quantity, quality, start=0, end=self.density, step=1)
        transitions = self._triangulate(atoms)

        df = pd.DataFrame(0, index=self.all_elements, columns=self.all_elements)

        for elem1, transition in transitions.items():
            for elem2, count in transition.items():
                df.loc[elem1, elem2] = count

        df = df.div(df.sum(axis=1), axis=0)
        df = df.fillna(0)

        return df

    def _get_composition(self, composition: str) -> (list, list):
        composition = ChemFormula(composition.strip()).element

        quantity = list(composition.keys())
        quality = list(composition.values())

        return quantity, quality


    def _distribute(self, quantity: list[str], quality: list[int], start: int, end: int, step: int) -> list[Atom]:
        atoms = []
        id = 1

        for z in range(start, end, step):
            for y in range(start, end, step):
                for x in range(start, end, step):
                    _type = random.choices(quantity, weights=quality)[0]
                    atom = Atom(_type, coords=(x, y, z))
                    atoms.append(atom)
                    id += 1

        return atoms


    def _triangulate(self, atoms):
        points = []
        atom_types = {}

        for idx, atom in enumerate(atoms):
            coords = atom.coords()
            points.append(coords)
            atom_types[idx] = atom.type

        triangulation = Delaunay(points)
        transitions = defaultdict(lambda: defaultdict(int))

        for simplex in triangulation.simplices:
            for i in range(3):
                atom_idx_1 = simplex[i]
                atom_idx_2 = simplex[(i + 1) % 3]
                atom_type_1 = atom_types[atom_idx_1]
                atom_type_2 = atom_types[atom_idx_2]
                transitions[atom_type_1][atom_type_2] += 1

        return transitions
