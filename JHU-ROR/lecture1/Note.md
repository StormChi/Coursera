# Ruby Basics
`3.times { puts "Hello World"}`

# Flow of Control
```
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
unless is basically if something is not equal to something else
```
a = 5
unless a == 6
  puts "a is not 6"
end

# => a is not 6
```

```
a = 10
while a > 9
  puts a 
  a -= 1
  # same as a = a - 1
end

# => 10
```

```
a = 9
until a >= 10
  puts a 
  a += 1
end

# => 9
```

## Modifier Form
```
# if modifier form
a = 5
b = 0

puts "One liner" if a == 5 and b == 0
# => One liner
```
```
# while modifier form
times_2 = 2
times_2 *= 2 while times_2 < 100
puts times_2 
# => 128
```
## True/False
`false` and `nil` objects are false


**Everything else** is true!