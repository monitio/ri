<div align="left">

# ri
Download and import Python modules without Pip.

<hr/>

## How to use:

> [!WARNING]
> Some libraries may have a different final import. Check their usage first.

1. Download [ri.py](/dist/RAW/ri.py) and save it to your project directory.
2. In your `main.py` file, `import ri` and follow the steps below based on where the main module is:
    - Github: For github you can have `gh@` and then whatever your `raw.githubusercontent.com/` link is after. So an example would be: `ri.im("gh@monitio/rusl/refs/heads/main/dist/RAW/Python/rusl.py")` ([rusl](https://github.com/monitio/rusl) uses this instead of pip!)
    - Any where else: You will need to have the long URL like: `https://raw.githubusercontent.com/monitio/rusl/refs/heads/main/dist/RAW/Python/rusl.py`
3. Import the module like you would with any other normal python library: `import fileName` (remember to change the name as what the file is called so if it is `module.py` you would do `import module`)
4. Use the library as normal!

</div>