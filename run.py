from time import time
from typing import Dict, Tuple, Protocol, Any, List

from tqdm import trange

from genetic0012 import Genetic0012


class GetterHint(Protocol):
    def __call__(self, message: str, **kwargs): ...


class Field:
    @staticmethod
    def get_str(message: str, **kwargs) -> str:
        default_max_size = 100000 # is this a bad idea? maximum of 100 thousand chars!
        max_size = kwargs.get('max_size', default_max_size)
        min_size = kwargs.get('min_size', 1)  # by default at least one thing should be passed!
        inp = input(f"{message}:")
        while not min_size <= len(inp) <= max_size:
            print(f"Invalid value, only {min_size} to {max_size if max_size!=default_max_size else '~'} "
                  f"chars lengths are allowed.")
            inp = input(f"{message}:")
        return inp

    @staticmethod
    def get_int(message: str, **kwargs) -> int:
        max_ = kwargs.get('max')  # better way to set maximum than max implemented in str :)
        min_ = kwargs.get('min')
        inp = input(f"{message} (integer):")
        while not (inp.isdigit() and (min_ <= int(inp) if min_ else True) and (max_ >= int(inp) if max_ else True)):
            print(f"Invalid value or characters! only from "
                  f"{min_ if min_ else '~'} to {max_ if max_ else '~'} are allowed!")
            inp = input(f"{message} (integer):")
        return int(inp)

    @staticmethod
    def get_float(message: str, **kwargs) -> float:
        max_ = kwargs.get('max')
        min_ = kwargs.get('min')
        inp = input(f"{message} (float):")
        while not ((inp.isdigit() or (len(inp.split('.')) == 2 and all(val.isdigit() for val in inp.split('.'))))
                   and (min_ <= float(inp) if min_ else True) and (max_ >= float(inp) if max_ else True)):
            print(f"Invalid value or characters! only from "
                  f"{min_ if min_ else '~'} to {max_ if max_ else '~'} are allowed!")
            inp = input(f"{message} (float):")
        return float(inp)

    GETTERS: Dict[type, Tuple[GetterHint, str]] = {
        str: (get_str, 'max_size', 'min_size'),
        int: (get_int, 'max', 'min'),
        float: (get_float, 'max', 'min'),
    }

    def __init__(self, name, type_: type = str, **kwargs):
        assert type_ in self.GETTERS, "This type of data can't be obtained from user"
        assert all(kw in self.GETTERS[type_] for kw in kwargs), f'{type_} can only get {self.GETTERS[type_][1:]}'
        self.name = name
        self.type_ = type_
        self.kwargs = kwargs

    def get(self) -> Any:
        return self.GETTERS[self.type_][0](f"Enter {self.name}:", **self.kwargs)


parameters = {
    'out_put_count': Field("Output Count", int, min=1, max=100),
    'population_size': Field("Population Size", int, min=10, max=5000),
    'generation_count': Field("Generation Count", int, min=10, max=10000),
    'pc': Field("Possibility Of Crossover", float, min=0.001, max=1.0),
    'pm': Field("Possibility Of Mutate", float, min=0.001, max=1.0),
}


def get_parameters(params: Dict[str, Field]) -> Dict[str, Any]:
    result = {}
    for param_name, param_filed in params.items():
        result[param_name] = param_filed.get()
    return result


if __name__ == '__main__':
    total = Field("Total Runs", int, min=1, max=100).get()
    algorithm_params = get_parameters(parameters)
    results: List[Tuple[float, list]] = []
    big_tick = time()
    for run in trange(total):
        tick = time()
        gen = Genetic0012(**algorithm_params)
        res = gen.run()
        tock = time()
        results.append((tock-tick, res))
    big_tock = time()

    print(f"Algorithm Finished Within {round(big_tock-big_tick, 4)} seconds! Results:\n",
          "Time\t\tResult",
          "\n-- ".join(f"{round(t, 2)}, {l}" for t, l in results))
