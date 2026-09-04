## Task 1: Soft Link & Hard Link

In Linux, a "link" is a way to create a shortcut or an alternative pointer to an existing file.

| Feature | Soft Link (Symbolic Link) | Hard Link |
| :--- | :--- | :--- |
| **What it is** | A shortcut pointing to a file path. | An exact duplicate entry pointing to the physical data (inode) on the disk. |
| **If original is deleted** | The link breaks (becomes a "dangling link"). | The link still works and retains the data. |
| **Cross-filesystem?** | Yes. Can link across different partitions. | No. Must be on the same partition/filesystem. |
| **Linking Directories** | Yes, can point to directories. | No, cannot link to directories. |
| **Inode Number** | Has its own unique inode number. | Shares the exact same inode number as the original file. |

### Practice Commands
```bash
# 1. Create a test file
touch myfile.txt

# 2. Create a Soft Link (-s flag)
ln -s myfile.txt my_softlink.txt

# 3. Create a Hard Link (No flags)
ln myfile.txt my_hardlink.txt

# 4. Verify the links (Notice the inode numbers with -i)
ls -li

# 5. Delete the links (Deleting links never deletes the original target)
rm my_softlink.txt my_hardlink.txt
```

## Task 2: adduser vs useradd

Both commands create new users, but they behave very differently:

* **`useradd`**: A low-level, native binary. Adds the user to the system database but does NOT create a home directory or prompt for a password by default.
* **`adduser`**: A high-level, interactive script (wrapper around `useradd`). Automatically creates the home directory, copies skeleton configuration files, and interactively sets up the password and user details.

**Best Practice on Ubuntu/Debian:** 
`adduser` is strictly preferred as it sets up the user environment safely and interactively.

### Practice Command
```bash
sudo adduser testuser
```

## Task 3: journalctl

`journalctl` is the command-line utility used to query and read logs collected by `systemd`. It centralizes logs for the kernel, boot processes, and all background services into one highly searchable format.

### Common Commands
```bash
# View all system logs (Press 'q' to quit)
journalctl

# View kernel messages only (Great for boot issues)
journalctl -k

# Check logs for a specific service (e.g., ssh)
journalctl -u ssh

# Watch logs in real-time (Like tail -f)
journalctl -u ssh -f

# Filter by time
journalctl --since "1 hour ago"
```

## Task 4: Linux Command Cheat Sheet

### Navigation & Directories
* `pwd` - Print working directory.
* `ls -lah` - List all files (including hidden) with human-readable sizes.
* `cd /var/log` - Change directory.

### File Operations
* `touch filename` - Create an empty file.
* `mkdir -p /path/to/folder` - Create a directory (and parents if needed).
* `cp file.txt copy.txt` - Copy a file.
* `mv file.txt /new/path/` - Move or rename a file.

### Viewing & Filtering Text
* `cat file.txt` - Output the entire file contents.
* `grep "error" file.txt` - Search for "error" inside the file.
* `tail -n 20 file.txt` - View the last 20 lines of a file.

### System Status
* `top` (or `htop`) - View live CPU/RAM usage and running processes.
* `df -h` - Check disk space usage.