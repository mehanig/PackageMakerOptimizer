# PackageMakerOptimizer
Allow to link content inside PackageMaker project without duplication to shrink product space

### Purpose

We want to create native installer for our products (scripts for After Effects)
It's possible that user have multiple versions of AE installed, and to give an option for selecting specific version we need to use PackageMaker content Choices.

Each choice have folder associated with it.
In our products folder is always the same, what differs is location to move that folder.
The way PackageMaker works it create unique pkg for every choice content, event if it's same content from other Choices
After build, final installer contain multiple equal pkgs.

To solve this problem, we generate new version of project, where all the content linked to first available package.
After if, generated content might look buggy, but that's OK.

### How to use

1. Move `pmoptimizer.py` next to `YourProject`.pmdoc
2. Find content name (can be found using `Show Package Content` on `YourProject`.pmdoc and looking at files like `01content-contents.xml` (here content=content), if there will be files like `01data-contents.xml` then content=data)
3. run with python3 `python3 pmoptimizer.py -p YourProject -c content`

### Result
Installer size shrinked by N times (N = amount of choices in installer) if content is same.

Example of optimized project:
![optpm](https://cloud.githubusercontent.com/assets/5033274/24830315/62d240bc-1c8c-11e7-821a-2725cd1bceed.gif)
