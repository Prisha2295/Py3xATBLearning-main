#### 1. Basic OS Information

https://gist.github.com/PramodDutta/dddcaf61fa39b77c1eb0645bd0ecf269



```python
import os

# Get the name of the operating system
print(os.name)  # e.g., 'posix' for Unix/Linux, 'nt' for Windows

# Get current working directory
print(os.getcwd())

# Change current working directory
os.chdir('/path/to/new/directory')
```

#### 2. File and Directory Operations

```python
# List contents of a directory
print(os.listdir('/path/to/directory'))

# Create a new directory
os.mkdir('new_directory')

# Create a directory and all intermediate directories
os.makedirs('path/to/new/directory')

# Remove a file
os.remove('file.txt')

# Remove an empty directory
os.rmdir('empty_directory')

# Remove a directory and its contents
os.removedirs('path/to/directory')

# Rename a file or directory
os.rename('old_name.txt', 'new_name.txt')
```

#### 3. Path Operations

```python
# Join path components
path = os.path.join('folder', 'subfolder', 'file.txt')

# Get the base name of a path
print(os.path.basename('/path/to/file.txt'))  # Outputs: file.txt

# Get the directory name of a path
print(os.path.dirname('/path/to/file.txt'))  # Outputs: /path/to

# Check if a path exists
print(os.path.exists('/path/to/file.txt'))

# Check if a path is a file
print(os.path.isfile('/path/to/file.txt'))

# Check if a path is a directory
print(os.path.isdir('/path/to/directory'))
```

#### 4. File Attributes

```python
# Get file size in bytes
size = os.path.getsize('file.txt')

# Get file modification time
mtime = os.path.getmtime('file.txt')

# Get file access time
atime = os.path.getatime('file.txt')
```

#### 5. Environment Variables

```python
# Get the value of an environment variable
print(os.environ.get('PATH'))

# Set an environment variable
os.environ['MY_VAR'] = 'value'
```

#### 6. Process Management

```python
# Get the current process ID
print(os.getpid())

# Execute a command in a subshell
os.system('echo Hello, World!')
```

#### 7. Walking Directory Trees

```python
for root, dirs, files in os.walk('/path/to/directory'):
    print(f"Current directory: {root}")
    print(f"Subdirectories: {dirs}")
    print(f"Files: {files}")
```

#### 8. File Descriptors

```python
# Open a file and get its descriptor
fd = os.open('file.txt', os.O_RDWR)

# Write to the file using the descriptor
os.write(fd, b'Hello, World!')

# Close the file descriptor
os.close(fd)
```

These examples cover a wide range of functionalities provided by the OS module in Python. Remember to handle exceptions appropriately when working with file systems and to use these functions carefully, especially those that modify the file system.