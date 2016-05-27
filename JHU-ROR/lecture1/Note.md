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

### Reading from Non Existing File
``` Ruby
File.foreach ( 'do_not_exist.txt' ) do |line|
  puts line.chomp
end

# Error
```
### Handling Exceptions
``` Ruby
begin

  File.foreach( 'do_not_exist.txt' ) do |line|
    puts line.chomp
  end

rescue Exception => e 
  puts e.message
  puts "Let's pretend this didn't happen..."
end
```

### Alternative to Exceptions 
``` Ruby
if File.exist? 'test.txt'
  File.foreach( 'test.txt' ) do |line|
    puts line.chomp
  end
end
```

### Writing to File
```Ruby
File.open("test1.txt", "w") do |file|
  file.puts "One line"
  file.puts "Another"
end
```
#### test1.txt
One line

Another

# Strings
### Strings / Interpolation
``` Ruby
single_quoted = 'ice cream \n followed by it\'s a party!'
double_quoted = "ice cream \n followed by it\'s a party!"

puts single_quoted            # => ice cream \n followed by it's a party!
puts double_quoted            # => ice cream
                              # =>   followed by it's a party!
                              
def multiple(one, two)
  "#{one} numtiplied by #{two} equals #{one * two}"      # Interpolation(only available for double-quoted strings)
end
puts multiply(5, 3)
# 5 multiplied by 3 equals 15
```
### More Strings
``` Ruby
my_name = " tim"
puts my_name.lstrip.capitalize         # => Tim
p my_name                              # => " tim"
my_name.lstrip!                        # (destructive) removes the leading space
my_name[0] = 'K'                       # replace the first character
puts my_name                           # => Kim

cur_weather = %Q{It's a hot day outside Grab your umbrellas...}

cur_weather.lines do |line|
  line.sub! 'hot', 'rainy'             # substitute 'hot' with 'rainy'
  puts "#{line.strip}"
end

# => It's a rainy day outside
# => Grab your umbrellas
```
# Arrays
``` Ruby
het_arr = [1, "two", :three]                       # heterogeneous types
puts het_arr[1]                                    # => two (array indices start at 0)

arr_words = %w{ what a great day today! }
puts arr_words[-2]                                 # => day
puts "#{arr_words.first} - #{arr_words.last}"      # => what -today!
p arr_words[-3, 2]                                 # => ["great", "day"] (go back 3 and take 2)

# (Range type covered later...)
p arr_words[2..4]                                  # => ["great", "day", "today"]

# Make a String out of array elements separated by ','
puts arr_words.join(',')                           # => what,a,great,day,today!
```
``` Ruby
# You want a stack (LIFO)? Sure
stack = []; stack << "one"; stack.push("two")
puts stack.pop                                  # => two

# You need a queue (FIFO)? We have those too...
queue = []; queue.push "one"; queue.push "two"
puts queue.shift                                # => one

a = [5,3,4,2].sort!.reverse!
p a # =>[5,4,3,2] (actually modifies the array)
p a.sample(2)                                   # => 2 random elements

a[6] = 33
p a                                             # => [5, 4, 3, 2, nil, nil, 33]
```
``` Ruby
a = [1, 3, 4, 7, 8, 10]
a.each { |num| print num }            # => 1347810 (no new line)
puts                                  # => (print new line)

new_arr = a.select { |num| num > 4 }
p new_arr                             # => [7, 8, 10]
new_arr = a.select { |num| num < 10 }
           .reject { |num| num.even? }

p new_arr                             # => [1, 3, 7]

# Multiple each element by 3 producing new array
new_arr = a.map {|x| x * 3}
p new_arr                             # => [3, 9, 12, 21, 24, 30]
```
# Ranges
```Ruby
some_range = 1..3
puts some_range.max                   # => 3
puts some_range.include? 2            # => true

puts (1...10) === 5.3                 # => true           Interesting. i miss a space like this puts(1...10) === 5.3, the output is false.
puts ('a'...'r') === "r"              # => false (end-exclusive)

p ('k'..'z').to_a.sample(2)           # => ["k", "w"]
# or another random array with 2 letters in Range

age = 55
case age
  when 0..12 then puts "Still a baby"
  when 13..99 then puts "Teenager at heart!"
  else puts "You are getting older..."
end
# => Teenager at heart!
```
# Hashes
### Hashes
```Ruby
editor_props = { "font" => "Arial", "size" => 12, "color" => "red" }

# THE ABOVE IS NOT A BLOCK - IT'S A HASH 
puts editor_props.length                         # => 3
puts editor_props["font"]                        # => Arial

editor_props["background"] = "Blue"
editor_props.each_pair do |key, value|
  puts "key: #{key} value: #{value}"
end

# => Key: font value: Arial
# => Key: size value: 12
# => Key: color value: red
# => Key: background value: Blue
```
``` Ruby
word_frequency = Hash.new(0)

sentence = "Chicka chicka boom boom"
sentence.split.each do |word|
  word_frequency[word.downcase] += 1
end

p word_frequency       # => {"chickda" => 2, "boom" => 2}
```
``` Ruby
family_tree_19 = {oldest: "Jim", older: "Joe", younger: "Jack"}
family_tree_19[:youngest] = "Jeremy"
p family_tree_19
# => {:oldest=>"Jim", :older=>"Joe", :younger=>"Jack", :youngest => "Jeremy" }

# Named parameter "like" behavior...
def adjust_colors (props = {foreground: "red", background: "white"])
  puts "Foreground: #{props[:foreground]}" if props[:foreground]
  puts "Background: #{props[:background]}" if props[:background]
end
adjust_colors        # => foreground: red
                     # => background: white 
adjust_colors ({ :foreground => "green" })        # => foreground: green      
adjust_colors background: "yella"                 # => background: yella      Use this one style.
adjust_colors :background => "magenta"            # => background: magenta    
```

### Block and Hash Confusion
``` Ruby
# Lets say you have a Hash
a_hash = { :one => "one" }

# Then, you output it
puts a_hash              # => {:one => "one"}

# If you try to do it in one step - you get a SyntaxError
# puts { :one => "one" }

# RUBY GETS CONFUSED AND THINKS {} IS A BLOCK!!!

# To get around this - you can use parens
puts ({ :one => "one" })    # => {:one => "one"}

# Or drop the {} altogether...
puts one: "one" # => {:one=>"one"}
```






 