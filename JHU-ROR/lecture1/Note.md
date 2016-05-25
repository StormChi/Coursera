# Ruby Basics
```Ruby 
3.times { puts "Hello World"}
```

# Flow of Control
``` Ruby
a = 5 # declare a variable

if a == 3
  puts "a is 3"
elsif a == 5
  puts "a is 5"
else
  puts "a is not 3 or 5"
end

# => a is 5
```

``` Ruby
#unless is basically if something is not equal to something else

a = 5
unless a == 6
  puts "a is not 6"
end

# => a is not 6
```

```Ruby
a = 10
while a > 9
  puts a 
  a -= 1
  # same as a = a - 1
end

# => 10
```

```Ruby
a = 9
until a >= 10
  puts a 
  a += 1
end

# => 9
```

### Modifier Form
```Ruby
# if modifier form

a = 5
b = 0

puts "One liner" if a == 5 and b == 0

# => One liner
```

```Ruby
# while modifier form

times_2 = 2
times_2 *= 2 while times_2 < 100
puts times_2 

# => 128
```
### True/False
－ `false` and `nil` objects are false


－ **Everything else** is true!

### Triple Equal
```Ruby
if /sera/ === "coursera"
  puts "Triple Equals"
end

# => Triple Equals

if "coursera" == "coursera"
  puts "also works"
end

# => also works

if Integer === 21
  puts "21 is an Ingeger"
end

# => 21 is an Integer
```

### Case Expressions
```Ruby
age = 21

case # 1ST FLAVOR
  when age >= 21
    puts "You can buy a drink"
  when 1 == 0
    puts "Written by a drunk programmer"
  else
    puts "default condition"
end

# => You can buy a drink
```

```Ruby
name = 'Fisher'
case name # 2nd FLAVOR
  when /fish/i then puts "Something is fishy here"
  when 'Smith' then puts "Your name is Smith"
end

# => Something is fishy here
```

### For loop
```Ruby
# Hardly used

for i in 0..2
  puts i
end

# => 0
# => 1
# => 2
```

# Functions

### Methods
```Ruby
def simple
  puts "no parens"
end

def simple1()
  puts "yes parens"
end

simple() # => no parens
simple   # => no parens
simple1  # => yes parens
```
### Return
```Ruby
def add(one, two)
  one + two
end

def divide(one, two)
  return "I don't think so" if two == 0
  one / two
end

puts add(2, 2)       # => 4
puts divide(2, 0)    # => I don't think so
puts divide(12, 4)   # => 3
```
### Expressive Method Names
Method names can end with:
- '?' - Predicate methods
- '!' - Dangerous side-effects
``` Ruby
def can_divide_by?(number)
  return false if number.zero?
  true
end

puts can_divide_by? 3    # => true
puts can_divide_by? 0    # => false
```

### Default Arguments
－ Ternary operator: condition ? true: false
``` Ruby
def factorial(n)
  n == 0? 1 : n * factorial(n - 1)
end

def factorial_with_dafault(n = 5)
  n == 0? 1 : n * factorial_with_dafault(n - 1)
end

puts factorial 5                   # => 120
puts factorial_with_dafault        # => 120
puts factorial_with_dafault(3)     # => 6
```

### Splat

```Ruby
def max(one_param, *numbers, another)
  # Variable length parameters passed in
  # become an array
  numbers.max
end

puts max("something", 7, 32, -4, "more")  # => 32
```  

# Blocks
```Ruby
1.times { puts "Hello World!" }

# => Hello World!

2.times do |index|
  if index > 0
    puts index
  end
end

# => 1

2.times { |index| puts index if index > 0 }

# => 1
```
### Implicit
``` Ruby
def two_times_implicit
  return "No block" unless block_given?   # if a block is not given, you either going to return
  yield
  yield
end

puts two_times_implicit { print "Hello " }    # => Hello
                                              # => Hello
                                              
puts two_times_implicit                       # => No block
```                                          
### Explicit
```Ruby
def two_times_implicit(&i_am_a_block)
  return "No block" if i_am_a_block.nil?
  i_am_a_block.call 
  i_am_a_block.call 
end

puts two_times_implicit   # => No block
two_times_implicit { puts "Hello" }   # => Hello
                                      # => Hello
```
# Files

### Reading from File
``` Ruby
File.foreach( 'test.txt' ) do |line|
  puts line
  p line
  p line.chomp     # chops off newline character
  p line.split     # array of words in line
end
```
####test.txt

The first line of the file

And the second

Third

#### output
The first line of the file

"The first line of the file\n"

"The first line of the file"

["The", "first", "line", "of", "the", "file"]

And the second

"And the second\n"

"And the second"

["And", "the", "second"]

Third

"Third"

"Third"

["Third"]

### 

 