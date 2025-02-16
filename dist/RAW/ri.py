# ri.py
import sys
import urllib.request
import importlib.util

def im(url, name=None):
    """
    Imports a Python module from a remote URL (e.g., a raw GitHub link)
    or from a shorthand notation and registers it in sys.modules.

    Parameters:
        url (str): The URL of the Python source file, or a shorthand starting with 'gh@'
                   (e.g., "gh@username/repo/branch/module.py").
        name (str, optional): The name to register the module under.
                              If None, the name is automatically derived from the filename
                              (e.g., "module.py" becomes "module").

    Returns:
        module: The imported module.
    """
    # Convert shorthand URL if it starts with "gh@"
    if url.startswith("gh@"):
        url = url.replace("gh@", "https://raw.githubusercontent.com/", 1)
    
    try:
        # Open the URL using urllib.request from the standard library.
        with urllib.request.urlopen(url) as response:
            # Check that the HTTP response code is 200 (OK)
            if response.getcode() != 200:
                raise ImportError(f"Failed to fetch module from URL: {url} (HTTP status {response.getcode()})")
            # Read and decode the source code
            source = response.read().decode("utf-8")
    except Exception as e:
        raise ImportError(f"Failed to fetch module from URL: {url} ({e})")
    
    # If no name is provided, derive it from the file name in the URL
    if name is None:
        # Get the last segment of the URL (e.g., "module.py")
        filename = url.rstrip('/').split('/')[-1]
        # Remove the ".py" extension if present
        name = filename[:-3] if filename.endswith(".py") else filename
    
    # Create a module spec and module object without a loader
    spec = importlib.util.spec_from_loader(name, loader=None)
    module = importlib.util.module_from_spec(spec)
    
    # Execute the downloaded source code in the module's namespace
    exec(source, module.__dict__)
    
    # Register the module in sys.modules so it can be imported elsewhere
    sys.modules[name] = module
    return module
