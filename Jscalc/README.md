# 🦑 jscalc

To solve the "jscalc" challenge, we are dealing with a JavaScript calculator vulnerable to command injection due to its use of the eval() function.

## To exploit the vulnerability:

- **Identify the Vulnerability**: The use of `eval()` in the server code to evaluate user input poses a risk of remote code execution (RCE). Our goal is to exploit this to read files or run commands on the server.

- **Exploit the Vulnerability**: The target is to read the flag file (`/flag.txt`). We can use Node.js' `fs` module to read the file system.

  **Payload**:
  ```javascript
  require('fs').readFileSync('/flag.txt').toString()
  ```
  This will read the content of the flag file. Since the input is being evaluated directly in the `eval()` function, this payload executes on the server.
  
- `require('fs')`: This imports the filesystem module in Node.js, which will allow us to interact with the file system.
-  `readFileSync('/flag.txt')`: This method reads the file synchronously. If the file is found, its contents will be returned as a buffer.
-  `.toString()`: This converts the buffer to a string so we can read the contents of the file.
