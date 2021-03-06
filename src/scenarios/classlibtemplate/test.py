import os
from shared.runner import TestTraits, Runner
from shared import const

EXENAME = 'classlibtemplate'


def main():
    traits = TestTraits(exename=EXENAME,
                        guiapp='false', 
                        timeout= f'{const.MINUTE*10}'
                        )
    runner = Runner(traits)
    runner.run()


if __name__ == "__main__":
    main()
