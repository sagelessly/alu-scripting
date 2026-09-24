**# alu-scripting README**

This is a copy of the scripts for this repository, alu-scripting, using regular expressions in Ruby. These scripts perform different patterns on the input provided using the method `scan` to extract the text from the input.

### Regular Exp

The scripts are designed to showcase regular expressions in the context of pattern matching within text data.

### Usage

These scripts require the use of Ruby to run.

#### Examples:

1. **First Script:**
   ```ruby
   #!/usr/bin/env ruby
   puts ARGV[0].scan(/School/).join
   ```
   This script looks for a piece of text containing the word "School" and prints out that text.

2. **Second Script:**
   ```ruby
   #!/usr/bin/env ruby
   puts ARGV[0].scan(/hbt{2,5}n/).join
   ```
   It searches for patterns with 'hbt' followed by 2 to 5 't' and ending with 'n'.

3. **Third Script:**
   ```ruby
   #!/usr/bin/env ruby
   puts ARGV[0].scan(/hb?tn/).join
   ```
   This script is searching for patterns that contain ‘hbt' and optionally ‘b' and ‘tn'.

4. **Fourth Script:**
   ```ruby
   #!/usr/bin/env ruby
   puts ARGV[0].scan(/hbt{1,5}n/).join
   ```
   Pattern search with 'hbt' pattern followed by 1 to 5 't' and ending with 'n'.

5. **Fifth Script:**
   ```ruby
   #!/usr/bin/env ruby
   puts ARGV[0].scan(/hbt*n/).join
   ```
   This script will match the pattern "hbt" and then one or more 't' and end with the letter 'n'.
6. **ETC**
### Cloning Steps

To start using the scripts, clone this repository:

1. Open a terminal.

2. Run the following command:
   ```
   git clone https://github.com/lscblack/alu-scripting.git
   ```
4. Navigate to the directory where you have your scripts stored.5. Select the directory you have your scripts in.
    ```
    cd regular_expressions
    ```
