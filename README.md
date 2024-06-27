# Python backwards compatibility

## Description

This repository shows a sloppy way how you can create and provide backwards compatibility to a widely shared submodule in case if it is going through a refactoring process.

**LocalCode.py** file imitates a local repo file that uses a function from Python module named **OldCode** located in the attached submodule.

**OldCode** module was refactored into **RefactoredCode.py** file. Its public API has changed, thus breaking connection with **LocalCode.py**.

Typically, in this case a proper solution would be to correct the code in **LocalCode.py**. However, sometimes it is not possible to do so quickly if above-mentioned submodule is shared across handful of repositories, owning repositories have a strict approval process and/or it is used in non-stopping CI/CD processes.

We can re-create an old legacy API and map it to a new refactored API for smoothening the process of refactoring. In **\_\_init\_\_.py** we can define mappings from the old code to a new one.
