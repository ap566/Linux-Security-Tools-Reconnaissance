# Linux Fundamentals

## 1. Files and directories

Linux represents files, devices, and many system resources through a filesystem tree. The root directory is `/`.

| Command | Purpose |
|---|---|
| `pwd` | Print current directory |
| `ls -la` | List files, including hidden files, with details |
| `cd /path` | Change directory |
| `mkdir lab` | Create a directory |
| `touch notes.txt` | Create an empty file |
| `cp source.txt copy.txt` | Copy a file |
| `mv old.txt new.txt` | Move or rename a file |
| `cat notes.txt` | Display file contents |
| `less notes.txt` | Read a file page by page |
| `file notes.txt` | Identify file type |
| `find . -name "*.txt"` | Find matching files under current directory |

Practice in a safe folder you own:

```bash
mkdir -p ~/security-lab/practice
cd ~/security-lab/practice
touch notes.txt
echo "Linux lab notes" > notes.txt
cat notes.txt
```

## 2. Permissions

Linux permissions apply to the file owner, group, and others. The common permission letters are:

- `r`: read
- `w`: write
- `x`: execute

View permissions:

```bash
ls -l
```

Example:

```text
-rwxr-xr--
```

This means owner has read/write/execute, group has read/execute, and others have read.

Change permissions symbolically:

```bash
chmod u+x script.sh
chmod go-rwx private.txt
```

Change permissions numerically:

```bash
chmod 640 notes.txt
```

`640` means owner read/write, group read, others no permissions.

Change ownership (requires appropriate privileges):

```bash
sudo chown username:groupname notes.txt
```

Do not use broad permissions such as `chmod -R 777` as a general fix.

## 3. Users and groups

Useful commands:

```bash
whoami
id
who
groups
getent passwd
getent group
```

On systems where you have administrator authorization, user and group administration may use:

```bash
sudo adduser labuser
sudo groupadd labgroup
sudo usermod -aG labgroup labuser
```

Log out and back in for new group membership to apply to a normal login session. Do not create or modify accounts on systems you do not administer.

## 4. Processes

A process is a running instance of a program.

```bash
ps aux
top
pgrep -a python
```

To stop a process you own, identify its PID carefully:

```bash
kill PID
```

Use `kill -9` only as a last resort because it does not allow the process to shut down cleanly.

## 5. Basic security practices

- Apply security updates using your distribution's supported update process.
- Use strong, unique passwords and MFA where available.
- Use `sudo` only when administrator privileges are needed.
- Keep file permissions restrictive.
- Remove or disable services you do not need.
- Use a firewall and review its rules.
- Back up important files.
- Do not run commands copied from untrusted sources without understanding them.

## 6. Linux distribution note

Commands for package installation differ by distribution. For example, Debian/Ubuntu use `apt`, while Fedora uses `dnf`. Read the distribution's official documentation before changing system configuration.
